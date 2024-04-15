import requests


def cnpjName(cnpj:str):
    url = f"https://n8n-app.referencia.company/webhook/bigDataCNPJ?cnpj={cnpj}"
    headers = {
    "accept": "application/json",
    "API-KEY": "^9SebyRg1kM*DjLDVM^%"
    }