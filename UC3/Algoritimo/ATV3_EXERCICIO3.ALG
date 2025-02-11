Algoritmo "atv3_exercicio3"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira
// Descrição   : Crie um algoritmo que receba como entrada o preço de um produto e um percentual de desconto. O algoritmo deve calcular e exibir o preço final do produto após a aplicação do desconto.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 05/09/2024
Var
// Seção de Declarações das variáveis 

preco : real
porc : real
cent : real
m : real
preco_fin: real


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

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

escreva("o valor final do produto é: ",preco_fin)






Fimalgoritmo