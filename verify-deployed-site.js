const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  console.log('🌐 VERIFYING DEPLOYED GITHUB PAGES SITE\n');

  // Test the deployed page
  await page.goto('https://anton-abyzov.github.io/ai-power/episodes/01-portfolio-no-code/content/00-introduction/');
  await page.waitForTimeout(3000);

  // Check for our converted diagram embeds with data-testid
  const diagramDivs = await page.$$eval('div[data-testid="excalidraw-diagram"]', elements =>
    elements.map(el => {
      const img = el.querySelector('img');
      return {
        frameId: img?.getAttribute('data-frame-id'),
        frameName: img?.getAttribute('data-frame-name'),
        src: img?.src?.split('/').pop(),
        displayed: img?.getBoundingClientRect().width > 0,
        naturalWidth: img?.naturalWidth,
        naturalHeight: img?.naturalHeight,
        complete: img?.complete
      };
    })
  );

  console.log('📊 DIAGRAMS ON DEPLOYED SITE:');
  if (diagramDivs.length === 0) {
    console.log('  ❌ No diagrams found with data-testid="excalidraw-diagram"');
  } else {
    let allWorking = true;
    diagramDivs.forEach(diagram => {
      const status = diagram.displayed && diagram.complete ? '✅' : '❌';
      if (!diagram.displayed || !diagram.complete) allWorking = false;
      console.log(`  ${status} ${diagram.frameName} (${diagram.frameId})`);
      console.log(`     Source: ${diagram.src}`);
      console.log(`     Size: ${diagram.naturalWidth}x${diagram.naturalHeight}`);
      console.log(`     Loaded: ${diagram.complete}`);
    });

    if (allWorking) {
      console.log('\n🎉 SUCCESS! All diagrams are displaying correctly on the deployed site!');
    } else {
      console.log('\n⚠️  Some diagrams are not displaying correctly.');
    }
  }

  // Take screenshot of the deployed page
  await page.screenshot({ path: 'deployed-site-verification.png', fullPage: false });

  console.log('\n📸 Screenshot saved: deployed-site-verification.png');
  console.log('\n✅ DEPLOYMENT VERIFICATION COMPLETE');

  await browser.close();
})();