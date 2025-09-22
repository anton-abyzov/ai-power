#!/usr/bin/env python3
"""
Convert Obsidian Excalidraw embeds to inline SVG with viewBox for MkDocs.
This uses the exported SVG files directly for better compatibility.
"""

import os
import re
import json
import shutil
from pathlib import Path

# Frame coordinates extracted from the Excalidraw file
FRAME_COORDS = {
    'KoJdwhj1PwVlHIsIixIRr': {'x': -2838, 'y': -2618, 'width': 1793, 'height': 1006},
    'rVOSTdETPrlwu1WhoIxKN': {'x': -303, 'y': -2451, 'width': 963, 'height': 561},
    'PEMM5ClHbU_L4mXxJZVbE': {'x': 1455, 'y': -2591, 'width': 1880, 'height': 1260},
    'g_huRGX4AReE-0V69pVaT': {'x': -2849, 'y': -491, 'width': 973, 'height': 873},
    'StLOY6fAw2MqVGdsakh51': {'x': 1956, 'y': -497, 'width': 1055, 'height': 888},
    'Ztri2CGQKDYpPN5xoF3qH': {'x': 2577, 'y': 1405, 'width': 1178, 'height': 827},
}

def convert_excalidraw_links(content, svg_path_prefix="../../diagrams"):
    """
    Convert Obsidian Excalidraw embeds to inline SVG with viewBox.

    Pattern: ![[episodes/01-portfolio-no-code/diagrams/all-diagrams.excalidraw.md#^frame=FRAME_ID]]
    To: <svg viewBox="x y width height">...</svg>
    """
    # Pattern to match Obsidian Excalidraw embeds
    pattern = r'!\[\[episodes/[^/]+/diagrams/[^#]+\.excalidraw\.md#\^frame=([^\]]+)\]\]'

    def replace_embed(match):
        frame_id = match.group(1)

        # Get frame coordinates
        if frame_id not in FRAME_COORDS:
            print(f"Warning: Frame {frame_id} not found in coordinates map")
            return match.group(0)  # Return original if not found

        coords = FRAME_COORDS[frame_id]

        # Create embedded SVG with viewBox for the specific frame
        # Using object tag for better compatibility
        svg_embed = f'''<div style="width: 100%; height: 600px; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; background: white;">
<svg viewBox="{coords['x']} {coords['y']} {coords['width']} {coords['height']}"
     style="width: 100%; height: 100%;"
     xmlns="http://www.w3.org/2000/svg">
  <image href="{svg_path_prefix}/all-diagrams.excalidraw.light.svg"
         x="-5000" y="-5000" width="15000" height="10000"/>
</svg>
</div>'''

        return svg_embed

    # Replace all Excalidraw embeds
    converted = re.sub(pattern, replace_embed, content)
    return converted

def process_markdown_file(source_path, dest_path):
    """Process a single markdown file."""
    # Read the source file
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Convert Excalidraw links
    converted_content = convert_excalidraw_links(content)

    # Ensure destination directory exists
    dest_path.parent.mkdir(parents=True, exist_ok=True)

    # Write the converted content
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(converted_content)

    if source_path != dest_path:
        print(f"Converted: {source_path} -> {dest_path}")

def sync_episodes_to_docs():
    """
    Sync episodes folder to docs folder with conversions.
    """
    root_dir = Path(__file__).parent.parent
    episodes_dir = root_dir / "episodes"
    docs_episodes_dir = root_dir / "docs" / "episodes"

    if not episodes_dir.exists():
        print(f"Episodes directory not found: {episodes_dir}")
        return

    # Process all markdown files in episodes
    for source_file in episodes_dir.rglob("*.md"):
        # Skip README.md files to avoid MkDocs conflicts
        if source_file.name == "README.md":
            print(f"Skipping README.md: {source_file}")
            continue

        # Calculate relative path and destination
        rel_path = source_file.relative_to(episodes_dir)
        dest_file = docs_episodes_dir / rel_path

        # Process markdown file with conversions
        process_markdown_file(source_file, dest_file)

    # Copy non-markdown files directly
    for source_file in episodes_dir.rglob("*"):
        if source_file.is_file() and not source_file.suffix == ".md":
            rel_path = source_file.relative_to(episodes_dir)
            dest_file = docs_episodes_dir / rel_path

            dest_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_file, dest_file)
            print(f"Copied: {source_file} -> {dest_file}")

if __name__ == "__main__":
    print("Converting Obsidian Excalidraw embeds to inline SVG...")
    sync_episodes_to_docs()
    print("Conversion complete!")