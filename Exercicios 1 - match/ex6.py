def estado_servidor(dados):
    match dados:
        case {"status": "ok", "tempo_resposta": t} if t > 200:
            return "Servidor lento"
        case {"status": "ok", "tempo_resposta": _}:
            return "Servidor ativo"
        case {"status": "erro", "tempo_resposta": _}:
            return "Servidor indisponível"
        case _:
            return "Estado desconhecido"
        
print(estado_servidor({"status": "ok", "tempo_resposta": 350}))