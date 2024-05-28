import io
import duckdb
import pandas as pd
import streamlit as st

st.write("""
# SQL SRS
Spaced Repitition""")

con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review?",
        ("Cross Joins", "GroupBy", "Window Functions"),
        index=None,
        placeholder="Select a theme..."
    )

    st.write('You selected', theme)

    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme ='{theme}'").df()
    st.write(exercise)

    try:
        exercise_name = exercise.loc[0, "exercise_name"]
        with open(f"answers/{exercise_name}.sql", "r") as f:
            answer = f.read()
            solution = con.execute(answer).df()

    except Exception as e:
        print(e)

st.header("enter your code:")
query = st.text_area(label='votre code SQL ici', key="user_input")

if query:
    result = con.execute(f"{query}").df()
    st.dataframe(result)

    if len(result.columns) != len(solution.columns):
        st.write("Some columns are missing")

    n_line_missing = abs(result.shape[0] - solution.shape[0])
    if n_line_missing != 0:
        st.write(f'result has {n_line_missing} lines difference with the solution_df')

    try:
        result = result[solution.columns]
        st.dataframe(result.compare(solution))
    except KeyError as e:
        st.write("Some columns are missing")


tab1, tab2 = st.tabs(["Tables", "Solution"])

with tab1:
    try:
        exercise_tables = exercise.loc[0, "tables"]
        for table in exercise_tables:
            st.write(f"table: {table}")
            st.dataframe(con.execute(f"SELECT * FROM {table}").df())
    except KeyError as e:
        print(e)
with tab2:
    try:
        st.text(answer)
    except NameError as e:
        print(e)
