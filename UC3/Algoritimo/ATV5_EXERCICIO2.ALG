Algoritmo "atv5_exercicio2"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira 
// Descri��o   :  algoritmo que leia um nome de usu�rio e uma senha e informe se o login foi bem-sucedido, comparando os valores inseridos
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 04/10/2024
Var
// Se��o de Declara��es das vari�veis 
user : caracter
password : caracter

usuario, senha: caracter
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 


user <- ("petrus")
password <- ("277353")


escreva("Digite o usuario: ")
leia(usuario)

limpatela


escreva("Digite a senha ")
leia(senha)

limpatela


se user <> usuario entao
   escreva("erro, usuario nao reconhecido")

senao
     se password = senha entao
        escreva("Login Ben sucedido")

     senao
          escreva("Erro, senha errada")
     fimse


fimse




Fimalgoritmo