Algoritmo "atv6_exercicio1"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descri��o   :  algoritmo que leia tr�s lados de um tri�ngulo e classifique-o como equil�tero (todos os lados iguais), is�sceles (dois lados iguais) ou escaleno (todos os lados diferentes). Verifique primeiro se os valores inseridos formam um tri�ngulo v�lido.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 07/10/2024
Var
// Se��o de Declara��es das vari�veis 
lado1,lado2,lado3 : real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 

escreva("informe o lado 1 ")
leia(lado1)
limpatela

escreva("informe o lado 2 ")
leia(lado2)
limpatela

escreva("informe o lado 3 ")
leia(lado3)
limpatela


se (lado1 + lado2) < lado3 entao
   escreva("N � um triangulo")
   
   
senao
     se (lado1 = lado2) e (lado1 = lado3) e (lado2 = lado3)entao
        escreva("� um triangulo equilatero")
        
     senao
          se (lado1 = lado2) ou (lado1 = lado3) ou (lado2 = lado3)entao
             escreva("� um triangulo isosceles")
          senao
               escreva("� um escaleno")

          fimse

fimse
          




fimse





Fimalgoritmo
