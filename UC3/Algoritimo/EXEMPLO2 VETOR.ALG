Algoritmo "EXEMPLO2 VETOR"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 23/10/2024
Var
// Se��o de Declara��es das vari�veis 
nm : vetor [0..9] de inteiro
i, r : inteiro


Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 


para i de 0 ate 9 faca
     escreva("Informe um valor: ")
     leia(nm[i])

fimpara

para i de 0 ate 9 faca
     r <- r + nm[i]

fimpara
escreva(r)


Fimalgoritmo