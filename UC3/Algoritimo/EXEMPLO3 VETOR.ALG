Algoritmo "EXEMPLO3 VETOR"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 23/10/2024
Var
// Se��o de Declara��es das vari�veis 
nome : vetor [0..4] de caracter
i, c : inteiro
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 

c <- 4
para i de 0 ate 4 faca
     escreva("Informe o", i , "� nome:" )
     leia(nome[i])


fimpara

para i de 0 ate 4 faca
     escreval(nome[c])
     c <- c - 1

fimpara

Fimalgoritmo