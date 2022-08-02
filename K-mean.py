from math import sqrt
import random
import numpy

def func(x,y,n,k,a):
    z = random.sample(range(0,9),k) #Choose k numbers of random values So< Z is an array

    #Manhattan
    if(a==1):        
        arr_Man = [0.0]*n*k
        l=0
        for i in range(n):
            for j in range(len(z)):
                c = z[j] #c is equal to the random values
                Man = abs(x[i] - x[c]) + abs(y[i] - y[c])
                arr_Man[l] = round(Man,1)
                l+=1

        s_man = numpy.array_split(arr_Man,n) #Spliting the array to n numbers of array each will have k numbers of values
        sum_x = [0.0]*k                      #So, s_man is an array of arrays
        sum_y = [0.0]*k
        count = [0]*k
        Avg_x = [0.0]*k
        Avg_y = [0.0]*k
        v = [0]*n
        for i in range(0,n):
            arr=s_man[i] #arr is equal to to the k size arrays
            s = numpy.min(arr) #Getting the smallest value in the array
            c = numpy.where(arr == s) #Getting its index
            m = c[0][0] 
            count[m] += 1 
            sum_x[m] += x[i] 
            sum_y[m] += y[i] 
            v[i] = m+1

        Avg_x = numpy.divide(sum_x,count)
        Avg_y = numpy.divide(sum_y,count)
        New_Centroids = [0]*k
        print('\nManhattan Distance:')
        M_Distance=[0]*k
        for i in range(k):
            m=i+1
            M_Distance[i] = m
        print('\nM Distance:%s'%M_Distance)
        for i in range(n):
            print('(%d,%d) ==> %s ==> Cluster %d'%(x[i],y[i],s_man[i],v[i]))
        print('\n')
        for i in range(k):
            m=i+1
            New_Centroids[i] = '(%f,%f)'%(Avg_x[i],Avg_y[i])
            print('New M%d = %s'%(m,New_Centroids[i]))
        print('\n')

    #Euclidian
    elif(a==2):
        arr_Ecu = [0.0]*n*k
        l=0
        for i in range(n):
            for j in range(len(z)):
                c = z[j]                        
                Ecu = sqrt(pow((x[i] - x[c]),2) + pow((y[i] - y[c]),2))
                arr_Ecu[l] = round(Ecu,1)
                l+=1
        s_Ecu = numpy.array_split(arr_Ecu,n)
        sum_x = [0.0]*k
        sum_y = [0.0]*k
        count = [0]*k
        Avg_x = [0.0]*k
        Avg_y = [0.0]*k
        v = [0]*n
        for i in range(0,n):
            arr=s_Ecu[i]
            s = numpy.min(arr)           
            c = numpy.where(arr == s)
            m = c[0][0]
            count[m] += 1 
            sum_x[m] += x[i]
            sum_y[m] += y[i]
            v[i] = m+1

        Avg_x = numpy.divide(sum_x,count)
        Avg_y = numpy.divide(sum_y,count)
        New_Centroids = [0]*k
        print('\nEuclidian Distance:')
        M_Distance=[0]*k
        for i in range(k):
            m=i+1
            M_Distance[i] = m
        print('\nM Distance:%s'%M_Distance)
        for i in range(n):
            print('(%d,%d) ==> %s ==> Cluster %d'%(x[i],y[i],s_Ecu[i],v[i]))
        print('\n')
        for i in range(k):
            m=i+1
            New_Centroids[i] = '(%f,%f)'%(Avg_x[i],Avg_y[i])
            print('New M%d = %s'%(m,New_Centroids[i]))
        print('\n')

    else:
        print('Choice Not Found!')
        return

x = [3,3,3,4,4,5,5,7,7,8]
y = [4,6,8,5,7,1,5,3,5,5]
n = len(x)
k = int(input('Enter No. of Clusters:\t'))
a = int(input('For Manhattan 1 | For Euclidian 2:\t'))
func(x,y,n,k,a)