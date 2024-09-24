#Calculadora de antecipacao de prestacoes
#Em pagamentos de PRIMEIRA e ULTIMA parcela de um financiamento

print ("Insira o valor financiado abaixo. Ex.: 20000 sem virgulas sem pontos")
f = int(input("valor financiado: "))
print ("Insira o valor das parcelas abaixo. Ex.: 500 (arredondado sem virgulas)")
x = int(input ("valor das parcelas: "))
print ("Insira a taxa de juros abaixo. Ex.: 144 (sem virgulas para 1,44%)")
y = int(input ("taxa de juros: "))
print ("Insira o numero de parcelas abaixo. Ex.: 60")
z = int(input ("número de parcelas: "))
k = 0 #Valor inicial do k, pois na expressao ha uma iteracao dele para obter a soma das ultimas parcelas
q = z/2 #limitacao da parcela antecipada
while (q + 1) != z:
    z = z - 1
    w = x/((1 + (y / 10000)) ** (z))
    k = k + w
t = (q * x) + k
u = round(t,2)
v = round(k,2)
g = u-f
h = round(g,2)
print (u, "valor total final (sem considerar IOF na base de calculos)")
print (v, "soma da metade das parcelas totais antecipadas com o desconto")
print (h, "juros em cima do valor financiado")
