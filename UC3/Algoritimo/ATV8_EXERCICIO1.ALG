Algoritmo "atv8_exercicio1"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descrição   : um programa que exiba os primeiros N termos da sequência de Fibonacci. O valor de N deve ser fornecido pelo usuário.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 11/10/2024
Var
// Seção de Declarações das variáveis 
n,c,a, b, fibonacci : inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
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