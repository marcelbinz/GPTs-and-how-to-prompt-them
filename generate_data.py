import numpy as np
import pandas as pd

num_runs = 20
num_examples = 12
num_numbers = 10

data = []
for r in range(num_runs):
    for e in range(num_examples):
        digits = np.random.choice(np.arange(2, 10), size=num_numbers)
        row = [r, e, digits[0], digits[1], digits[2], digits[3], digits[4], digits[5], digits[6], digits[7], digits[8], digits[9], digits.sum()]
        data.append(row)

df = pd.DataFrame(data, columns=['run', 'example', 'digit_0', 'digit_1', 'digit_2', 'digit_3', 'digit_4', 'digit_5', 'digit_6', 'digit_7', 'digit_8', 'digit_9', 'result'])
print(df)
df.to_csv('data/problems.csv')
