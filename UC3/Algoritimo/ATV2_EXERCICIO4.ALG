Algoritmo "atv2_exercicio4"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira
// Descrição   : Faça um programa que leia um número inteiro e mostre o seu antecessor e seu sucessor.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 03/09/2024
Var
// Seção de Declarações das variáveis 
numero, antecessor, sucessor : Inteiro


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...

escreva("Escolha um numero inteiro ")
leia(numero)

limpatela

antecessor <- numero - 1
sucessor <- numero + 1

escreva("seu numero é: ", numero, " com o antecessor: ", antecessor, " e seu sucessor: ", sucessor )




Fimalgoritmo