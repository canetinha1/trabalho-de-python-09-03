nome =input( "Digite o nome do estudante: ")

soma_notas = 0
quantidade_trimestre = 3
meta_aprovação = 180

for i in range(1, quantidade_trimestre + 1):
    nota = float(input(f"Informe a nota do {i}º trimestre"))
soma_notas += nota

print("-" * 30)
print(f"Estudante: {nome}") 
print(f"Pontuação Total: {soma_notas}")

if soma_notas >= meta_aprovação:
    print("Status: Aprovado! Parabéns!!")
else:
    pontos_faltantes = meta_aprovação - soma_notas
    print("Status: REPROVADO!")
    print(f"faltaram {pontos_faltantes} pontos para atingir o mínimo de {meta_aprovação}")