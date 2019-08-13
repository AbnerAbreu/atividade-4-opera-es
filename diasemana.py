
diasemana = {1:'domingo',
             2:'segunda',
             3:'terça',
             4:'quarta',
             5:'quinta',
             6:'sexta',
             7:'sabado'}

dia = int(input('digite um numero: '))

try:
   print(diasemana[dia])
except:
   print('Ops esse numero não existe na lista')

