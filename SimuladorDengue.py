import random
import os
import sys
import re
import time

tabela = []

# criar uma classe contaminação para iniciar o processo de contaminaçao e de cura da pessoa
class Tabelafuncao:
    def print_tabelainicio():
        print(" --------------------------------------------------------------------------------------------------")
        print("Cidade           | Quantidade de Mosquitos | Chance De Contaminação | Tempo para obter tratamento. ")
        print("---------------------------------------------------------------------------------------------------")
        print("São Paulo        |       15000             | 5%                     | 14 dias                      ")
        print("Serra            |       10000             | 2%                     | 7 dias                       ")
        print("Vitoria          |       20000             | 1%                     | 15 dias                      ")
        print("Ribeirão Preto   |       15000             | 5%                     | 12 dias                      ")
        print("Bauru            |       10000             | 2%                     | 9 dias                       ")
        print("Santo André      |       20000             | 1%                     | 13 dias                      ")
        print("Sorocaba         |       15000             | 5%                     | 14 dias                      ")
        print("Santos           |       10000             | 2%                     | 8 dias                       ")
        print("Campinas         |       20000             | 1%                     | 7 dias                       ")
        print(" --------------------------------------------------------------------------------------------------")

    def exibir_tabela(tabela):
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Nome                                     | Cidade                  | Se sobreviveu ou faleceu | Tempo utilizado na simulação | Crescimento Diario dos mosquitos (em %)")
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        for linha in tabela:
            print(f"{linha['Nome']:<40} | {linha['Cidade']:<23} | {linha['Status']:<24} | {linha['Tempo']:<28} | {linha['Reprodução']:<27}")
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")

class Limpatela:
    def clear_screen():
        if os.name == 'nt':  # para Windows
            os.system('cls')
        else:  # para Unix/Linux/MacOS/BSD/etc
            os.system('clear')

class Verificacontinuação:
    def confirmacontinuacao():
        continuar = input("Deseja continuar? (sim/nao): ")
        if continuar.lower() == 'nao':
            sys.exit()
        if continuar.lower() == 'sim':
            main()
        else:
            voltamenu = input("Digite um comando valido! : (Pressione Enter para voltar) ")
            Verificacontinuação.confirmacontinuacao()
        
    def verificaletra(nome):
        if not re.match(r'^[a-zA-ZÀ-ÿ ]+$', nome):
            voltamenu = input("Digite apenas letras! : (Pressione Enter para voltar ao cadastro do sobrevivente) ")
            Limpatela.clear_screen()
            menusimulacao()
        if len(nome) > 40:
            voltamenu = input("O nome que você digitou é grande demais! : (Pressione Enter para voltar ao cadastro do sobrevivente) ")
            Limpatela.clear_screen()
            menusimulacao()
    
    def verificanumero(idade):
        if not re.fullmatch(r'-?[\d.,]+', idade):
            voltamenu = input("Digite apenas números! : (Pressione Enter para voltar ao cadastro do sobrevivente) ")
            Limpatela.clear_screen()
            menusimulacao()
        idade = int(idade)
        if idade < 0:
            voltamenu = input("Digite apenas números positivos! : (Pressione Enter para voltar ao cadastro do sobrevivente) ")
            Limpatela.clear_screen()
            menusimulacao()
        if idade > 100:
            voltamenu = input("Digite números de 1 a 100! : (Pressione Enter para voltar ao cadastro do sobrevivente) ")
            Limpatela.clear_screen()
            menusimulacao()
    
    def verificaidade(idade):
        if not re.fullmatch(r'-?[\d.,]+', idade):
            voltamenu = input("Digite apenas números! : (Pressione Enter para voltar ao cadastro do sobrevivente) ")
            Limpatela.clear_screen()
            menusimulacao()
        idade = int(idade)
        if idade < 0:
            voltamenu = input("Digite apenas números positivos! : (Pressione Enter para voltar ao cadastro do sobrevivente) ")
            Limpatela.clear_screen()
            menusimulacao()
        if idade > 120:
            voltamenu = input("Digite números de 1 a 120! : (Pressione Enter para voltar ao cadastro do sobrevivente) ")
            Limpatela.clear_screen()
            menusimulacao()

