import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Loading a data
data = pd.read_csv('births.csv')
data['day'].fillna(0,inplace=True)
data['day'].astype(int)
data['decade'] = 10*(data['year'] // 10)
birth_decade = data.pivot_table('births',index='decade',columns='gender',aggfunc='sum')
birth_decade.plot()
plt.ylabel("Total birth per year")
plt.show()


# Removing Outlierr and  Missing Values
quartiles = np.percentile(data['births'],[25,50,75])
mu = quartiles[1]
sig = 0.74 * (quartiles[2] - quartiles[0])

data = data.query('(births > @mu - 5 * @sig) & (births < @mu + 5 * @sig)')
data['day'] = data['day'].astype(int)
data.index = pd.to_datetime(1000*data.year + 100*data.month + data.day,format='%Y%m%d')

data['dayofWeek'] = data.index.dayofWeek

data.pivot_table('births',index='dayofWeek',columns='decade',aggfunc='mean').plot()
plt.gca().set_xticklabels(['MON','TUES','WED','THURS','FRI','SAT','SUN'])
plt.ylabel("Mean Birth by day")
plt.show()

