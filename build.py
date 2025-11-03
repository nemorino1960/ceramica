#!/usr/bin/env python3
"""
Ceramica - Static Site Generator
Un semplice generatore che converte Markdown in HTML utilizzando template Jinja2

Version: 1.0.0
Author: nemorino60
Date: 2025-11-03
License: MIT
"""

__version__ = "1.0.0"
__author__ = "nemorino60"
__date__ = "2025-11-03"

import os
import json
import shutil
import re
from pathlib import Path
from typing import Dict, Any, List
import markdown
from jinja2 import Environment, FileSystemLoader, Template

class StaticSiteGenerator:
    """Classe principale per la generazione del sito statico"""
    
    def __init__(self, base_dir: str = "."):
        """
        Inizializza il generatore
        
        Args:
            base_dir: Directory base del progetto
        """
        self.base_dir = Path(base_dir)
        self.config = self._load_config()
        self.jinja_env = Environment(
            loader=FileSystemLoader(self.base_dir / self.config['paths']['templates'])
        )
        
    def _load_config(self) -> Dict[str, Any]:
        """Carica il file di configurazione"""
        config_path = self.base_dir / "config" / "config.json"
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _parse_frontmatter(self, content: str) -> tuple[Dict[str, Any], str]:
        """
        Estrae il frontmatter YAML-like da un file Markdown
        
        Args:
            content: Contenuto del file Markdown
            
        Returns:
            Tupla con (metadata, contenuto)
        """
        frontmatter_pattern = r'^---\s*\n(.*?)\n---\s*\n'
        match = re.match(frontmatter_pattern, content, re.DOTALL)
        
        if match:
            frontmatter_text = match.group(1)
            content = content[match.end():]
            
            # Parse semplice del frontmatter (formato key: value)
            metadata = {}
            for line in frontmatter_text.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    metadata[key.strip()] = value.strip()
            
            return metadata, content
        
        return {}, content
    
    def _process_markdown(self, md_content: str) -> str:
        """
        Converte Markdown in HTML
        
        Args:
            md_content: Contenuto Markdown
            
        Returns:
            HTML generato
        """
        md = markdown.Markdown(extensions=[
            'extra',      # Tabelle, code blocks, etc.
            'codehilite', # Syntax highlighting
            'toc',        # Table of contents
            'nl2br'       # Newline to <br>
        ])
        return md.convert(md_content)
    
    def _get_pages(self) -> List[Path]:
        """
        Ottiene l'elenco di tutti i file Markdown nella cartella pages (ricorsivamente)
        
        Returns:
            Lista di Path ai file Markdown
        """
        pages_dir = self.base_dir / self.config['paths']['pages']
        return list(pages_dir.rglob('*.md'))
    
    def _build_page(self, page_path: Path, output_dir: Path):
        """
        Costruisce una singola pagina
        
        Args:
            page_path: Path al file Markdown sorgente
            output_dir: Directory di output
        """
        # Leggi il file
        with open(page_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Estrai metadata e contenuto
        metadata, md_content = self._parse_frontmatter(content)
        
        # Converti Markdown in HTML
        html_content = self._process_markdown(md_content)
        
        # Carica il template
        template_name = metadata.get('template', 'base.html')
        template = self.jinja_env.get_template(template_name)
        
        # Calcola il path relativo rispetto alla cartella pages
        pages_dir = self.base_dir / self.config['paths']['pages']
        relative_path = page_path.relative_to(pages_dir)
        
        # Calcola la profondità per i link relativi (../ per tornare alla root)
        depth = len(relative_path.parts) - 1
        base_path = '../' * depth if depth > 0 else './'
        
        # Prepara i dati per il template
        page_data = {
            'title': metadata.get('title', 'Untitled'),
            'description': metadata.get('description', ''),
            'base_path': base_path,
        }
        
        # Renderizza la pagina
        rendered = template.render(
            site=self.config['site'],
            page=page_data,
            content=html_content
        )
        
        # Calcola il path di output mantenendo la struttura delle sottocartelle
        output_relative = relative_path.with_suffix('.html')
        output_path = output_dir / output_relative
        
        # Crea le sottocartelle necessarie
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Salva il file HTML
        output_path.write_text(rendered, encoding='utf-8')
        print(f"✓ Generata: {output_relative}")
    
    def _copy_assets(self, output_dir: Path):
        """
        Copia gli asset nella directory di output
        
        Args:
            output_dir: Directory di output
        """
        assets_src = self.base_dir / self.config['paths']['assets']
        assets_dst = output_dir / 'assets'
        
        if assets_src.exists():
            if assets_dst.exists():
                shutil.rmtree(assets_dst)
            shutil.copytree(assets_src, assets_dst)
            print(f"✓ Assets copiati in {assets_dst}")
    
    def _copy_resources(self, output_dir: Path):
        """
        Copia le risorse nella directory di output
        
        Args:
            output_dir: Directory di output
        """
        resources_src = self.base_dir / self.config['paths']['resources']
        
        if resources_src.exists():
            for item in resources_src.iterdir():
                dst = output_dir / item.name
                if item.is_file():
                    shutil.copy2(item, dst)
                elif item.is_dir():
                    if dst.exists():
                        shutil.rmtree(dst)
                    shutil.copytree(item, dst)
            print(f"✓ Risorse copiate da {resources_src}")
    
    def _create_output_dir(self, output_dir: Path):
        """
        Crea/pulisce la directory di output
        
        Args:
            output_dir: Directory di output da creare
        """
        if output_dir.exists():
            shutil.rmtree(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
    
    def build(self, mode: str = 'debug'):
        """
        Costruisce il sito
        
        Args:
            mode: 'debug' per build locale, 'deploy' per produzione
        """
        print(f"\n{'='*50}")
        print(f"Generazione sito in modalità: {mode.upper()}")
        print(f"{'='*50}\n")
        
        # Determina la directory di output
        output_dir = self.base_dir / self.config['paths'][mode]
        
        # Crea/pulisce la directory di output
        self._create_output_dir(output_dir)
        
        # Processa tutte le pagine
        pages = self._get_pages()
        print(f"Trovate {len(pages)} pagine da processare:\n")
        
        for page in pages:
            self._build_page(page, output_dir)
        
        # Copia gli asset
        print()
        if self.config['build']['copy_assets']:
            self._copy_assets(output_dir)
        
        # Copia le risorse
        self._copy_resources(output_dir)
        
        print(f"\n{'='*50}")
        print(f"✓ Build completata! Output in: {output_dir}")
        print(f"{'='*50}\n")
        
        if mode == 'debug':
            print("Per visualizzare il sito locale:")
            print(f"  cd {output_dir}")
            print("  python -m http.server 8000")
            print("  Apri http://localhost:8000 nel browser\n")


def main():
    """Funzione principale"""
    import sys
    
    # Gestione argomenti
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        
        # Mostra versione
        if arg in ['--version', '-v', 'version']:
            print(f"Ceramica v{__version__}")
            print(f"Author: {__author__}")
            print(f"Date: {__date__}")
            sys.exit(0)
        
        # Mostra help
        if arg in ['--help', '-h', 'help']:
            print("Ceramica - Static Site Generator")
            print(f"Version: {__version__}\n")
            print("Uso: python build.py [opzione]\n")
            print("Opzioni:")
            print("  debug, dev        Build per test locale (default)")
            print("  deploy, prod      Build per produzione")
            print("  --version, -v     Mostra versione")
            print("  --help, -h        Mostra questo messaggio")
            sys.exit(0)
    
    # Determina la modalità (debug o deploy)
    mode = 'debug'
    if len(sys.argv) > 1:
        if sys.argv[1] in ['deploy', 'production', 'prod']:
            mode = 'deploy'
        elif sys.argv[1] in ['debug', 'dev', 'development']:
            mode = 'debug'
        else:
            print("Uso: python build.py [debug|deploy]")
            print("  debug  : Build per test locale (default)")
            print("  deploy : Build per produzione")
            print("Usa --help per maggiori informazioni")
            sys.exit(1)
    
    # Crea e avvia il generatore
    try:
        generator = StaticSiteGenerator()
        generator.build(mode)
    except FileNotFoundError as e:
        print(f"❌ Errore: File non trovato - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Errore durante la generazione: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
