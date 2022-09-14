import sqlite3
import pandas as pd
from nsetools import Nse
nse = Nse()

    
class DataToSQL:
    db: any    
    
    def update_top_movers_table(self, top_movers, category):
        all_data = []
        cols = ["symbol", "ltp", "change", "netPrice"]
        
        for ind, row in enumerate(top_movers):
            row["change"] = round(row["ltp"] - row["previousPrice"], 2)
            row['netPrice'] = str(row['netPrice']) + '%'
            data = [row[key] for key in cols] + [ind+1, category.upper()]
            all_data.append(data)
            
        self.db.executemany(f"""UPDATE TOP_MOVERS 
                                SET SYMBOL=?, LTP=?, CHANGE=?, NETPRICE=?
                                WHERE ID=? AND CATEGORY=?""", all_data)
        self.db.commit()



# # cursor = conn.cursor()
# SQL = SQLConnector()
# conn = SQL.connect("test.sqlite")

# top_gainers = nse.get_top_gainers()[:5]
# SQL.update_top_movers(conn, top_gainers, "Gainers")

# top_losers = nse.get_top_losers()[:5]
# SQL.update_top_movers(conn, top_losers, "Losers")

# df = SQL.get_data_from_table(conn, "TOP_MOVERS")

# print(df.columns)
# print(df)
# # print(top_movers)
# print(SQL.get_data_from_table(conn, "TOP_MOVERS", ["SYMBOL", "LTP"]))


# conn.close()

