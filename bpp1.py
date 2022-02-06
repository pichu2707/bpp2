import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('finanzas2020.csv', sep='\t')
print(df)

Ene = df['Enero']
Feb = df['Febrero']
Mar = df['Marzo']
Abr = df['Abril']
May = df['Mayo']
Jun = df['Junio']
Jul = df['Julio']
Ago = df['Agosto']
Sep = df['Septiembre']
Oct = df['Octubre']
Nov = df['Noviembre']
Dic = df['Diciembre']

print("----------------------Mes de Enero----------------------------------")
enero = []
ene_numero_error = 0
for i in Ene:
    try:
        i = int(i)
        enero.append(int(i))
        if i >=0:
            gasto_ene=i
        else:
            ahorro_ene=i
    except:
        ene_numero_error += 1
        print(f"este valor no es un entero: {i}")
    

totalmes_ene = sum(enero)
print(totalmes_ene)
print(ene_numero_error)
print(f"esto es el gasto de Enero {gasto_ene}")
print(f"este es el ahorro de Enero {ahorro_ene}")
print("----------------------Mes de Febrero----------------------------------")
febrero = []
feb_numero_error = 0
for i in Feb:
    try:
        i = int(i)
        febrero.append(int(i))
        if i >=0:
            gasto_feb=i
        else:
            ahorro_feb=i
    except:
        feb_numero_error += 1
        print(f"este valor no es un entero: {i}")
    

totalmes_feb = sum(febrero)
print(totalmes_feb)
print(feb_numero_error)
print(f"esto es el gasto de Febrero {gasto_feb}")
print(f"este es el ahorro de Febrero {ahorro_feb}")
print("----------------------Mes de Marzo----------------------------------")
marzo = []
mar_numero_error = 0    
for i in Mar:
    try:
        i = int(i)
        marzo.append(int(i))
        if i >=0:
            gasto_mar=i
        else:
            ahorro_mar=i
    except:
        mar_numero_error += 1
        print(f"este valor no es un entero: {i}")
    

totalmes_mar = sum(marzo)
print(totalmes_mar)
print(mar_numero_error)
print(f"esto es el gasto de Marzo {gasto_mar}")
print(f"este es el ahorro de Marzo {ahorro_mar}")
print("----------------------Mes de Abril----------------------------------")
abril = []
abr_numero_error = 0  
for i in Abr:
    try:
        i = int(i)
        abril.append(int(i))
        if i >=0:
            gasto_abr=i
        else:
            ahorro_abr=i
    except:
        abr_numero_error += 1
        print(f"este valor no es un entero: {i}")


totalmes_abr = sum(abril)
print(totalmes_abr)
print(abr_numero_error)
print(f"esto es el gasto de Abril {gasto_abr}")
print(f"este es el ahorro de Abril {ahorro_abr}")
print("----------------------Mes de Mayo----------------------------------")
mayo = []
may_numero_error = 0
for i in May:
    try:
        i = int(i)
        mayo.append(int(i))
        if i >=0:
            gasto_may=i
        else:
            ahorro_may=i
    except:
        may_numero_error += 1
        print(f"este valor no es un entero: {i}")

totalmes_may = sum(mayo)
print(totalmes_may)
print(may_numero_error)
print(f"esto es el gasto de Mayo {gasto_may}")
print(f"este es el ahorro de Mayo {ahorro_may}")

print("----------------------Mes de Junio----------------------------------")
junio = []
jun_numero_error = 0    
for i in Jun:
    try:
        i = int(i)
        junio.append(int(i))
        if i >=0:
            gasto_jun=i
        else:
            ahorro_jun=i
    except:
        jun_numero_error += 1
        print(f"este valor no es un entero: {i}")
    
print(f"esto es el gasto de Junio {gasto_jun}")
print(f"este es el ahorro de Junio {ahorro_jun}")
totalmes_jun = sum(junio)
print(totalmes_jun)
print(jun_numero_error)

print("----------------------Mes de Julio----------------------------------")
julio = []
jul_numero_error = 0
for i in Jul:
    try:
        i = int(i)
        julio.append(int(i))
        if i >=0:
            gasto_jul=i
        else:
            ahorro_jul=i
    except:
        jul_numero_error += 1
        print(f"este valor no es un entero: {i}")


print(f"esto es el gasto de Julio {gasto_jul}")
print(f"este es el ahorro de Julio {ahorro_jul}")
totalmes_jul = sum(julio)
print(totalmes_jul)
print(jul_numero_error)

print("----------------------Mes de Agosto----------------------------------")
agosto = []
ago_numero_error = 0    
for i in Ago:
    try:
        i = int(i)
        agosto.append(int(i))
        if i >=0:
            gasto_ago=i
        else:
            ahorro_ago=i
    except:
        ago_numero_error += 1
        print(f"este valor no es un entero: {i}")

