import pandas as pd
import numpy as np

#Read data from file
df = pd.read_csv('agaricus-lepiota.data')
#Select all rows and columns, but exclude column 0.
dataset = df.iloc[:,0:]

#Use the one hot binary code
dataset = pd.get_dummies(dataset).astype(float)
print(dataset)

#Split dataset to train, validate and test = 60:20:20
train, validate, test = np.split(dataset.sample(frac=1, random_state=42), [int(.6*len(dataset)), int(.8*len(dataset))])

#Check split dataset shape
print(train.shape)
print(validate.shape)
print(test.shape)

#Convert dataset into int type
train = train.astype(int)
validate = validate.astype(int)
test = test.astype(int)

#Save dataset into 3 separated files
train.to_csv('training.txt', index=False, header=None)
validate.to_csv('val.txt', index=False, header=None)
test.to_csv('testing.txt', index=False, header=None)

print('Done')