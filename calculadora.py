import math
import os
import sys
import time
historico = []

def sair():
    print('Finalizando o programa...')
    time.sleep(2.1)
    sys.exit()



def f(n):
    # Se o número for inteiro (ex: 5.0), retorna sem o .0
    # Se for decimal (ex: 5.555), retorna com 2 casas
    return int(n) if n % 1 == 0 else round(n, 2)
    

def voltar_menu():
    while True:
        volt = input('Deseja retornar ao menu? s/n: ').lower()
        if volt == 's':
            return True
        elif volt == 'n':
            return False
        else:
            input('Por favor responda somente com s ou n, tecle Enter para tentar novamente: ')
                    
def exibir_titulo(titulo):
    limpar_tela()
    print(f'{titulo:^50}')
    print('='*50)


def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def opcoes():
    limpar_tela()
    print('='*50)
    print('Calculadora Python😍')
    print('='*50)
    print('*Dica: Para números com decimais, utilize ponto ao invés de virgula. Ex: 1.2, 2.7\n')
    while True:
        try:
            opcao = int(input('Escolha uma das opções abaixo, ou digite 0 para finalizar o programa:\n1- Adição\n2- Subtração\n3- Multiplicação\n4- Divisão\n5- Potenciação\n6- Raiz quadrada\n7- Porcentagem\n8- Histórico de operações\nOpção escolhida: '))
            return opcao
        except ValueError: 
            print('Opção incorreta! Tente novamente')
            time.sleep(1.1)
            limpar_tela()

def adicao():
    while True:
        exibir_titulo('MÓDULO DE ADIÇÃO')
        try:
            n1 = float(input('Digite o primeiro número: '))
            n2 = float(input('Digite o segundo número: '))
            resultado = n1 + n2
            time.sleep(0.5)
            print(f'{f(n1)} + {f(n2)} = {f(resultado)}')
            historico.append(f'{f(n1)} + {f(n2)} = {f(resultado)}')
            #Essa linha de código está presente em todas as operações, e serve para salvar cada uma que foi feita no 'historico[]'
            if voltar_menu():
                break
            else:
                time.sleep(0.7)
                continue
        
        except ValueError:
            print('Por favor digite apenas números, tente novamente...')
            time.sleep(1.2)


def subtracao():
    while True:
        exibir_titulo('MÓDULO DE SUBTRAÇÃO')
        try:
            n1 = float(input('Digite o primeiro número: '))
            n2 = float(input('Digite o segundo número: '))
            resultado = n1 - n2
            time.sleep(0.5)
            print(f'{f(n1)} - {f(n2)} = {f(resultado)}')
            historico.append(f'{f(n1)} - {f(n2)} = {f(resultado)}')
            if voltar_menu():
                break
            else:
                time.sleep(0.7)
                continue
        
        except ValueError:
            print('Por favor digite apenas números, tente novamente...')
            time.sleep(1.2)

def multiplicacao():
    while True:
        exibir_titulo('MÓDULO DE MULTIPLICAÇÃO')
        try:
            n1 = float(input('Digite o primeiro número: '))
            n2 = float(input('Digite o segundo número: '))
            resultado = n1 * n2
            time.sleep(0.5)
            print(f'{f(n1)} X {f(n2)} = {f(resultado)}')
            historico.append(f'{f(n1)} X {f(n2)} = {f(resultado)}')
            if voltar_menu():
                break
            else:
                time.sleep(0.7)
                continue
        
        except ValueError:
            print('Por favor digite apenas números, tente novamente...')
            time.sleep(1.2)


