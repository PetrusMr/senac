Algoritmo "EXEMPLO3 VETOR"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 23/10/2024
Var
// Seção de Declarações das variáveis 
nome : vetor [0..4] de caracter
i, c : inteiro
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

c <- 4
para i de 0 ate 4 faca
     escreva("Informe o", i , "° nome:" )
     leia(nome[i])


fimpara

para i de 0 ate 4 faca
     escreval(nome[c])
     c <- c - 1

fimpara

Fimalgoritmo