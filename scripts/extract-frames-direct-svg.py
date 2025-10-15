#!/usr/bin/env python3
"""
Extract individual frames from Excalidraw file and generate separate SVG files
Direct SVG generation from Excalidraw JSON without external dependencies
"""

import json
import os
import math
from pathlib import Path
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Frame name mapping for cleaner filenames
FRAME_NAME_MAP = {
    'KoJdwhj1PwVlHIsIixIRr': 'the-new-reality',
    'rVOSTdETPrlwu1WhoIxKN': 'the-opportunity',
    'PEMM5ClHbU_L4mXxJZVbE': 'what-youll-build',
    '_W_JdP3rpJypbhNkADqEX': 'frame-3-5',
    'g_huRGX4AReE-0V69pVaT': 'cost-comparison',
    'Sf8jn2Eo9OT3zH1cGwPek': 'why-markdown',
    'StLOY6fAw2MqVGdsakh51': 'essential-plugins',
    '9ZzwHK92FuFlxCy7kcnge': 'frame-6',
    'g9O_5V5J8RbOc6o25FUbR': 'frame-6-5',
    'Ztri2CGQKDYpPN5xoF3qH': 'frame-7',
    'F0FmZBCy1DOtGqDTonkYd': 'frame-8',
}

def get_element_bounds(elements):
    """Calculate bounds of elements"""
    if not elements:
        return 0, 0, 100, 100

    min_x = float('inf')
    min_y = float('inf')
    max_x = float('-inf')
    max_y = float('-inf')

    for el in elements:
        x = el.get('x', 0)
        y = el.get('y', 0)
        width = el.get('width', 0)
        height = el.get('height', 0)

        # Handle different element types
        if el['type'] in ['line', 'arrow']:
            points = el.get('points', [])
            for point in points:
                px = x + point[0]
                py = y + point[1]
                min_x = min(min_x, px)
                min_y = min(min_y, py)
                max_x = max(max_x, px)
                max_y = max(max_y, py)
        elif el['type'] == 'freedraw':
            points = el.get('points', [])
            for point in points:
                px = x + point[0]
                py = y + point[1]
                min_x = min(min_x, px)
                min_y = min(min_y, py)
                max_x = max(max_x, px)
                max_y = max(max_y, py)
        else:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x + width)
            max_y = max(max_y, y + height)

    return min_x, min_y, max_x, max_y

