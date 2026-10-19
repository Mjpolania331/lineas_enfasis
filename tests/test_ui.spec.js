const { test, expect } = require('@playwright/test');

test('Pagina principal carga correctamente', async ({ page }) => {
  await page.goto('http://localhost:80');
  await expect(page).toHaveTitle(/LINEAS-ENFASIS/i);
});
