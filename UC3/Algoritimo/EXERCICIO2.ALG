Algoritmo "exercicio2"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira
// Descri��o   : Desenvolva um algoritmo que solicite dois n�meros inteiros �mpares ao usu�rio e calcule a soma desses n�meros. Caso algum dos n�meros informados n�o seja �mpar, o algoritmo deve exibir uma mensagem de erro e solicitar que o usu�rio insira n�meros �mpares. Ao final o algoritmo deve exibir o resultado da soma.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 05/09/2024
Var
// Se��o de Declara��es das vari�veis 
numero1, numero2 : inteiro
soma : inteiro


Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 

funcao ehImpar(num: inteiro) : logico
inicio
retorne (num % 2 <> 0)
fimfuncao

escreva("Digite o primeiro n�mero �mpar: ")
leia(numero1)

limpatela

enquanto (nao ehImpar(numero1)) faca
escreva("N�mero inv�lido. Por favor, digite um n�mero �mpar: ")
leia(numero1)
fimenquanto

limpatela

escreva("Digite o segundo n�mero �mpar: ")
leia(numero2)

limpatela

enquanto (nao ehImpar(numero2)) faca
escreva("N�mero inv�lido. Por favor, digite um n�mero �mpar: ")
leia(numero2)

limpatela

fimenquanto

soma := numero1 + numero2

escreva("A soma dos n�meros �mpares �: ", soma)
Fimalgoritmo