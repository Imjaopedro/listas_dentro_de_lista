inventario = []
resposta = "S"

while resposta == "S":
    equipamento = [
        input("digite o nome do equipamento: "),
        float(input("digite o valor: ")),
        int(input("digite o serial do equipamento: ")),
        str(input("digite o departamento responsavel: "))
        ]

    inventario.append(equipamento)
    resposta = input("Deseja continuar? ").upper()


for elemento in inventario:
    print(f"equipamento: {elemento[0]}")
    print(f"valor: {elemento[1]}")
    print(f"serial: {elemento [2]}")
    print(f"departamento: {elemento [3]}")


des_busca = input("deseja buscar um equipamento pelo nome: ").upper()


busca = input("digite o equipamento que deseja buscar: ")

for elemento in inventario:
    if busca == elemento[0]:
        print(f"equipamento: {elemento[0]}")
        print(f"valor: {elemento[1]}")
        print(f"serial: {elemento [2]}")
        print(f"departamento: {elemento [3]}")




depreciacao = input("digite o equipamento que sofrerá depreciação: ")

for elemento in inventario:
    if depreciacao == elemento[0]:
        print(f"o valor antigo é: {elemento[1]}")
        elemento[1] = elemento[1] * 0.9
        print(f"O preço atual é:{elemento[1]}")

eliminar = input("deseja excluir algum item? ").upper()



eliminar_serial= int(input("Digite o serial do equipamento que deseja excluir: "))

for elemento in inventario:
    if eliminar_serial == elemento[2]:
        inventario.remove(elemento)
print("*"*20)
for elemento in inventario:
    print(f"Equipamento: {elemento[0]}")
    print(f"valor: {elemento [1]}")
    print(f"serial: {elemento [2]}")
    print(f"departamento: {elemento [3]}")

for elemento in inventario:
    soma = sum(elemento[0])
    print(f" a soma dos equipamentos é {soma}")


