# Will Mon 
#Vector main

import Vector2
import Vector3 

from Vector2 import *
from Vector3 import *


def main():

	V2Tester1 = Vector2(3,5)
	V2Tester2 = Vector2(2,1)
	V2Tester3 = Vector2()
	V2Tester4 = 0
	
	
	V3Tester1 = Vector3(30,10,20)
	V3Tester2 = Vector3(10, 20, 30)
	V3Tester3 = Vector3()
	V3Tester4 = 0
 	
	# Vecto3 testing 
	V2Tester3 = V2Tester1.add(V2Tester2)
	V2Tester3 = V2Tester1.sub(V2Tester2)
	V2Tester3 = V2Tester1.LinerIntro(V2Tester2)
	
	V2Tester3 = V2Tester1.Normalizer()
	V2Tester3 = V2Tester1.Radions()
	V2Tester3 = V2Tester1.Degrees()
	
	V2Tester4 = V2Tester1.Magnitude()
	V2Tester4 = V2Tester1.DotPro(V2Tester2)
	
	
	V3Tester3 = V3Tester1.add(V3Tester2)
	V3Tester3 = V3Tester1.sub(V3Tester2)
	V3Tester3 = V3Tester1.LinerIntro(V3Tester2)
	
	V3Tester4 = V3Tester1.Magnitude()
	V3Tester4 = V3Tester1.DotPro(V3Tester2)
	
	V3Tester3 = V3Tester1.Normalizer()
	
	#Vector2 Output
	print("'Vector2 Testing'")
	print("(",V2Tester3.x,",",V2Tester3.y, ")")
	print(V2Tester4)
	
	print()
	
	#Vecto3 Output 
	print("'Vecto3 Teseting'")
	print("(",V3Tester3.x,",",V3Tester3.y, ",",V3Tester3.z,")")
	print(V3Tester4)
	
main()