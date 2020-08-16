#Law of Large Numbers
import matplotlib.pyplot as plt
import pandas as pd
import random

numberOfRolls = 1000

numerator = 0;
denominator = 0;

proportion = []
rolls = []

for x in range(0,numberOfRolls):
    rolls.append(x + 1)
    roll = random.randint(1,6)

    if roll % 2 == 0:
        numerator = numerator + 1
        denominator = denominator + 1
    else:
        denominator = denominator + 1

    proportion.append(float(numerator / denominator))

dataframe = pd.DataFrame({
    'proportion': proportion,
    'rolls': rolls
})

dataframe.plot(kind='line', x='rolls', y='proportion')

plt.title('Proportion of Even rolls over # of rolls')
plt.show()


