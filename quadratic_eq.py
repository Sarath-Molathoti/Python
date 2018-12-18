a = int ( input ("Enter a value : "))
b = int ( input ("Enter b value : "))
c = int ( input ("Enter c value : "))
d = ( b * b ) - (4 * a * c)
import math
if ( d < 0 ):
   print "Roots are imaginary"
else:
   root1 = ( - b + math.sqrt(d) ) / ( 2 * a)
   root2 = ( - b - math.sqrt(d) ) / ( 2 * a)
   print ("Root1 = %d \nRoot2 = %d" % (root1, root2))

