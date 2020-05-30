# Inicialización standard tranversal
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from datetime import date, datetime, time, timedelta
from babel.dates import format_date, format_datetime, format_time, format_timedelta, Locale
import locale                                    # para tratar de poner espanol
import os
import runpy
from pyexcel_ods import get_data

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


#listo los archivos
scripts = []
for dirname, dirnames, filenames in os.walk('/home/egidio/Dropbox/Compucosas/programas py'):
    for filename in filenames:
        scripts.append(os.path.join(dirname, filename))
# los cargo
for script in scripts:
    if script[-3:] == '.py':
        exec(open(str(script)).read())

BD = pd.read_pickle('../llamadas_contraspaso.pkl')

