segundos = input('Digite a quantidade de segundos que quer converter: ')
total_segundos = int(segundos)

horas = total_segundos // 3600 # só a parte inteira
segundos_restantes = total_segundos % 3600 # o resto da divisãp
minutos = segundos_restantes // 60 # divisão inteira
segundos_restantes_final = segundos_restantes % 60 # restp da divisão

print (horas, 'horas', minutos, 'minutos e ', segundos_restantes_final, 'segundos')