import json
import os
from time import sleep

class Aluno:
    def __init__(self, nome, n1, n2, n3_minimo):
        self.nome = nome
        self.n1 = n1
        self.n2 = n2
        self.n3_minimo = n3_minimo

class GerenciadorAlunos:
    def __init__(self):
        self.arquivo = os.path.join(os.path.dirname(__file__), 'alunos.json')
        if not os.path.exists(self.arquivo):
            with open(self.arquivo, 'w') as f:
                json.dump([], f)

    def adicionar_aluno(self, nome, n1, n2, n3_minimo):
        with open(self.arquivo, 'r') as f:
            alunos = json.load(f)

        alunos.append({'nome': nome, 'n1': n1, 'n2': n2, 'n3_minimo': n3_minimo})

        with open(self.arquivo, 'w') as f:
            json.dump(alunos, f, indent=4)
        print("ALUNO ADICIONADO COM SUCESSO!")

    def listar_por_aluno(self, nome_aluno):
        with open(self.arquivo, 'r') as f:
            alunos = json.load(f)

        for aluno in alunos:
            if aluno['nome'] == nome_aluno:
                print("=" * 100)
                print("DADOS DO ALUNO:")
                print("-" * 100)
                n3_minimo = aluno.get('n3_minimo', 'N/A')
                print(f"NOME: {aluno['nome']}, n1: {aluno['n1']}, n2: {aluno['n2']}, n3_minimo: {n3_minimo}")
                print("*" * 100)
                print("=" * 100)
                return
        
        print("ALUNO NÃO ENCONTRADO!")

    def atualizar_aluno(self, nome_antigo, novo_nome, nova_n1, nova_n2, nova_n3_minimo):
        with open(self.arquivo, 'r') as f:
            alunos = json.load(f)

        for aluno in alunos:
            if aluno['nome'] == nome_antigo:
                aluno['nome'] = novo_nome
                aluno['n1'] = nova_n1
                aluno['n2'] = nova_n2
                aluno['n3_minimo'] = nova_n3_minimo
                break

        with open(self.arquivo, 'w') as f:
            json.dump(alunos, f, indent=4)
        print("ALUNO ATUALIZADO COM SUCESSO!")

    def excluir_aluno(self, nome):
        with open(self.arquivo, 'r') as f:
            alunos = json.load(f)

        alunos = [aluno for aluno in alunos if aluno['nome'] != nome]

        with open(self.arquivo, 'w') as f:
            json.dump(alunos, f, indent=4)
        print("🗑 ALUNO EXCLUÍDO COM SUCESSO!")

    def verifica_aluno(self, nome):
        global lExiste
        lExiste = False
        with open(self.arquivo, 'r') as f:
            alunos = json.load(f)

        for x in alunos:
            if x['nome'] == nome:
                lExiste = True

    def calcular_n3_minimo(self, n1, n2):
        
        limite_n3 = (35 - (n1 + 2 * n2)) / 2
        return limite_n3


def exibir_menu():
    print("\nMENU:")
    print("1. ADICIONAR ALUNO")
    print("2. PESQUISAR ALUNO")
    print("3. ATUALIZAR ALUNO")
    print("4. EXCLUIR ALUNO")
    print("5. SAIR")


def main():
    gerenciador = GerenciadorAlunos()

    while True:
        exibir_menu()
        opcao = input("ESCOLHA UMA OPÇÃO:\n>>>")

        if opcao == "1":
            nome = input("DIGITE O NOME DO ALUNO:\n>>>")
            n1 = float(input("DIGITE A NOTA DO PRIMEIRO TRIMESTRE DE QUALQUER MATÉRIA:\n>>>"))
            n2 = float(input("DIGITE A NOTA DO SEGUNDO TRIMESTRE DA MESMA MATÉRIA:\n>>>"))

            
            n3_minimo = gerenciador.calcular_n3_minimo(n1, n2)

            gerenciador.adicionar_aluno(nome, n1, n2, n3_minimo)

        elif opcao == "2":
            nome_aluno = input("DIGITE O NOME DO ALUNO:\n>>>")
            break
            gerenciador.listar_por_aluno(nome_aluno)
        elif opcao == "3":
            nome_antigo = input("DIGITE O NOME A SER ATUALIZADO:\n>>>")
            gerenciador.verifica_aluno(nome_antigo)
            if lExiste:
                novo_nome = input("DIGITE O NOVO NOME:\n>>>")
                nova_n1 = float(input("DIGITE A NOVA NOTA DO PRIMEIRO TRIMESTRE:\n>>>"))
                nova_n2 = float(input("DIGITE A NOVA NOTA DO SEGUNDO TRIMESTRE:\n>>>"))

                
                nova_n3_minimo = gerenciador.calcular_n3_minimo(nova_n1, nova_n2)

                gerenciador.atualizar_aluno(nome_antigo, novo_nome, nova_n1, nova_n2, nova_n3_minimo)
            else:
                print("ALUNO NÃO ENCONTRADO!")
                sleep(3)
                exibir_menu()
        elif opcao == "4":
            nome = input("DIGITE O NOME DO ALUNO A SER EXCLUÍDO:\n>>>")
            gerenciador.excluir_aluno(nome)
        elif opcao == "5":
            print("SAINDO...")
            sleep(3)
            break
        else:
            print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")


if __name__ == "__main__":
    main()
