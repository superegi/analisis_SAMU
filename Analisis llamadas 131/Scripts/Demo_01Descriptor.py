# Inicializo el lector standard
exec(open('inicializador_standard.py').read())





db1 = BD.loc[BD.Fecha > pd.to_datetime('2020-05-01')]

# Periodo de estudio
dum_t1 = db1.Fecha.describe()['first']
dum_t2 = db1.Fecha.describe()['last']

# Cantidad de días del estudio
dum_dt = db1.Fecha.describe()['last'] - db1.Fecha.describe()['first']

# Cantidad de llamadas en el estudio
dum_n = db1.Fecha.describe()['count']


print('El periodo de estudio fue desde el {} al {}. '
	.format(dum_t1.strftime('%d-%b-%Y'), dum_t2.strftime('%d-%b-%Y'))
	)

print('El tiempo de estudio corresponde a {} días, lo mismo que {} meses. '
	.format(dum_dt.days, str(dum_dt.days/30))
	)