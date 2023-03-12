import time

def fup(x):
	beg = time.time()
	j = 3.141632
	for i in range(x):
		j *=  2 
	end = time.time() - beg
	return end
	
def sup(x):
	while(x!=0):
		x=int(input("Digite um número qualquer ou zero para sair? "))

		t1 = float(fup(x))
		t2 = float(fup(x))
		t3 = float(fup(x))
		t4 = float(fup(x))
		t5 = float(fup(x))
		
		avg = (t1+t2+t3+t4+t5) / 3
		if(x==0):
			break
		print("O tempo médio em milissegundos para calcular: {0:.1f}".format(avg*1000))
x=-1
sup(x)
