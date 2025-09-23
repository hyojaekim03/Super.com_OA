import pandas as pd
import re
from io import StringIO # need to read string as a file (csv)
import sqlite3

raw_data = 'Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12, 33];20055.0;london_MONTreal\n'

df = pd.read_csv(StringIO(raw_data), sep=';')

#1
df["FlightCodes"] = df["FlightCodes"].interpolate().astype(int)

#2
df[["To", "From"]] = df["To_From"].str.upper().str.split("_", expand=True)
df = df.drop(columns=["To_From"])

#3
# assumption made: Numbers are still allowed -> included numbers in regex expression
df["Airline Code"] = df["Airline Code"].str.replace(r'[^A-Za-z0-9\s]','', regex=True).str.strip().str.replace(r'\s+', ' ', regex=True)

#4 - write to local sqlite db
conn = sqlite3.connect('flights.db')
df.to_sql('flights', conn, if_exists='replace', index=False)

#test: read from db
query = 'SELECT * FROM flights'
result_df = pd.read_sql_query(query, conn)
print(result_df)