Algoritmo "atv6_exercicio2"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descri��o   : algoritmo que leia o sal�rio de um funcion�rio e aplique aumentos:
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 07/10/2024
Var
// Se��o de Declara��es das vari�veis 

salario : real


Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreva("Informe o salario ")
leia(salario)

limpatela

se salario <= 1000 entao
   salario <- salario * 0.2 + salario
   
   escreva("O salario � de : ", salario)


senao
     se salario <= 3000 entao
        salario <- salario * 0.15 + salario
        
        escreva("salario � de : ", salario)
        
     senao
          salario<- salario * 0.1 + salario
          
          escreva(" salario � de :", salario)
     
     
     fimse


fimse









Fimalgoritmo