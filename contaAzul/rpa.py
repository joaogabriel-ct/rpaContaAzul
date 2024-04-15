import re
from playwright.async_api import async_playwright


async def alterCloser(name: str, namEmp: str, cnpj: str):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://login.contaazul.com/#/")
        await page.locator("input[type=\"email\"]").fill("sEU_EMAIL")
        await page.locator("input[type=\"password\"]").fill("SUA_SENHA")
        await page.get_by_role("button", name="Entrar").click()
        await page.wait_for_timeout(5000)
        await page.goto("https://app.contaazul.com/#/ca/vendas/contratos")
        
        await page.get_by_role("button", name="Mais filtros").click()
        await page.locator("#gateway span").filter(has_text="Cliente").click()
        await page.get_by_role("tooltip").get_by_role("textbox").click()
        await page.get_by_role("tooltip").get_by_role("textbox").fill(f'{cnpj}')
        await page.get_by_role("button", name=f'{namEmp}').click()
        await page.get_by_role("button", name="Aplicar").click()
        await page.wait_for_timeout(2500)
        x = page.locator('//*[@id="gateway"]/section/div[3]/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/table/tbody/tr[*]').count()
        #x = page.locator(".ds-u-padding--sm").count()
        await page.wait_for_timeout(2500)
        count = await x
        for i in range(count):
            await page.wait_for_timeout(3000)
            await page.locator(".ds-u-padding--sm").first.click()
            await page.wait_for_timeout(5000)
            #await page.locator(".ds-u-padding--sm").click()
            await page.get_by_role("button", name="Editar contrato").click()
            await page.locator("div:nth-child(3) > div:nth-child(4)").click()
            await page.locator("fieldset").filter(has_text="Informações da venda Tipo da").get_by_role("textbox").nth(1).fill(f"{name}")
            await page.get_by_role("button", name=f'{name}').click()
            await page.get_by_role("button", name="Salvar").click()
            await page.get_by_label("Esta e as vendas seguintes").check()
            await page.wait_for_timeout(1500)
            await page.get_by_role("button", name="Salvar").click()
            await page.wait_for_timeout(2500)
            await page.go_back()
        await context.close()
        await browser.close()
        return f'Bot Executado corretamente.'
