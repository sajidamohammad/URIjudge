x1,y1=map(float, raw_input().split(" "))
x2,y2=map(float, raw_input().split(" "))
print "%.4f"%round((abs(x2-x1)**2+abs(y2-y1)**2)**0.5,4)
