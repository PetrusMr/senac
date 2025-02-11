Algoritmo "atv1_exercicio03"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira
// Descrição   : media de notas
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 29/08/2024
Var
// Seção de Declarações das variáveis 
nota1 : real
nota2 : real
nota3 : real
soma : real
media : real


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

escreva("digite a primeira nota: ")
leia(nota1)


escreva("digite a segunda nota: ")
leia(nota2)


escreva("digite a terceira nota: ")
leia(nota3)

soma <- nota1 + nota2 + nota3

media <- soma / 3

escreva ("o resultado da media é: ")
escreva(media)


Fimalgoritmo