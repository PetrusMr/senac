Algoritmo "atv8_exercicio1"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descri��o   : um programa que exiba os primeiros N termos da sequ�ncia de Fibonacci. O valor de N deve ser fornecido pelo usu�rio.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 11/10/2024
Var
// Se��o de Declara��es das vari�veis 
n,c,a, b, fibonacci : inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreva("Digite o numero a ser fibonnaciado ")
leia(n)
limpatela

a <- 0
b <- 1

para c de 1 ate n faca
     fibonacci <- a + b
     
     a <- b
     b <- fibonacci
     escreva(a)



fimpara


Fimalgoritmo