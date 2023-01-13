from time import sleep

sleep(1.5)
times = ('franca', 'flabasquete', 'minas', 'são paulo', 'bauru', 'unifacisa', 'paulistano',
         'pinheiros', 'corinthians', 'rio claro', 'caxias do sul', 'pato basquete', 'mogi',
         'basquete cearense', 'cerrado')
print('\033[32m=-\033[m' * 15)
for t in times:
    print(t)
print('\033[33m=-\033[m' * 15)
sleep(1.5)
print(f'os cincos primeiros são: \033[32m{times[0:5]}\033[m')
sleep(1.5)
print('\033[33m=-\033[m' * 15)
sleep(1.5)
print(f'os quatro ultimos são: \033[32m{times[-4:]}\033[m')
sleep(1.5)
print('\033[33m=-\033[m' * 15)
sleep(1.5)
print(f'os times em ordem alfabetica: \033[32m{sorted(times)}\033[m')
sleep(1.5)
print('\033[33m=-\033[m' * 15)
sleep(1.5)
print(f'o minas ta na \033[32m{times.index("minas")+1}ª posição\033[m')
