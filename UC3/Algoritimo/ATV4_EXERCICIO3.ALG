Algoritmo "atv4_exercicio3"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira
// Descri��o   : um algoritmo que leia tr�s notas de um aluno, calcule a m�dia e informe se ele foi aprovado (m�dia maior ou igual a 7) ou reprovado (m�dia inferior a 7).
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 02/10/2024
Var
// Se��o de Declara��es das vari�veis 
nota1, nota2, nota3, resultado: real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 

escreval("Digite o valor da nota1")
leia(nota1)

limpatela

escreval("Digite o valor da nota2")
leia(nota2)

limpatela

escreval("Digite o valor da nota3")
leia(nota3)

limpatela

resultado<- (nota1 + nota2 + nota3 )/3

se (resultado >= 7) entao
   escreval("Aprovado, sua nota � de: ", resultado)

senao
     escreval("Reprovado, sua nota � de: ", resultado)

   
fimse




Fimalgoritmo