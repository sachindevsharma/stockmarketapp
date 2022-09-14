import pandas as pd 
from dataclasses import dataclass
from sql import MongoConnector


@dataclass
class TOP_MOVERS:
    client: any
    
    def __post_init__(self):
        self.top_movers_col = self.client["stocks"]["top_movers"]
    
    def get_top_gainers(self):
        data = list(self.top_movers_col.find({"Category": "GAINERS"}, 
                                             {"Symbol": 1, "LTP": 1, "Change": 1, "% Change": 1, "_id": False}))
        df = pd.DataFrame(data)
        return df
    
    def get_top_losers(self):
        data = list(self.top_movers_col.find({"Category": "LOSERS"}, 
                                             {"Symbol": 1, "LTP": 1, "Change": 1, "% Change": 1, "_id": False}))
        df = pd.DataFrame(data)
        return df