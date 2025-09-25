#!/usr/bin/env python3
"""
Convert Obsidian Excalidraw embeds to use individual frame SVGs.
Uses pre-extracted frame SVG files for precise diagram display.
"""

import os
import re
import shutil
from pathlib import Path

def convert_checklist_format(content):
    """
    Convert emoji checkboxes to plain list items for proper MkDocs rendering.
    - ✅ text -> - text
    - ☑️ text -> - text
    - ✓ text -> - text
    Also ensure blank lines before lists for proper MkDocs rendering.
    """
    # Remove checkmark emojis but keep as list items
    patterns = [
        (r'^(\s*)-\s*✅\s*', r'\1- '),  # Remove green checkmark
        (r'^(\s*)-\s*☑️\s*', r'\1- '),  # Remove ballot box with check
        (r'^(\s*)-\s*✓\s*', r'\1- '),   # Remove check mark
    ]

    lines = content.split('\n')
    result_lines = []
    in_list = False

    for i, line in enumerate(lines):
        # Remove emoji checkboxes but keep list format
        for pattern, replacement in patterns:
            line = re.sub(pattern, replacement, line)

        # Check if this line starts a list
        is_list_item = line.strip().startswith('- ')

        # Add blank line before starting a new list
        if is_list_item and not in_list:
            # If previous line has content and isn't blank, add blank line
            if i > 0 and result_lines and result_lines[-1].strip():
                result_lines.append('')
            in_list = True
        elif not is_list_item and line.strip():
            # Not a list item and has content, so we're out of the list
            in_list = False

        result_lines.append(line)

    return '\n'.join(result_lines)

def convert_excalidraw_links(content):
    """
    Convert Obsidian Excalidraw embeds to use individual frame SVGs.

    Pattern: ![[episodes/01-portfolio-no-code/diagrams/all-diagrams.excalidraw.md#^frame=FRAME_ID]]
    To: <img> tag with the specific frame SVG
    """
    # Pattern to match Obsidian Excalidraw embeds
    pattern = r'!\[\[episodes/[^/]+/diagrams/[^#]+\.excalidraw\.md#\^frame=([^\]]+)\]\]'

    # Frame name and file mapping
    FRAME_MAP = {
        'KoJdwhj1PwVlHIsIixIRr': ('The New Reality', 'the-new-reality'),
        'rVOSTdETPrlwu1WhoIxKN': ('The Opportunity', 'the-opportunity'),
        'PEMM5ClHbU_L4mXxJZVbE': ('What You\'ll Build', 'what-youll-build'),
        '_W_JdP3rpJypbhNkADqEX': ('Frame 3.5', 'frame-3-5'),
        'g_huRGX4AReE-0V69pVaT': ('Cost Comparison', 'cost-comparison'),
        'Sf8jn2Eo9OT3zH1cGwPek': ('Why Markdown', 'why-markdown'),
        'StLOY6fAw2MqVGdsakh51': ('Essential Plugins', 'essential-plugins'),
        '9ZzwHK92FuFlxCy7kcnge': ('Frame 6', 'frame-6'),
        'g9O_5V5J8RbOc6o25FUbR': ('Frame 6.5', 'frame-6-5'),
        'Ztri2CGQKDYpPN5xoF3qH': ('Frame 7', 'frame-7'),
        'F0FmZBCy1DOtGqDTonkYd': ('Frame 8', 'frame-8'),
    }

    def replace_embed(match):
        frame_id = match.group(1)
        if frame_id in FRAME_MAP:
            frame_name, frame_file = FRAME_MAP[frame_id]
        else:
            frame_name = 'Diagram'
            frame_file = 'unknown'

        # Use the specific frame SVG
        svg_embed = f'''<div style="width: 100%; max-width: 1200px; margin: 2rem auto; text-align: center;" data-testid="excalidraw-diagram">
<img src="../../diagrams/frames/{frame_file}.svg"
     alt="{frame_name}"
     title="{frame_name}"
     data-frame-id="{frame_id}"
     data-frame-name="{frame_name}"
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

    # Apply all conversions
    converted_content = convert_excalidraw_links(content)
    converted_content = convert_checklist_format(converted_content)

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