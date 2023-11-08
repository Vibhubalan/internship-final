import pandas as pd 


data=pd.read_csv('main1.csv')

data1.head()

import warnings

warnings.filterwarnings('ignore')

data.head()

data['Company_type'].unique()

data.describe()

data.info()

data.isnull().sum()

data['Gender'].unique()

data['Gender']=data['Gender'].map({'Male':1,'Female':0})

data.head()

data['Qualification'].unique()

data['Qualification']=data['Qualification'].map({'Bachelor Degree':5,'Diploma':4,'PUC':3,'BCA':2,'PG':1,'Phd':0})

data.head()

data['Origin'].unique()

data['Origin']=data['Origin'].map({'Urban':3,'Remote':2,'Rural':1,'Semi urban':0})

data.head()

data['Experience'].unique()

data.['Company_type'].unique()

data['Company_type'].unique()

data['Company_type']=data['Company_type'].map({'Private limited company':6,'Corporative':5,'Partnership':4,'International company':3,'Not yet working':2,'Nonprofit Organization':1,'Private institution':0})

data.head()

data['Status'].unique()

data['Status']=data['Status'].map({'Employed':1,'Unemployed':0})

data.head()

x=data.drop('Status',axis=1)

y=data['Status']

x

y

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=42)

from sklearn.linear_model import LogisticRegression

lr=LogisticRegression()

lr.fit(x_train,y_train)

y_pred1=lr.predict(x_test)

y_pred1

from sklearn.metrics import accuracy_score

score1=accuracy_score(y_test,y_pred1)

print(score1)

data

new_data=pd.DataFrame({
    'Gender':1,
    'Qualification':4,
    'Passout':2017,
    'Origin':3,
    'Experience':1,
    'Company_type':6,
},index=[0])

p=lr.predict(new_data)
prob=lr.predict_proba(new_data)
if p==1:
    print('Employed')
else :
    print('Not Employed')

import matplotlib.pyplot as plt

import seaborn as sns

plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
sns.countplot(x='Experience',hue='Status',data=data1)
plt.subplot(1,2,2)
sns.countplot(x='Passout',hue='Status',data=data1)

data


plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
sns.countplot(x='Gender',hue='Status',data=data1)
plt.subplot(1,2,2)
sns.countplot(x='Origin',hue='Status',data=data1)

plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
sns.countplot(x='Qualification',hue='Status',data=data1)
plt.subplot(1,2,2)
sns.countplot(x='Company_type',hue='Status',data=data1)


