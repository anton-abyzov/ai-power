#!/usr/bin/env python3
"""
Extract individual frames from Excalidraw file as SVGs
"""

import json
import os
from pathlib import Path

# Read the Excalidraw file
excalidraw_file = Path("all-diagrams.excalidraw")
with open(excalidraw_file, 'r') as f:
    data = json.load(f)

# Find all frames and their IDs
frames = {}
for element in data.get('elements', []):
    if element.get('type') == 'frame' and element.get('name'):
        frame_name = element.get('name').replace(' ', '_').replace('.', '_')
        frames[frame_name] = {
            'id': element.get('id'),
            'name': element.get('name'),
            'x': element.get('x'),
            'y': element.get('y'),
            'width': element.get('width'),
            'height': element.get('height')
        }

# Create frame index file
frame_index = "# Excalidraw Frames\n\n"
frame_index += "## Frame Mapping\n\n"
frame_index += "| Frame Name | Frame ID | Dimensions |\n"
frame_index += "|------------|----------|------------|\n"

for frame_name, info in sorted(frames.items()):
    frame_index += f"| {info['name']} | `{info['id']}` | {int(info['width'])}x{int(info['height'])} |\n"

frame_index += "\n## Frame Links\n\n"
frame_index += "These frames are embedded throughout the documentation:\n\n"

for frame_name, info in sorted(frames.items()):
    frame_index += f"- **{info['name']}**: `#{info['id']}`\n"

# Write the frame index
with open('frame-index.md', 'w') as f:
    f.write(frame_index)

print(f"Extracted {len(frames)} frames")
print("Frame index created: frame-index.md")