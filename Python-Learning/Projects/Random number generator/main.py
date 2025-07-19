from random import randint
import pandas as pd

Random_numbers = [0]


for i in range(1000):
    value = randint(0, 99)
    Random_numbers.append(value) 
    print(Random_numbers)
df = pd.DataFrame (Random_numbers, columns = ['RandomNumber'])
print(df)
df.to_excel('main.xlsx')