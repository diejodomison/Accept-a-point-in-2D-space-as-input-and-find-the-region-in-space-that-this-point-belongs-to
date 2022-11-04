x=float(input())
y=float(input())
if x>0 and y>0:
    print("first quadrant")
elif x>0 and y<0:
    print("fourth quadrant")
elif x<0 and y>0:
    print("second quadrant")
elif x<0 and y<0:
    print("third quadrant")
elif x==0 and y!=0:
    print("x-axis")
elif x!=0 and y==0:
    print("y-axis")
else:
    print("origin")