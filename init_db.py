import io
import pandas as pd
import duckdb

con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)
# -----------------------------------------------
# EXERCICES LIST
# -----------------------------------------------

data = {
    "theme": ["Cross Joins"],
    "exercise_name": ["beverages and food"],
    "tables": [["beverages", "food_items"]],
    "last_reviewed": ["1997-01-01"],
}

memory_state_df = pd.DataFrame(data)
con.execute("CREATE OR REPLACE TABLE memory_state AS SELECT * FROM memory_state_df")

# -----------------------------------------------
# CROSS JOIN EXERCISES
# -----------------------------------------------

csv = '''
beverage, price
orange juice, 2.5
expresso, 2
tea, 3'''

beverages = pd.read_csv(io.StringIO(csv))
con.execute("CREATE OR REPLACE TABLE beverages AS SELECT * FROM beverages")

csv2 = '''
food_item, food_price
cookie, 2.5
pain au chocolat, 2
muffin, 3
'''

food_items = pd.read_csv(io.StringIO(csv2))
con.execute("CREATE OR REPLACE TABLE food_items AS SELECT * FROM food_items")
