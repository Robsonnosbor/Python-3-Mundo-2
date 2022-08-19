print('{:=^40}'.format ( ' ROBSON ELETRO ' ))
preço = float(input('Preço das compras: R$ '))
print(''' FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção?'))
if opção == 1:
    tota = preço - (preço * 10 / 100)        
elif opção == 2:
        tota = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2  
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparc = int(input('quantas parcelas?'))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparc, parcela))   
else:
    total = 0
    print('OPÇÃO INVÁLIDA de pagamento. tente novamente!')
print(' Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))  
