# achar a estação de acordo com o mês e dia

# apresentação
print('\n\t\t\t --- Estação do Ano --- \n ')

# entrada
mes1 = {'janeiro', 'fevereiro', 'março'}
mes2 = {'abril', 'maio', 'junho'}
mes3 = {'julho', 'agosto', 'setembro'}
mes4 = {'outubro', 'novembro', 'dezembro'}

m = input('escolha o mês que deseja saber: ')

if m in mes1:
    print(f'a estação é verão')

elif m in mes2:
    print(f'a estação é outono')

elif m in mes3:
    print(f'a estação é inverno')

elif m in mes4:
    print(f'a estação é primavera')


else:
    print(f'nao é valido')
