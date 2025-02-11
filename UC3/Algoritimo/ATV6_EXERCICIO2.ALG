Algoritmo "atv6_exercicio2"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descrição   : algoritmo que leia o salário de um funcionário e aplique aumentos:
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 07/10/2024
Var
// Seção de Declarações das variáveis 

salario : real


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreva("Informe o salario ")
leia(salario)

limpatela

se salario <= 1000 entao
   salario <- salario * 0.2 + salario
   
   escreva("O salario é de : ", salario)


senao
     se salario <= 3000 entao
        salario <- salario * 0.15 + salario
        
        escreva("salario é de : ", salario)
        
     senao
          salario<- salario * 0.1 + salario
          
          escreva(" salario é de :", salario)
     
     
     fimse


fimse









Fimalgoritmo