def divisao():
    while True:
        exibir_titulo('MÓDULO DE DIVISÃO')
        try:
            n1 = float(input('Digite o primeiro número: '))
            n2 = float(input('Digite o segundo número: '))
            if n2 == 0:
                resultado_final = '∞ (Infinito)'
                #Divisões feitas por 0 não são aceitas na matemática, por isso adicionei esse seguinte resultado
            else:
                resultado_final = f(n1/n2)
            time.sleep(0.5)
            print(f'{f(n1)} ÷ {f(n2)} = {resultado_final}')
            historico.append(f'{f(n1)} ÷ {f(n2)} = {resultado_final}')
            if voltar_menu():
                break
            else:
                time.sleep(0.7)
                continue
        
        except ValueError:
            print('Por favor digite apenas números, tente novamente...')
            time.sleep(1.2)


def potenciacao():
    while True:
        exibir_titulo('MÓDULO DE POTENCIAÇÃO')
        try:
            base = float(input('Digite a base: '))
            expoente = float(input('Digite o expoente: '))
            time.sleep(0.5)
            if base == 0 and expoente <0:
                print('Essa operação nem é possível, tá querendo quebrar o programa é?😡')
                #Tratamento de entrada do usuário, potências com base 0 e expoentes menores que 0 não são aceitas
                time.sleep(1.8)
                continue
            resultado = math.pow(base, expoente)
            print(f'{f(base)} elevado à {f(expoente)} = {f(resultado)}')
            historico.append(f'{f(base)} ^ {f(expoente)} = {f(resultado)}')
            if voltar_menu():
                break
            else:
                time.sleep(0.7)
                continue
        
        except ValueError:
            print('Entrada inválida ou operação impossível nos números reais.')
            time.sleep(1.2)

def raiz_quadrada():
    while True:
        exibir_titulo('MÓDULO DE RAIZ QUADRADA')
        try:
            n1 = float(input('Digite um número para descobrir sua raiz quadrada: '))
            if n1 <0:
                print ('Raiz de número negativo não rola mano(a)😡')
                #Tratamento de entrada caso o usuário digite número negativo, que não são aceitos em operações com números reais
                time.sleep(1.8)
                continue
            resultado_final = math.sqrt(n1)
            time.sleep(0.5)
            print(f'√{f(n1)} = {f(resultado_final)}')
            historico.append(f'√{f(n1)} = {f(resultado_final)}')
            if voltar_menu():
                break
            else:
                time.sleep(0.7)
                continue
        
        except ValueError:
            print('Por favor digite apenas números, tente novamente...')
            time.sleep(1.2)

def porcentagem():
    while True:
        exibir_titulo('MÓDULO DE PORCENTAGEM')
        try:
            n1 = float(input('Digite um valor: '))
            n2 = float(input('Digite o valor da porcentagem que deseja: '))
            resultado_porcen = (n1 * n2)/100
            time.sleep(0.5)
            print(f'{f(n2)}% de {f(n1)} = {f(resultado_porcen)}')
            historico.append(f'{f(n2)}% de {f(n1)} = {f(resultado_porcen)}')
            if voltar_menu():
                break
            else:
                time.sleep(0.7)
                continue
        
        except ValueError:
            print('Por favor digite apenas números, tente novamente...')
            time.sleep(1.2)

def historico_op():
    exibir_titulo('OPERAÇÕES REALIZADAS')
    if not historico:
        print('Nenhuma operação realizada até o momento...')
    else:
        for contas in historico:
            print(f'• {contas}')
            #mostra cada uma das operações feitas, pontuando cada uma
    input('Pressione Enter para voltar ao menu: ')

def menu_principal():
    while True: 
        limpar_tela()
        escolha = opcoes()
        time.sleep(0.6)
        match escolha:
            case 1:
                adicao()
            case 2:
                subtracao()
            case 3:
                multiplicacao()
            case 4:
                divisao()
            case 5:
                potenciacao()
            case 6:
                raiz_quadrada()
            case 7:
                porcentagem()
            case 8:
                historico_op()
            case 0:
                sair()
            case _:
                print('Opção inválida, tente novamente')
                time.sleep(1.2)
                

if __name__ == '__main__':
    menu_principal()
    # Garante que o menu só seja executado se o arquivo for rodado diretamente.
    # Evita que o programa inicie sozinho caso as funções sejam importadas por outro script.
