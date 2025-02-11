Algoritmo "atv6_exercicio4"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descrição   : algoritmo que calcule o imposto de renda a pagar com base no salário. Utilize as faixas:
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 07/10/2024
Var
// Seção de Declarações das variáveis 
salario : real




Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreva("Digite o teu salario ")
leia(salario)
limpatela

se salario <=1900 entao
   escreva("Isento de imposto")
   

senao
     se salario <= 2800 entao
        salario <- salario * 0.075
        escreva("O imposto cobrado será de: ", salario)

     senao
          se salario <= 3700 entao
             salario <- salario * 0.15
             escreva("O imposto cobrado será de : ", salario)
             

          senao
               salario <- salario * 0.225
               escreva("O imposto cobrado será de : ",salario)

          fimse


     fimse


fimse





Fimalgoritmo