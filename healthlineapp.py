import pandas as pd
import streamlit as st

df = pd.read_csv('disease_data.csv')

st.title("Disease Information Explorer")

diseases = df['disease'].unique()
select_disease = st.selectbox('Select a disease',diseases)

disease_data = df[df['disease'] == select_disease]

for _, row in disease_data.iterrows():
    with st.expander(row["section"]):
        st.write(row["content"])