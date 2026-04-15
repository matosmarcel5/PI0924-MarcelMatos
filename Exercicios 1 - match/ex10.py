def jogo(j1, j2):
    match (j1, j2):
        case (a, b) if a == b:
            return "Empate"
        case ("pedra", "tesoura") , ("tesoura", "papel") , ("papel", "pedra"):
            return "Jogador 1 venceu"
        case _:
            return "Jogador 2 venceu"

print(jogo("pedra", "tesoura"))