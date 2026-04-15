def tipo_dado(valor):
    match valor:
        case int():
            return "Número inteiro"
        case float():
            return "Número decimal"
        case str() as s if s.isdigit():
            return "String numérica"
        case str():
            return "String textual"
        case list():
            return "Lista"
        case _:
            return "Tipo desconhecido"
        
print(tipo_dado([10, 20, 30]))