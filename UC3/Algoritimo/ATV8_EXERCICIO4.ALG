Algoritmo "atv8_exercicio4"
// Disciplina   : UC3 ALGORITMOS
// Professor   : Mateus de Paula Pereira
// Descri��o   : usu�rio para inserir um capital inicial, uma taxa de juros e o n�mero de meses, e calcule o valor acumulado usando juros compostos. Exiba o saldo para cada m�s at� o final do per�odo.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 16/10/2024
Var
// Se��o de Declara��es das vari�veis
c, max, min, num: inteiro
nm: vetor[1..10] de inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc...




max <- -99999
min <- 999999

para c de 1 at� 10 fa�a
     escreval("Informe um n�mero:")
     leia(num)
     nm[c] <- num


     se num > max ent�o
         max <- num
     fimse
     se num < min ent�o
         min <- num
     fimse
fimpara


escreval("Dos seguintes numeros")
para c de 1 ate 10 faca
     escreval(nm[c])
     
fimpara

escreval("O maior n�mero �:", max)
escreval("O menor n�mero �:", min)

Fimalgoritmo
