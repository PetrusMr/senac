Algoritmo "atv5_exercicio5"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descri��o   : algoritmo que leia um ano e informe se ele � bissexto ou n�o. Um ano � bissexto se for divis�vel por 4 e n�o for divis�vel por 100, exceto se tamb�m for divis�vel por 400.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 04/10/2024
Var
// Se��o de Declara��es das vari�veis 
ano  : inteiro


Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 



escreva("Digite o ano ")
leia(ano)

limpatela

se (ano % 4 = 0 ) e (ano % 100 <> 0 ) ou (ano % 400 = 0) entao
   escreva("O ano � bissexto")
   
senao
     escreva("O ano n�o � bissexto")

fimse


Fimalgoritmo