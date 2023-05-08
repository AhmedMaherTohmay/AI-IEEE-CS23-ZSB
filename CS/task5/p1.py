import os
import pandas as pd
# data=pd.read_csv('task5/ex.csv')
data = pd.read_csv('AI-IEEE-CS23-ZSB/ex.csv')
# Proportion  😎
#       Proportion of students that are female
#       🙂 not efficient
#       females=data[data['gender']=='female']
#       print('Proportion_of_female_is = ',round(len(females)/len(data),3))
prop_m=data.gender.value_counts()['male']/data.shape[0]
prop_f=data.gender.value_counts()['female']/data.shape[0]

print('Proportion_of_male_is = ',round(prop_m,3))
print('Proportion_of_female_is = ',round(prop_f,3))


# Admission rate 😎
rate_m=data[data['gender']=='male'].admitted.value_counts()[True]/data.gender.value_counts()['male']
rate_f=data[data['gender']=='female'].admitted.value_counts()[True]/data.gender.value_counts()['female']


print(rate_m)
print(rate_f)