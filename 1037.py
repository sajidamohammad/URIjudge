number=float(input())

if number>=0 and number<=25.00:
		print "Intervalo [0,25]"
elif number>25.00 and number<=50.00:
		print "Intervalo (25,50]"
elif number>50.00 and number<=75.00:	
		print "Intervalo (50,75]"
elif number>75.00 and number<=100.00:
		print "Intervalo (75,100]"
else:
	print "Fora de intervalo"
