# Função sem o recurso LAMBDA

def soma_numeros(x, y):
    soma = x + y
    return (soma)


print(f"A soma eh: {soma_numeros(6, 9)}")

# Função com o recurso LAMBDA

soma_numeros_lambda = lambda x,y : x + y

print(f"A soma eh: {soma_numeros(12, 5)}")
