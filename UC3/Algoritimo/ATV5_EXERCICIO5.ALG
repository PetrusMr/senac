Algoritmo "atv5_exercicio5"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descrição   : algoritmo que leia um ano e informe se ele é bissexto ou não. Um ano é bissexto se for divisível por 4 e não for divisível por 100, exceto se também for divisível por 400.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 04/10/2024
Var
// Seção de Declarações das variáveis 
ano  : inteiro


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 



escreva("Digite o ano ")
leia(ano)

limpatela

se (ano % 4 = 0 ) e (ano % 100 <> 0 ) ou (ano % 400 = 0) entao
   escreva("O ano é bissexto")
   
senao
     escreva("O ano não é bissexto")

fimse


Fimalgoritmo