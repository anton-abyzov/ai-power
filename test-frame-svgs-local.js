const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  console.log('🔍 TESTING FRAME-SPECIFIC SVGS ON LOCAL SITE\n');

  // Test the introduction page
  await page.goto('http://127.0.0.1:8000/ai-power/episodes/01-portfolio-no-code/content/00-introduction/');
  await page.waitForTimeout(2000);

  // Check for frame-specific SVGs
  const frameSvgs = await page.$$eval('div[data-testid="excalidraw-diagram"] img', elements =>
    elements.map(el => {
      const src = el.src;
      const frameFile = src.split('/').pop();
      return {
        frameName: el.getAttribute('data-frame-name'),
        frameId: el.getAttribute('data-frame-id'),
        src: frameFile,
        isFrameSpecific: src.includes('/frames/'),
        displayed: el.getBoundingClientRect().width > 0,
        naturalWidth: el.naturalWidth,
        naturalHeight: el.naturalHeight,
        complete: el.complete
      };
    })
  );

  console.log('📊 FRAME-SPECIFIC DIAGRAMS ON PAGE:');
  if (frameSvgs.length === 0) {
    console.log('  ❌ No diagrams found with data-testid="excalidraw-diagram"');
  } else {
    let allFrameSpecific = true;
    frameSvgs.forEach(diagram => {
      const status = diagram.displayed && diagram.complete && diagram.isFrameSpecific ? '✅' : '❌';
      if (!diagram.isFrameSpecific) allFrameSpecific = false;

      console.log(`  ${status} ${diagram.frameName} (${diagram.frameId})`);
      console.log(`     File: ${diagram.src}`);
      console.log(`     Frame-specific: ${diagram.isFrameSpecific ? 'Yes' : 'No'}`);
      console.log(`     Size: ${diagram.naturalWidth}x${diagram.naturalHeight}`);
      console.log(`     Loaded: ${diagram.complete}`);
    });

    if (allFrameSpecific) {
      console.log('\n🎉 SUCCESS! All diagrams are using frame-specific SVG files!');
    } else {
      console.log('\n⚠️  Some diagrams are not using frame-specific SVG files.');
    }
  }

  // Take a screenshot to verify visually
  await page.screenshot({ path: 'local-site-frame-svgs.png', fullPage: false });

  console.log('\n📸 Screenshot saved: local-site-frame-svgs.png');
  console.log('\n✅ LOCAL SITE VERIFICATION COMPLETE');

  await browser.close();
})();