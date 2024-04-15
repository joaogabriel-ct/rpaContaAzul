from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://login.contaazul.com/#/")
    page.locator("input[type=\"email\"]").fill("ti@referenciaseguros.com.br")
    page.locator("input[type=\"password\"]").fill("KsUBfR9TFYy2cOAe33fp@")
    page.get_by_role("button", name="Entrar").click()
    page.wait_for_timeout(5000)
    page.goto("https://app.contaazul.com/#/ca/visao-geral")
    page.wait_for_timeout(2500)
    page.wait_for_timeout(5000)
    page.frame_locator("#tracksale-iframe").get_by_role("link", name="X").click()

    page.wait_for_timeout(2500)
    page.locator("#NEGOTIATIONS").get_by_text("Vendas", exact=True).click()
    
    page.get_by_role("treeitem", name="Contratos").click()
    page.get_by_role("button", name="Mais filtros").click()
    page.locator("#gateway span").filter(has_text="Cliente").click()
    page.get_by_role("tooltip", name="Carregando...").get_by_role("textbox").fill("31391505000158")
    page.get_by_role("button", name="CAMILA CRISTOVAO NUNES").click()
    page.get_by_role("button", name="Aplicar").click()
    x = page.locator('//*[@id="gateway"]/section/div[3]/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/table/tbody/tr[*]').count()
    for i in range(x):
        page.locator(".ds-u-padding--sm").nth(i).click()
        page.wait_for_timeout(5000)
        page.goto("https://app.contaazul.com/#/ca/visao-geral")
    
    page.wait_for_timeout(5000)
    page.get_by_role("button", name="Editar contrato").click()
    page.get_by_role("button", name="ALEXANDRE").click()
    page.locator("fieldset").filter(has_text="Informações da venda Tipo da").get_by_role("textbox").nth(1).click()
    page.get_by_role("button", name="ALEXANDRE").click()
    page.get_by_role("button", name="Salvar").click()
    page.get_by_text("Esta e as vendas seguintes").click()
    page.get_by_role("button", name="Salvar").click()

    # ---------------------//*[@id="gateway"]/section/div[3]/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/table
    # //*[@id="gateway"]/section/div[3]/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/table/tbody
    # //*[@id="gateway"]/section/div[3]/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/table/tbody/tr[1]
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
