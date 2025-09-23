const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();

  console.log('Final check - diagrams should be visible now...\n');

  // Navigate to the introduction page
  await page.goto('https://anton-abyzov.github.io/ai-power/episodes/01-portfolio-no-code/content/00-introduction/');
  await page.waitForTimeout(3000);

  // Check for img elements
  const imgElements = await page.$$eval('img[src*="all-diagrams"]', elements => elements.map(el => ({
    src: el.src,
    naturalWidth: el.naturalWidth,
    naturalHeight: el.naturalHeight,
    displayed: el.getBoundingClientRect().width > 0,
    width: el.getBoundingClientRect().width,
    height: el.getBoundingClientRect().height
  })));

  console.log('✅ DIAGRAMS FOUND:');
  imgElements.forEach((img, i) => {
    console.log(`\n  Diagram ${i + 1}:`);
    console.log(`    Visible: ${img.displayed ? '✓ YES' : '✗ NO'}`);
    console.log(`    Display size: ${Math.round(img.width)}x${Math.round(img.height)}px`);
    console.log(`    Natural size: ${img.naturalWidth}x${img.naturalHeight}px`);
  });

  // Scroll to see all diagrams
  await page.evaluate(() => window.scrollTo(0, 500));
  await page.waitForTimeout(1000);

  // Take screenshot
  await page.screenshot({ path: 'final-diagrams.png', fullPage: false });
  console.log('\n📸 Screenshot saved as final-diagrams.png');

  console.log('\n👀 Browser will stay open for 15 seconds for visual inspection...');
  console.log('   (Diagrams should show the full Excalidraw canvas)');
  await page.waitForTimeout(15000);

  await browser.close();

  const allVisible = imgElements.length > 0 && imgElements.every(img => img.displayed && img.naturalWidth > 0);
  if (allVisible) {
    console.log('\n🎉 SUCCESS: All diagrams are now visible on the deployed site!');
    console.log('Note: They show the full canvas. Frame cropping can be added later.');
  } else {
    console.log('\n⚠️  Issues detected with diagram display');
  }
})();