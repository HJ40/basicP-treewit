def f3(x):
    if 5<=x<=50:
        print("10")
    elif 51<=x<=100:
        print("15")    
    elif 101<=x<=300:
        print("25")  
    elif 301<=x<=500:
        print("35")  
    elif x>=500:
        print("45")  
print(f3(35))