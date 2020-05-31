# Inicializo el lector standard
exec(open('inicializador_standard.py').read())

print('Inicio...')
# Cargo las funciones descriptivas
exec(open('Funciones_descriptoras.py').read())


print('Marzo 2019 vs 2020')
bucle_DLG_cantidad(BD, '2019-03-04')
plt.savefig('../Resultado_script/Llamadas_Cantidad_Marzo2019.png')
plt.clf()
#plt.show()
bucle_DLG_cantidad(BD, '2020-03-02')
plt.savefig('../Resultado_script/Llamadas_Cantidad_Marzo2020.png')
plt.clf()
#plt.show()

print('Abril 2019 vs 2020')
bucle_DLG_cantidad(BD, '2019-04-01')
plt.savefig('../Resultado_script/Llamadas_Cantidad_Abril2019.png')
plt.clf()
#plt.show()
bucle_DLG_cantidad(BD, '2020-04-06')
plt.savefig('../Resultado_script/Llamadas_Cantidad_Abril2020.png')
plt.clf()
#plt.show()

bucle_DLG_duracion(BD, '2019-03-04')
plt.savefig('../Resultado_script/Llamadas_duracion_Marzo2019.png')
plt.clf()
#plt.show()
bucle_DLG_duracion(BD, '2020-03-02')
plt.savefig('../Resultado_script/Llamadas_duracion_Marzo2020.png')
plt.clf()
#plt.show()

bucle_DLG_duracion(BD, '2019-04-01')
plt.savefig('../Resultado_script/Llamadas_duracion_Abril2019.png')
plt.clf()
#plt.show()
bucle_DLG_duracion(BD, '2020-04-06')
plt.savefig('../Resultado_script/Llamadas_duracion_Abril2020.png')
plt.clf()
#plt.show()

DLG_duracion(BD, '2018-03-20', '2018-05-15')
DLG_duracion(BD, '2019-03-20', '2019-05-15')
DLG_duracion(BD, '2020-03-20', '2020-05-15', titulo = 'Duración de llamadas por hora \n Mismo periodo 2018, 2019 y 2020')
plt.savefig('../Resultado_script/Duración por hora.png')
# plt.show()
plt.clf()

DLG_cantidad(BD, '2018-03-20', '2018-05-15')
DLG_cantidad(BD, '2019-03-20', '2019-05-15')
DLG_cantidad(BD, '2020-03-20', '2020-05-15', titulo = 'Cantidad de llamadas por hora \n Mismo periodo 2018, 2019 y 2020')
plt.savefig('../Resultado_script/Cantidad por hora.png')
# plt.show()
plt.clf()

# print(tablaCDR_general(BD, '2019-03-20', '2019-05-15'))
# print(tablaCDR_general(BD, '2020-03-20', '2020-05-15'))



# Gráficos año 2018
tab2018 = tabla_indicadores(BD ,start='2018-01-02', end = '2019-01-01', freq='30D')
tab = tab2018
grafo_usoyllamadas(tab, 'Uso CR y cantidad llamadas \n 2018')
# plt.show()
plt.savefig('../Resultado_script/Usoyllamadas_2018.png',bbox_inches="tight")
plt.clf()
grafo_perdidasyduracion(tab, 'Llamadas perdidas y duración \n 2018')
# plt.show()
plt.savefig('../Resultado_script/Perdidasyduracion_2018.png',bbox_inches="tight")
plt.clf()

# Gráficos año 2019
tab2019 = tabla_indicadores(BD ,start='2019-01-03', end = '2020-01-01', freq='30D')
tab = tab2019
grafo_usoyllamadas(tab, 'Uso CR y cantidad llamadas \n 2019')
# plt.show()
plt.savefig('../Resultado_script/Usoyllamadas_2019.png',bbox_inches="tight")
plt.clf()
grafo_perdidasyduracion(tab, 'Llamadas perdidas y duración \n 2019')
# plt.show()
plt.savefig('../Resultado_script/Perdidasyduracion_2019.png',bbox_inches="tight")
plt.clf()

# Gráficos año 2020
tab2020 = tabla_indicadores(BD ,start='2020-01-02', end = '2020-05-20', freq='10D')
tab = tab2020
grafo_usoyllamadas(tab, 'Uso CR y cantidad llamadas \n 2020')
# plt.show()
plt.savefig('../Resultado_script/Usoyllamadas_2020.png',bbox_inches="tight")
plt.clf()
grafo_perdidasyduracion(tab, 'Llamadas perdidas y duración \n 2020')
# plt.show()
plt.savefig('../Resultado_script/Perdidasyduracion_2020.png',bbox_inches="tight")
plt.clf()


tab = tabla_indicadores(BD ,start='2019-10-02', end = '2019-12-10', freq='5D')
tab = tab
grafo_usoyllamadas(tab, 'Uso CR y cantidad llamadas \n Marchas 2019')
plt.savefig('../Resultado_script/Usoyllamadas_Marchas2019.png',bbox_inches="tight")
plt.clf()
grafo_perdidasyduracion(tab, 'Llamadas perdidas y duración \n Marchas 2019')
# plt.show()
plt.savefig('../Resultado_script/Perdidasyduracion_Marchas2019.png',bbox_inches="tight")
plt.clf()


# tab = pd.DataFrame({'2018'       : tablaCDR_general(BD, '2018.03.01', '2018-11-30'),
#               'Mar2019'    : tablaCDR_general(BD, '2019.03.01', '2019-03-30'),
#               'Abr2019'    : tablaCDR_general(BD, '2019.04.01', '2019-04-30'),
#               'May2019'    : tablaCDR_general(BD, '2019.05.01', '2019-05-30'),
#               'Nov2019'    : tablaCDR_general(BD, '2019.09.01', '2019-09-30'),
#               'Mar2020'    : tablaCDR_general(BD, '2020.03.01', '2020-03-15'),
#               'Abr2020'    : tablaCDR_general(BD, '2020.04.01', '2020-04-30'),
#               'May2020'    : tablaCDR_general(BD, '2020.05.01', '2020-05-30')
#              }
#             ).T

