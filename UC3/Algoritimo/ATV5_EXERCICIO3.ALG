Algoritmo "atv5_exercicio3"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descri��o   : algoritmo que leia a hora informada pelo usu�rio (em formato 24 horas) e o dia da semana, e informe se o estabelecimento est� aberto ou fechado. Considere que o estabelecimento funciona das 8h �s 18h de Segunda � Sexta.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 04/10/2024
Var
// Se��o de Declara��es das vari�veis 
hora : real
segunda, terca, quarta, quinta, sexta : caracter
dia : caracter


Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
segunda <- "segunda"
terca <- "ter�a"
quarta <- "quarta"
quinta <- "quinta"
sexta <- "sexta"


escreva("Digite o horario ")
leia(hora)

limpatela


escreva("Digite o dia da semana ")
leia(dia)

limpatela

se (hora >= 8) e (hora <= 18) e (dia = segunda) ou (dia = terca) ou (dia = quarta) ou (dia = quinta) ou (dia = sexta)  entao
   escreva("Est� aberta")
   
senao
     escreva("Est� Fechado")

   
   


fimse




Fimalgoritmo