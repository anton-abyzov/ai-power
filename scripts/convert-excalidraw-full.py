#!/usr/bin/env python3
"""
Convert Obsidian Excalidraw embeds to use the full diagram.
This is a temporary solution until we can properly export individual frames.
"""

import os
import re
import shutil
from pathlib import Path

def convert_excalidraw_links(content):
    """
    Convert Obsidian Excalidraw embeds to use the full SVG diagram.

    Pattern: ![[episodes/01-portfolio-no-code/diagrams/all-diagrams.excalidraw.md#^frame=FRAME_ID]]
    To: <img> tag with the full SVG
    """
    # Pattern to match Obsidian Excalidraw embeds
    pattern = r'!\[\[episodes/[^/]+/diagrams/[^#]+\.excalidraw\.md#\^frame=([^\]]+)\]\]'

    # Frame names for reference in alt text
    FRAME_NAMES = {
        'KoJdwhj1PwVlHIsIixIRr': 'The New Reality',
        'rVOSTdETPrlwu1WhoIxKN': 'The Opportunity',
        'PEMM5ClHbU_L4mXxJZVbE': 'What You\'ll Build',
        '_W_JdP3rpJypbhNkADqEX': 'Frame 3.5',
        'g_huRGX4AReE-0V69pVaT': 'Cost Comparison',
        'Sf8jn2Eo9OT3zH1cGwPek': 'Why Markdown',
        'StLOY6fAw2MqVGdsakh51': 'Essential Plugins',
        '9ZzwHK92FuFlxCy7kcnge': 'Frame 6',
        'g9O_5V5J8RbOc6o25FUbR': 'Frame 6.5',
        'Ztri2CGQKDYpPN5xoF3qH': 'Frame 7',
        'F0FmZBCy1DOtGqDTonkYd': 'Frame 8',
    }

    def replace_embed(match):
        frame_id = match.group(1)
        frame_name = FRAME_NAMES.get(frame_id, 'Diagram')

        # For now, use the full diagram SVG
        # Add a note that this shows the full diagram
        svg_embed = f'''<div style="width: 100%; max-width: 1200px; margin: 2rem auto; text-align: center;" data-testid="excalidraw-diagram">
<img src="../../diagrams/all-diagrams.excalidraw.light.svg"
     alt="{frame_name}"
     title="{frame_name}"
     data-frame-id="{frame_id}"
     data-frame-name="{frame_name}"
     style="width: 100%; height: auto; max-height: 600px; object-fit: contain; border: 1px solid #e1e4e8; border-radius: 8px; background: white;">
<p style="margin-top: 0.5rem; font-size: 0.9em; color: #666; font-style: italic;">
  Note: Showing full diagram. Scroll to find "{frame_name}" section.
</p>
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
    print("Converting Obsidian Excalidraw embeds to use full diagram...")
    print("NOTE: This is a temporary solution. Individual frame export is still needed.")
    sync_episodes_to_docs()
    print("Conversion complete!")