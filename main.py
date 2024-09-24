'''---> Comentário de Bloco
Título: Revisão de Python
Autor: Sofia.
Data: 2024.04.02
'''
# --> Comentário de linha
# Objetivo: Revisar os fundamentos de Programação em Python
print('Hello Word!')


# Entrada --> input()
nome = input('Digite seu nome: ')
print('Você disse:', nome)
valor1 = int(input('digite um valor: '))
valor2 = int(input('Digite outro valor: '))
total = valor1 + valor2
print('Soma dos valores digitados é:', total)


# Saída --> print()
print('Soso') # 'string'
print( '100 + 100') # 'str'
print(100 + 100) # operação

# Variáveis --> espaço de memória que armazena valores temporariamente
# str --> Armazena textos e caracteres
nome = 'Sionara'
print (' A variavel nome é do tipo:', type(nome), 'e tem armazenado o valor: %s' %nome)
# int --> armazena números inteiros positivos e negativos
valorX = -81
print('Armazena variável valor X é do tipo:', type (valorX), 'e tem armazenado o valor: %d' %valorX )
# float --> Armazena nu´mero de ponto flutuante positivios e negativos --> NÃO USA , USA .
pi = 3.141559
print('A variável pi é do tipo:', type(pi), 'e tem armazenado o valor: %.2f' %pi)
# bool --> Armazena True ou False
teste = 10 > 50
print('A variável teste é do tipo:', type(teste), 'e tem armazenado o valor:', teste)

# Operadores 
# Aritméticos --> +, -, *, /, **, //, %
print(5*5) 
print(15/4) # --> resultado float
print(10//3) # --> resultado int 
print(10%4)
# Atribuição
A = 10 # --> = (RECEBE)
A += 1 # --> INCREMENTO SOMA 1
A -= 1 # --> DECREMENTO DIMINUI 1
# rELACIONAIS --> fAZEM COMPARAÇÃO E RETORNAM TRUE OU fALSE
A == 10 # == é igual == True
A != 10 # diferente == False
# >; <; >=; <=
# Lógicos --> Concatenação de operadores relacionais 
# and == e; or == ou; not == não

# Repetição
# laço for --> Quando eu sei quantas vezes vai repetir
for i in range(11, 102, 2):
  print(i)

palavra = 'Programação'
for letra in palavra:  
  print(letra)

tecla = 1
while tecla != 0: # --> Repete até a condição ser Falsa
  tecla = int(input('Digite um número: '))

# Condição --> if; else; elif
idade = int(input('Informe a idade: '))
if idade >= 18: # Testa e faz se o resultado True
  print('pode ir pro Bailão!')
elif idade >= 16: # Faz se o if == False e o elif == True
  print('Vai pro Bailão com a Mamãe e o Papai!')
else: # Faz se o resultado do if for == a False
  print('Não pode ir pro Bailão hoje!')
  
# Função --> def
def soma(X, Y):    
  R = X + Y
  return R

print(soma(10,5))
print(soma(100,50))
A = int(Input('Digite um valor: '))
B = int(input('Digite outro valor: '))
print('Soma de %d e %d é igual a %d' %(A, B, (soma(A,B))))



