
def ways(string):

	if len(string)<2 and int(string[0]) == 0:
		print("no of ways 0")
	elif len(string)<2:
		return 1
	if int(string[0]) == 0:
		noofway = 0
	else:
		noofway = 1

	for i in range(1,len(string)):

		if int(string[i]) < 7:
			prev = int(string[i-1])

			if prev>0 and prev<3:
				noofway += 1
			else:
				pass
		else:
			pass

	print("noofway = ",noofway) 


if __name__ == '__main__':
	string = input()

	ways(string)