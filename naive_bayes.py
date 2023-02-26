#-------------------------------------------------------------------------
# AUTHOR: Austin Celestino
# FILENAME: naive_bayes.py
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

#reading the training data in a csv file
#--> add your Python code here
labels = []
db = []
X = []
Y = []
errors = 0
total = 0

#reading the data in a csv file
with open('weather_training.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      holder = []
      if i > 0: #skipping the header
         if row[1] == "Sunny":
             holder.append(1)
         elif row[1] == "Overcast":
             holder.append(2)
         else:
             holder.append(3)
         if row[2] == "Hot":
             holder.append(1)
         elif row[2] == "Mild":
             holder.append(2)
         else:
             holder.append(3)
         if row[3] == "High":
             holder.append(1)
         else:
             holder.append(2)
         if row[4] == "Strong":
             holder.append(1)
         else:
             holder.append(2)
         if row[5] == "Yes":
             Y.append(1)
         else:
             Y.append(2)
         X.append(holder)

#transform the original training features to numbers and add them to the 4D array X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
# X =

#transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
# Y =

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the test data in a csv file
#--> add your Python code here
xTest = []
yTest = []
with open('weather_test.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      holder = []
      if i == 0:
          header = row
      if i > 0: #skipping the header
         db.append(row)
         labels.append(row[0])
         if row[1] == "Sunny":
             holder.append(1)
         elif row[1] == "Overcast":
             holder.append(2)
         else:
             holder.append(3)
         if row[2] == "Hot":
             holder.append(1)
         elif row[2] == "Mild":
             holder.append(2)
         else:
             holder.append(3)
         if row[3] == "High":
             holder.append(1)
         else:
             holder.append(2)
         if row[4] == "Strong":
             holder.append(1)
         else:
             holder.append(2)
         if row[5] == "Yes":
             yTest.append(1)
         else:
             yTest.append(2)
         xTest.append(holder)

#printing the header os the solution
#--> add your Python code here
for i in range(len(header)):
    print(header[i], end=" ")
print("")
#use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
#--> add your Python code here
for i in range(len(xTest)):
    prediction = clf.predict([xTest[i]])[0]
    probability = clf.predict_proba([xTest[i]])[0].max()
    if probability >= 0.75:
        for j in range(5):
            print(db[i][j], end=" ")
        if prediction == 1:
            print("Yes")
        else:
            print("No")
#print(clf.predict_proba([xTest[0]])[0].max())


