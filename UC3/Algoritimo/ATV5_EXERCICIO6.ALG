Algoritmo "atv5_exercicio6"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descrição   : algoritmo que leia a temperatura em graus Celsius e informe se o clima está frio (abaixo de 15°C), ameno (entre 15°C e 30°C) ou quente (acima de 30°C).
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 04/10/2024
Var
// Seção de Declarações das variáveis 
temp : real


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

escreva("Digite a temperatura em Cº ")
leia(temp)


limpatela


se temp < 15 entao
   escreva("o clima está frio ")

senao
     se (temp >= 15) e (temp <=30) entao
        escreva("Temperatura está amena")

     senao
          se (temp > 30)entao
             escreva("Está quente")
             
          fimse


     fimse
   
fimse
   


Fimalgoritmo