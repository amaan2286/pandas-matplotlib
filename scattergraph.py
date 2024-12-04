import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {'X': np.arange(1, 11),
        'Y1': np.random.rand(10) * 10,  # Random values for line graph
        'Y2': np.random.randint(5, 15, 10)}  # Random values for bar graph

df = pd.DataFrame(data)
# Scatter Plot
plt.figure(figsize=(8, 5))
plt.scatter(df['X'], df['Y1'], color='green', label='Scatter Plot')
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()