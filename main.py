import os

lista = []

def adicionarItem(titulo, descricao):
    lista.append({"titulo": titulo, "descricao": descricao, "situacao": " "})
    print("Item adicionado com sucesso!")

    return 0

def mostrarLista():
    os.system("cls" if os.name == "nt" else "clear")

    if not lista:
        print("Não há itens adicionados na lista...")
    else:
        for indice, item in enumerate(lista, start=1):
            print(f"{indice}. {item['titulo']}: {item['descricao']} [ {item['situacao']} ]")

    return 0

while True:
    print("======== TO-DO LIST ========")
    print("Escolha sua opção abaixo")
    print("[1] Adicionar item na lista")
    print("[2] Remover item da lista")
    print("[3] Concluir tarefa")
    print("[4] Ver sua lista")
    print("[5] Limpar lista")
    print("[6] Sair")
    try:
        opcao = int(input("Digite a sua opção: "))
    except ValueError:
        os.system("cls" if os.name == "nt" else "clear")
        print("Digite apenas números válidos!")
        continue

    match opcao:
        case 1:
            os.system("cls" if os.name == "nt" else "clear")

            print("Digite um título simples para seu item")
            titulo = input()
            print("Digite a descrição do seu item")
            descricao = input()

            adicionarItem(titulo, descricao)

        case 2:
            mostrarLista()

            if lista:
                try:
                    num = int(input("Qual item deseja remover? "))
                    lista.pop(num-1)
                except IndexError:
                    print("Você digitou um número que não se encaixa ou não existe na lista!")
                except ValueError:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("Digite apenas números válidos!")
                    continue

        case 3:
            mostrarLista()

            if lista:
                try:
                    num = int(input("Qual item deseja concluir? "))
                    lista[num-1] = {"titulo": lista[num-1]["titulo"], "descricao": lista[num-1]["descricao"], "situacao": "X"}
                    print("Tarefa concluída com sucesso, parabéns!")
                except ValueError:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("Digite apenas números válidos!")
                    continue
            else:
                print("Não há nenhum item da lista para ser concluído...")

        case 4:
            mostrarLista()

        case 5:
            os.system("cls" if os.name == "nt" else "clear")
            opcao = input("Tem certeza que deseja apagar a sua lista? [s/n] ").lower()
            if opcao == "s":
                print("Lista limpa com sucesso!")
                lista = []   

        case 6:
            os.system("cls" if os.name == "nt" else "clear")

            print("Obrigado por usar o TO-DO LIST!")
            break

        case _:
            print("Opção incorreta!")