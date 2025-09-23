# Super.com OA Challenge 

Here are some assumptions I made for this OA + additional comments and documentation. 

- We can keep the numbers in the column name for the 'Airline Code' column.
- We can keep the space between 'Airline' and 'Code' for the Airline Code column - although it is not very SQL friendly, it was never required. In a production SQL database, I would change the column name to 'AirlineCode'. 
- Interpolation (linear) works here because the missing values follow a predictable sequence (+10). If that pattern wasn’t guaranteed, I’d use a different fill strategy.
