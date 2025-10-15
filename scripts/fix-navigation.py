#!/usr/bin/env python3
"""
Fix navigation links in content files to remove duplicate 'content' in paths.
"""

import os
import re
from pathlib import Path

def fix_navigation_links_in_file(file_path):
    """Fix navigation links in a single file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Fix navigation links that have ../content/XX-name/ to ../XX-name/
    content = re.sub(
        r'href="../content/([^"]+)/"',
        r'href="../\1/"',
        content
    )

    # Write back only if changed
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed navigation links in: {file_path}")
        return True
    return False

def main():
    """Fix navigation links in all content files."""
    root_dir = Path(__file__).parent.parent
    content_dir = root_dir / "episodes" / "01-portfolio-no-code" / "content"

    if not content_dir.exists():
        print(f"Content directory not found: {content_dir}")
        return

    fixed_count = 0
    for md_file in content_dir.glob("*.md"):
        if fix_navigation_links_in_file(md_file):
            fixed_count += 1

    print(f"Fixed navigation links in {fixed_count} files")

if __name__ == "__main__":
    main()