# data type 
# 1. Int 
age = 19
print(type(age))
# 2. float 
heigh = 111.5
print(type(heigh))
# 3. bool
komo = True
moko = False 
print(type(moko))
print(type(komo))
# 4. str 
hello = " kitty "
print(type(hello))

# ======[ Type conversion]======
abc = 100
print("======[  type conversion]======")
print(int(abc)+100)
a="120"
b="180"
print(int(a)+int(b))
# floast
float()
teddy = 10 #int
print("teddy : ", float(teddy))
# str

def foo():
    print( "No" )

    if True:
        print("yeah")
    else : 
        print("Uhmm")    
print("Done")        

print(10+15) # 25
# print("Hello"+5)
print("Hello + Kitty :","Hello + Kitty")

# ======[-]======
print(500-254)
# ======[*]======
print(22/7*50)
# ======[/]======
print(22/7)
# ======[%]======
print(22/7%3)
# ======[**]======
print(22/7**50)

'''
def f0(x):
    if x == 4: 
        print("not obb number")  
    else:
        print("obb number")

print(f0(2))

'''

def f1(x):
    if x%2 == 0:
        print("not odd number")
    else:
        print("odd number")

print(f1(10))



def f2(x):
    if  x==0:
        print("F")
    elif x==1.0:
        print("D")
    elif x==1.5:
        print("D+")
    elif x==2.0:
        print("C")
    elif x==2.5:
        print("C+")
    elif x==3:
        print("B")
    elif x==3.5:
        print("B+")
    elif x==4:
        print("A")
print(f2(4))        



def f3(x):
    if 5<=x<=50:
        print("10")
    elif 51<=x<=100:
        print("15")    


