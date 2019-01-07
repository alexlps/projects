#from pyspark.sql import HiveContext
import pandas as pd
import numpy as np
import datetime as dt 

# Importando base consolidada com os caches anuais
df = pd.read_excel("c:\\teste\Vendas_de_Combustiveis_m3.xls","analitico")


# Adicionando coluna mês. Tive que transpor as colunas...
df = pd.melt(df.reset_index(), id_vars=['produto','ano','regiao','estado','unidade'], 
var_name='mes', value_name='vol_demanda_m3')


# Tratando as linhas invalidas com o valor "index" após transpor as colunas mensais
df = df[df.mes.str.contains("index") == False]


# Adicionando campo ano_mes_foto
df['ano_mes_foto'] = dt.datetime.today().strftime("%m/%Y")


# Ordenando os campos
df = df[['ano', 'mes', 'estado', 'produto', 'unidade', 'vol_demanda_m3' , 'ano_mes_foto' ]]

display(df)


# Salvando tabela no HIVE adicionando partição nos campos "ano" e "mes"

# OBS.: O Comando abaixo salva a tabela no HIVE utilizando a lib do hive.context.
# Como utilizei um Jupyter Notebook, o comando abaixo seria compilado em um abiente com cluster configurado.

df.write().mode(SaveMode.Append).partitionBy("ano","mes").saveAsTable("base_anp")