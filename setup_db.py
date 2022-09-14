import sqlite3
from nsetools import Nse
nse = Nse()

conn = sqlite3.connect("test.sqlite")

# DROP ALL TABLES BEFORE CREATING IT
conn.execute("DROP TABLE IF EXISTS TOP_MOVERS")
print("Dropped all the tables")

# CREATE ALL THE TABLES

conn.execute('''CREATE TABLE TOP_MOVERS
                (ID            INT     NOT NULL,
                CATEGORY       TEXT    NOT NULL, 
                SYMBOL         TEXT    NOT NULL,
                LTP            INT     NOT NULL,
                CHANGE         TEXT    NOT NULL,
                NETPRICE       TEXT    NOT NULL,
                PRIMARY KEY (ID, CATEGORY));''')
print("Table TOP_MOVERS created successfully")



def insert_top_movers(conn, top_movers, category):
    all_data = []
    cols = ["symbol", "ltp", "change", "netPrice"]
    
    for ind, row in enumerate(top_movers):
        row["change"] = round(row["ltp"] - row["previousPrice"], 2)
        row['netPrice'] = str(row['netPrice']) + '%'
        data = [ind+1, category.upper()] + [row[key] for key in cols]
        all_data.append(tuple(data))
        
    conn.executemany(f"INSERT INTO TOP_MOVERS (ID, CATEGORY, SYMBOL, LTP, CHANGE, NETPRICE) VALUES (?, ?, ?, ?, ?, ?)", all_data)
    conn.commit()


# Insert Data to TOP_MOVERS TABLE
insert_top_movers(conn, nse.get_top_gainers()[:5], "Gainers")
insert_top_movers(conn, nse.get_top_losers()[:5], "Losers")

print("Data inserted to table TOP_MOVERS successfully")



conn.close()

