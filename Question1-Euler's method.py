#Euler's Method 
import math
import library

#Function 1 
def f_1(x,y):
    return (y*math.log(y))/x 
    
#Function 2 
def f_2(x,y):
    return 6-((2*y)/x)
    

#Analytical solution for first differential equation
def fxn1(x,y):
    arr1=[]
    arr2=[]
    h=0.2
    i=0 
    while i<=10:
        arr1.append(x)
        arr2.append(y)
        y=math.exp(0.5*x)
        x=x+h
        i=i+1 
    return arr1,arr2 


#Analytical solution for second differential equation 
def fxn2(x,y):
    arr1=[]
    arr2=[]
    h=0.2 
    i=0  
    while i<=10:
        arr1.append(x)
        arr2.append(y)
        y=2*x - (45/(x**2))
        x=x+h
        i=i+1 
    return arr1,arr2 

    
    
#main function 
arr1,arr2=library.Euler(f_1,0.2,2,2.71828)  #Call function 1 and compute the data points
print("Tabular representation of x vs y for function 1 through Euler's method")
for n, v in zip(arr1, arr2):        #Table for function 1
        print("{} |---> {}".format(n, v))
print(" ")
        
arr11,arr12=fxn1(2,2.71828)         #Compute the analytical solution
print("Tabular representation of x vs y for function 1 through analytical method")
for n, v in zip(arr11, arr12):      #table for analytical solution        
        print("{} |---> {}".format(n, v))

print(" ")       
arr3,arr4=library.Euler(f_2,0.2,3,1)        #Call function 2 and compute the data points
print("Tabular representation of x vs y for function 2 through Euler's method")
for n, v in zip(arr3, arr4):        #table for function 2 
        print("{} |---> {}".format(n, v))

print(" ")        
arr21,arr22=fxn2(3,1)               #Compute the analytical solution
print("Tabular representation of x vs y for function 1 through Analytical method")
for n, v in zip(arr21, arr22):      #table for analytical solution       
        print("{} |---> {}".format(n, v))
        
        
'''
Tabular representation of x vs y for function 1 through Euler's method
2 |---> 2.71828
2.2 |---> 2.990107817154157
2.4000000000000004 |---> 3.2878435750351978
2.6000000000000005 |---> 3.6139516008972397
2.8000000000000007 |---> 3.9711217179604184
3.000000000000001 |---> 4.362290993607738
3.200000000000001 |---> 4.79066720624618
3.4000000000000012 |---> 5.259754276390103
3.6000000000000014 |---> 5.773379896945629
3.8000000000000016 |---> 6.335725599294895
4.000000000000002 |---> 6.951359501008974
 
Tabular representation of x vs y for function 1 through analytical method
2 |---> 2.71828
2.2 |---> 2.718281828459045
2.4000000000000004 |---> 3.0041660239464334
2.6000000000000005 |---> 3.320116922736548
2.8000000000000007 |---> 3.6692966676192453
3.000000000000001 |---> 4.055199966844676
3.200000000000001 |---> 4.481689070338067
3.4000000000000012 |---> 4.953032424395118
3.6000000000000014 |---> 5.4739473917272035
3.8000000000000016 |---> 6.04964746441295
4.000000000000002 |---> 6.685894442279275
 
Tabular representation of x vs y for function 2 through Euler's method
3 |---> 1
3.2 |---> 2.0666666666666664
3.4000000000000004 |---> 3.0083333333333333
3.6000000000000005 |---> 3.8544117647058824
3.8000000000000007 |---> 4.626143790849674
4.000000000000001 |---> 5.339181286549708
4.200000000000001 |---> 6.0052631578947375
4.400000000000001 |---> 6.633333333333335
4.600000000000001 |---> 7.230303030303031
4.800000000000002 |---> 7.801581027667986
5.000000000000002 |---> 8.35144927536232
 
Tabular representation of x vs y for function 1 through Analytical method
3 |---> 1
3.2 |---> 1.0
3.4000000000000004 |---> 2.0054687500000012
3.6000000000000005 |---> 2.907266435986161
3.8000000000000007 |---> 3.72777777777778
4.000000000000001 |---> 4.483656509695294
4.200000000000001 |---> 5.1875000000000036
4.400000000000001 |---> 5.848979591836738
4.600000000000001 |---> 6.475619834710748
4.800000000000002 |---> 7.073345935727792
5.000000000000002 |---> 7.646875000000005




'''
