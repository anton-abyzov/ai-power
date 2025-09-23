#!/usr/bin/env node

/**
 * Export individual frames from Excalidraw file as separate SVG files
 * This uses the Excalidraw JSON data to create focused exports
 */

const fs = require('fs');
const path = require('path');

// Read the Excalidraw JSON file
const excalidrawFile = path.join(__dirname, '..', 'episodes', '01-portfolio-no-code', 'diagrams', 'all-diagrams.excalidraw.excalidraw');
const excalidrawData = JSON.parse(fs.readFileSync(excalidrawFile, 'utf8'));

// Frame mapping
const FRAME_MAP = {
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

// Extract frames from elements
const frames = excalidrawData.elements.filter(el => el.type === 'frame');

console.log(`Found ${frames.length} frames in the Excalidraw file\n`);

// For each frame, we need to:
// 1. Find all elements within the frame bounds
// 2. Create a new Excalidraw file with just those elements
// 3. Export it as SVG

frames.forEach(frame => {
  if (!FRAME_MAP[frame.id]) {
    console.log(`Skipping unmapped frame: ${frame.id}`);
    return;
  }

  const frameName = FRAME_MAP[frame.id];

  // Get frame bounds
  const frameX = frame.x;
  const frameY = frame.y;
  const frameWidth = frame.width;
  const frameHeight = frame.height;

  // Find elements within frame bounds
  const elementsInFrame = excalidrawData.elements.filter(el => {
    if (el.type === 'frame') return false; // Don't include frame elements
    if (el.isDeleted) return false; // Skip deleted elements

    // Check if element is within frame bounds
    const elX = el.x;
    const elY = el.y;
    const elWidth = el.width || 100;
    const elHeight = el.height || 100;

    // Check if element overlaps with frame
    const overlapsX = elX < frameX + frameWidth && elX + elWidth > frameX;
    const overlapsY = elY < frameY + frameHeight && elY + elHeight > frameY;

    return overlapsX && overlapsY;
  });

  console.log(`Frame "${frameName}": ${elementsInFrame.length} elements`);

  // Create a simplified Excalidraw file for this frame
  const frameExcalidraw = {
    ...excalidrawData,
    elements: elementsInFrame,
    appState: {
      ...excalidrawData.appState,
      viewBackgroundColor: '#ffffff'
    }
  };

  // Save the frame-specific Excalidraw file
  const frameExcalidrawPath = path.join(__dirname, '..', 'episodes', '01-portfolio-no-code', 'diagrams', 'frames', `${frameName}.excalidraw`);
  fs.writeFileSync(frameExcalidrawPath, JSON.stringify(frameExcalidraw, null, 2));

  console.log(`  Saved: ${frameName}.excalidraw`);
});

console.log('\n📝 IMPORTANT: You need to manually export these .excalidraw files as SVGs:');
console.log('1. Open each .excalidraw file in Obsidian or excalidraw.com');
console.log('2. Export as SVG');
console.log('3. Save with the same name (e.g., the-new-reality.svg)');
console.log('\nAlternatively, use the Excalidraw CLI or API to automate the export.');