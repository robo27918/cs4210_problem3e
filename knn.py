#-------------------------------------------------------------------------
# AUTHOR: Roberto S Toribio
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []
label = { "+":1, 
           
         "-":2
        }

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

error_count =0
#loop your data to allow each instance to be your test set
for i, instance in enumerate(db):

    #add the training features to the 2D array X and remove the instance that will be used for testing in this iteration.
    #For instance, X = [[1, 3], [2, 1,], ...]]. Convert values to float to avoid warning messages
    #test_set = [db[i][0], db[i][1]]
    test_set = [instance[0],instance[1]]
    X = [[float(train_inst[0]), float(train_inst[1])] for train_inst in db if train_inst[0:2] != test_set]
    
    #transform the original training classes to numbers and add them to the vector Y. Do not forget to remove the instance that will be used for testing in this iteration.
    #For instance, Y = [1, 2, ,...]. Convert values to float to avoid warning messages
    Y = [label[train_inst[2]]for train_inst in db if train_inst[0:2] != test_set]
    print ("Printing the class labels", Y)
    #--> add your Python code here
    # X =
    # Y =
    #testSample =
    test_set =[float(test_set[0]), float(test_set[1])] #convert to floats since comparison has already been completed
    print("training instances are:", X)
    print ("test set is:", test_set)
    print ()
    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    #--> add your Python code here
    class_predicted = clf.predict([test_set])[0]
    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here
    true_label = label[db[i][2]]
    
   
    if true_label != class_predicted:
        error_count +=1
#print the error rate
#--> add your Python code here
print("Error rate:",error_count / len(db))





