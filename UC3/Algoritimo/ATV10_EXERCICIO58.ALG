Algoritmo "atv10_exercicio58"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 25/10/2024
Var
// Se��o de Declara��es das vari�veis 
aluno, quantidade, r : real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 

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

escreval("A quantidade de aluno foi de ", quantidade, " e a m�dia de idade deles ser� de: ", r)

Fimalgoritmo