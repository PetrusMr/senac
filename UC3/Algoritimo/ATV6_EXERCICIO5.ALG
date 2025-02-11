Algoritmo "atv6_exercicio5"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descrição   : algoritmo que leia a idade de uma criança e informe em qual ano escolar ela deve estar, conforme a tabela:
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 07/10/2024
Var
// Seção de Declarações das variáveis 
idade : real


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreva("Informe a idade")
leia(idade)
limpatela

se (idade < 4) ou (idade >= 18) entao
   escreva(" Fora da educação regular")


senao
     se idade < 6 entao
        escreva("Pré-escola")
     
     senao
          se idade < 11 entao
             escreva("Ensino Fundamental I")


          senao
               se idade < 15 entao
                  escreva("Ensino Fundamental II")
               senao
                    escreva(" Ensino Médio")


               fimse

          fimse
     
     fimse


fimse





Fimalgoritmo