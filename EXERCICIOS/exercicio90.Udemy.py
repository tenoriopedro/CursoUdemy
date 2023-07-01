## lista de compras
from time import sleep
produtos = []
print('~' *40)
print('SUA LISTA DE COMPRAS'.center(40))
print('~' *40)

while True:
    try:
        sleep(1)
        print('''[A]dicionar produto
[E]liminar produto
[L]istar produtos
[S]air da lista''')
        sleep(1)
        escolha = input('Escolha uma das opções acima: ').lower().strip()
        ## validação dos primeiros dados
        if len(escolha) > 1:
            print('\033[31mERRO!! Escolha apenas uma opção por vez.\033[m')
            continue
        if escolha.isalpha() == False:
            print('\033[31mERRO!! Escolha as letras de acordo com o enunciado.\033[m')
            continue
        if escolha not in 'aels':
            print('\033[31mERRO!! Escolha as letras de acordo com o enunciado\033[m')
            continue
        sleep(1)
        ## escolha das opções
        if escolha == 'a':
            print('-' *40)
            item = input(' - Digite o produto que quer adicionar: ').strip()
            produtos.append(item)
            print(' - Adicionado com sucesso')
            print('-' *40)
        if escolha == 'e':
            print('-' *40)
            if len(produtos) == 0:
                print('Sua lista esta vazia, não há nenhum produto para eliminar')
            else:
                eliminar = input('Digite o produto que quer eliminar: ').strip()
                produtos.remove(eliminar)
                print('Eliminado com sucesso')
            print('-' *40)
        if escolha == 'l':
            print('-' *40)
            if len(produtos) == 0:
                print('Não há nenhum produto na sua lista.')
            if len(produtos) > 0:
                for i, p in enumerate(produtos):
                    print(f'{i+1} - {p}')
            print('-' *40)
        if escolha == 's':
            print('Você optou por sair.')
            if len(produtos) > 0:
                print('E sua lista de compras ficou assim: ')
                for i, p in enumerate(produtos):
                    print(f'{i + 1} - {p}')
            else:
                print('Sua lista de compras ficou vazia.')
            print('Obrigado volte sempre')
            break
    # se der algum erro
    except (IndexError, ValueError):
        print('-' * 40)
        print('\033[31mEste produto não existe.\033[m')
        print('-' *40)
        continue