print('this program will check if the given word is palindrome or not.')
choice = 'yes'
while choice=='yes' :
	String=input('Enter any Word   ')
	String1=String.lower()
	length=int(len(String))
	newstr=''
	for i in range (length-1,-1,-1) :
		newstr += String1[i]
	if String1 == newstr :
		print(String,' is a palindrome')
	else :
		print(String, " is not a palindrome")
	choice='no'
	choice=input('Do you want to check another Yes/No:    ')
	choice=choice.lower()
if choice=='no' :
	print('-----Thankyou------')
elif choice != 'yes' or 'no' :
	print('Invalid Input')
	choice=input('Do you want to check another Yes/No:    ')
	choice=choice.lower()