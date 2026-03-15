import requests

urls = {
    "PATENTES_PRIORIDADES.csv": "https://dadosabertos.inpi.gov.br/download/patentes/PATENTES_PRIORIDADES.csv"
}

for nome, url in urls.items():
    print(f"Baixando {nome}...")
    resp = requests.get(url, timeout=120)
    resp.raise_for_status()  # interrompe se der erro HTTP
    with open(nome, "wb") as f:
        f.write(resp.content)
    print(f"{nome} salvo!")
