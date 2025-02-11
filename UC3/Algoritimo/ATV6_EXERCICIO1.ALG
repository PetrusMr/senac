Algoritmo "atv6_exercicio1"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descrição   :  algoritmo que leia três lados de um triângulo e classifique-o como equilátero (todos os lados iguais), isósceles (dois lados iguais) ou escaleno (todos os lados diferentes). Verifique primeiro se os valores inseridos formam um triângulo válido.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 07/10/2024
Var
// Seção de Declarações das variáveis 
lado1,lado2,lado3 : real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

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
   escreva("N é um triangulo")
   
   
senao
     se (lado1 = lado2) e (lado1 = lado3) e (lado2 = lado3)entao
        escreva("é um triangulo equilatero")
        
     senao
          se (lado1 = lado2) ou (lado1 = lado3) ou (lado2 = lado3)entao
             escreva("é um triangulo isosceles")
          senao
               escreva("é um escaleno")

          fimse

fimse
          




fimse





Fimalgoritmo
