from Aluno import aluno
import pandas as pd
import os
#criando o meu objeto
aluno1 = aluno("Ney", 5, 8)
aluno2 = aluno("Lucas", 10, 6)
#apresantando os dados
dados_alunos = ({
    "Nome":[aluno1.nome, aluno2.nome],
    "Nota1":[aluno1.nota1, aluno2.nota2],
    "Nota2":[aluno1.nota2, aluno2.nota2],
    "Media p/Aluno":[aluno1.calcularMedia(), aluno2.calcularMedia()],
    "Frequência Ref.":[0.75, ""],
    "Média Ref.": [6, ""]})
df = pd.DataFrame(dados_alunos)
print("Estes são os dados dos nosso alunos: \n",df)

mn = input("\nVamos verificar se eles foram aprovados? [1]sim ou [2]não \n")

if mn == "1":
   os.system("clear")
   cont = 0
   while cont < 2:     
    print("""\n Selecione o aluno:
    1.{}
    2.{}
    """.format(aluno1.nome, aluno2.nome))
    
    op = input("Qual é a opcão desejada? ")
    os.system("clear")
    cont += 1 
    os.system("clear")

    #selecionar opções
    if (op == "1"):
      print(aluno1.setFrequencia())       
    elif (op == "2"):
      print(aluno2.setFrequencia())    
else:
    print("Até logo!")  