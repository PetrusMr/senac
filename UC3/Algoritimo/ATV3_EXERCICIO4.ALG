Algoritmo "atv3_exercicio4"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira
// Descri��o   : Escreva um algoritmo que calcule a m�dia ponderada de tr�s notas fornecidas pelo usu�rio. O usu�rio tamb�m deve informar as notas e o peso de cada nota. O algoritmo deve exibir a m�dia ponderada ao final.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 05/09/2024
Var
// Se��o de Declara��es das vari�veis 
peso1, peso2, peso3, nota1, nota2, nota3, r, mediac, mediab :real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 

escreva("digite o peso 1: ")
leia(peso1)

limpatela

escreva("digite o peso 2: ")
leia(peso2)

limpatela

escreva("digite o peso 3: ")
leia(peso3)

limpatela

escreva("digite a nota 1: ")
leia(nota1)

limpatela

escreva("digite a nota 2: ")
leia(nota2)

limpatela

escreva("digite a nota 3: ")
leia(nota3)

limpatela

mediac<- peso1 * nota1 + peso2 * nota2 + peso3 * nota3

mediab<- peso1 + peso2 + peso3

r<- mediac / mediab

escreva("o resultado  da media �: ",r)





Fimalgoritmo