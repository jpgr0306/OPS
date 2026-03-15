import requests

urls = {
    "PATENTES_CONTEUDO.csv": "https://dadosabertos.inpi.gov.br/download/patentes/PATENTES_CONTEUDO.csv",
    "PATENTES_PRIORIDADES.csv": "https://dadosabertos.inpi.gov.br/download/patentes/PATENTES_PRIORIDADES.csv",
    "PATENTES_DEPOSITANTES.csv": "https://dadosabertos.inpi.gov.br/download/patentes/PATENTES_DEPOSITANTES.csv",
    "PATENTES_PROCURADORES.csv": "https://dadosabertos.inpi.gov.br/download/patentes/PATENTES_PROCURADORES.csv",
    "PATENTES_CLASSIFICACAO_IPC.csv": "https://dadosabertos.inpi.gov.br/download/patentes/PATENTES_CLASSIFICACAO_IPC.csv",
    "PATENTES_INVENTORES.csv": "https://dadosabertos.inpi.gov.br/download/patentes/PATENTES_INVENTORES.csv",
    "PATENTES_DESPACHOS.csv": "https://dadosabertos.inpi.gov.br/download/patentes/PATENTES_DESPACHOS.csv",
    "PATENTES_VINCULOS.csv": "https://dadosabertos.inpi.gov.br/download/patentes/PATENTES_VINCULOS.csv",
    "PATENTES_RENUMERACOES.csv": "https://dadosabertos.inpi.gov.br/download/patentes/PATENTES_RENUMERACOES.csv",
    "PATENTES_DADOS_BIBLIOGRAFICOS.csv": "https://dadosabertos.inpi.gov.br/download/patentes/PATENTES_DADOS_BIBLIOGRAFICOS.csv",
}

for nome, url in urls.items():
    print(f"Baixando {nome}...")
    resp = requests.get(url, timeout=120)
    resp.raise_for_status()  # interrompe se der erro HTTP
    with open(nome, "wb") as f:
        f.write(resp.content)
    print(f"{nome} salvo!")
