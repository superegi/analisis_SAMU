
# Defino las funciones


# Función que corta dataset en fechas. Si no
# se define fecha le suma 1 mes
def corte_dataset(dataset, inicio= None, fin=None):
    inicio = pd.to_datetime(inicio)
    fin = pd.to_datetime(fin)
    if inicio != None:
        if fin !=None:
            print('Seteado inicio y fin')
            db1 = dataset.loc[
                (dataset.Fecha > inicio) &
                (dataset.Fecha < fin)]
        else:
            fin = inicio + timedelta(weeks=1)
            print('Seteado inicio, NO fin')
            db1 = dataset.loc[
                (dataset.Fecha > inicio) &
                (dataset.Fecha < fin)]
    else:
        print('No hay rango de fecha seteado. Se procede con todo')
        db1 = dataset
    
    print('Rango de fecha: Inicio({}) y fin({})'.format(inicio, fin))
    return db1

# Función descriptora de llamadas, normalizada por mes y día
def tablaCDR_general(dataset, inicio= None, fin=None):
    # Selecciono un rango de fechas para la función
    db1 = corte_dataset(dataset, inicio, fin)
    
    # Hago las métricas
    descripcion_dum = db1.Fecha.describe()
    var = pd.Series([])
    var['Primera observacion']  = descripcion_dum[4]
    var['Ultima observacion']   = descripcion_dum[5]
    var['Duracion en dias']     = (descripcion_dum[5] - descripcion_dum[4]).days
    var['Duracion en meses']    = (descripcion_dum[5] - descripcion_dum[4]).days/30
    var['Llamadas (n)']         = descripcion_dum[0]
    var['Llamadas (n/mes)']     = var['Llamadas (n)']/var['Duracion en meses']
    var['Llamadas (n/dia)']     = var['Llamadas (n)']/var['Duracion en dias']
    
    var['Llamadas Hacia SAMU/mes']         = db1.loc[db1.Tipo_llamada=='Hacia SAMU'].Fecha.count()/var['Duracion en meses']
    var['Llamadas Hacia SAMU/dia']         = db1.loc[db1.Tipo_llamada=='Hacia SAMU'].Fecha.count()/var['Duracion en dias']
    
    var['Duración llamada prom (min)']     = db1.loc[db1.Tipo_llamada=='Hacia SAMU'].Duracion.mean()/60
    
    var['Llamadas traspasadas/mes']            = db1.loc[db1.Trapaso=='Si'].Fecha.count()/var['Duracion en meses']
    var['Llamadas traspasadas/dia']        = db1.loc[db1.Trapaso=='Si'].Fecha.count()/var['Duracion en dias']
    
    var['Uso horario (%prom)']             = np.mean(          # corresponde al uso de 1 hora de CR
        ((db1.groupby(db1.Fecha.dt.hour)).Duracion.sum())/(var['Duracion en dias']*60)/60 *100)

    var['Llamadas perdidas/mes']       = db1.loc[db1.Estado=='Perdida'].Fecha.count()/var['Duracion en meses']
    var['Llamadas perdidas/dia']       = db1.loc[db1.Estado=='Perdida'].Fecha.count()/var['Duracion en dias']

    return var

# Tabla indicadores
def tabla_indicadores(dataset, start=None, **kwargs):
    datelist1 = pd.date_range(start,**kwargs)
    dictado = dict()
    for x in datelist1:
        dictado[
            str(x.strftime("%d%b%y"))] = tablaCDR_general(dataset, x, fin=(pd.to_datetime(x)+datelist1.freq))
    tab = pd.DataFrame(dictado).T
    return tab

#graficos desde la tabla
def grafo_usoyllamadas(tabla, titulo=None):
    fig,ax = plt.subplots()
    ax.plot(tabla[['Uso horario (%prom)']], color="black", marker="o")
    ax.set_ylim([50,600])
    ax.set_xlabel("Periodo",fontsize=14)
    ax.title.set_text(titulo)
    plt.xticks(rotation='vertical')
    ax.set_ylabel("Uso del CR en %",color="black",fontsize=14)

    ax2=ax.twinx()
    ax2.plot(tabla[['Llamadas (n/mes)']], color="#2ca02c", marker="x")
    ax2.set_ylim([27000,39000])
    ax2.set_ylabel("Cantidad llamadas (n/mes)",color="#2ca02c",fontsize=14)


