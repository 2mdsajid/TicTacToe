import random
def clear():
	import os
	os.system( 'clear' )

global list,l2
list=[]
l2=[]
def data():
	global theBoard,x,y
	theBoard = {'1': ' ', '2': ' ', '3': ' ',
	 '4': ' ', '5': ' ', '6': ' ',
	 '7': ' ', '8': ' ', '9': ' '}
	x="0"
	y="x"

data()

def win():
	if theBoard["1"] == x and theBoard["2"] == x and theBoard["3"] == x or theBoard["4"]  == x and theBoard["5"] == x and theBoard["6"] == x or theBoard["7"] == x and theBoard["8"] == x and theBoard["9"] == x or theBoard["1"] == x and theBoard["5"] == x and theBoard["9"] == x or theBoard["3"] == x and theBoard["5"] == x and theBoard["7"] == x or theBoard["1"] == x and theBoard["4"]  == x and theBoard["7"] == x or theBoard["2"] == x and theBoard["5"] == x and theBoard["8"] == x or theBoard["3"] == x and theBoard["6"] == x and theBoard["9"] == x:
		print("\nYou Won")
		m = input("more(y/n)")
		if m == "y":
			clear()
			list.clear()
			l2.clear()
			data()
			inp()

		else:
			exit()
		
	elif theBoard["1"] == y and theBoard["2"] == y and theBoard["3"] == y or theBoard["4"]  == y and theBoard["5"] == y and theBoard["6"] == y or theBoard["7"] == y and theBoard["8"] == y and theBoard["9"] == y or theBoard["1"] == y and theBoard["5"] == y and theBoard["9"] == y or theBoard["3"] == y and theBoard["5"] == y and theBoard["7"] == y or theBoard["1"] == y and theBoard["4"]  == y and theBoard["7"] == y or theBoard["2"] == y and theBoard["5"] == y and theBoard["8"] == y or theBoard["3"] == y and theBoard["6"] == y and theBoard["9"] == y:
		print("\nComputer won")
		m = input("more(y/n)")
		if m == "y":
			clear()
			list.clear()
			l2.clear()
			data()
			inp()
		else:
			exit()
	elif len(list) == 9:
		print("\nTie !")
		m = input("more(y/n)")
		if m == "y":
			clear()
			list.clear()
			data()
			inp()
		else:
			exit()		
win()


def cmp():
	global cm,d
	cm = True
	se = [int(list[-1])+1, int(list[-1])+3, int(list[-1])-1, int(list[-1])-3]


	if list[-1] == "1":
		if "9" in list or "3" in list:
			d=5
		elif "3" in list:
			d=2
		elif "7" in list:
			d=4
		else:
			a1 = [2,4,6,7]
			for el in l2:
				if el in a1:
					a1.remove(el)
			d = random.choice(a1)
			l2.append(d)
			a1.remove(d)
	elif list[-1] == "7":
		if "1" in list:
			d=4
		elif "9" in list:
			d=8
		elif "3" in list:
			d=5
		else:
			a7 = [4,8]
			aa7 = [""]
			for el in l2:
				if el in a7:
					a7.remove(el)
			d = random.choice(a7)
			l2.append(d)
			a7.remove(d)
	elif list[-1] == "5":
		if "1" in list:
			d= 9
		elif "9" in list:
			d= 1
		elif "3" in list:
			d=7
		elif "7" in list:
			d=3
		else:
			a5 = [2,4,6,8]
			for el in l2:
				if el in a5:
					a5.remove(el)
			d = random.choice(a5)
			l2.append(d)
			a5.remove(d)
	elif list[-1] == "9":
		if "1" in list or "3" in list:
			d= 5
		elif "7" in list:
			d=8
		elif "3" in list:
			d=6
		else:
			a9 =[6,8]
			for el in l2:
				if el in a9:
					a9.remove(el)
			d = random.choice(a9)
			l2.append(d)
			a9.remove(d)
	else: 
		d = random.choice(se)
		if d>9 or d<1:
			cmp()
	
	
	if str(d) in list:
		cmp()
	else:
		theBoard[str(d)] = y
		list.append(str(d))
		clear()
		printBoard(theBoard)

	
def inp():
	global cm
	cm = False
	d = input("\n> ")
	if d not in list:
		theBoard[d] = x
		list.append(d)	
	clear()
	printBoard(theBoard)


def printBoard(board):
 print(board['1'] + '|' + board['2'] + '|' + board['3'])
 print('-+-+-')
 print(board['4'] + '|' + board['5'] + '|' + board['6'])
 print('-+-+-')
 print(board['7'] + '|' + board['8'] + '|' + board['9'])
 win()
 if cm == False:
 	cmp()
 else:
 	inp()

print("""Use numbers as shown in
the tic-tac-toe board below !

Enter the number to write in your turn !
yours is "0" and Computer is "x"
good luck !
""")
print("1" + '|' + "2" + '|' +"3")
print('-+-+-')
print("4" + '|' +"5" + '|' + "6")
print('-+-+-')
print("7" + '|' + "8" + '|' +"9")
inp()