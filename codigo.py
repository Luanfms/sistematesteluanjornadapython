# titulo - Sistema de vendas
# Seção cadastrar vendas
    #campo data
    #campo vendedor - Ana, Bruno, Carla
    # campo do produto - notebook, fone, celular
    # campo quantidade
    # campo valor
    # botão cadastrar venda
        # quand clicar no botão -> adicionar a venda na tabela
# Seção vendas cadastradas 
        # tabela com as vendas
# Seção Dashboard
    # card/métrica -> faturameto total
    # grafico de barra/coluna -> venda por vendedor
    # grafico de pizza -> venda por produto

# streamlit run codigo.py

import streamlit as st
import pandas as pd
import plotly.express as px

# carregar a base de vendas
tabela_vendas = pd.read_csv('vendas.csv')

st.write('# Sistema de Vendas')

# seção de cadatros de vendas
st.sidebar.write('## Cadastrar Vendas')
data =st.sidebar.date_input('DATA')
vendedor = st.sidebar.selectbox ('Vendedor',['Ana', 'Bruno','Carla'])
produto = st.sidebar.selectbox ('Produto', ['Notebook','Celular', 'Fone'])
quantidade = st.sidebar.number_input ('Quantidade', step=1)
valor = st.sidebar.number_input ('Valor')
botao_cadastrar = st.sidebar.button ('Cadastrar Vendas')

#logica de cadastro
if botao_cadastrar:
    nova_venda = [str(data), vendedor, produto, quantidade, valor]
    ultima_linha = len(tabela_vendas)
    tabela_vendas.loc[ultima_linha] = nova_venda
    tabela_vendas.to_csv('vendas.csv', index=False)
    st.success('Venda Cadastrada')
    
#seção de vizualizar vendas
st.write('## Vendas Cadastradas')
st.dataframe(tabela_vendas) 

# seção de Dashboard
st.write('## Deashboard')
    
    # card/métrica -> faturameto total
faturamento = tabela_vendas['valor'].sum()
st.metric('Faturamento Total', f'R${faturamento}')

    # grafico de barra/coluna -> venda por vendedor

grafico = px.bar(tabela_vendas, x='vendedor', y='valor', color='produto')
st.plotly_chart(grafico)

    # grafico de pizza -> venda por produto
grafico2 = px.pie(tabela_vendas, names='produto', values='valor', hole=0.5)
st.plotly_chart(grafico2)