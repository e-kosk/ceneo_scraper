import os
import pandas as pd


base_path = './opinions'
print(*os.listdir(base_path))

product_id = input('Product ID: ') or '85910996'

opinions = pd.read_json(os.path.join(base_path, product_id + '.json'))
opinions = opinions.set_index('opinion_id')

average_score = opinions.stars.mean().round(2)
pros = opinions.pros.count()
cons = opinions.cons.count()

print(average_score)
print(pros, cons)
