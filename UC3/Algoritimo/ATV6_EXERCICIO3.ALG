Algoritmo "atv6_exercicio3"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descrição   : algoritmo que leia três notas de um aluno (de 0 a 10) e calcule a média. Com base na média:
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 07/10/2024
Var
// Seção de Declarações das variáveis 
nota1,nota2,nota3, media : real



Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreva("informa a nota1 ")
leia(nota1)
limpatela

escreva("informa a nota2 ")
leia(nota2)
limpatela

escreva("informa a nota3 ")
leia(nota3)
limpatela





se (nota1 < 3) ou (nota2 < 3) ou (nota3 < 3 ) entao
   escreva("reprovado!!")

senao
     media <- (nota1 + nota2 + nota3) / 3
     
     se media < 5 entao
        escreva("reprovado!!")
        
     senao
          se media < 7 entao
             escreva("recuperacao")
             
          
          senao
             escreva("Aprovado")
          fimse

     fimse




fimse


Fimalgoritmo