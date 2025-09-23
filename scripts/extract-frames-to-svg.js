#!/usr/bin/env node

/**
 * Extract individual frames from Excalidraw file and generate separate SVG files
 * Uses excalidraw-to-svg library for proper SVG generation
 */

const fs = require('fs');
const path = require('path');
const excalidrawToSvg = require('excalidraw-to-svg');

// Frame name mapping for cleaner filenames
const FRAME_NAME_MAP = {
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
};

async function extractFramesToSvg() {
  console.log('📊 Starting Excalidraw frame extraction...\n');

  // Read the main Excalidraw file
  const excalidrawFile = path.join(__dirname, '..', 'episodes', '01-portfolio-no-code', 'diagrams', 'all-diagrams.excalidraw.excalidraw');
  const excalidrawData = JSON.parse(fs.readFileSync(excalidrawFile, 'utf8'));

  // Get all frame elements
  const frameElements = excalidrawData.elements.filter(el => el.type === 'frame' && !el.isDeleted);
  console.log(`Found ${frameElements.length} frames to extract\n`);

  // Output directory for frame SVGs
  const outputDir = path.join(__dirname, '..', 'docs', 'episodes', '01-portfolio-no-code', 'diagrams', 'frames');
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  // Process each frame
  for (const frame of frameElements) {
    const frameName = FRAME_NAME_MAP[frame.id] || frame.name?.toLowerCase().replace(/\s+/g, '-') || frame.id;
    console.log(`Processing frame: ${frameName} (${frame.id})`);

    // Get all elements that belong to this frame
    const frameChildElements = excalidrawData.elements.filter(el =>
      el.frameId === frame.id && !el.isDeleted
    );

    console.log(`  Found ${frameChildElements.length} elements in frame`);

    // Calculate bounds to adjust coordinates
    const bounds = getElementsBounds([frame, ...frameChildElements]);
    const padding = 50; // Add some padding around the content

    // Adjust all element coordinates to be relative to frame origin with padding
    const adjustedElements = frameChildElements.map(el => ({
      ...el,
      x: el.x - bounds.minX + padding,
      y: el.y - bounds.minY + padding
    }));

    // Add the frame element itself with adjusted coordinates
    const adjustedFrame = {
      ...frame,
      x: padding,
      y: padding,
      // Keep original width and height
      width: frame.width,
      height: frame.height
    };

    // Create a new Excalidraw document with just this frame's elements
    const frameDocument = {
      type: "excalidraw",
      version: 2,
      source: excalidrawData.source,
      elements: [adjustedFrame, ...adjustedElements],
      appState: {
        ...excalidrawData.appState,
        viewBackgroundColor: "#ffffff",
        // Set the viewport to show the entire frame content
        scrollX: 0,
        scrollY: 0,
        zoom: {
          value: 1
        }
      },
      files: excalidrawData.files || {}
    };

    try {
      // Generate SVG using excalidraw-to-svg
      console.log(`  Generating SVG...`);
      const svgElement = await excalidrawToSvg(frameDocument);

      // Get the SVG string
      const svgString = svgElement.outerHTML;

      // Adjust SVG viewBox to fit content properly
      const adjustedSvg = adjustViewBox(svgString, frame.width + padding * 2, frame.height + padding * 2);

      // Save the SVG file
      const outputPath = path.join(outputDir, `${frameName}.svg`);
      fs.writeFileSync(outputPath, adjustedSvg);
      console.log(`  ✅ Saved: ${frameName}.svg\n`);

    } catch (error) {
      console.error(`  ❌ Error generating SVG for ${frameName}:`, error.message);
      console.log();
    }
  }

  console.log('✨ Frame extraction complete!');
}

function getElementsBounds(elements) {
  let minX = Infinity, minY = Infinity;
  let maxX = -Infinity, maxY = -Infinity;

  for (const el of elements) {
    const elMinX = el.x;
    const elMinY = el.y;
    const elMaxX = el.x + (el.width || 0);
    const elMaxY = el.y + (el.height || 0);

    minX = Math.min(minX, elMinX);
    minY = Math.min(minY, elMinY);
    maxX = Math.max(maxX, elMaxX);
    maxY = Math.max(maxY, elMaxY);
  }

  return { minX, minY, maxX, maxY };
}

function adjustViewBox(svgString, width, height) {
  // Adjust the SVG viewBox to properly frame the content
  const viewBoxPattern = /viewBox="[^"]*"/;
  const widthPattern = /width="[^"]*"/;
  const heightPattern = /height="[^"]*"/;

  let adjusted = svgString.replace(viewBoxPattern, `viewBox="0 0 ${width} ${height}"`);
  adjusted = adjusted.replace(widthPattern, `width="${width}"`);
  adjusted = adjusted.replace(heightPattern, `height="${height}"`);

  return adjusted;
}

// Run the extraction
extractFramesToSvg().catch(error => {
  console.error('Fatal error:', error);
  process.exit(1);
});