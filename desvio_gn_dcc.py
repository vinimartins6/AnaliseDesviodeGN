from google.colab import files
files.upload()

import pandas as pd
import numpy as np

df = pd.read_excel("Consumo_GN (4).xlsx")
df

df['dia_semana'].value_counts()[:7]

# Quinta-feira
df_quinta = df[df['dia_semana']=='quinta-feira']
df_quinta['Desvio_do_dia_diferenca'].mean()

# Sábado
df_sabado = df[df['dia_semana']=='sábado']
df_sabado['Desvio_do_dia_diferenca'].mean()

# Quarta-feira
df_quarta = df[df['dia_semana']=='quarta-feira']
df_quarta['Desvio_do_dia_diferenca'].mean()

# Segunda-feira
df_segunda = df[df['dia_semana']=='segunda-feira']
df_segunda['Desvio_do_dia_diferenca'].mean()

# Domingo
df_domingo = df[df['dia_semana']=='domingo']
df_domingo['Desvio_do_dia_diferenca'].mean()

# Desvios RK
df_desvios_RK=df[df['Desvio_RK']>0.1]
df_desvios_RK['dia_semana'].value_counts()[:7]

# Quinta-feira RK
df_quinta = df_desvios_RK[df_desvios_RK['dia_semana']=='quinta-feira']
df_quinta['Desvio_RK_diferença'].mean()

# sábado RK
df_sabado = df_desvios_RK[df_desvios_RK['dia_semana']=='sábado']
df_sabado['Desvio_RK_diferença'].mean()

# quarta-feira RK
df_quarta = df_desvios_RK[df_desvios_RK['dia_semana']=='quarta-feira']
df_quarta['Desvio_RK_diferença'].mean()

# segunda-feira RK
df_segunda = df_desvios_RK[df_desvios_RK['dia_semana']=='segunda-feira']
df_segunda['Desvio_RK_diferença'].mean()

# domingo RK
df_domingo = df_desvios_RK[df_desvios_RK['dia_semana']=='domingo']
df_domingo['Desvio_RK_diferença'].mean()

df_RK = df_desvios_RK[df_desvios_RK['%_producao']>1]
df_RK['%_producao'].mean()

df_RK = df_desvios_RK[df_desvios_RK['%_producao']<1]
df_RK['%_producao'].mean()

df_RK = df_desvios_RK[df_desvios_RK['%_producao']==0]
len(df_RK)/len(df_desvios_RK)

df_RK = df_desvios_RK[df_desvios_RK['%_producao']==0]
len(df_RK)/len(df)