Algoritmo "EXEMPLO2 VETOR"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 23/10/2024
Var
// Seção de Declarações das variáveis 
nm : vetor [0..9] de inteiro
i, r : inteiro


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 


para i de 0 ate 9 faca
     escreva("Informe um valor: ")
     leia(nm[i])

fimpara

para i de 0 ate 9 faca
     r <- r + nm[i]

fimpara
escreva(r)


Fimalgoritmo