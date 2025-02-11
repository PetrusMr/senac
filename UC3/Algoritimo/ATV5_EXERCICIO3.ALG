Algoritmo "atv5_exercicio3"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descrição   : algoritmo que leia a hora informada pelo usuário (em formato 24 horas) e o dia da semana, e informe se o estabelecimento está aberto ou fechado. Considere que o estabelecimento funciona das 8h às 18h de Segunda à Sexta.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 04/10/2024
Var
// Seção de Declarações das variáveis 
hora : real
segunda, terca, quarta, quinta, sexta : caracter
dia : caracter


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
segunda <- "segunda"
terca <- "terça"
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
   escreva("Está aberta")
   
senao
     escreva("Está Fechado")

   
   


fimse




Fimalgoritmo