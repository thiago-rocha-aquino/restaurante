import os
rest = [] # restaurantes
def exibir_nome_programa(): #nome do app
   print("       🇸​​​​​🇦​​​​​🇧​​​​​🇴​​​​​🇷​​​​​ 🇪​​​​​🇽​​​​​🇵​​​​​🇷​​​​​🇪​​​​​🇸​​​​​🇸​​​​\n​")

def nome_opcoes():  #opções para o usuario escolher
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def finalizar(): # opção 4, para finalizar
    os.system("cls")
    print("finalizando app\n")

def opcao_inv(): # caso o usuario digite acima de 4 ou uma string
    print("opção inválida!\n")
    input("digite qualquer tecla")
    main()

def listar_rest(): # opção 2 para ver os restaurantes já listados no app
    os.system("cls")
    print("listando os retaurantes\n")
    for rest in rest:
        print(f".{rest}")
    input("\ndigite qualquer tecla")
    main()

    pass    

def escolher_opcoes(): # funcionalidade das opções para o usuario escolher
    try:  
        opcao = int(input("digite uma opção: "))

        if ( opcao == 1):
            cadastrar_rest()
        elif (opcao == 2):
            listar_rest()
        elif( opcao == 3):
            print("#")
        elif ( opcao == 4):
            finalizar()    
        else:
            opcao_inv()
    except: 
        opcao_inv()  

def cadastrar_rest(): # opção 1 para cadastar clientes
    os.system("cls")
    print("cadastro de novos restaurantes\n")
    nome_res = input("digite o nome do restaurante que deseja cadastrar:\n ")
    rest.append(nome_res)
    print(f"o restaurante {nome_res} foi cadastrado!\n")
    input("digite uma tecla para voltar ao menu principal: s")
    main()
    

def main():
    os.system("cls")
    exibir_nome_programa()
    nome_opcoes()
    escolher_opcoes()

if __name__ == "__main__":
    main()
