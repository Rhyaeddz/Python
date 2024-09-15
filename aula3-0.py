'''
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições do mesmo if (ruim)
    <- Contagem de complexidade (ruim)
'''
velocidades = 50 # velocidade atual do carro
localCarro = 90 # local em que o carro está na estrada

RADAR1 = 60 # velocidade máxima do radar 1
LOCAL1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

CarSpeedPassRadar1 = velocidades > RADAR1
CarPassRadar1 = localCarro >= (LOCAL1 - RADAR_RANGE) and \
    localCarro <= (LOCAL1 - RADAR_RANGE)
CarMultedRadar1 = CarSpeedPassRadar1 and CarPassRadar1 

if CarSpeedPassRadar1 :
    print('velocidade do carro passou pelo radar 1')

if CarPassRadar1 :
    print('O carro passou pelo radar 1')
    
if CarMultedRadar1:
    print('O carro passou na acima da velocidade permitida e foi multado!')