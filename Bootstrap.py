# -*- coding: utf-8 -*-
"""
@author: Emily_Meadows
"""
#%%
from random import randint
true_num = randint(1,1000)
count = 0


for i in range(20):
    try :
        guess = int(input("Guess an integer between 1 and 1000: "))
   
    #this is what you're trying to catch
    except ValueError:
        guess = int(input("No! I said an integer. Try again: "))
   

   
    count = count + 1
   
    if guess - true_num > 0:
        print("Your guess was too high")
    elif guess - true_num < 0 :
        print("Your guess was too low")
    elif guess - true_num == 0 :
        print(f"You are correct! It took {count} tries to guess correct")
        break


#%%
import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *

#dataframe is a class, inside it is methods/functions
dat = pd.DataFrame({"handspan": [20, 20, 19, 24.2, 20, 20.2, 21.5, 17, 19.5, 
                           21.5, 18, 18,20.5, 20, 20.3, 21.5, 19, 20.4, 
                           22.7, 22.9, 17, 23, 23.8, 22, 21.5, 21.5]})

boot_means = []

for i in range(10_000):
    #data frame (class) with one sample
    boot_sample = dat.sample(26, replace = True)

    boot_means.append(float(boot_sample.mean()))

#histogram of means
plt.hist(boot_means)

#turn list into dataframe
dfboot = pd.DataFrame({'x': boot_means})

#make a histogram
(
ggplot(dfboot, aes(x = 'x')) +
geom_histogram()
)

plt.xlabel('Handspan')
plt.ylabel('Count')
plt.title('Count of Handspan Bootstrap?')
plt.show()

#%% 
import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *
import os

#change all \ to \\ 
os.chdir("C:\\Users\\meado\\Downloads")
dat = pd.read_csv('2017_Fuel_Economy_Data.csv')

dat = dat["Combined Mileage (mpg)"]
n = len(dat)
n_boot = 10_000
stat = "mean"

boot_stat = []

for i in range(n_boot):
    #data frame (class) with one sample
    boot_sample = dat.sample(n, replace = True)
    
    if stat == 'median':
        boot_stat.append(float(boot_sample.median()))
    elif stat == 'mean':
        boot_stat.append(float(boot_sample.mean())) 
    elif stat == 'std dev':
        boot_stat.append(float(boot_sample.std()))
    else:
        raise TypeError("Wrong statistic name") #throw an exception

#turn list into dataframe
dfboot = pd.DataFrame({'x': boot_stat})

#make a histogram
(
ggplot(dfboot, aes(x = 'x')) +
geom_histogram()
)
#%%

class Boot_CI():
    def __init__(self):
        "Initialize the simulation"
        self.stat = "mean"
        self.dat = None
        self.n_boot = 0
        self.boot_stat = None
        self.ci_level = 0.95
        
test = Boot_CI()




















