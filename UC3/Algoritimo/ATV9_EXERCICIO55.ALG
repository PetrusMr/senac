Algoritmo "atv9_exercicio55"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descrição   : Vamos melhorar o jogo que fizemos no exercício 32. A partir de agora, o computador vai sortear um número entre 1 e 10 e o jogador vai ter 4tentativas para tentar acertar.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 21/10/2024
Var
// Seção de Declarações das variáveis 

nm, b, c : inteiro
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

b <- randi(6)

para c de 1 ate 4 faca
     escreva("Escreva um numero para acertar ")
     leia(nm)
     se nm = b entao
        escreva("Voce acertou! ")
        interrompa
     senao
          escreva("Voce errou! ")
     fimse


fimpara
escreva("Fim")


Fimalgoritmo