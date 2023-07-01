"""
CONSTANTE = "variáveis em letras MAIUSCULAS não vão mudar"
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 61  # velocidade atual do carro
local_carro = 90  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade maxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 esta
RADAR_RANGE = 1  # a distancia onde o radar pega

## EX:
alcance_carro_1 = local_carro >= (LOCAL_1 - RADAR_RANGE)
alcance_carro_2 = local_carro <= (LOCAL_1 + RADAR_RANGE)
vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = alcance_carro_1 and alcance_carro_2
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou no radar 1')

if carro_multado_radar_1:
    print('Carro foi multado no radar 1')