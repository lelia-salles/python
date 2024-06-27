# A tabela de RH possui dados como nome, endereço, admissão, carga horária diária, semanal
# valor da hora aula, dias da semana, do mês, custo semanal, custo mensal
# idéia de negócio: fazer um formulário de cadastro de funcionário e pagamento automático que registre os dados
# em formulário do google forms, escolha dois bancos para fazer a integração de pagamento. Todos os pagamentos devem
# ser feitos 30 dias após a data de admissão do funcionário.
# o formulário deve conter dados se o contratado é MEI, CLT ou governo, calcular impostos devidos como férias,  fgts, inss,
# entre outros e realizar o pagamento de acordo.
# o formulário deve armazenar e mostrar os valores que foram descontados mas devem ser pagos para fgts, inss, férias
# adicionar salário além da hora/aula
nome = input("Digite o nome completo do funcionário: ")  # constante
endereco = input("Digite o endereço completo do funcionário: ")  # variável
admissao = input("Digite a data de admissão: ")  # constante
area_atuacao = input('Digite a área de atuação: ')
cargaHoraria_dia = float(input("Digite a carga horária diária "))  # variável
valorAula_hora = float(input("Digite o valor da hora/aula: " ))  #variável
diaria = cargaHoraria_dia/cargaHoraria_dia #variável
cargaHoraria_semana = cargaHoraria_dia * 5  # variável
dias_da_semana = float(diaria * 5)  #variável
dias_do_mes = dias_da_semana * 4 #variável
custo_semanal = float(valorAula_hora * dias_da_semana) #variável
custo_mensal = valorAula_hora * dias_do_mes #variável

# carga horária dia não deve ultrapassar 8 horas
#checar como fazer operação matemática com diferentes tipos de dados, exemplo float e int
#checar como converter o input do usuário de string para float ou inteiro
print('Nome: ', nome, ' Endereço: ', endereco, ' Admissão: ' , admissao, 'Área de atuação: ', area_atuacao ,
      ' Carga horária diária : ' , cargaHoraria_dia, ' Carga horária semanal: ', cargaHoraria_semana,
      ' Valor hora/aula: ', valorAula_hora, ' Dias da semana: ', dias_da_semana,
      ' Dias do mês: ', dias_do_mes, ' Custo semanal ', custo_semanal, ' Custo mensal: ', custo_mensal)


