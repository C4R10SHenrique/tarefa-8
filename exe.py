# Passo 1: Criar a Lista de Números
numeros = list(range(1, 21))  

# Passo 2: Gerar os Quadrados dos Pares e Ímpares
quadrados_pares = [x**2 for x in numeros if x % 2 == 0]  
quadrados_impares = [x**2 for x in numeros if x % 2 != 0]  

# Passo 3: Armazenar os Dados no Dicionário
quadrados_dict = {
    'Pares': quadrados_pares,      
    'Ímpares': quadrados_impares   
}

# Passo 4: Exibir os Resultados
print("Quadrados dos Números Pares de 1 a 20:")
print(quadrados_dict['Pares'])   
print("\nQuadrados dos Números Ímpares de 1 a 20:")
print(quadrados_dict['Ímpares'])  