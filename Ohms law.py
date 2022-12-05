def isfloat(num):
		try:
				float(num)
				return True
		except ValueError:
				return False

wrong = 'Invalid Input. Let´s start over..'

while True:
	print("Choose the first parameter that we know about")
	print("1 = Volt")
	print("2 = Ampere")
	print("3 = Ohm")
	choice1 = input("Enter a choice (1, 2 or 3): ")
	
	if choice1 == ('1'):
		volt = input("How many Volts do we have? ")
		if isfloat(volt):
			print("Great! Choose the second parameter that we know about")
			print("2 = Ampere")
			print("3 = Ohm")
			choice2 = input("Enter a choice (2 or 3): ")
			
			if choice2 == ('2'):
				ampere = input("How many Amperes do we have? ")
				if isfloat(ampere):
					ohm = float(volt) / float(ampere)
					break
					
				else: 
					print(wrong)
				
			elif choice2 == ('3'):
				ohm = input("How many Ohms do we have? ")
				if isfloat(ohm):
					ampere = float(volt) / float(ohm)
					break
					
				else: 
					print(wrong)
			
			else: 
				print(wrong)
			
		else: 
			print(wrong)
		
	elif choice1 == ('2'):
		ampere = input("How many Amperes do we have? ")
		if isfloat(ampere):
			print("Great! Choose the second parameter that we know about")
			print("1 = Volt")
			print("3 = Ohm")
			choice2 = input("Enter a choice (1 or 3): ")
			
			if choice2 == ('1'):
				volt = input("How many Volts do we have? ")
				if isfloat(volt):
					ohm = float(volt) / float(ampere)
					break
					
				else: 
					print(wrong)
				
			elif choice2 == ('3'):
				ohm = input("How many Ohms do we have? ")
				if isfloat(ohm):
					volt = float(ampere) * float(ohm)
					break
					
				else: 
					print(wrong)
			
			else: 
				print(wrong)
			
		else: 
			print(wrong)
		
	elif choice1 == ('3'):
		ohm = input("How many Ohms do we have? ")
		if isfloat(ohm):
			print("Great! Choose the second parameter that we know about")
			print("1 = Volt")
			print("2 = Ampere")
			choice2 = input("Enter a choice (1 or 2): ")
			
			if choice2 == ('1'):
				volt = input("How many Volts do we have? ")
				if isfloat(volt):
					ampere = float(volt) / float(ohm)
					break
					
				else: 
					print(wrong)
				
			elif choice2 == ('2'):
				ampere = input("How many Amperes do we have? ")
				if isfloat(ampere):
					volt = float(ampere) * float(ohm)
					break
					
				else: 
					print(wrong)
			
			else: 
				print(wrong)
			
		else: 
			print(wrong)
			
	else:
		print(wrong)

watt = float(ampere) * float(ampere) * float(ohm)

print("V =", volt, "Volt")	
print("I =", ampere, "Ampere")
print("R =", ohm, "Ohm")
print("P =", watt, "Watt") 



