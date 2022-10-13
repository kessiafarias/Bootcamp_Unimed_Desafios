# Importando as Bibliotecas 

import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")

# Upload do Arquivo

from google.colab import files 
arq = files.upload()

# Criando nosso Dataframe 

df = pd.read_excel("AdventureWorks.xlsx")


# Visuaalizando as 5 primeiras linhas 

df.head()

# Quantidade de linhas e colunas 

df.shape

# Verificando os tipos de dados 

df.dtypes

# Qual a receita total?

df["Valor Venda"].sum()

# Qual o custo total? Criando uma coluna de custo

df["Custo"] = df["Custo Unitário"].mul(df["Quantidade"])

# Qual custo total?

round(df["Custo"].sum(), 2)

df.head(1)

# Agora que temos a receita, o custo e total, podemos achar o lucro total
# Vamos criar uma coluna de lucro que será receita - o custo

df["Lucro"] = df["Valor Venda"] - df["Custo"]

df.head(1)

# Lucro total

round(df["Lucro"].sum(), 2)

# Criando uma coluna com total de dias para enviar o produto

df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days

df.head(1)

# Extraindo apenas os dias 

df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days

df["Tempo_envio"].dtype


# Média de tempo de envio por marca

df.groupby("Marca")["Tempo_envio"].mean()


# Verificando se temos dados faltantes

df.isnull().sum()


# Vamos agrupar por ano e marca

df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum()

pd.options.display.float_format = "{:20,.2f}".format


# Resetando o Index

lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum().reset_index()
lucro_ano

# Qual total de produtos vendidos 

df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)

# Gráfico - Total de produtos vendidos

df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title= "Total de Produtos Vendidos")
plt.xlabel("Total")
plt.ylabel("Produtos");

# Grafico de Barras

df.groupby(df["Data Venda"].dt.year)["Lucro"].sum().plot.bar(title = "Lucro x Ano")
plt.xlabel("Ano")
plt.ylabel("Receita");

df.groupby(df["Data Venda"].dt.year)["Lucro"].sum()

# Selecionando apenas as vendas de 2009

df_2009 = df[df["Data Venda"].dt.year ==2009]

df_2009.head()


#Grafico de Linha

df_2009.groupby(df_2009["Data Venda"].dt.month)["Lucro"].sum().plot(title = "Lucro x Mês")
plt.xlabel("Mês")
plt.ylabel("Lucro");


# Grafico de Barras

df_2009.groupby("Marca")["Lucro"].sum().plot.bar(title = "Lucro x Marca")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation = "horizontal");


# Grafico de Barras

df_2009.groupby("Classe")["Lucro"].sum().plot.bar(title = "Lucro x Classe")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation = "horizontal");


# Estatísticas

df["Tempo_envio"].describe()

# Grafico de Boxplot 

plt.boxplot(df["Tempo_envio"]);

# Grafico de Histograma 

plt.hist(df["Tempo_envio"]);

# Tempo minimo de envio

df["Tempo_envio"].min()

# Tempo maximo de envio

df["Tempo_envio"].max()

# Identificando Outller

df[df["Tempo_envio"] == 20]

# Salvando o projeto 

df.to_csv("df_vendas_novo.csv", index=False)