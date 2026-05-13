# geogehtml

A minimalist CLI tool to convert GeoGebra (`.ggb`) files into standalone HTML files using a Jinja2 template.

## Installation

Install directly from GitHub via `pip`:

```bash
pip install git+https://github.com/tna76874/geogehtml.git

```

## Usage

The tool provides a `geogehtml` command that can be used from anywhere:

```bash
# Convert to HTML (output will be 'filename.html')
geogehtml your_file.ggb

# Specify a custom output path
geogehtml your_file.ggb -o result.html

# Use a custom Jinja2 template (optional)
geogehtml your_file.ggb -t custom_template.j2

```
