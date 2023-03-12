import random
alunoum=input("digite o nome do aluno 1:")
alunodois=input("digite o nome do aluno 2:")
alunotres=input("digite o nome do aluno 3:")
alunoquatro=input("digite o nome do aluno 4:")

var = random.sample([alunoum, alunodois, alunotres, alunoquatro], k=4)
print(var)