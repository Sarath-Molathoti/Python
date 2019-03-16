%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize']=(20.0,10.0)

#reading data
data=pd.read_csv("headbrain.csv")
print (data.shape)
data.head()

#collecting x and y values
X=data['Head Size(cm^3)'].values
Y=data['Brain Weight(grams)'].values

#mean of X and Y
mean_x=np.mean(X)
mean_y=np.mean(Y)

#Total number of values
m = len(X)

#Using the formula to calculate m and c
numer=0
denom=0
for i in range(m):
    numer += (X[i] - mean_x) * (Y[i] - mean_y)
    denom += (X[i] - mean_x) ** 2
b1=numer/denom
b0=mean_y-(b1*mean_x)

#print coefficients
print(b1,b0)

#plotting values and regression line

max_x=np.max(X) + 100
min_x=np.min(X) - 100

#calculating line values x and y
x=np.linspace(min_x,max_x,1000)
y=b0+b1*x

#plotting line
plt.plot(x,y,color='red',label='Regression Line')
#plotting scatter points
plt.scatter(X,Y,c='blue',label='Scatter Plot')

plt.xlabel('Head Size in cm3')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()
