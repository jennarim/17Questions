#-----------------------------------------------------------------------#
#			17 Questions Program by Ivanna Pena and Jenna Rim			#
#-----------------------------------------------------------------------#

print("Think of a number between 0 and 2^10 (1024).\nI will ask you at most 17 questions, but you can lie maximum once.\nAnswer using T or F");

choice = " "
lie = " "
bit0, bit1, bit2, bit3, bit4, bit5, bit6, bit7, bit8, bit9 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
Bits = [bit0, bit1, bit2, bit3, bit4, bit5, bit6, bit7, bit8, bit9]
q = 11 #question number
questionInQuestion = 1
bitInQuestion = 1

# Asks Questions 1 - 10
for i in range(1, 11):
	# Questions 1 - 10
	if i == 1:
		choice = input(str(i) + ". Is the 1st high order bit 0? ")
	elif i == 2:
		choice = input(str(i) + ". Is the 2nd high order bit 0? ")
	elif i == 3:
		choice = input(str(i) + ". Is the 3rd high order bit 0? ")
	else:
		choice = input(str(i) + ". Is the " + str(i) + "th high order bit 0? ")
	
	# If they say True, then the ith high order bit is 0
	if choice == "T":
		Bits[i-1] = 0
	# If they say False, then the ith higher order bit is 1
	elif choice == "F":
		Bits[i-1] = 1
	else:
		print("Invalid input. ")
		quit()
	print(Bits) # Displays the binary number after each question

# Asks Questions 11 - 17
while q < 18:

	# If they lied in questions 7, 8, 9 10:
	if questionInQuestion == 7:
		lie = input(str(q) + ". Did you lie in any of the questions " + str(questionInQuestion) + ", " + str(questionInQuestion + 1) + ", " + str(questionInQuestion + 2) + ", " + str(questionInQuestion + 3) + "? ")
	# If they lied in questions 1, 2, 3 or 4, 5, 6:
	else:
		lie = input(str(q) + ". Did you lie in any of the questions " + str(questionInQuestion) + ", " + str(questionInQuestion + 1) + ", " + str(questionInQuestion + 2) + "? ")
	

	# If they said they lied:
	if lie == "T":
		for n in range(3):
			q += 1

			# Then ask for the order bit again
			if (bitInQuestion == 1):
				choice = input(str(q) + ". Is the 1st high order bit 0? ")
			elif (bitInQuestion == 2):
				choice = input(str(q) + ". Is the 2nd high order bit 0? ")
			elif (bitInQuestion == 3):
				choice = input(str(q) + ". Is the 3rd high order bit 0? ")
			else:
				choice = input(str(q) + ". Is the " + str(bitInQuestion) + "th high order bit 0? ")

			# If there is a contradiction, lie detected. End program.
			if (choice == "T" and Bits[bitInQuestion - 1] == 1):
				Bits[bitInQuestion - 1] = 0
				print(Bits)
				quit()
			if (choice == "F" and Bits[bitInQuestion - 1] == 0):
				Bits[bitInQuestion - 1] = 1
				print(Bits)
				quit()
			# If there is no contradition, move on to the next question.
			elif (choice == "T" and Bits[bitInQuestion - 1] == 0) or (choice == "F" and Bits[bitInQuestion - 1] == 1):
				bitInQuestion += 1
		
		# Last question
		q += 1
		if q == 17:
			choice = input("17. Is the 10th high order bit 0? ")
			if (choice == "T" and Bits[bitInQuestion - 1] == 1):
				Bits[bitInQuestion - 1] = 0
				print(Bits)
				quit()
			if (choice == "F" and Bits[bitInQuestion - 1] == 0):
				Bits[bitInQuestion - 1] = 1
				print(Bits)
				quit()
			else:
				print(Bits)
				quit()
		else:
			print(Bits)
			quit()

	# If they said they told the truth:
	elif lie == "F":
		questionInQuestion = questionInQuestion + 3
		bitInQuestion = bitInQuestion + 3
		if questionInQuestion > 8:
			print(Bits)
			quit()
		q += 1
		print(Bits)
