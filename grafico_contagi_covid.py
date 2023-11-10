#fare grafico dei contagi covid di una certa regione

import numpy as pd
import matplotlib.pyplot as mpl
import pandas as pd




datatot = pd.read_csv('covid_dati.csv',index_col= 'data', parse_dates=True,  sep=',') #lettura di tutti i dati
data1 = datatot[['denominazione_regione','terapia_intensiva', 'deceduti']]     #selezione colonne giuste
#non seleziono la data perchè l'indice della tabella!!!!
#il grafico metterà sull'asse x l'indice della tabella--> quindi la data !!!

for i , (reg , valori) in enumerate (data1.groupby('denominazione_regione')):
    if reg== 'Molise':
        
        dati1_veneto = valori.drop(['denominazione_regione'], axis=1)   #tolgo dal mio dataframe la colonna del nome delle regioni
    

    
    
dati1_veneto.plot()  

