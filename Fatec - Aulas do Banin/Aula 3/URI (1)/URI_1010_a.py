READONE=input()
READTWO=input()

ARRAY_READONE=READONE.split(" ")
CODE_PROD_ONE=int(ARRAY_READONE[0])
QTD_PROD_ONE=int(ARRAY_READONE[1])
UNIT_VALUE_PROD_ONE=round(float(ARRAY_READONE[2]), 2)
FULL_COST_PROD_ONE = QTD_PROD_ONE * UNIT_VALUE_PROD_ONE

ARRAY_READTWO=READTWO.split(" ")
CODE_PROD_TWO=int(ARRAY_READTWO[0])
QTD_PROD_TWO=int(ARRAY_READTWO[1])
UNIT_VALUE_PROD_TWO=round(float(ARRAY_READTWO[2]), 2)
FULL_COST_PROD_TWO = QTD_PROD_TWO * UNIT_VALUE_PROD_TWO

VALUE_TO_PAY = FULL_COST_PROD_ONE + FULL_COST_PROD_TWO

print("VALOR A PAGAR: R$ {:.2f}".format(VALUE_TO_PAY))