Algoritmo "atv4_exercicio2"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira
// Descri��o   : Crie um algoritmo que leia o valor de um produto e aplique um desconto de 10% caso o valor seja superior a R$100. Caso contr�rio, exiba o valor sem desconto.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 02/10/2024
Var
// Se��o de Declara��es das vari�veis 
valor : real


desconto : real
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 


escreval("De o valor do produto")
leia(valor)

limpatela

se (valor > 100) entao
   desconto<- valor * 10
   desconto <- desconto /100
   desconto <- valor - desconto
   escreval("O valor com desconto � de: ", desconto)

senao
     escreva("O valor do produto � de: ", valor)



fimse




Fimalgoritmo