def grafo_perdidasyduracion(tabla, titulo=None):
    fig,ax = plt.subplots()
    tabla['Llamadas perdidas/mes'].plot(kind='bar', color='#1f77b4')
    ax.set_ylim([100,1200])
    ax.set_xlabel("Periodo",fontsize=14)
    ax.title.set_text(titulo)
    plt.xticks(rotation='vertical')
    ax.set_ylabel("Llamadas perdidas/mes",color="#1f77b4",fontsize=14)

    ax2=ax.twinx()
    ax2.plot(tabla[['Duración llamada prom (min)']], color="r", marker="x")
    ax2.set_ylim([1,2.5])
    ax2.set_ylabel("Duración llamada prom (min)",color="r",fontsize=14)

# graficos de cantidad de llamadas y uso de CR
def DLG_cantidad(dataset, inicio=None, fin=None, ax= None, titulo=None, **kwargs):
    # Selecciono un rango de fechas para la función
    db1 = corte_dataset(dataset, inicio, fin)
    
    # Métricas #######
    metricas = tablaCDR_general(db1) 
    dum_t1 = metricas['Primera observacion']
    dum_t2 = metricas['Ultima observacion']
    dum_dt = metricas['Duracion en dias']
    
    # Gráfico de llamadas por hora ########################################################
    ax = ax or plt.gca()  # si hay ax se queda, si no lo hay lo creo
    (db1.groupby(db1.Fecha.dt.hour).count().Fecha/dum_dt).plot(
        ax = ax,
        label=' {} al {}. '.format(dum_t1.strftime('%d-%b-%Y'), dum_t2.strftime('%d-%b-%Y')),
        **kwargs)
    plt.xlabel('Hora del día')
    plt.ylabel('Cantidad de llamadas')
    plt.title(titulo)
    plt.ylim([0,90])
    plt.grid()
    plt.legend(loc='lower right')
    
def DLG_duracion(dataset, inicio=None, fin=None, ax= None, titulo=None, **kwargs):
    # Selecciono un rango de fechas para la función
    db1 = corte_dataset(dataset, inicio, fin)
    
    # Métricas #######
    metricas = tablaCDR_general(db1) 
    dum_t1 = metricas['Primera observacion']
    dum_t2 = metricas['Ultima observacion']
    dum_dt = metricas['Duracion en dias']
    
    # Gráfico de llamadas por hora ########################################################
    ax = ax or plt.gca()  # si hay ax se queda, si no lo hay lo creo
    ((db1.groupby(db1.Fecha.dt.hour)).Duracion.sum()/(dum_dt*60)).plot(
        ax = ax,
        label=' {} al {}. '.format(dum_t1.strftime('%d-%b-%Y'), dum_t2.strftime('%d-%b-%Y')),
        **kwargs)
    plt.xlabel('Hora del día')
    plt.ylabel('Duración acumulada de llamadas en minutos')
    plt.title(titulo)
    plt.ylim([0,140])
    plt.grid()
    plt.legend(loc='lower right')

# Defino algunos bucles
def bucle_DLG_cantidad(dataset, inicio=None, fin=None, repeticiones=4):
    inicio = pd.to_datetime(inicio)
    for x in range(repeticiones):
        print('Vuelta:', x)
        t1     = inicio + timedelta(days=x*7)
        t2     = t1 + timedelta(days=7)
        DLG_cantidad(dataset, t1, t2)

def bucle_DLG_duracion(dataset, inicio=None, fin=None, repeticiones=4):
    inicio = pd.to_datetime(inicio)
    for x in range(repeticiones):
        print('Vuelta:', x)
        t1     = inicio + timedelta(days=x*7)
        t2     = t1 + timedelta(days=7)
        DLG_duracion(dataset, t1, t2)


