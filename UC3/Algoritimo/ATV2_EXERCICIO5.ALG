Algoritmo "atv2_exercicio5"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira
// Descrição   : Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar. Considere a cotação do dolar atual.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 03/09/2024
Var
// Seção de Declarações das variáveis 

reais : real
dolar : real
cotacao : real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

cotacao <- 5.64

escreva("Digite o valor da sua carteira em reais aki: ")
leia(reais)

limpatela

dolar <- reais / cotacao

escreva("Seu dinheiro em dolar é: ", dolar)




Fimalgoritmo