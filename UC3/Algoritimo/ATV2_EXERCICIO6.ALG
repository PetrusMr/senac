Algoritmo "atv2_exercicio6"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira
// Descri��o   : Fa�a um algoritmo que leia a largura e altura de uma parede, calcule e mostre a �rea a ser pintada e a quantidade de tinta necess�ria para o servi�o, sabendo que cada litro de tinta pinta uma �rea de 2metros quadrados.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 03/09/2024
Var
// Se��o de Declara��es das vari�veis 

altura, largura, area : real
litro : inteiro

r: real


Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
litro <- 2

escreva("qual � a altura da parede?: ")
leia(altura)

limpatela

escreva("qual a largura da parede?: ")
leia(largura)

limpatela

area <- altura * largura

r <- area / litro

escreva("a quantidade de latas de tinta gasta ser�: ", r)





Fimalgoritmo