Dias_Alugados = int(input('Quantos dias você ficou com o carro?'))
Diaria = Dias_Alugados * 60
print('O total a pagar em relação a diarias é de R${:.2f}'.format(Diaria))

KM_Rodados = float(input('Quantos KMs você rodou com o carro?'))
Valor_KM = KM_Rodados * 0.15
print('O total a se pagar em relação a quilometragem é de R${:.2f}'.format(Valor_KM))

Soma_Total = Diaria + Valor_KM
print('O valor Total do aluguel é de R${:.2f}'.format(Soma_Total))
