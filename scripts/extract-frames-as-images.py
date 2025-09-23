#!/usr/bin/env python3
"""
Extract individual frames from the Excalidraw SVG as separate cropped images.
This creates individual SVG files for each frame with proper viewBox settings.
"""

import os
import re
import json
from pathlib import Path
import xml.etree.ElementTree as ET

# Frame coordinates extracted from the Excalidraw file
FRAME_COORDS = {
    'KoJdwhj1PwVlHIsIixIRr': {'x': -2839, 'y': -2619, 'width': 1793, 'height': 1005, 'name': 'the-new-reality'},  # Frame 1
    'rVOSTdETPrlwu1WhoIxKN': {'x': -304, 'y': -2451, 'width': 964, 'height': 561, 'name': 'the-opportunity'},  # Frame 2
    'PEMM5ClHbU_L4mXxJZVbE': {'x': 1455, 'y': -2592, 'width': 1881, 'height': 1261, 'name': 'what-youll-build'},  # Frame 3
    '_W_JdP3rpJypbhNkADqEX': {'x': 4211, 'y': -2627, 'width': 1697, 'height': 493, 'name': 'frame-3-5'},  # Frame 3.5
    'g_huRGX4AReE-0V69pVaT': {'x': -2850, 'y': -492, 'width': 974, 'height': 874, 'name': 'cost-comparison'},  # Frame 4
    'Sf8jn2Eo9OT3zH1cGwPek': {'x': -540, 'y': -537, 'width': 1422, 'height': 986, 'name': 'why-markdown'},  # Frame 4.5
    'StLOY6fAw2MqVGdsakh51': {'x': 1957, 'y': -498, 'width': 1056, 'height': 888, 'name': 'essential-plugins'},  # Frame 5
    '9ZzwHK92FuFlxCy7kcnge': {'x': -2922, 'y': 1243, 'width': 1733, 'height': 1079, 'name': 'frame-6'},  # Frame 6
    'g9O_5V5J8RbOc6o25FUbR': {'x': -195, 'y': 1386, 'width': 1244, 'height': 847, 'name': 'frame-6-5'},  # Frame 6.5
    'Ztri2CGQKDYpPN5xoF3qH': {'x': 2578, 'y': 1405, 'width': 1178, 'height': 827, 'name': 'frame-7'},  # Frame 7
    'F0FmZBCy1DOtGqDTonkYd': {'x': 5042, 'y': 1410, 'width': 1905, 'height': 1045, 'name': 'frame-8'},  # Frame 8
}

def extract_frames():
    """Extract individual frames from the main SVG file."""

    root_dir = Path(__file__).parent.parent
    source_svg = root_dir / "episodes" / "01-portfolio-no-code" / "diagrams" / "all-diagrams.excalidraw.light.svg"
    output_dir = root_dir / "docs" / "episodes" / "01-portfolio-no-code" / "diagrams" / "frames"

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Read the source SVG content
    with open(source_svg, 'r', encoding='utf-8') as f:
        svg_content = f.read()

    # Parse the SVG to get its original viewBox
    # Extract viewBox from the SVG element
    viewbox_match = re.search(r'viewBox="([^"]+)"', svg_content)
    if viewbox_match:
        original_viewbox = viewbox_match.group(1)
        print(f"Original SVG viewBox: {original_viewbox}")

    # Process each frame
    for frame_id, frame_info in FRAME_COORDS.items():
        # Add padding around the frame
        padding = 50
        view_x = frame_info['x'] - padding
        view_y = frame_info['y'] - padding
        view_width = frame_info['width'] + (padding * 2)
        view_height = frame_info['height'] + (padding * 2)

        # Create a new SVG with cropped viewBox
        frame_svg = f'''<svg version="1.1"
     xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink"
     viewBox="{view_x} {view_y} {view_width} {view_height}"
     width="{view_width}"
     height="{view_height}"
     style="background: white;">
  <image href="../all-diagrams.excalidraw.light.svg"
         x="-5000" y="-5000"
         width="15000" height="10000"
         preserveAspectRatio="none"/>
</svg>'''

        # Save the frame SVG
        output_file = output_dir / f"{frame_info['name']}.svg"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(frame_svg)

        print(f"Created frame: {output_file.name} ({view_width}x{view_height})")

    print(f"\n✅ Extracted {len(FRAME_COORDS)} frames to {output_dir}")

    # Also copy to the episodes folder for local preview
    episodes_output_dir = root_dir / "episodes" / "01-portfolio-no-code" / "diagrams" / "frames"
    episodes_output_dir.mkdir(parents=True, exist_ok=True)

    import shutil
    for svg_file in output_dir.glob("*.svg"):
        shutil.copy2(svg_file, episodes_output_dir / svg_file.name)

    print(f"✅ Also copied frames to {episodes_output_dir} for Obsidian preview")

if __name__ == "__main__":
    extract_frames()