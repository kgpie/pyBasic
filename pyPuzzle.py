import sys

thismodule = sys.modules[__name__]

def line_break():
	print("-"*75)
    
x = 1# used in puzzle 6
    
def outputFunc(funcName):

    
    print(funcName.__name__)
    print(funcName.__doc__)
    print("\nOUTPUT:\n", end="    ")
    funcName()
    print("\n")
    
    
def puzzle0():
    '''
    --------------------------
    dict1 = {"a":"b", "c":"d"}
    dict2 = {"c":"d", "a":"b"}
    
    return dict1==dict2
    --------------------------'''
    dict1 = {"a":"b", "c":"d"}
    dict2 = {"c":"d", "a":"b"}
    
    print(dict1==dict2)    
    
    
def puzzle1():

    '''
    --------------------------
    puzzle2:
    z=set('abc')
    z.add('san')
    z.update(set(['p','q']))
    --------------------------'''
    
    z=set('abc')
    z.add('san')
    z.update(set(['p','q']))
    
    
    print(z)
    
    
def puzzle2():

    '''
    --------------------------
    puzzle3:
    set1={1,2,3,int('4')}
    set2={3,str(4)}
    
    return set1.union(set2)
    --------------------------'''
    
    set1={1,2,3,int('4')}
    set2={3,str(4)}
    
    
    print(set1.union(set2))
    

def puzzle3():

    '''
    --------------------------
    puzzle4:
    l=[1,2,3,4]
    
    for i in l[::1]:
        print(i, end=" ")
    
    return ""
    --------------------------'''
    
    l=[1,2,3,4]
    
    for i in l[::1]:
        print(i, end=" ")
        
        
def puzzle4():
    
    '''
    print( [i for i in range(0,3,3)])
    '''
    print( [i for i in range(0,3,3)])
    
    
def puzzle5():
    
    '''
    a = 35
    print("%f"%a)
    '''
    a = 35
    print("%f"%a)
    
    
def puzzle5():
    
    '''
    e = "butter"
    def f(a): print(a)+e
    f("bitter")
    '''
    e = "butter"
    def f(a): print(a+e)
    f("bitter")
    
    
def puzzle6():
       
    '''
    x = 1
    
    def cg():
        global x
        print(x+1)
    cg()
    '''
    
    
    def cg():
        global x
        print(x+1)
    cg()
    

def puzzle7():
       
    '''
    a=[1,2,3]
    b=a
    print(a is b, a==b)
    '''
    
    a=[1,2,3]
    b=a
    print(a is b, a==b)
    
    
def puzzle8():
       
    '''
    a=1/3
    b=3/1
    print(a*b)
    '''
    
    a=1/3
    b=3/1
    print(a*b)
    
    
def puzzle9():
       
    '''
    a=True
    b=False
    print(a or b and b and a)
    '''
    
    a=True
    b=False
    print(a or a and b and a)
        
    
def puzzle10():
       
    '''
    a=~4
    b=a+4
    print(b)
    '''
    
    a=~4
    b=a+4
    print(b)
    
    
def puzzle11():
       
    '''
    a=100
    b=5
    print(a//b*a/b)
    '''
    
    a=100
    b=5
    print(a//b*a/b)
    
    
def puzzle12():
       
    '''
    myList = ["python", "hub"]
    
    for i in myList:
        myList.append(i.upper)
        
    print(myList)
    '''
    
    myList = ["python", "hub"]
    
    for i in myList:
        #myList.append(i.upper())
        print(myList)
        
    print("INFITNITE LOOP)
    
    
def puzzle13():
    
    '''
    x = [[0],[1]]
    print((''.join(list(map(str,x))),))
    '''
    
    x = [[0],[1]]
    print((''.join(list(map(str,x))),))


if __name__=='__main__':

    line_break()
    line_break()
    
    n=0
    
    
    for key, value in dict(locals()).items():
        if "function" in str(value) and "puzzle" in str(value):
            n=n+1

    
    for i in range(n):
        func = getattr(thismodule, "puzzle{}".format(i))
        outputFunc(func) 
        line_break()
        #input()#'''
    
