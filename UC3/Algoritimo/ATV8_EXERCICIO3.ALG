Algoritmo "atv8_exercicio3"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descri��o   : Pe�a ao usu�rio para inserir um capital inicial, uma taxa de juros e o n�mero de meses, e calcule o valor acumulado usando juros compostos. Exiba o saldo para cada m�s at� o final do per�odo.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 16/10/2024
Var
// Se��o de Declara��es das vari�veis 
capital, taxa, r : real
meses, c : inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 

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