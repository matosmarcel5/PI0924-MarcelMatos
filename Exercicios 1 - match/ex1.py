def tipo_dia(dia):
    match dia.lower():
        case "sábado"  "sabado"  "domingo":
            return "Fim de semana"
        case "segunda"  "terça"  "terca"  "quarta"  "quinta"  "sexta":
            return "Dia útil"
        case _:
            return "Dia inválido"
        
print(tipo_dia("domingo"))