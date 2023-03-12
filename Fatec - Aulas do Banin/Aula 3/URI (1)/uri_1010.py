READONE=input()
READTWO=input()

prodcodeone=int(READONE[0:2])
unitsone=int(READONE[3])
valueone=round(float(READONE[5:9]),2)

prodcodetwo=int(READTWO[0:2])
unitstwo=int(READTWO[3])
valuetwo=round(float(READTWO[5:9]),2)

TOPAY= ((unitsone)*(valueone))+((unitstwo)*(valuetwo))
print("VALOR A PAGAR: R$ {:.2f}".format((TOPAY)))
