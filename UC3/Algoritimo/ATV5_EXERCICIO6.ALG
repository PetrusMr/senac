Algoritmo "atv5_exercicio6"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descri��o   : algoritmo que leia a temperatura em graus Celsius e informe se o clima est� frio (abaixo de 15�C), ameno (entre 15�C e 30�C) ou quente (acima de 30�C).
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 04/10/2024
Var
// Se��o de Declara��es das vari�veis 
temp : real


Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 

escreva("Digite a temperatura em C� ")
leia(temp)


limpatela


se temp < 15 entao
   escreva("o clima est� frio ")

senao
     se (temp >= 15) e (temp <=30) entao
        escreva("Temperatura est� amena")

     senao
          se (temp > 30)entao
             escreva("Est� quente")
             
          fimse


     fimse
   
fimse
   


Fimalgoritmo