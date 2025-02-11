Algoritmo "atv9_exercicio51"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descrição   : Faça um aplicativo que leia o preço de 8 produtos. No final, mostre na tela qual foi o maior e qual foi o menor preço digitados.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 21/10/2024
Var
// Seção de Declarações das variáveis 
produto, f_prod, f2_prod : caracter
valor, max, min, f_valor  : real
i :inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
max <- -999999
min <- 9999999



para i de 1 ate 8 faca
     escreval("Informe o produto ")
     leia(produto)
     
     escreval("Informe O valor ")
     leia(valor)

     se valor > max entao
        max <- valor
        f_prod <- produto
        
     senao
          se valor < min entao
             min <- valor
             f2_prod <- produto

          fimse

     fimse

fimpara

escreval(" O maior valor é: ",f_prod ," Com o valor de: ",max)
escreva(" O menor valor é: ",f2_prod," Com o valor de", min)




Fimalgoritmo