import os

mensagem = []

nome = input("Nome: ")

while True:
    #limpar terminal
    os.system('cls')

    if len(mensagem) > 0:
        for m in mensagem:
            print(m['nome'], "-", m['texto'])

    print("-------------------------")

    #obtendo texto
    texto = input ("mensagem: ") 
    if texto == "fim":
        break

    #adicionando mensagem na lista  
    mensagem.append({
        "nome":nome,
        "texto": texto
    })