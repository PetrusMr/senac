Algoritmo "atv7_exercicio2"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descri��o   : Pe�a ao usu�rio um n�mero inteiro positivo e calcule e exiba a soma de todos os n�meros de 1 at� esse n�mero.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 09/10/2024
Var
// Se��o de Declara��es das vari�veis 


nm, x, r : inteiro


Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 


escreva("Digite um numero inteiro e positivo ")
leia(nm)
limpatela

se (nm <= 0) ENTAO
escreva ("Numero n positivo")

senao
      para r de 1 ate nm faca
      x <- x + r

fimpara
fimse
escreva(x)




Fimalgoritmo