Algoritmo "atv5_exercicio7"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descrição   : algoritmo que leia a velocidade de um veículo e informe se ele está dentro do limite permitido (até 80 km/h), acima do limite permitido ou muito acima do limite (acima de 100 km/h).
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 04/10/2024
Var
// Seção de Declarações das variáveis 

velo : real



Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

escreva("Digite a velociade do veiculo ")
leia(velo)

se (velo<= 80) entao
   escreva("esta dentro da velocidade ")
senao
     se (velo >80) e (velo <100) entao
        escreva("Acima do limite da velocidade")
     senao
          se (velo > 100) entao
             escreva("está muito acima do limite ")
          

          fimse
     fimse

fimse






Fimalgoritmo