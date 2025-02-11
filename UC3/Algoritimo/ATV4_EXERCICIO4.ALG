Algoritmo "atv4_exercicio4"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira
// Descrição   : Desenvolva um algoritmo que leia o salário de um funcionário e aplique um aumento de 20% caso o salário seja inferior a R$1.500. Se o salário for maior ou igual a esse valor, aplique um aumento de 10%.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 02/10/2024
Var
// Seção de Declarações das variáveis 
salario : real
resultado : real



Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

escreval("Digite o valor do seu salario")
leia(salario)

limpatela

se (salario < 1500) entao
   resultado <- salario * 20
   resultado <- resultado / 100
   resultado <- salario + resultado
   escreval("Seu salario com aumento é de: ", resultado)
   
senao
     resultado <- salario * 10
     resultado <- resultado / 100
     resultado <- salario + resultado
     escreval("Seu salario com aumento é de: ", resultado)



fimse






Fimalgoritmo