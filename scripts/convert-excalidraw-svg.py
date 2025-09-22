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

# Frame coordinates extracted from the Excalidraw file with padding
FRAME_COORDS = {
    'KoJdwhj1PwVlHIsIixIRr': {'x': -2839, 'y': -2619, 'width': 1793, 'height': 1005},  # Frame 1
    'rVOSTdETPrlwu1WhoIxKN': {'x': -304, 'y': -2451, 'width': 964, 'height': 561},  # Frame 2
    'PEMM5ClHbU_L4mXxJZVbE': {'x': 1455, 'y': -2592, 'width': 1881, 'height': 1261},  # Frame 3
    '_W_JdP3rpJypbhNkADqEX': {'x': 4211, 'y': -2627, 'width': 1697, 'height': 493},  # Frame 3.5
    'g_huRGX4AReE-0V69pVaT': {'x': -2850, 'y': -492, 'width': 974, 'height': 874},  # Frame 4
    'Sf8jn2Eo9OT3zH1cGwPek': {'x': -540, 'y': -537, 'width': 1422, 'height': 986},  # Frame 4.5
    'StLOY6fAw2MqVGdsakh51': {'x': 1957, 'y': -498, 'width': 1056, 'height': 888},  # Frame 5
    '9ZzwHK92FuFlxCy7kcnge': {'x': -2922, 'y': 1243, 'width': 1733, 'height': 1079},  # Frame 6
    'g9O_5V5J8RbOc6o25FUbR': {'x': -195, 'y': 1386, 'width': 1244, 'height': 847},  # Frame 6.5
    'Ztri2CGQKDYpPN5xoF3qH': {'x': 2578, 'y': 1405, 'width': 1178, 'height': 827},  # Frame 7
    'F0FmZBCy1DOtGqDTonkYd': {'x': 5042, 'y': 1410, 'width': 1905, 'height': 1045},  # Frame 8
}

def convert_excalidraw_links(content, svg_path_prefix="../diagrams"):
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

        # Add padding around the frame for better visibility
        padding = 50
        view_x = coords['x'] - padding
        view_y = coords['y'] - padding
        view_width = coords['width'] + (padding * 2)
        view_height = coords['height'] + (padding * 2)

        # Calculate aspect ratio for responsive height
        aspect_ratio = view_height / view_width
        # Max height of 600px, but scale down if needed
        max_width = 1200
        calculated_height = min(600, max_width * aspect_ratio)

        # Create embedded SVG with viewBox for the specific frame
        svg_embed = f'''<div style="width: 100%; max-width: {max_width}px; margin: 2rem auto;">
<div style="width: 100%; height: 0; padding-bottom: {aspect_ratio * 100:.1f}%; position: relative; border: 1px solid #e1e4e8; border-radius: 8px; overflow: hidden; background: white;">
<svg viewBox="{view_x} {view_y} {view_width} {view_height}"
     style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
     xmlns="http://www.w3.org/2000/svg"
     preserveAspectRatio="xMidYMid meet">
  <image href="{svg_path_prefix}/all-diagrams.excalidraw.light.svg"
         x="-5000" y="-5000" width="15000" height="10000"
         preserveAspectRatio="none"/>
</svg>
</div>
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