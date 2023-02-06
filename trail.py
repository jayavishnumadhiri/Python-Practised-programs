globvar = 'Hello'
def test1():
	global globvar
	globvar = 'Good Morning'
		
def test2():
	globvar = 'Good Night'
	print(globvar)
	
print(globvar)
test1()
test2()
print(globvar)
			
