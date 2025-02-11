Algoritmo "atv8_exercicio5"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descrição   : algoritmo que peça ao usuário para digitar vários números e some todos os números digitados. O programa deve parar quando o número zero for digitado, e não deve incluir o zero na soma
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 16/10/2024
Var
// Seção de Declarações das variáveis 
nm, l_nm, r : inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
l_nm <- 0

enquanto verdadeiro faca
         escreval("informe um numero ")
         leia(nm)
         
         se nm = 0 entao
            escreva("fim, numero digitado foi 0 ")
            interrompa
            
         senao
              r <- l_nm + nm
              escreval(r)
              l_nm <- r

         fimse


fimenquanto


Fimalgoritmo