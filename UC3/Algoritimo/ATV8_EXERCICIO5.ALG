Algoritmo "atv8_exercicio5"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descri��o   : algoritmo que pe�a ao usu�rio para digitar v�rios n�meros e some todos os n�meros digitados. O programa deve parar quando o n�mero zero for digitado, e n�o deve incluir o zero na soma
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 16/10/2024
Var
// Se��o de Declara��es das vari�veis 
nm, l_nm, r : inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
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