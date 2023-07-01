### LETRA QUE APARECEU MAIS VEZES (ITERANDO STRINGS)

frase = 'O Python é uma lingaguem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido Van Hossum.'

frase_inteira = frase.lower().replace(' ', '')

i = 0
letra_apareceu_mais = ''
quant_apareceu_mais = 0

while i < len(frase_inteira):
    letra = frase_inteira[i]
    quant_vezes = frase_inteira.count(letra)

    if quant_apareceu_mais < quant_vezes:
        quant_apareceu_mais = quant_vezes
        letra_apareceu_mais = letra

    i += 1

print(f'A letra "{letra_apareceu_mais.upper()}" aparece {quant_apareceu_mais} vezes')