def create_svg_element(el, offset_x, offset_y, files=None):
    """Create SVG element from Excalidraw element"""
    el_type = el['type']
    x = el.get('x', 0) - offset_x
    y = el.get('y', 0) - offset_y

    stroke_color = el.get('strokeColor', '#000000')
    bg_color = el.get('backgroundColor', 'transparent')
    stroke_width = el.get('strokeWidth', 1)
    opacity = el.get('opacity', 100) / 100

    if el_type == 'rectangle':
        rect = ET.Element('rect')
        rect.set('x', str(x))
        rect.set('y', str(y))
        rect.set('width', str(el.get('width', 0)))
        rect.set('height', str(el.get('height', 0)))
        rect.set('stroke', stroke_color)
        rect.set('stroke-width', str(stroke_width))
        rect.set('fill', bg_color if bg_color != 'transparent' else 'none')
        rect.set('opacity', str(opacity))

        # Add rounded corners if present
        roundness = el.get('roundness')
        if roundness and isinstance(roundness, dict) and roundness.get('type') == 3:
            rect.set('rx', '10')
            rect.set('ry', '10')

        return rect

    elif el_type == 'ellipse':
        ellipse = ET.Element('ellipse')
        cx = x + el.get('width', 0) / 2
        cy = y + el.get('height', 0) / 2
        ellipse.set('cx', str(cx))
        ellipse.set('cy', str(cy))
        ellipse.set('rx', str(el.get('width', 0) / 2))
        ellipse.set('ry', str(el.get('height', 0) / 2))
        ellipse.set('stroke', stroke_color)
        ellipse.set('stroke-width', str(stroke_width))
        ellipse.set('fill', bg_color if bg_color != 'transparent' else 'none')
        ellipse.set('opacity', str(opacity))
        return ellipse

    elif el_type == 'text':
        text = ET.Element('text')
        text.set('x', str(x))
        text.set('y', str(y + el.get('fontSize', 16)))
        text.set('font-size', str(el.get('fontSize', 16)))

        # Map Excalidraw font family codes to actual fonts
        font_family = el.get('fontFamily', 1)
        font_map = {
            1: 'Virgil, Segoe UI Emoji',  # Hand-drawn
            2: 'Helvetica, Segoe UI Emoji',  # Normal
            3: 'Cascadia, Segoe UI Emoji',  # Code
            4: 'Comic Sans MS, Segoe UI Emoji',  # Comic
            5: 'Virgil, Segoe UI Emoji'  # Default to hand-drawn
        }
        actual_font = font_map.get(font_family, 'Virgil, Segoe UI Emoji')
        text.set('font-family', actual_font)

        text.set('fill', stroke_color)
        text.set('opacity', str(opacity))

        # Handle multi-line text
        text_content = el.get('text', '')
        if '\n' in text_content:
            # For multi-line text, create tspan elements
            lines = text_content.split('\n')
            for i, line in enumerate(lines):
                tspan = ET.SubElement(text, 'tspan')
                tspan.set('x', str(x))
                tspan.set('dy', '1.2em' if i > 0 else '0')
                tspan.text = line
        else:
            text.text = text_content

        return text

    elif el_type == 'line':
        line = ET.Element('path')
        points = el.get('points', [])
        if points:
            path_d = f"M {x + points[0][0]} {y + points[0][1]}"
            for point in points[1:]:
                path_d += f" L {x + point[0]} {y + point[1]}"
            line.set('d', path_d)
            line.set('stroke', stroke_color)
            line.set('stroke-width', str(stroke_width))
            line.set('fill', 'none')
            line.set('opacity', str(opacity))

            # Handle stroke style
            stroke_style = el.get('strokeStyle')
            if stroke_style == 'dashed':
                line.set('stroke-dasharray', '5,5')
            elif stroke_style == 'dotted':
                line.set('stroke-dasharray', '2,2')

            return line

    elif el_type == 'freedraw':
        path = ET.Element('path')
        points = el.get('points', [])
        if points:
            path_d = f"M {x + points[0][0]} {y + points[0][1]}"
            for point in points[1:]:
                path_d += f" L {x + point[0]} {y + point[1]}"
            path.set('d', path_d)
            path.set('stroke', stroke_color)
            path.set('stroke-width', str(stroke_width))
            path.set('fill', 'none')
            path.set('opacity', str(opacity))
            path.set('stroke-linecap', 'round')
            path.set('stroke-linejoin', 'round')
            return path

    elif el_type == 'arrow':
        # Create a group for the arrow (line + arrowheads)
        group = ET.Element('g')
        group.set('opacity', str(opacity))

        # Create the arrow line
        points = el.get('points', [])
        if points and len(points) >= 2:
            # Create path for the arrow line
            path = ET.Element('path')
            path_d = f"M {x + points[0][0]} {y + points[0][1]}"
            for point in points[1:]:
                path_d += f" L {x + point[0]} {y + point[1]}"
            path.set('d', path_d)
            path.set('stroke', stroke_color)
            path.set('stroke-width', str(stroke_width))
            path.set('fill', 'none')

            # Handle stroke style
            stroke_style = el.get('strokeStyle')
            if stroke_style == 'dashed':
                path.set('stroke-dasharray', '5,5')
            elif stroke_style == 'dotted':
                path.set('stroke-dasharray', '2,2')

            # Add marker for arrowhead if present
            if el.get('endArrowhead') or el.get('lastCommittedPoint'):
                # Create a unique marker ID
                marker_id = f"arrowhead-{el['id'][:8]}"

                # Define the arrowhead marker
                defs = ET.Element('defs')
                marker = ET.SubElement(defs, 'marker')
                marker.set('id', marker_id)
                marker.set('markerWidth', '10')
                marker.set('markerHeight', '10')
                marker.set('refX', '9')
                marker.set('refY', '3')
                marker.set('orient', 'auto')
                marker.set('markerUnits', 'strokeWidth')

                # Create the arrowhead shape
                arrow_path = ET.SubElement(marker, 'path')
                arrow_path.set('d', 'M 0 0 L 10 3 L 0 6 L 3 3 z')
                arrow_path.set('fill', stroke_color)

                # Add the marker reference to the path
                path.set('marker-end', f"url(#{marker_id})")

                # Return both defs and path in the group
                group.append(defs)

            group.append(path)
            return group

        return None

    elif el_type == 'image':
        # Handle image elements with embedded data
        image = ET.Element('image')
        image.set('x', str(x))
        image.set('y', str(y))
        image.set('width', str(el.get('width', 0)))
        image.set('height', str(el.get('height', 0)))
        image.set('opacity', str(opacity))
        image.set('preserveAspectRatio', 'xMidYMid meet')

        # Get the file ID and look up the data URL
        file_id = el.get('fileId')
        if file_id and files and file_id in files:
            file_data = files[file_id]
            data_url = file_data.get('dataURL')
            if data_url:
                # Use the data URL directly as the href
                # Note: using 'href' attribute which works in modern SVG
                image.set('href', data_url)
            else:
                print(f"  Warning: No dataURL for image {file_id}")
        else:
            if file_id:
                print(f"  Warning: Image with fileId {file_id} not found in files")

        return image

    return None

