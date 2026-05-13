#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import base64
import argparse
import os
import sys
from importlib import resources
from jinja2 import Template

def ggb_to_html(input_file, template_path, output_file):
    # 1. GGB File einlesen
    with open(input_file, "rb") as f:
        ggb_data = f.read()
        ggb_base64 = base64.b64encode(ggb_data).decode('utf-8')

    settings = {
        "showMenuBar": False,
        "showAlgebraInput": False,
        "showToolBar": False,
        "enableShiftDragZoom": False,
        "enableRightClick": False,
        "showZoomButtons": False,
    }

    # 2. Template laden (Logik für Systempfad oder Custom Path)
    if template_path and os.path.exists(template_path):
        with open(template_path, "r", encoding="utf-8") as t:
            template_content = t.read()
    else:
        # Lade das mitgelieferte Template aus dem Package-Resource-Pfad
        # 'geogehtml' ist der Package-Name, 'template.j2' der Dateiname
        try:
            template_content = resources.read_text('geogehtml', 'template.j2')
        except Exception as e:
            print(f"Fehler beim Laden des Standard-Templates: {e}")
            return

    jinja_template = Template(template_content)

    # 4. HTML generieren
    rendered_html = jinja_template.render(
        ggb_base64=ggb_base64,
        settings=settings
    )

    # 5. Speichern
    with open(output_file, "w", encoding="utf-8") as out:
        out.write(rendered_html)
    
    print(f"Erfolg: {output_file} wurde erstellt.")

def main():
    parser = argparse.ArgumentParser(description="GeoGebra GGB zu HTML Converter")
    parser.add_argument("input", help="Pfad zur .ggb Datei")
    parser.add_argument("-t", "--template", help="Optionaler Pfad zu einem eigenen Jinja2 Template")
    parser.add_argument("-o", "--output", help="Name der Output HTML Datei")

    args = parser.parse_args()
    output_name = args.output if args.output else os.path.splitext(args.input)[0] + ".html"
    
    ggb_to_html(args.input, args.template, output_name)

if __name__ == "__main__":
    main()