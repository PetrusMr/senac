Algoritmo "atv4_exercicio4"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira
// Descri��o   : Desenvolva um algoritmo que leia o sal�rio de um funcion�rio e aplique um aumento de 20% caso o sal�rio seja inferior a R$1.500. Se o sal�rio for maior ou igual a esse valor, aplique um aumento de 10%.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 02/10/2024
Var
// Se��o de Declara��es das vari�veis 
salario : real
resultado : real



Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 

escreval("Digite o valor do seu salario")
leia(salario)

limpatela

se (salario < 1500) entao
   resultado <- salario * 20
   resultado <- resultado / 100
   resultado <- salario + resultado
   escreval("Seu salario com aumento � de: ", resultado)
   
senao
     resultado <- salario * 10
     resultado <- resultado / 100
     resultado <- salario + resultado
     escreval("Seu salario com aumento � de: ", resultado)



fimse






Fimalgoritmo