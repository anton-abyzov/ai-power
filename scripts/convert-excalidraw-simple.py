#!/usr/bin/env python3
"""
Convert Obsidian Excalidraw embeds to simple img tags for MkDocs.
Uses the full SVG image for maximum compatibility.
"""

import os
import re
import json
import shutil
from pathlib import Path

def convert_excalidraw_links(content):
    """
    Convert Obsidian Excalidraw embeds to simple img tags.

    Pattern: ![[episodes/01-portfolio-no-code/diagrams/all-diagrams.excalidraw.md#^frame=FRAME_ID]]
    To: <img> tag with the full SVG
    """
    # Pattern to match Obsidian Excalidraw embeds
    pattern = r'!\[\[episodes/[^/]+/diagrams/[^#]+\.excalidraw\.md#\^frame=([^\]]+)\]\]'

    def replace_embed(match):
        frame_id = match.group(1)

        # For now, just embed the full SVG with a note about which frame it should show
        # This ensures the diagram is at least visible
        svg_embed = f'''<div style="width: 100%; max-width: 1200px; margin: 2rem auto; text-align: center;">
<img src="../../diagrams/all-diagrams.excalidraw.light.svg"
     alt="Diagram - Frame {frame_id}"
     style="width: 100%; height: auto; max-height: 600px; object-fit: contain; border: 1px solid #e1e4e8; border-radius: 8px; background: white;">
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
    print("Converting Obsidian Excalidraw embeds to simple img tags...")
    sync_episodes_to_docs()
    print("Conversion complete!")