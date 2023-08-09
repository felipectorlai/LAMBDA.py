# Funçãp sem o recurso LAMBDA

def retorna_maior(a,b):
    if (a > b):
        return (a)
    else:
        return (b)

print(f"O maior valor é: {retorna_maior(8, 4)}")

# Função com o recurso LAMBDA

retorna_maior_lamda = lambda a,b: a if (a > b) else b

print(f"O maior valor é: {retorna_maior(3, 15)}")
