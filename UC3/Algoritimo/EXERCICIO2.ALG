Algoritmo "exercicio2"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira
// Descrição   : Desenvolva um algoritmo que solicite dois números inteiros ímpares ao usuário e calcule a soma desses números. Caso algum dos números informados não seja ímpar, o algoritmo deve exibir uma mensagem de erro e solicitar que o usuário insira números ímpares. Ao final o algoritmo deve exibir o resultado da soma.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 05/09/2024
Var
// Seção de Declarações das variáveis 
numero1, numero2 : inteiro
soma : inteiro


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

funcao ehImpar(num: inteiro) : logico
inicio
retorne (num % 2 <> 0)
fimfuncao

escreva("Digite o primeiro número ímpar: ")
leia(numero1)

limpatela

enquanto (nao ehImpar(numero1)) faca
escreva("Número inválido. Por favor, digite um número ímpar: ")
leia(numero1)
fimenquanto

limpatela

escreva("Digite o segundo número ímpar: ")
leia(numero2)

limpatela

enquanto (nao ehImpar(numero2)) faca
escreva("Número inválido. Por favor, digite um número ímpar: ")
leia(numero2)

limpatela

fimenquanto

soma := numero1 + numero2

escreva("A soma dos números ímpares é: ", soma)
Fimalgoritmo