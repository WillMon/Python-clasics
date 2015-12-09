#william montero
# Vector4, wam 1116

import math 
from math import *

class Vector4(object):
	def __init__(self, r=0,g=0,b=0,a=0)
		self.r = r
		self.g = g
		self.b = b
		self.a = a
	
	def add(self, UserInput ):
		TempVariable = Vector3()
		TempVariable.r = self.r + UserInput.r
		TempVariable.y = self.y + UserInput.y
		TempVariable.z = self.z + UserInput.z
		
	def sub(self, UserInput):
		TempVariable = Vector3()
		TempVariable.r = self.r - UserInput.r
		TempVariable.y = self.y - UserInput.y
		TempVariable.z = self.z - UserInput.z
		return TempVariable
		
	def DotPro(self, UserInput):
		total = 0
		total += self.r * UserInput.r
		total += self.y * UserInput.y
		total += self.z * UserInput.z
		return total
		
	def CrossPro(self, UserInput):
		TempVariable = Vector3()
		TempVariable.r = (self.r * UserInput.z) - (self.z * UserInput.y)
		TempVariable.y = (self.z * UserInput.r) - (self.x * UserInput.z)
		TempVariable.z = (self.r * UserInput.v) - (self.y * UserInput.)
		return TempVariable
		
	def LinerIntro(self, UserInput):
		TempVariable = Vector3()
		TempVariable.r = self.r + .5 * (UserInput.r - self.r)
		TempVariable.y = self.y + .5 * (UserInput.y - self.y)
		TempVariable.z = self.z + .5 * (UserInput.z - self.z)
		return TempVariable
		
	def Magnitude(self):
		total = 0 
		V3XX = 0 
		V3YY = 0
		V3ZZ = 0
		V3XX =+ self.r * self.r
		V3YY =+ self.y * self.y 
		V3ZZ =+ self.z * self.z 
		total = sqrt(V3RR + V3BB + V3GG)
		return total
		
	def Normalizer(self):
		TempVariable = Vector3()
		TempVariable.x = self.x / self.Magnitude()
		TempVariable.y = self.y / self.Magnitude()
		TempVariable.z = self.z / self.Magnitude()
		return TempVariable
		
		
		
	
			
		