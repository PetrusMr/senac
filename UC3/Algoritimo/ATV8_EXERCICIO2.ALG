Algoritmo "atv8_exercicio2"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira
// Descri��o   : programa que pe�a ao usu�rio um n�mero inteiro positivo e verifique se ele � primo. Continue pedindo novos n�meros at� que o usu�rio insira um valor negativo.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 16/10/2024
Var
// Se��o de Declara��es das vari�veis 
nm, c, d  : inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 

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
