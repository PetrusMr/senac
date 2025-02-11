Algoritmo "atv2_exercicio6"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira
// Descrição   : Faça um algoritmo que leia a largura e altura de uma parede, calcule e mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2metros quadrados.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 03/09/2024
Var
// Seção de Declarações das variáveis 

altura, largura, area : real
litro : inteiro

r: real


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
litro <- 2

escreva("qual é a altura da parede?: ")
leia(altura)

limpatela

escreva("qual a largura da parede?: ")
leia(largura)

limpatela

area <- altura * largura

r <- area / litro

escreva("a quantidade de latas de tinta gasta será: ", r)





Fimalgoritmo