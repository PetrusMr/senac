Algoritmo "atv1_exercicio04"
// Disciplina   : UC3 ALGORITIMOS
// Professor   :Mateus de Paula Pereira 
// Descrição   : calcula metade e o dobro
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 30/08/2024
Var
// Seção de Declarações das variáveis 

numero : inteiro
dobro : real
r : real

operacao : caracter


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

dobro <- 2


escreva("coloque o numero inteiro")
leia(numero)

escreva ("digite a operação ( * / )")
leia(operacao)

escolha operacao

caso "*"
   r <- numero * dobro
     
caso "/"
   r <- numero / dobro



fimescolha
escreva("O resultado é: " )
escreva(r)

Fimalgoritmo