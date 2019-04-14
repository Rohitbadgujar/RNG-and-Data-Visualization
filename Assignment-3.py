
# coding: utf-8

# In[15]:


import numpy as np
import math
import matplotlib.pyplot as plt

ind = False
while not ind:
    try:
        print('Enter 1. WeiBull Distribution,  2. Geometric Distribution,  3. Exponential Distribution:')
        case = int(input('Enter option 1/2/3: '))
        ind = True # we only get here if the previous line didn't throw an exception
    except ValueError:
        print('Invalid input!')
if(case == 1):
#WeiBull Distribution
    parsed = False
    aList = []
    weibullList = []

    #User input as Alpha and Beta and Validate the inputs
    while not parsed:
        try:
            alpha = float(input('Enter Alpha value: '))
            beta = float(input('Enter Beta value: '))
            parsed = True # we only get here if the previous line didn't throw an exception
        except ValueError:
            print('Invalid value for Alpha or Beta!')
    for x in range(0,100):
        aList.append(alpha*(math.pow(-math.log(1-np.random.uniform(0, 1)),beta)))
    aList.sort()
    #Write aList into file
    with open("weiBull_RandomSeq.txt", 'w') as file_handler:
        for item in aList:
            file_handler.write("{}\n".format(item))
            
    for x in range(0,100):
        weibullList.append(1-math.exp(-(math.pow(aList[x]/alpha,beta))))
    weibullList.sort()
     
    #Write CDF data into file
    with open("weiBull_CdfSeq.txt", 'w') as file_handler:
        for item in weibullList:
            file_handler.write("{}\n".format(item))
    fig = plt.figure()
    plt.plot(aList, weibullList,'blue')
    plt.yscale('linear')
    plt.ylabel('Probability')
    plt.xlabel('Random Variable')
    plt.title('Weibull Distribution')
    plt.grid(True)
    fig.savefig('weiBullPlot.pdf')
    
elif (case == 2):
#Geometric Distribution
    parsed = False
    while not parsed:
        try:
            q = float(input('Enter q value: '))
            parsed = True # we only get here if the previous line didn't throw an exception
        except ValueError:
            print('Invalid value for q!')
    
    
    aList = []
    geoList = []
    for x in range(0, 100):
        aList.append(math.log(1 - (np.random.uniform(0, 1)))/math.log(q))
    aList.sort()
    #Write aList into file 
     
    with open("geo_RandomSeq.txt", 'w') as file_handler:
        for item in aList:
            file_handler.write("{}\n".format(item))
            
    #Read aList from file
    for x in range(0, 100):
        geoList.append(1-math.pow(q,aList[x]))
        
    #Write geoList to file
      #Write aList into file
    with open("geo_CdfSeq.txt", 'w') as file_handler:
        for item in geoList:
            file_handler.write("{}\n".format(item))
    # plot with various axes scales
    
    fig = plt.figure()
    plt.plot(aList, geoList,'yellow')
    plt.yscale('linear')
    plt.ylabel('Probability')
    plt.xlabel('Random Variable')
    plt.title('Geometric Distribution')
    plt.grid(True)
    fig.savefig('geoPlot.pdf')
elif (case == 3):
#Exponential Distribution
    #Generate Random numbers using inverse formula;
    parsed = False
    while not parsed:
        try:
            lmd = float(input('Enter Value for Lambda:'))
            parsed = True # we only get here if the previous line didn't throw an exception
        except ValueError:
            print('Invalid value for lambda!')
    aList = []
    for x in range(0, 100):
        aList.append((-1/lmd)*math.log((np.random.uniform(0, 1))))
    aList.sort()   
    #Write aList into file 
         
    with open("exp_RandomSeq.txt", 'w') as file_handler:
        for item in aList:
            file_handler.write("{}\n".format(item))
    #Read aList from file 
    expList = []
    for x in range(0,100):
        expList.append(1-(1/math.exp(aList[x])))
    #Write expList to file
         
    with open("exp_CdfSeq.txt", 'w') as file_handler:
        for item in expList:
            file_handler.write("{}\n".format(item))
    #Read expList and plot the graph
    fig = plt.figure()
    plt.plot(aList, expList,'orange')
    plt.yscale('linear')
    plt.ylabel('Probability')
    plt.xlabel('Random Variable')
    plt.title('Exponential Distribution')
    plt.grid(True)
    fig.savefig('expPlot.pdf')
else:
    print('Invalid Input')

