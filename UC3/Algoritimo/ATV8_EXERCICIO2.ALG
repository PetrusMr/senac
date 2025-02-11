Algoritmo "atv8_exercicio2"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira
// Descrição   : programa que peça ao usuário um número inteiro positivo e verifique se ele é primo. Continue pedindo novos números até que o usuário insira um valor negativo.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 16/10/2024
Var
// Seção de Declarações das variáveis 
nm, c, d  : inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

enquanto verdadeiro faca
escreval("Digite um numero inteiro positivo ")
leia(nm)
         
se nm < 0 entao
escreval("numero negativo")
interrompa

fimse

para c de 1 ate nm faca

se nm % c = 0 entao
d <- d +1


fimse
fimpara
se d = 2 entao
escreval("primo")

d <- 0

senao
     escreval("n primo")

d <- 0

fimse
fimenquanto



Fimalgoritmo
