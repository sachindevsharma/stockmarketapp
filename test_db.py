import sqlite3
import pandas as pd
from nsetools import Nse
nse = Nse()

conn = sqlite3.connect("test.sqlite")

    
def update_top_movers(conn, top_movers, category):
    all_data = []
    cols = ["symbol", "ltp", "change", "netPrice"]
    
    for ind, row in enumerate(top_movers):
        row["change"] = round(row["ltp"] - row["previousPrice"], 2)
        row['netPrice'] = str(row['netPrice']) + '%'
        data = [row[key] for key in cols] + [ind+1, category.upper()]
        all_data.append(data)
        
    conn.executemany(f"""UPDATE TOP_MOVERS 
                     SET SYMBOL=?, LTP=?, CHANGE=?, NETPRICE=?
                     WHERE ID=? AND CATEGORY=?""", all_data)
    conn.commit()
    
def get_data_from_table(conn, table_name, cols=None):
    if cols is None:
        query = f"SELECT * FROM {table_name} ORDER BY ID"
    else:
        col_name = ",".join(cols)
        query = f"SELECT {col_name} FROM {table_name} ORDER BY ID"
        
    return pd.read_sql_query(query, conn)


# cursor = conn.cursor()
top_gainers = nse.get_top_gainers()[:5]
update_top_movers(conn, top_gainers, "Gainers")

top_losers = nse.get_top_losers()[:5]
update_top_movers(conn, top_losers, "Losers")

df = get_data_from_table(conn, "TOP_MOVERS")

print(df.columns)
print(df)
# print(top_movers)
print(get_data_from_table(conn, "TOP_MOVERS", ["SYMBOL", "LTP"])
)
# cursor = conn.execute("SELECT * FROM TOP_MOVERS")

# for row in cursor:
#     print(row)



conn.close()

