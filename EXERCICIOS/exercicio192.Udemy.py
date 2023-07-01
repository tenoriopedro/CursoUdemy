import json



def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados


def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados


def listar(lista):
    pos = 1
    for item in lista:
        print(f'{pos} - {item}')
        pos += 1

arq = 'exercicio195.Udemy.json'
lista_tarefas = ler([], arq)
lista_reserva = []

while True:
    print('Comandos: listar, desfazer, refazer')
    tarefa = input('Diga uma tarefa ou um comando: ').strip()

    if tarefa == 'listar':
        if len(lista_tarefas) == 0:
            print('Nada para listar')
            continue
        else:

            listar(lista_tarefas)
            continue

    elif tarefa == 'desfazer':
        if len(lista_tarefas) == 0:
            print('Nada para desfazer')
            continue
        else:
            lista_tarefas.pop()
            salvar(lista_tarefas, arq)
            listar(lista_tarefas)

            continue
    elif tarefa == 'refazer':
        if len(lista_reserva) == len(lista_tarefas):
            print('Nada para refazer')
            continue
        else:
            i = 0
            while i < len(lista_reserva):
                if lista_reserva[i] in lista_tarefas:
                    i += 1
                else:
                    lista_tarefas.append(lista_reserva[i])
                    break
            listar(lista_tarefas)
            salvar(lista_tarefas, arq)
            continue
    else:
        lista_tarefas.append(tarefa)
        lista_reserva.append(tarefa)
        salvar(lista_tarefas, arq)
        listar(lista_tarefas)