Algoritmo "atv1_exercicio5"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira
// Descri��o   : Elabore um algoritmo que calcule o valor final de um produto ap�s aplicar um desconto de 10%. Utilize vari�veis do tipo real para armazenar o valor original do produto e o valor final.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 03/09/2024
Var
// Se��o de Declara��es das vari�veis
valor1 : real
desconto : real
valor2 : real


Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 

escreva ("escreva o valor do produto:")
leia (valor1)

escreva ("escreva o valor do desconto:")
leia (desconto)

valor2 <- desconto / 100 * valor1

escreva ("o valor do produto com desconto ser� de:")
escreva (valor2)
Fimalgoritmo