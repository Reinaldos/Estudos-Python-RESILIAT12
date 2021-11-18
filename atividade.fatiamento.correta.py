sentenca = 'X-DSPAM-Confidence:0.8485'

indiceDoDoisPontos = sentenca.find(':')

print('Indice do : é ', indiceDoDoisPontos)

multiplicacao = float(sentenca[indiceDoDoisPontos + 1:]) * 100

print(multiplicacao)
