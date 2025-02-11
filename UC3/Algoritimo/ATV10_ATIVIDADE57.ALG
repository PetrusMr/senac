Algoritmo "atv10_atividade57"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 25/10/2024
Var
// Seção de Declarações das variáveis 
salario_masc, salario_fem, fem, masc  : real
sexo, confirmar : caracter
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

enquanto verdadeiro faca
         escreva("Homem ou mulher")
         leia(sexo)

         se sexo = "m" ou "M" entao
            escreva("Informe o seu salario")
            leia(salario_fem)
            fem <- fem + salario_fem
         
         senao
              escreva("Informe o seu salario")
              leia(salario_masc)
              masc <- masc + salario_masc
         fimse
         
         escreva("Quer continuar? s/n ")
         leia(confirmar)
         se confirmar = "n" ou "N" entao
            interrompa
         

         fimse
         
fimenquanto
escreval("o salario masculino é de: ", masc)
escreval("o salario feminino é de: ",fem)

Fimalgoritmo