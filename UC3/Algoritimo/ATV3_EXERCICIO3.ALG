Algoritmo "atv3_exercicio3"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira
// Descri��o   : Crie um algoritmo que receba como entrada o pre�o de um produto e um percentual de desconto. O algoritmo deve calcular e exibir o pre�o final do produto ap�s a aplica��o do desconto.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 05/09/2024
Var
// Se��o de Declara��es das vari�veis 

preco : real
porc : real
cent : real
m : real
preco_fin: real


Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 

cent<- 100

escreva("digite o valor do produto: ")
leia(preco)

limpatela

escreva("digite a % do valor: ")
leia(porc)

limpatela

m <- preco * porc

preco_fin<- m / cent

preco_fin<- preco - preco_fin

escreva("o valor final do produto �: ",preco_fin)






Fimalgoritmo