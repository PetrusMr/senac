Algoritmo "atv8_exercicio3"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descrição   : Peça ao usuário para inserir um capital inicial, uma taxa de juros e o número de meses, e calcule o valor acumulado usando juros compostos. Exiba o saldo para cada mês até o final do período.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 16/10/2024
Var
// Seção de Declarações das variáveis 
capital, taxa, r : real
meses, c : inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

escreva("informe o capital inicial ")
leia(capital)
limpatela

escreva("informe a taxa ")
leia(taxa)
limpatela

escreva("Informe os meses ")
leia(meses)
limpatela

taxa <- taxa /100

para c de 1 ate meses faca

       r <- capital * (1 + taxa) ^ meses
fimpara

escreva(r)

Fimalgoritmo