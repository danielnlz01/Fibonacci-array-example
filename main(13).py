numero=int(input())
n1=0
n2=1
lista=[n1,n2]
while numero<0:
  numero=int(input())
for i in range (0,numero-2):
  #Calc fibonacci
  fib=n1+n2
  lista.append(fib)
  n1=n2
  n2=fib
if numero==0:
  lista=[]
  print(lista)
elif numero>0:
  print(lista)