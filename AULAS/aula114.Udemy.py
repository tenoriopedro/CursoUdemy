## Higher Order Functions
## Funções de primeira classe
## Closure

## High Order Functions "função que executa outra função"

def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


print(executa(saudacao, 'Bom dia' , 'Luiz'))


## função que executa outra função
## Higher Order Functions -> Funções que podem receber e/ou retornar outras funções
## First-Class Functions -> Funções que são tratadas como outros tipos dados comuns(string,inteiros,etc..)

## Closure

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')

print(falar_bom_dia('Pedro')) ## closure ocorre quando fecha () 'falar_bom_dia'