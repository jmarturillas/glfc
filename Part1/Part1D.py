

"""
Problem : Given the two transaction tables, table1 and table2. Create a script/code the determines if all the
transactions in table 2 are equal to the transactions in table1 for the date after 10/21/2019

Table 1
_______________________________________________
| TransactionName  | Transaction_date | Value |
| JuanDeLaCruz     | 10/01/2019       | 1     |
| JuanDeLaCruz     | 10/22/2019       | 2     |
| MariaMakiling    | 10/3/2019        | 3     |
| MariaMakiling    | 10/23/2019       | 4     |
-----------------------------------------------

Table 2
_______________________________________________
| TransactionName  | Transaction_date | Value |
| JuanDeLaCruz     | 10/22/2019       | 2     |
| MariaMakiling    | 10/23/2019       | 4     |
-----------------------------------------------
"""

import pandas as pd
import numpy as np

table_1 = {
    "TransactionName": ["JuanDeLaCruz", "JuanDeLaCruz", "MariaMakiling", "MariaMakiling"],
    "Transaction_date": ["10/01/2019", "10/22/2019", "10/3/2019", "10/23/2019"],
    "Value": [1, 2, 3, 4]
}

table_2 = {
    "TransactionName": ["JuanDeLaCruz", "MariaMakiling"],
    "Transaction_date": ["10/22/2019","10/23/2019"],
    "Value": [2, 4]
}

df_1 = pd.DataFrame(table_1)
df_2 = pd.DataFrame(table_2)

table_list_1 = []
table_list_2 = []

matching_rows = []

for index, row in df_1.iterrows():
    row_table_1 = row['TransactionName'], row['Transaction_date'], row['Value']
    table_list_1.append(row_table_1)

for index_2, row in df_2.iterrows():
    row_table_2 = row['TransactionName'], row['Transaction_date'], row['Value']
    table_list_2.append(row_table_2)

for row_1 in table_list_1:
    for row_2 in table_list_2:
        if row_1 == row_2:
            matching_rows.append(row_1)
            matching_rows.append(row_2)

print(matching_rows)
