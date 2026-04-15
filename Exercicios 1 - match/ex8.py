def operacao(op, n1, n2):
    match op:
        case "soma":
            return n1 + n2
        case "subtrai":
            return n1 - n2
        case "multiplica":
            return n1 * n2
        case "divide":
            return n1 / n2 if n2 != 0 else "Erro: divisão por zero"
        case _:
            return "Operação inválida"
        
print(operacao("divide", 20, 4))