class Resultadosimulacao:
    def __init__(self, nome, idade, infectado):
        self.nome = nome
        self.infectado = infectado
        self.idade = idade

    def calculo_resultado(self,multiplicamosquito,escolhadias):
        self.multiplicamosquito = self.multiplicamosquito * 100
        self.multiplicamosquito = str(self.multiplicamosquito)
        self.multiplicamosquito = self.multiplicamosquito + "%"
        self.escolhadias = str(self.escolhadias)
        self.escolhadias = self.escolhadias + " " + "dias"
        return self.multiplicamosquito, self.escolhadias 
   
    def mostrar_animacao_procurandotratamento():
        formas_calculando = ['Procurando tratamento.', 'Procurando tratamento..', 'Procurando tratamento...']
        for forma in formas_calculando:
            print(forma, end='', flush=True)  # Exibir a mensagem sem pular para a próxima linha
            time.sleep(1)  # Espera de 1 segundo entre cada forma
            print('\r', end='')  # Move o cursor de volta para o início da linha



class Contaminacao:
    def __init__(self, nomecidade, nome, idade, tempotratamento,escolhadias,multiplicamosquito):
        self.nome = nome
        self.nomecidade = nomecidade
        self.tempotratamento = tempotratamento
        self.idade = idade
        self.escolhadias = escolhadias
        self.multiplicamosquito = multiplicamosquito / 100
        
    def inicia_contaminacao(self, indivi):
        chancemorte = self.calcula_chancemorte(self.idade)
        
        morte = 0  # Inicializa a variável morte
        if indivi.infectado == 1:
            for i in range(self.tempotratamento):
                if Cidade.verificacontaminacao(self,chancemorte) == 1:
                    Resultadosimulacao.mostrar_animacao_procurandotratamento()
                    print("Você Morreu".ljust(30))
                    morte = 1
                    break
            if morte == 1:
                if morte == 1:
                    status = "Faleceu"
                    self.multiplicamosquito, self.escolhadias = Resultadosimulacao.calculo_resultado(self,self.multiplicamosquito,self.escolhadias)               
                nova_linha = {"Nome": self.nome, "Cidade": self.nomecidade, "Status": status, "Tempo": self.escolhadias, "Reprodução": self.multiplicamosquito}
                tabela.append(nova_linha)
                Verificacontinuação.confirmacontinuacao()   
        
        if morte == 0:
            Resultadosimulacao.mostrar_animacao_procurandotratamento()
            print("Parabens você sobreviveu!!!".ljust(30))
            if morte == 0:
                status = "Sobreviveu"
                self.multiplicamosquito, self.escolhadias = Resultadosimulacao.calculo_resultado(self,self.multiplicamosquito,self.escolhadias) 
            nova_linha = {"Nome": self.nome, "Cidade": self.nomecidade, "Status": status, "Tempo": self.escolhadias, "Reprodução": self.multiplicamosquito}
            tabela.append(nova_linha)
            Verificacontinuação.confirmacontinuacao()
    
    def calcula_chancemorte(self, idade):
        if idade < 5:
            return 4
        elif 5 <= idade < 9:
            return 2
        elif 10 <= idade < 14:
            return 6
        elif 15 <= idade < 19:
            return 8
        elif 20 <= idade < 34:
            return 10
        elif 35 <= idade < 49:
            return 12
        elif 50 <= idade < 64:
            return 14
        elif 65 <= idade < 79:
            return 18
        else:
            return 20
    
    def reproduzmosquito(self, mosquitosquantidade, contadias, chancecontaminacao,multiplicamosquito):
        contadias = contadias + 1
        aumentochance = mosquitosquantidade // 100000
        if aumentochance >= 1:
            chancecontaminacao = chancecontaminacao + aumentochance
        mosquitosquantidade = mosquitosquantidade + (mosquitosquantidade * multiplicamosquito)
        return mosquitosquantidade, chancecontaminacao

                

class Pessoa:
    def __init__(self, nome, idade, infectado):
        self.nome = nome
        self.infectado = infectado
        self.idade = idade
    
    def edita_infectado():
        infectado = 1
        
        
