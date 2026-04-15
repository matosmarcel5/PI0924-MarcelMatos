def classificar_produto(produto):
    match produto:
        case {"categoria": "eletrônico", "preco": p} if p > 1000:
            return "Produto de luxo"
        case {"categoria": "eletrônico", "preco": _}:
            return "Produto comum"
        case {"categoria": "alimento", "preco": _}:
            return "Produto alimentar"
        case _:
            return "Categoria desconhecida"
        
print(classificar_produto({"categoria": "eletrônico", "preco": 1500}))