import duckdb
import pandas as pd
import streamlit as st

st.write("""
# SQL SRS
Spaced Repitition""")

data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(['Cat', "Dog", "Owl"])

with st.sidebar:
    option = st.selectbox(
        "What would you like to review?",
        ("Joins", "GroupBy","Window Functions"),
        index=None,
        placeholder="Select a theme..."
    )

    st.write('You selected', option)

with tab1:
    input_text = st.text_area(label='entrez votre input')
    st.write(input_text)
    st.dataframe(df)
    st.write(df)

with tab2:
    st.header("A dog")
    sql_query = st.text_area(label='entrez votre requête')
    result = duckdb.query(sql_query).df()
    st.write(f'Vous avez entré la query suivante: {sql_query}')
    st.dataframe(result)

with tab3:
    st.header("An owl")
