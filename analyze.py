import pandas as pd

df = pd.read_csv('results/zeroshot_experiment.csv')
print((df['result'].astype('str') == df['response']).astype('float').mean())
