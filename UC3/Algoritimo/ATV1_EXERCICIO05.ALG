Algoritmo "atv1_exercicio5"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira
// Descrição   : Elabore um algoritmo que calcule o valor final de um produto após aplicar um desconto de 10%. Utilize variáveis do tipo real para armazenar o valor original do produto e o valor final.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 03/09/2024
Var
// Seção de Declarações das variáveis
valor1 : real
desconto : real
valor2 : real


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

escreva ("escreva o valor do produto:")
leia (valor1)

escreva ("escreva o valor do desconto:")
leia (desconto)

valor2 <- desconto / 100 * valor1

escreva ("o valor do produto com desconto será de:")
escreva (valor2)
Fimalgoritmo