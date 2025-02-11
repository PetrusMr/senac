Algoritmo "atv7_exercicio5"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descrição   : Ao usuário um número inteiro positivo e calcule e exiba o fatorial desse número
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 09/10/2024
Var
// Seção de Declarações das variáveis 
 n, i, fatorial: inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreva("Digite um número inteiro positivo: ")
leia(n)


se n < 0 entao
   escreva("negativo n fatoria")
senao

     fatorial <- 1


     para i de 1 ate n faca
          fatorial <- fatorial * i
     fimpara


escreva("O fatorial de ", n, " é ", fatorial)
fimse

Fimalgoritmo