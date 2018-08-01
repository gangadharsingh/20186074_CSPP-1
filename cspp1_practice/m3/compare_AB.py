'''
@author : gangadharsingh
This program is about comparing variables
'''
VARA = 25
VARB = 10
if type(VARA) == str and type(VARB) == str:
    print("string involved")
elif VARA > VARB:
    print("bigger")
elif VARA == VARB:
    print("equal")
else:
    print("smaller")
