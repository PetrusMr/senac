Algoritmo "atv5_exercicio7"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descri��o   : algoritmo que leia a velocidade de um ve�culo e informe se ele est� dentro do limite permitido (at� 80 km/h), acima do limite permitido ou muito acima do limite (acima de 100 km/h).
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 04/10/2024
Var
// Se��o de Declara��es das vari�veis 

velo : real



Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 

escreva("Digite a velociade do veiculo ")
leia(velo)

se (velo<= 80) entao
   escreva("esta dentro da velocidade ")
senao
     se (velo >80) e (velo <100) entao
        escreva("Acima do limite da velocidade")
     senao
          se (velo > 100) entao
             escreva("est� muito acima do limite ")
          

          fimse
     fimse

fimse






Fimalgoritmo