Algoritmo "atv5_exercicio4"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descri��o   : algoritmo que leia tr�s valores correspondentes aos lados de um tri�ngulo e informe se eles podem formar um tri�ngulo. Para formar um tri�ngulo, a soma de dois lados deve ser sempre maior que o terceiro lado.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 04/10/2024
Var
// Se��o de Declara��es das vari�veis 
lado_a, lado_b , lado_c : real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 

escreva("Digite o primeiro lado")
leia(lado_a)

limpatela

escreva("Digite o segundo lado")
leia(lado_b)

limpatela

escreva("Digite o terceiro lado")
leia(lado_c)

limpatela


se lado_a + lado_b > lado_c entao
     escreva("� um triangulo")
     
senao
     escreva("N�o � um triangulo")

fimse



Fimalgoritmo