Algoritmo "atv1_exercicio04"
// Disciplina   : UC3 ALGORITIMOS
// Professor   :Mateus de Paula Pereira 
// Descri��o   : calcula metade e o dobro
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 30/08/2024
Var
// Se��o de Declara��es das vari�veis 

numero : inteiro
dobro : real
r : real

operacao : caracter


Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 

dobro <- 2


escreva("coloque o numero inteiro")
leia(numero)

escreva ("digite a opera��o ( * / )")
leia(operacao)

escolha operacao

caso "*"
   r <- numero * dobro
     
caso "/"
   r <- numero / dobro



fimescolha
escreva("O resultado �: " )
escreva(r)

Fimalgoritmo