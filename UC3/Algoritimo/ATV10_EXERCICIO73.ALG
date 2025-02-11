Algoritmo "atv10_exercicio73"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descrição   : Crie um programa que preencha automaticamente (usando lógica, não apenas atribuindo diretamente) um vetor numérico com 10 posições, conforme abaixo
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 23/10/2024
Var
// Seção de Declarações das variáveis
nm : vetor [0..9] de inteiro
i, c : inteiro


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
c <- 9
para i de 0 ate 9 faca
     nm [i] <- c
     c <- c - 1


fimpara


Fimalgoritmo