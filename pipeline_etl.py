import pandas as pd
print("1. [Extract] lendo os dados brutos")
df= pd.read_csv("dados_brutos.csv")
print(f"total de linha brutas carregadas: {len(df)}")
print("\n2. [TRANSFORM] Iniciando a limpeza e tratamento de dados")
df= df.drop_duplicates()
print(f"Linhas após remover duplicadas: {len(df)}")
df[("produto")] = df["produto"].fillna("Produto Genérico")
df["data_venda"] = df["data_venda"].fillna("10/05/2026")
df["valor"] = pd.to_numeric(df["valor"],errors="coerce")
def categorizar_ticket (valor) :
    if valor >= 200:
        return "Valor padrão"
    else:
        return "Padrão"
df ["categorizar_ticket"]=df ["valor"].apply(categorizar_ticket)
print("\n Dados limpos e transformado com sucesso!")
print(df)
print("\n3. [LOAD] Salvando a base  e tratada...")    
df.to_csv("dados_tratados.csv", index=False)
df.to_excel("Relatorio_tratado.xlsx",index=False)   
print("Processo de ETL concluído com sucesso! Arquivos 'dados_tratados.csv' e 'relatorio_tratado.xlsx' gerados.")     