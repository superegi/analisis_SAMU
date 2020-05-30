# Inicializo el lector standard
exec(open('inicializador_standard.py').read())

print('Inicio...')
# Cargo las funciones descriptivas
exec(open('Funciones_descriptoras.py').read())


print('Marzo 2019 vs 2020')
bucle_DLG_cantidad('2019-03-04')
plt.savefig('../Resultado_script/Llamadas_Cantidad_Marzo2019.png')
plt.clf()
#plt.show()
bucle_DLG_cantidad('2020-03-02')
plt.savefig('../Resultado_script/Llamadas_Cantidad_Marzo2020.png')
plt.clf()
#plt.show()

print('Abril 2019 vs 2020')
bucle_DLG_cantidad('2019-04-01')
plt.savefig('../Resultado_script/Llamadas_Cantidad_Abril2019.png')
plt.clf()
#plt.show()
bucle_DLG_cantidad('2020-04-06')
plt.savefig('../Resultado_script/Llamadas_Cantidad_Abril2020.png')
plt.clf()
#plt.show()


bucle_DLG_duracion('2019-03-04')
plt.savefig('../Resultado_script/Llamadas_duracion_Marzo2019.png')
plt.clf()
#plt.show()
bucle_DLG_duracion('2020-03-02')
plt.savefig('../Resultado_script/Llamadas_duracion_Marzo2020.png')
plt.clf()
#plt.show()

bucle_DLG_duracion('2019-04-01')
plt.savefig('../Resultado_script/Llamadas_duracion_Abril2019.png')
plt.clf()
#plt.show()
bucle_DLG_duracion('2020-04-06')
plt.savefig('../Resultado_script/Llamadas_duracion_Abril2020.png')
plt.clf()
#plt.show()

