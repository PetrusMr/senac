Algoritmo "atv7_exercicio5"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descri��o   : Ao usu�rio um n�mero inteiro positivo e calcule e exiba o fatorial desse n�mero
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 09/10/2024
Var
// Se��o de Declara��es das vari�veis 
 n, i, fatorial: inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreva("Digite um n�mero inteiro positivo: ")
leia(n)


se n < 0 entao
   escreva("negativo n fatoria")
senao

     fatorial <- 1


     para i de 1 ate n faca
          fatorial <- fatorial * i
     fimpara


escreva("O fatorial de ", n, " � ", fatorial)
fimse

Fimalgoritmo