class Cidade:
    def __init__(self, nomecidade, nome, qtdmosquitos, chancecontaminacao,tempotratamento,escolhadias,multiplicamosquito):
        self.nome = nome
        self.nomecidade = nomecidade
        self.qtdmosquitos = qtdmosquitos
        self.chancecontaminacao = chancecontaminacao * 100
        self.tempotratamento = tempotratamento
        self.escolhadias = escolhadias
        self.multiplicamosquito = multiplicamosquito / 100

    def exibir_informacoes(self):
        print(f"Cidade: {self.nome}")
        print(f"qtdmosquitos: {self.qtdmosquitos}")
        print(f"chance de contaminaçao: {self.chancecontaminacao}% ")
    
    def verificacontaminacao(self, chancecontaminacao):
        # sorteia um numero entre 1 e 100
        x = random.randint(1, 100)
        # se o numero sorteado for menor ou igual a chancecontaminaçao
        if x <= chancecontaminacao:
            # return positivo
            return 1
        # senao
        else:
            # return negativo
            return 0
    
    def simulardias(self,pessoa,dias):
        # percorrer a quantidade de dias
        for i in range(dias):
            # fazer o sorteio com a porcentagem de contaminaçao da cidade
            self.qtdmosquitos, self.chancecontaminacao = Contaminacao.reproduzmosquito(self,self.qtdmosquitos,i,self.chancecontaminacao,self.multiplicamosquito)
            contaminou = self.verificacontaminacao(self.chancecontaminacao)
            # se infectou
            if contaminou == 1:
                # marcar a pessoa como infectada
                Pessoa.edita_infectado()
                # mostrar que a pessoa foi infectada
                print("Você foi infectado!")
                break      
        # se a pessoa não foi contaminada
        if contaminou == 0:
            # emitir uma mensagem parabenizando a pessoa
            print("Parabens você não foi contaminado!!!")
            morte = 0
            if morte == 0:
                status = "Sobreviveu"
                self.multiplicamosquito, self.escolhadias = Resultadosimulacao.calculo_resultado(self,self.multiplicamosquito,self.escolhadias) 
            nova_linha = {"Nome": self.nome, "Cidade": self.nomecidade, "Status": status, "Tempo": self.escolhadias, "Reprodução": self.multiplicamosquito}
            tabela.append(nova_linha)
            Verificacontinuação.confirmacontinuacao()

def menusimulacao():

    Limpatela.clear_screen()
    nome = input("Digite o seu nome: ")
    Verificacontinuação.verificaletra(nome)
    idade = input("Digite a sua idade:(em anos) ")
    Verificacontinuação.verificaidade(idade)
    idade = int(idade)
    infectado = 0
    individuo = Pessoa(nome,idade,infectado)

    Tabelafuncao.print_tabelainicio()
    
    tempos = {'São Paulo':14, 'Serra':7, 'Vitoria':15, 'Ribeirão Preto':12, 'Bauru':9, 'Santo André':13, 'Sorocaba':14, 'Santos':8, 'Campinas':7}
    mosquitos = {'São Paulo':15000, 'Serra':10000, 'Vitoria':20000, 'Ribeirão Preto':15000, 'Bauru':10000, 'Santo André':20000, 'Sorocaba':15000, 'Santos':10000, 'Campinas':20000}
    contaminacao = {'São Paulo':0.05, 'Serra':0.02, 'Vitoria':0.01, 'Ribeirão Preto':0.05, 'Bauru':0.02, 'Santo André':0.01, 'Sorocaba':0.05, 'Santos':0.02, 'Campinas':0.01}
    
    escolhacidade = str(input("Selecione sua Cidade: "))
    if escolhacidade not in tempos:
        voltamenu = input("Essa cidade não esta disponivel! : (Pressione Enter para voltar ao cadastro do sobrevivente) ")
        Limpatela.clear_screen()
        menusimulacao()
    else:
        escolhadias = input("Selecione a quantidade de dias que deseja ficar na cidade: ")
        Verificacontinuação.verificanumero(escolhadias)
        escolhadias = int(escolhadias)
    
    multiplicamosquito = input("Escolha em quantos % deseja aumentar a reproduçâo dos mosquitos por dia (de 0 a 100%): ")
    Verificacontinuação.verificanumero(multiplicamosquito)
    multiplicamosquito = float(multiplicamosquito)
       
    tempotratamento = tempos[escolhacidade]
    mosquitosquantidade = mosquitos[escolhacidade]
    chancecontaminacao = contaminacao[escolhacidade]
        
    cidade = Cidade(escolhacidade, nome, mosquitosquantidade, chancecontaminacao,tempotratamento,escolhadias,multiplicamosquito)
    cidade.simulardias(individuo, escolhadias)
    contaminacao_instancia = Contaminacao(escolhacidade,nome, idade, tempotratamento,escolhadias,multiplicamosquito)
    contaminacao_instancia.inicia_contaminacao(individuo)


def main():
    Limpatela.clear_screen()
    menu = str(input("Digite INICIAR se deseja iniciar uma nova simulação ou digite TABELA se deseja observar resultados de outras simulaçoes: "))
    if menu.lower() == "iniciar":
        menusimulacao()
    if menu.lower() == "tabela":
        Tabelafuncao.exibir_tabela(tabela)
        Verificacontinuação.confirmacontinuacao()
        
        
    else:
        voltamenu = input("Digite um comando valido: (Pressione Enter para voltar ao menu) ")
        main()



main()

