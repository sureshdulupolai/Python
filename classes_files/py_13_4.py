# ---------------------------
import arith
# all file will import
# if you will use all file import method
# then you need to write ( filename.functionName() )

var = arith.powerx(5, 2)
print(var)



# ------------------------------------------
from arith import quo, powerx
# best method : for resource utilization
# if you will use this method
# then you don't need to write the ( fileName )
# directily you can call a function

var = quo(7, 2)
print(var)


# --------------------------------------------
from arith import *
# ( * ) <- is also know as "ALL"
# this process is not good, file become havy
# beacuse this import all the function from the file 
# it doesn't metter you are using that function or not

var = powerx(6, 2)
print(var)


# ------------------------------------------------
from math import cos as suresh
# ( cos ) functionName change to ( suresh )
# ( cos ) -> cos0

var = suresh(5)
print(var)