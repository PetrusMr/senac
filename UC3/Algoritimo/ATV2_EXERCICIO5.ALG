Algoritmo "atv2_exercicio5"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira
// Descri��o   : Fa�a um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos d�lares ela pode comprar. Considere a cota��o do dolar atual.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 03/09/2024
Var
// Se��o de Declara��es das vari�veis 

reais : real
dolar : real
cotacao : real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 

cotacao <- 5.64

escreva("Digite o valor da sua carteira em reais aki: ")
leia(reais)

limpatela

dolar <- reais / cotacao

escreva("Seu dinheiro em dolar �: ", dolar)




Fimalgoritmo