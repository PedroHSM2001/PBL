# Autor: Pedro Henrique  Santana Moreira
# Componente Curricular: Algoritmos I
# Concluido em: 18/04/2019
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum trecho de código de outro colega ou de outro autor, tais
#como provindos de livros e apostilas, e páginas ou documentos eletrônicos da internet. #####

print('Seja bem vindo(a) ao simulador do valor da conta de energia elétrica!') 
tarifa = float(input('Qual o valor da Tarifa Residencial de Baixa Tensão atual(custo por kWh gasto)?''\n')) #Solicitar o valor da tarifa residencial
total = 0 
consumoSetor = 0
setorAd = 'sim'
while setorAd == 'sim': #Depois de finalizar o setor o usuario decide se vai querer adicionar mais algum 
        for contador in range(0, 5): #O programa irá repetir 5 vezes as perguntas, 1 vez para cada aparelho do setor na respectiva ordem
            print('\n','Digite os dados dos respectivos aparelhos elétrico-eletrônicos na seguinte ordem: ')
            print(' 1 - Ar-condicionado','\n','2 - Computador','\n','3 - Geladeira','\n','4 - Lâmpada','\n','5 - Televisor') #ordem dos aparelhos
            print('Caso não possua o aparelho no setor, digite 0 quando solicitar a quantidade!','\n')
            quantidade = float(input('Quantos aparelhos desse tipo possui o setor?''\n'))
            if(quantidade != 0):   #caso haja o aparelho no setor ele fará as demais perguntas
                pot = float(input('Qual a potência (em Watts) do aparelho?''\n'))
                qhd = float(input('Qual a quantidade de horas de uso diario desse aparelho?''\n'))
                qdm = float(input('Quantos dias esse aparelho é usado no mês?''\n'))
                consumo = (((qhd * qdm) * pot) * quantidade) / 1000 #cálculo do consumo em Kwh
                print(f'O consumo desse aparelho foi: {consumo}Kwh')#consumo do aparelho
                print('O Valor gasto por esse aparelho foi R$ %.2f: ' %(consumo * tarifa),'\n')#valor gasto pelo aparelho, sem as taxas
                consumoSetor = consumoSetor + consumo#gurdando o valor do consumo em uma variavel que será exibita depois
            else:
                print('Aparelho Inexistente no setor. Próximo aparelho!', '\n')#caso não haja o aparelho no setor, irá para o próximo aparelho
        print('\n','Setor Finalizado!','\n',f'O consumo total desse setor foi: {consumoSetor} Kwh!')#consumo total do setor
        print(' O valor gasto  nesse setor seria: R$ %.2f ' %(consumoSetor * tarifa), '\n')#valor gasto por esse setor, sem as taxas
        total = total + consumoSetor#guardando o valor do consumo do setor, para ser exibido no final o valor total
        consumoSetor = 0
        setorAd = input('Você deseja adicionar mais um setor? (Digite "sim" ou "não")''\n')#pergunta se o usuario quer adicionar mais algum setor
print(f'O gasto total foi de {total} Kwh ') #Consumo total, com todos os setores
valor = total * tarifa
print('O Valor da conta sem os impostos seria R$ ''%.2f' %(valor)) #Valor final sem as taxas
print('O valor da conta final seria R$ ''%.2f' %(valor * 1.3626))  #Valor final com as taxas adicionadas