def extract_frame_to_svg(frame, elements, output_path, files=None):
    """Extract a single frame to SVG"""
    # Get frame elements
    frame_elements = [el for el in elements if el.get('frameId') == frame['id'] and not el.get('isDeleted', False)]

    if not frame_elements:
        print(f"  Warning: No elements found in frame {frame['id']}")
        return False

    # Calculate bounds
    min_x, min_y, max_x, max_y = get_element_bounds(frame_elements)

    # Add padding
    padding = 50
    width = max_x - min_x + 2 * padding
    height = max_y - min_y + 2 * padding

    # Create SVG root
    svg = ET.Element('svg')
    svg.set('xmlns', 'http://www.w3.org/2000/svg')
    svg.set('width', str(width))
    svg.set('height', str(height))
    svg.set('viewBox', f'0 0 {width} {height}')

    # Add white background
    bg = ET.Element('rect')
    bg.set('width', str(width))
    bg.set('height', str(height))
    bg.set('fill', 'white')
    svg.append(bg)

    # Add frame border (optional)
    frame_border = ET.Element('rect')
    frame_border.set('x', str(padding))
    frame_border.set('y', str(padding))
    frame_border.set('width', str(frame.get('width', max_x - min_x)))
    frame_border.set('height', str(frame.get('height', max_y - min_y)))
    frame_border.set('stroke', '#e0e0e0')
    frame_border.set('stroke-width', '1')
    frame_border.set('fill', 'none')
    frame_border.set('stroke-dasharray', '5,5')
    svg.append(frame_border)

    # Sort elements by their z-index (approximated by order in array)
    # Elements should be rendered in order they appear

    # Add elements to SVG
    for el in frame_elements:
        svg_el = create_svg_element(el, min_x - padding, min_y - padding, files)
        if svg_el is not None:
            svg.append(svg_el)

    # Convert to string with pretty printing
    rough_string = ET.tostring(svg, encoding='unicode')
    reparsed = minidom.parseString(rough_string)
    pretty_svg = reparsed.toprettyxml(indent="  ")

    # Remove extra blank lines
    lines = pretty_svg.split('\n')
    lines = [line for line in lines if line.strip()]
    pretty_svg = '\n'.join(lines[1:])  # Skip XML declaration

    # Write to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(pretty_svg)

    return True

def main():
    print('📊 Starting Excalidraw frame extraction (Python)...\n')

    # Paths
    root_dir = Path(__file__).parent.parent
    excalidraw_file = root_dir / 'episodes' / '01-portfolio-no-code' / 'diagrams' / 'all-diagrams.excalidraw.excalidraw'
    output_dir = root_dir / 'docs' / 'episodes' / '01-portfolio-no-code' / 'diagrams' / 'frames'
    episodes_output_dir = root_dir / 'episodes' / '01-portfolio-no-code' / 'diagrams' / 'frames'

    # Create output directories
    output_dir.mkdir(parents=True, exist_ok=True)
    episodes_output_dir.mkdir(parents=True, exist_ok=True)

    # Load Excalidraw data
    with open(excalidraw_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    elements = data['elements']
    files = data.get('files', {})

    print(f'Found {len(files)} embedded images in Excalidraw file')

    # Get all frames
    frames = [el for el in elements if el['type'] == 'frame' and not el.get('isDeleted', False)]
    print(f'Found {len(frames)} frames to extract\n')

    # Process each frame
    success_count = 0
    for frame in frames:
        frame_name = FRAME_NAME_MAP.get(frame['id'], frame.get('name', frame['id']).lower().replace(' ', '-'))
        print(f'Processing frame: {frame_name} ({frame["id"]})')

        output_path = output_dir / f'{frame_name}.svg'
        episodes_path = episodes_output_dir / f'{frame_name}.svg'

        if extract_frame_to_svg(frame, elements, output_path, files):
            # Copy to episodes directory as well
            import shutil
            shutil.copy2(output_path, episodes_path)
            print(f'  ✅ Saved: {frame_name}.svg (to both docs/ and episodes/)\n')
            success_count += 1
        else:
            print(f'  ❌ Failed to extract {frame_name}\n')

    print(f'✨ Frame extraction complete! {success_count}/{len(frames)} frames extracted successfully.')

if __name__ == '__main__':
    main()