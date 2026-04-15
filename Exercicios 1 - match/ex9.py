def processar_requisicao(req):
    match req:
        case {"metodo": "GET", "conteudo": _}:
            return "Requisição GET recebida"
        case {"metodo": "POST", "conteudo": c} if c:
            return "Requisição POST com dados válidos"
        case {"metodo": "POST", "conteudo": ""}:
            return "Requisição POST sem dados"
        case _:
            return "Método não suportado"

print(processar_requisicao({"metodo": "POST", "conteudo": ""}))