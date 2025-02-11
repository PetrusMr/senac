Algoritmo "atv10_exercicio58"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 25/10/2024
Var
// Seção de Declarações das variáveis 
aluno, quantidade, r : real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

enquanto verdadeiro faca

         escreval("Informe a idade do aluno: ")
         leia(aluno)
         
         se aluno = 999 entao
         
            escreval("Idade acima ou igual a 999 ")
            interrompa
            
         senao
         
              quantidade <- quantidade + 1
              r <- r + aluno
              
         fimse

fimenquanto

r <- r / quantidade

escreval("A quantidade de aluno foi de ", quantidade, " e a média de idade deles será de: ", r)

Fimalgoritmo