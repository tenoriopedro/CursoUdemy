"""
Repetições
while(enquanto)
Executa uma ação enquanto uma condição for verdadeira
continue -> volta ao começo do laço
"""
c = 0

while c <= 10:
    c += 1
    if c == 6:
        print('Nao vou mostar.')
        continue
    print(c)