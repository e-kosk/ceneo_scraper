import os
import pandas as pd
import numpy as np

from matplotlib import pyplot as plt


base_path = './opinions'
print(*os.listdir(base_path))

product_id = input('Product ID: ') or '47044569'

opinions = pd.read_json(os.path.join(base_path, product_id + '.json'))
opinions = opinions.set_index('opinion_id')

average_score = opinions.stars.mean().round(2)
pros = opinions.pros.count()
cons = opinions.cons.count()

print(average_score)
print(pros, cons)



#histogram częstości występowania poszczególnych ocen (gwiazdek)
stars = opinions.stars.value_counts().sort_index().reindex(list(np.arange(0,5.5,0.5)), fill_value=0)
fig, ax = plt.subplots()
stars.plot.bar(color="#f5c3c2")
plt.title("*****Gwiazdki*****")
plt.xlabel("Liczba gwiazdek")
plt.ylabel("Liczba opinii")
plt.xticks(rotation=0)
# plt.show()
plt.savefig("figures_png/"+product_id+"_bar.png")
plt.close()

#udział poszczególnych rekomendacji w ogólnej liczbie opinii
recommendation = opinions.recommendation.value_counts()
fig, ax = plt.subplots()
recommendation.plot.pie(label="", autopct="%1.1f%%", colors=['#f5c3c2', '#89cff0'])
plt.title("<<<<Rekomendacja>>>>")
# plt.show()
plt.savefig("figures_png/"+product_id+"_pie.png")
plt.close()

opinions['purchased'] = opinions['purchase_date'].apply(lambda x: False if x==None else True)
stars_purchased = pd.crosstab(opinions['stars'], opinions['purchased'])
print(stars_purchased)