print(f"esto es el gasto de Agosto {gasto_ago}")
print(f"este es el ahorro de Agosto {ahorro_ago}")
totalmes_ago = sum(agosto)
print(totalmes_ago)
print(ago_numero_error)

print("----------------------Mes de Septiembre----------------------------------")
septiembre = []
sep_numero_error = 0    
for i in Sep:
    try:
        i = int(i)
        septiembre.append(int(i))
        if i >=0:
            gasto_sep=i
        else:
            ahorro_sep=i
    except:
        sep_numero_error += 1
        print(f"este valor no es un entero: {i}")


print(f"esto es el gasto de Septiembre {gasto_sep}")
print(f"este es el ahorro de Septiembre {ahorro_sep}")
totalmes_sep = sum(septiembre)
print(totalmes_sep)
print(sep_numero_error)

print("----------------------Mes de Octubre----------------------------------")
octubre = []
oct_numero_error = 0
for i in Oct:
    try:
        i = int(i)
        octubre.append(int(i))
        if i >=0:
            gasto_oct=i
        else:
            ahorro_oct=i
    except:
        oct_numero_error += 1
        print(f"este valor no es un entero: {i}")

totalmes_oct = sum(octubre)
print(totalmes_oct)
print(oct_numero_error)
print(f"esto es el gasto de Octubre {gasto_oct}")
print(f"este es el ahorro de Octubre {ahorro_oct}")

print("----------------------Mes de Noviembre----------------------------------")
noviembre = []
nov_numero_error = 0
for i in Nov:
    try:
        i = int(i)
        noviembre.append(int(i))
        if i >=0:
            gasto_nov=i
        else:
            ahorro_nov=i
    except:
        nov_numero_error += 1
        print(f"este valor no es un entero: {i}")
 
totalmes_nov = sum(noviembre)
print(totalmes_nov)
print(nov_numero_error)
print(f"esto es el gasto de Noviembre {gasto_nov}")
print(f"este es el ahorro de Noviembre {ahorro_nov}")
print("----------------------Mes de Diciembre----------------------------------")
diciembre = []
dic_numero_error = 0
for i in Dic:
    try:
        i = int(i)
        diciembre.append(int(i))
        if i >=0:
            gasto_dic=i
        else:
            ahorro_dic=i
    except:
        dic_numero_error += 1
        print(f"este valor no es un entero: {i}")
    

totalmes_dic = sum(diciembre)
print(totalmes_dic)
print(dic_numero_error)
print(f"esto es el gasto de diciembre {gasto_dic}")
print(f"este es el ahorro de diciembre {ahorro_dic}")
gastomes = [gasto_dic,gasto_nov,gasto_oct,gasto_sep,gasto_ago,gasto_jul,gasto_jun,gasto_may,gasto_abr,gasto_mar,gasto_feb,gasto_ene]
gastomes.sort(reverse=True)
print(gastomes)
def gasto(lst):
    valor_minimo = 99999
    for i in gastomes:
        if(i < valor_minimo):
            valor_minimo = i
    return(valor_minimo)

ahorromes = [ahorro_dic,ahorro_nov,ahorro_oct,ahorro_sep,ahorro_ago,ahorro_jul,ahorro_jun,ahorro_may,ahorro_abr,ahorro_mar,ahorro_feb,ahorro_ene]
ahorromes.sort()
print(ahorromes)

def ahorro(lst2):
    valor_max = -1000
    for i in ahorromes:
        if(i > valor_max):
            valor_max=i
    return(valor_max)
media = (gasto_dic+gasto_nov+gasto_oct+gasto_sep+gasto_ago+gasto_jul+gasto_jun+gasto_may+gasto_abr+gasto_mar+gasto_feb+gasto_ene)/12
print(media)
def mediames(media):
    cuenta = sum(gastomes)
    cuenta = cuenta/12
    return(cuenta)
# totalingre = sum(ahorromes)

# print('\n')
# print(f"aquí tenemos los gastos ordenados de más a menos de cada mes y son: {valor_minimo}")
# print(f"Los ahorros que se han tenido de más a menos en cada mes han sido: {ahorromes}")
# print(f"La media de gasto al año han sido de: {media}")
# print(f"Los ingresos del año totales han sido de: {totalingre}")
# gastotal = sum(gastomes)
# print(f'El gasto total ha sido de: {gastotal}')

#gráfica de los gastos
# fig, ax = plt.subplots()
# ax.plot(['diciembre', 'noviembre', 'octubre', 'septiembre', 'agosto', 'julio', 'junio', 'mayo', 'abril', 'marzo', 'febrero', 'enero'],[gasto_dic,gasto_nov,gasto_oct,gasto_sep,gasto_ago,gasto_jul,gasto_jun,gasto_may,gasto_abr,gasto_mar,gasto_feb,gasto_ene])
# plt.show()
