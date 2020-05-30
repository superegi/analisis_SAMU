# Inicializo el lector standard
exec(open('inicializador_standard.py').read())




# Defino las funciones

def descripcion_llamadas_general(inicio, fin, ax= None, **kwargs):
    # inicio y fin son fechas 
    db1 = BD.loc[
        (BD.Fecha > pd.to_datetime(inicio)) &
        (BD.Fecha < pd.to_datetime(fin))]
    # Periodo de estudio ########################################################
    dum_t1 = db1.Fecha.describe()['first']
    dum_t2 = db1.Fecha.describe()['last']

    # Cantidad de días del estudio ########################################################
    dum_dt = db1.Fecha.describe()['last'] - db1.Fecha.describe()['first']

    # Cantidad de llamadas en el estudio ############################################
    dum_n = db1.Fecha.describe()['count']
    print('El periodo de estudio fue desde el {} al {}. '
        .format(dum_t1.strftime('%d-%b-%Y'), dum_t2.strftime('%d-%b-%Y'))
        )
    print('El tiempo de estudio corresponde a {} días, lo mismo que {} meses. '
        .format(
            dum_dt.days,
            str(round(dum_dt.days/30,3))
            )
        )
    print('')
    print('La cantidad de llamadas en el periodo de estudio fue de {}llamadas,\
    equivalente a {} llamadas diarias y {} mensuales.'
        .format(
            dum_n,
            round(dum_n/pd.to_numeric(dum_dt.days)),
            round(30*dum_n/pd.to_numeric(dum_dt.days))
        )
         )
    print('')

def DLG_cantidad(inicio, fin, ax= None, **kwargs):
    # inicio y fin son fechas 
    db1 = BD.loc[
        (BD.Fecha > pd.to_datetime(inicio)) &
        (BD.Fecha < pd.to_datetime(fin))]
    # Periodo de estudio ########################################################
    dum_t1 = db1.Fecha.describe()['first']
    dum_t2 = db1.Fecha.describe()['last']

    # Cantidad de días del estudio ########################################################
    dum_dt = db1.Fecha.describe()['last'] - db1.Fecha.describe()['first']
    # Gráfico de llamadas por hora ########################################################
    ax = ax or plt.gca()  # si hay ax se queda, si no lo hay lo creo
    (db1.groupby(db1.Fecha.dt.hour).count().Fecha/dum_dt.days).plot(
        ax = ax,
        label=' {} al {}. '.format(dum_t1.strftime('%d-%b-%Y'), dum_t2.strftime('%d-%b-%Y')),
        **kwargs)
    plt.xlabel('Hora del día')
    plt.ylabel('Cantidad de llamadas')
    plt.title('Cantidad de llamadas según hora')
    plt.ylim([0,90])
    plt.grid()
    plt.legend(loc='lower right')
    
def DLG_duracion(inicio, fin, ax= None, **kwargs):
    # inicio y fin son fechas 
    db1 = BD.loc[
        (BD.Fecha > pd.to_datetime(inicio)) &
        (BD.Fecha < pd.to_datetime(fin))]
    # Periodo de estudio ########################################################
    dum_t1 = db1.Fecha.describe()['first']
    dum_t2 = db1.Fecha.describe()['last']

    # Cantidad de días del estudio ########################################################
    dum_dt = db1.Fecha.describe()['last'] - db1.Fecha.describe()['first']
    # Gráfico de llamadas por hora ########################################################
    ax = ax or plt.gca()  # si hay ax se queda, si no lo hay lo creo
    ((db1.groupby(db1.Fecha.dt.hour)).Duracion.sum()/(dum_dt.days*60)).plot(
        ax = ax,
        label=' {} al {}. '.format(dum_t1.strftime('%d-%b-%Y'), dum_t2.strftime('%d-%b-%Y')),
        **kwargs)
    plt.xlabel('Hora del día')
    plt.ylabel('Duración acumulada de llamadas en minutos')
    plt.title('Duración de llamadas por hora')
    plt.ylim([0,140])
    plt.grid()
    plt.legend(loc='upper left')


# Defino algunos bucles

def bucle_DLG_cantidad(fecha, repeticiones=4):
    Start1 = pd.to_datetime(fecha)
    n=0
    for x in range(repeticiones):
        inicio  = Start1 + timedelta(weeks=n)
        fin     = inicio + timedelta(weeks=1)
        DLG_cantidad(inicio, fin)
        n=n+1

def bucle_DLG_duracion(fecha, repeticiones=4):
    Start1 = pd.to_datetime(fecha)
    n=0
    for x in range(repeticiones):
        inicio  = Start1 + timedelta(weeks=n)
        fin     = inicio + timedelta(weeks=1)
        DLG_duracion(inicio, fin)
        n=n+1