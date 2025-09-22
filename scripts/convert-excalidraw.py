#!/usr/bin/env python3
"""
Convert Obsidian Excalidraw embeds to MkDocs-compatible HTML iframes.
This script processes markdown files and replaces Obsidian-style Excalidraw embeds
with HTML iframes that work in MkDocs.
"""

import os
import re
import shutil
from pathlib import Path

def convert_excalidraw_links(content):
    """
    Convert Obsidian Excalidraw embeds to HTML iframes for MkDocs.

    Pattern: ![[../diagrams/all-diagrams.excalidraw#^frame=FRAME_ID]]
    To: <div><iframe src="../../diagrams/viewer.html#FRAME_ID"></iframe></div>
    """
    # Pattern to match Obsidian Excalidraw embeds (full path with frame syntax)
    pattern = r'!\[\[episodes/[^/]+/diagrams/[^#]+\.excalidraw\.md#\^frame=([^\]]+)\]\]'

    def replace_embed(match):
        frame_id = match.group(1)
        # Return HTML iframe embed
        return (
            f'<div style="width: 100%; height: 600px; border: 1px solid #ddd; border-radius: 8px; overflow: hidden;">\n'
            f'<iframe src="../../diagrams/viewer.html#{frame_id}" width="100%" height="100%" frameborder="0"></iframe>\n'
            f'</div>'
        )

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

    print(f"Converted: {source_path} -> {dest_path}")

def sync_episodes_to_docs():
    """
    Sync episodes folder to docs folder with conversions.
    Only processes markdown files and applies Excalidraw conversions.
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

            # Skip Obsidian-specific files
            if source_file.suffix in [".excalidraw"]:
                continue

            dest_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_file, dest_file)
            print(f"Copied: {source_file} -> {dest_file}")

if __name__ == "__main__":
    print("Converting Obsidian Excalidraw embeds to MkDocs format...")
    sync_episodes_to_docs()
    print("Conversion complete!")