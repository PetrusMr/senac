Algoritmo "atv5_exercicio4"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descrição   : algoritmo que leia três valores correspondentes aos lados de um triângulo e informe se eles podem formar um triângulo. Para formar um triângulo, a soma de dois lados deve ser sempre maior que o terceiro lado.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 04/10/2024
Var
// Seção de Declarações das variáveis 
lado_a, lado_b , lado_c : real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

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
     escreva("È um triangulo")
     
senao
     escreva("Não é um triangulo")

fimse



Fimalgoritmo