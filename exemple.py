import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#matplotlib.use('TkAgg')
import os

#un_panda = [100, 5, 20, 80]
#un_panda_numpy = np.array(un_panda)
#print(un_panda_numpy)
#print(un_panda_numpy/21)

#famille_panda = [
#    [100, 5, 20, 80], # maman panda
#    [50, 2.5, 10, 40], # bebe panda
#    [110, 6, 22, 80], # papa panda
#]

#famille_panda_numpy = np.array(famille_panda)
#print(famille_panda)
#print(famille_panda_numpy[2, 0])

#famille_panda_df = pd.DataFrame(famille_panda_numpy, index = ['maman', 'bebe', 'papa'], columns = ['pattes', 'poil', 'queue', 'ventre'])
#print(famille_panda_df)

#mps = pd.read_csv("data/current_mps.csv", sep=";")
#print(mps.iloc[0])

""" fig, ax = plt.subplots()
ax.axis("equal") # permet que les axes soient de mêmes dimension donc que le camembert soit toujours rond!
ax.pie([24, 18], labels = ["Femmes", "Hommes"], autopct = "%1.1f pourcents")
plt.title("Pourcentage des hommes et des femmes qui font la vaisselle")
plt.show()
 """
ages = [25, 65, 26, 26, 46, 37, 36, 36, 28, 28, 57, 37, 48, 48, 37, 28, 60,
       25, 65, 46, 26, 46, 37, 36, 37, 29, 58, 47, 47, 48, 48, 47, 48, 60]

fig, ax = plt.subplots()
ax.hist(ages)
plt.show()