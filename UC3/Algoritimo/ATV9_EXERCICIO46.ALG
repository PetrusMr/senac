Algoritmo "atv9_exercicio46"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descri��o   : Crie um programa que calcule e mostre na tela o resultado da soma entre 6 + 8 + 10 + 12 + 14 + ... + 98 + 100.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 21/10/2024
Var
// Se��o de Declara��es das vari�veis 
nm, c, r : inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
nm <- 6

para c de 1 ate 48 faca

     r <- r + nm
     nm <- nm + 2

fimpara
escreva(r)

Fimalgoritmo