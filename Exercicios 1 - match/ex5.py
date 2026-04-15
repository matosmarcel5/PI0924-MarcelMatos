def analisar_mensagem(msg):
    msg_lower = msg.lower()
    match msg_lower:
        case "olá"  "ola"  "bom dia":
            return "Saudação"
        case _ if msg_lower.endswith("?"):
            return "Pergunta"
        case _ if "tchau" in msg_lower or "adeus" in msg_lower:
            return "Despedida"
        case _:
            return "Mensagem genérica"
        
print(analisar_mensagem("Tudo bem?"))