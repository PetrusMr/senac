Algoritmo "atv7_exercicio2"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descrição   : Peça ao usuário um número inteiro positivo e calcule e exiba a soma de todos os números de 1 até esse número.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 09/10/2024
Var
// Seção de Declarações das variáveis 


nm, x, r : inteiro


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 


escreva("Digite um numero inteiro e positivo ")
leia(nm)
limpatela

se (nm <= 0) ENTAO
escreva ("Numero n positivo")

senao
      para r de 1 ate nm faca
      x <- x + r

fimpara
fimse
escreva(x)




Fimalgoritmo