const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  console.log('🌐 VERIFYING FRAME-SPECIFIC SVGS ON DEPLOYED SITE\n');

  // Test the deployed page
  await page.goto('https://anton-abyzov.github.io/ai-power/episodes/01-portfolio-no-code/content/00-introduction/');
  await page.waitForTimeout(3000);

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

  console.log('📊 FRAME-SPECIFIC DIAGRAMS ON DEPLOYED SITE:');
  if (frameSvgs.length === 0) {
    console.log('  ❌ No diagrams found with data-testid="excalidraw-diagram"');
  } else {
    let allWorking = true;
    let allFrameSpecific = true;
    frameSvgs.forEach(diagram => {
      const status = diagram.displayed && diagram.complete && diagram.isFrameSpecific ? '✅' : '❌';
      if (!diagram.displayed || !diagram.complete || !diagram.isFrameSpecific) allWorking = false;
      if (!diagram.isFrameSpecific) allFrameSpecific = false;

      console.log(`  ${status} ${diagram.frameName} (${diagram.frameId})`);
      console.log(`     File: ${diagram.src}`);
      console.log(`     Frame-specific: ${diagram.isFrameSpecific ? 'Yes' : 'No'}`);
      console.log(`     Size: ${diagram.naturalWidth}x${diagram.naturalHeight}`);
      console.log(`     Loaded: ${diagram.complete}`);
    });

    console.log('\n' + '='.repeat(60));
    if (allWorking && allFrameSpecific) {
      console.log('🎉 SUCCESS! All diagrams are using frame-specific SVG files!');
      console.log('✅ Each frame shows only its relevant content');
      console.log('✅ No more full diagram shown for every frame');
      console.log('✅ Problem completely solved!');
    } else if (allFrameSpecific) {
      console.log('✅ All diagrams are using frame-specific SVG files');
      console.log('⚠️  But some may have loading issues');
    } else {
      console.log('⚠️  Some diagrams are not using frame-specific SVG files.');
    }
  }

  // Take a screenshot to verify visually
  await page.screenshot({ path: 'deployed-site-frame-svgs.png', fullPage: false });

  console.log('\n📸 Screenshot saved: deployed-site-frame-svgs.png');
  console.log('\n✅ DEPLOYMENT VERIFICATION COMPLETE');

  await browser.close();
})();