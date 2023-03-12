import random
alunoum=input("digite o nome do aluno 1:")
alunodois=input("digite o nome do aluno 2:")
alunotres=input("digite o nome do aluno 3:")
alunoquatro=input("digite o nome do aluno 4:")
var=[alunoum, alunodois, alunotres, alunoquatro]
var = random.sample(var, k=4)
print(var)
var = random.sample(var, k=3)
print(var)
var = random.sample(var, k=2)
print(var)
var = random.sample(var, k=1)
print(var)