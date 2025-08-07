import pandas as pd
import matplotlib.pyplot as plt

# ================================
# PARTE 1 – Criando e Unindo DataFrames
# ================================

# Dados de nomes
dados_nomes = {
    'ID': [1, 2, 3, 4, 5, 6],
    'Nome': ['Ana', 'Bernado', 'Ricardo', 'Alex', 'Mauricio', 'Carlos']
}

# Dados de idades
dados_idades = {
    'ID': [1, 2, 3, 4, 5, 6],
    'Idade': [25, 20, 33, 26, 50, 43]
}

# Criando os DataFrames
df_nomes = pd.DataFrame(dados_nomes)
df_idades = pd.DataFrame(dados_idades)

# Unindo os dois DataFrames pelo ID
df_completo = pd.merge(df_nomes, df_idades, on='ID', how='inner')
print("➡️ DataFrame completo (nome + idade):")
print(df_completo)

# ================================
# PARTE 2 – Estatísticas
# ================================

# Média das idades
media_idades = df_completo['Idade'].mean()
print("\n📊 Média das idades:", media_idades)

# Moda das idades
moda_idades = df_completo['Idade'].mode()
print("📊 Moda das idades:", moda_idades[0])  # Se houver mais de uma moda, pega a primeira

# ================================
# PARTE 3 – Adicionando coluna 'Eh_Adulto'
# ================================

df_completo['Eh_Adulto'] = df_completo['Idade'] >= 18

print("\n✅ DataFrame com coluna 'Eh_Adulto':")
print(df_completo)

# ================================
# PARTE 4 – Resetando índice
# ================================

df_completo.reset_index(drop=True, inplace=True)

print("\n🔄 DataFrame com índice resetado:")
print(df_completo)

# ================================
# PARTE 5 – Agrupamento por Adultos
# ================================

media_por_grupo = df_completo.groupby('Eh_Adulto')['Idade'].mean()
print("\n📊 Média das idades por grupo de adultos:")
print(media_por_grupo)

# ================================
# PARTE 6 – Manipulação de CSV: Classificação de Glicose
# ================================

# Caminhos de arquivos
caminho_suja = 'data/glicose_data_suja.csv'
caminho_limpa = 'data/glicose_data_limpa.csv'
caminho_grafico = 'figures/histograma_idades.png'

# Lê o arquivo de dados de glicose
df_glicose = pd.read_csv(caminho_suja)

# Função para classificar os resultados
def classificar_glicose(valor):
    if valor <= 90:
        return 'baixo'
    elif valor <= 120:
        return 'normal'
    else:
        return 'alto'

# Aplica a função de classificação
df_glicose['Classificacao'] = df_glicose['Resultado'].apply(classificar_glicose)

print("\n📋 Classificação dos resultados de glicose:")
print(df_glicose[['Resultado', 'Classificacao']])

# ================================
# PARTE 7 – Filtrando resultados 'baixo'
# ================================

glicose_baixa = df_glicose[df_glicose['Classificacao'] == 'baixo']
print("\n🔍 Dias com glicose classificada como 'baixo':")
print(glicose_baixa)

# ================================
# PARTE 8 – Substituindo valores (ex: 96 por 90)
# ================================

df_glicose.loc[df_glicose['Resultado'] == 96, 'Resultado'] = 90
print("\n🔄 Substituindo valor 96 por 90 (se existir):")
print(df_glicose[df_glicose['Resultado'] == 90])

# ================================
# PARTE 9 – Gráfico e salvamento
# ================================

# Criar histograma das idades
plt.hist(df_completo['Idade'], bins=5, color='skyblue', edgecolor='black')
plt.title('Distribuição das Idades')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.grid(True)
plt.savefig(caminho_grafico)  # Salva o gráfico na pasta figures
print(f"✅ Gráfico salvo em '{caminho_grafico}'")

# Salvar dataframe glicose limpo em CSV
df_glicose.to_csv(caminho_limpa, index=False)
print(f"✅ Arquivo limpo salvo em '{caminho_limpa}'")
