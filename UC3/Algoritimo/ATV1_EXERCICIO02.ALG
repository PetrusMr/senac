Algoritmo "atv1_exercicio02"
// Disciplina   : UC3 ALGORITIMOS
// Professor   :Mateus de Paula Pereira 
// Descrição   : converter celsius em fh
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 29/08/2024
Var
// Seção de Declarações das variáveis 
TC : real
TF : real
c1 : real
c2 : inteiro
meio : real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

// valor da constante
c1 <- 1.8
c2 <- 32

escreva("Graus celsius: ")
leia(TC)

meio <- TC * c1
TF <- meio + c2

escreva ("temperatura em FH é:")
escreva(TF)

Fimalgoritmo