A,B,C=map(float,raw_input().split(" "))
pi=3.14159
print "TRIANGULO: %.3f"%round(0.5*A*C,3)
print "CIRCULO: %.3f"%round(pi*C*C,3)
print "TRAPEZIO: %.3f"%round(((A+B)/2)*C,3)
print "QUADRADO: %.3f"%round(B*B,3)
print "RETANGULO: %.3f"%round(A*B,3)
