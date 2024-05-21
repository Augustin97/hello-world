import io

import duckdb
import pandas as pd
import streamlit as st

st.write("""
# SQL SRS
Spaced Repitition""")

data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

csv = '''
beverage, price
orange juice, 2.5
expresso, 2
tea, 3'''

beverages = pd.read_csv(io.StringIO(csv))

csv2 = '''
food_item, food_price
cookie, 2.5
pain au chocolat, 2
muffin, 3
'''

food_items = pd.read_csv(io.StringIO(csv2))

answer = '''
SELECT * FROM beverages
CROSS JOIN food_items'''

solution = duckdb.sql(answer).df()

st.header("enter your code:")
query = st.text_area(label='votre code SQL ici', key="user_input")

if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)

with st.sidebar:
    option = st.selectbox(
        "What would you like to review?",
        ("Joins", "GroupBy", "Window Functions"),
        index=None,
        placeholder="Select a theme..."
    )

    st.write('You selected', option)

tab1, tab2 = st.tabs(["Tables", "Solution"])

with tab1:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food items")
    st.dataframe(food_items)
    st.write("expected:")
    st.dataframe(solution)

with tab2:
    st.write(answer)
