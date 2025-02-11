Algoritmo "atv4_exercicio3"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira
// Descrição   : um algoritmo que leia três notas de um aluno, calcule a média e informe se ele foi aprovado (média maior ou igual a 7) ou reprovado (média inferior a 7).
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 02/10/2024
Var
// Seção de Declarações das variáveis 
nota1, nota2, nota3, resultado: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

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
   escreval("Aprovado, sua nota é de: ", resultado)

senao
     escreval("Reprovado, sua nota é de: ", resultado)

   
fimse




Fimalgoritmo