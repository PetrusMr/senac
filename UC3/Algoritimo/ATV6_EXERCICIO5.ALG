Algoritmo "atv6_exercicio5"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descri��o   : algoritmo que leia a idade de uma crian�a e informe em qual ano escolar ela deve estar, conforme a tabela:
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 07/10/2024
Var
// Se��o de Declara��es das vari�veis 
idade : real


Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreva("Informe a idade")
leia(idade)
limpatela

se (idade < 4) ou (idade >= 18) entao
   escreva(" Fora da educa��o regular")


senao
     se idade < 6 entao
        escreva("Pr�-escola")
     
     senao
          se idade < 11 entao
             escreva("Ensino Fundamental I")


          senao
               se idade < 15 entao
                  escreva("Ensino Fundamental II")
               senao
                    escreva(" Ensino M�dio")


               fimse

          fimse
     
     fimse


fimse





Fimalgoritmo