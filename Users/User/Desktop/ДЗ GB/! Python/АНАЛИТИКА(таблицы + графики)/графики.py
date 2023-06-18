from numpy import array 
from numpy import argmax 
from sklearn.preprocessing import LabelEncoder 
from sklearn.preprocessing import OneHotEncoder 
import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame(lst)
data.head()
values = array(lst) 
#print(values)               
encoder = LabelEncoder()                                     # первое применение целочисленного кодирования
integer_encoded = encoder.fit_transform(values) 
#print(integer_encoded)
onehot = OneHotEncoder(sparse=False)                         # место выполнения двоичного кодирования
integer_encoded = integer_encoded.reshape(len(integer_encoded), 1) 
onehot_encoded = onehot.fit_transform(integer_encoded) 
print(*values)
print(*integer_encoded)
print(*onehot_encoded) 


