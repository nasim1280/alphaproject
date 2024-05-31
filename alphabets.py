import turtle
sc = turtle.Screen() 
sc.setup(400, 300) 
name = turtle.textinput("Name In Lines!!", "type your name:") 

tu = turtle.Turtle()
turtle.screensize(canvwidth=900, canvheight=600)
tu.left(90)

def A(num):
	num = num*12
	for lines in range (num,num+2,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)
	for lines in range(num+2,num+7,1):
		tu.penup()
		tu.setpos(lines*12-450,-100)
		tu.pendown()
		tu.fd(100)
	for lines in range(num+2,num+7,1):
		tu.penup()
		tu.setpos(lines*12-450,100)
		tu.pendown()
		tu.fd(200)
	for lines in range (num+7,num+9,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)	
		
def B(num):
	num = num*12
	for lines in range (num,num+2,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)
	for lines in range(num+2,num+7,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(100)
	for lines in range(num+2,num+7,1):
		tu.penup()
		tu.setpos(lines*12-450,0)
		tu.pendown()
		tu.fd(100)
	for lines in range(num+2,num+7,1):
		tu.penup()
		tu.setpos(lines*12-450,200)
		tu.pendown()
		tu.fd(100)	
	for lines in range (num+7,num+9,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)

def C(num):
	num = num*12
	for lines in range (num,num+4,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)
	for lines in range(num+4,num+9,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(100)
	for lines in range(num+4,num+9,1):
		tu.penup()
		tu.setpos(lines*12-450,200)
		tu.pendown()
		tu.fd(100)		

def D(num):
	num = num * 12
	for lines in range (num,num+2,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)
	for lines in range(num+2,num+4,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(100)
	for lines in range(num+2,num+4,1):
		tu.penup()
		tu.setpos(lines*12-450,200)
		tu.pendown()
		tu.fd(100)
	for lines in range(num+4,num+9,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)			

def E(num):
	num = num*12
	for lines in range (num,num+4,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)
	for lines in range(num+4,num+9,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(100)
	for lines in range(num+4,num+9,1):
		tu.penup()
		tu.setpos(lines*12-450,0)
		tu.pendown()
		tu.fd(100)
	for lines in range(num+4,num+9,1):
		tu.penup()
		tu.setpos(lines*12-450,200)
		tu.pendown()
		tu.fd(100)									

def F(num):
	num = num*12
	for lines in range (num,num+4,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)
	for lines in range(num+4,num+9,1):
		tu.penup()
		tu.setpos(lines*12-450,0)
		tu.pendown()
		tu.fd(100)
	for lines in range(num+4,num+9,1):
		tu.penup()
		tu.setpos(lines*12-450,200)
		tu.pendown()
		tu.fd(100)			

def G(num):
	num = num*12
	for lines in range (num,num+4,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)
	for lines in range(num+4,num+7,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(100)
	for lines in range(num+4,num+9,1):
		tu.penup()
		tu.setpos(lines*12-450,200)
		tu.pendown()
		tu.fd(100)				
	for lines in range(num+7,num+9,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(300)
	for lines in range(num+5,num+7,1):
		tu.penup()
		tu.setpos(lines*12-450,0)
		tu.pendown()
		tu.fd(100)

def H(num):		
	num = num*12
	for lines in range (num,num+2,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)
	for lines in range(num+2,num+7,1):
		tu.penup()
		tu.setpos(lines*12-450,0)
		tu.pendown()
		tu.fd(100)
	for lines in range (num+7,num+9,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)

def I(num):
	num = num*12
	for lines in range (num,num+3,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(100)
	for lines in range(num,num+3,1):
		tu.penup()
		tu.setpos(lines*12-450,200)
		tu.pendown()
		tu.fd(100)
	for lines in range(num+3,num+6,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)
	for lines in range(num+6,num+9,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(100)	
	for lines in range (num+6,num+9,1):
		tu.penup()
		tu.goto(lines*12-450,200)
		tu.pendown()
		tu.fd(100)

def J(num):
	num = num*12
	for lines in range (num,num+3,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(200)
	for lines in range(num+3,num+6,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(100)
	for lines in range(num+6,num+9,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)	
	
def K(num):
	num = num*12
	for lines in range (num,num+2,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)
	for lines in range(num+2,num+5,1):
		tu.penup()
		tu.setpos(lines*12-450,0)
		tu.pendown()
		tu.fd(100)
	for lines in range(num+5,num+6,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)
	for lines in range(num+6,num+9,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(200)	
	for lines in range (num+6,num+9,1):
		tu.penup()
		tu.goto(lines*12-450,100)
		tu.pendown()
		tu.fd(200)

def L(num):
	num = num*12
	for lines in range(num,num+3,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)	
	for lines in range (num+3,num+9,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(100)

def M(num):
	num = num*12
	for lines in range (num,num+2,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)
	for lines in range(num+2,num+4,1):
		tu.penup()
		tu.setpos(lines*12-450,0)
		tu.pendown()
		tu.fd(300)
	for lines in range(num+4,num+5,1):
		tu.penup()
		tu.setpos(lines*12-450,-100)
		tu.pendown()
		tu.fd(300)
	for lines in range(num+5,num+7,1):
		tu.penup()
		tu.setpos(lines*12-450,0)
		tu.pendown()
		tu.fd(300)	
	for lines in range (num+7,num+9,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)

def N(num):
	num = num*12
	for lines in range (num,num+2,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)
	for lines in range(num+2,num+4,1):
		tu.penup()
		tu.setpos(lines*12-450,0)
		tu.pendown()
		tu.fd(300)
	for lines in range(num+4,num+5,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)
	for lines in range(num+5,num+7,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(300)	
	for lines in range (num+7,num+9,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)

def O(num):
	num = num*12
	for lines in range (num,num+2,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)
	for lines in range(num+2,num+7,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(100)
	for lines in range(num+2,num+7,1):
		tu.penup()
		tu.setpos(lines*12-450,200)
		tu.pendown()
		tu.fd(100)
	for lines in range(num+7,num+9,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)	

def P(num):
	num = num*12
	for lines in range (num,num+2,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)
	for lines in range(num+2,num+4,1):
		tu.penup()
		tu.setpos(lines*12-450,0)
		tu.pendown()
		tu.fd(100)
	for lines in range(num+2,num+4,1):
		tu.penup()
		tu.setpos(lines*12-450,200)
		tu.pendown()
		tu.fd(100)	
	for lines in range(num+4,num+9,1):
		tu.penup()
		tu.setpos(lines*12-450,0)
		tu.pendown()
		tu.fd(300)			

def Q(num):
	num = num*12
	for lines in range (num,num+2,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)
	for lines in range(num+2,num+5,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(100)
	for lines in range(num+2,num+7,1):
		tu.penup()
		tu.setpos(lines*12-450,200)
		tu.pendown()
		tu.fd(100)
	for lines in range(num+5,num+7,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(200)	
	for lines in range (num+7,num+9,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)

def R(num):
	num = num*12
	for lines in range (num,num+2,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)
	for lines in range(num+2,num+4,1):
		tu.penup()
		tu.setpos(lines*12-450,0)
		tu.pendown()
		tu.fd(100)
	for lines in range(num+2,num+5,1):
		tu.penup()
		tu.setpos(lines*12-450,200)
		tu.pendown()
		tu.fd(100)
	for lines in range(num+4,num+5,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(300)	
	for lines in range (num+5,num+6,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)
	for lines in range(num+6,num+9,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(100)
	for lines in range(num+6,num+9,1):
		tu.penup()
		tu.setpos(lines*12-450,0)
		tu.pendown()
		tu.fd(300)	
	
def S(num):
	num = num*12
	for lines in range (num,num+5,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(100)
	for lines in range(num,num+4,1):
		tu.penup()
		tu.setpos(lines*12-450,0)
		tu.pendown()
		tu.fd(300)
	for lines in range(num+4,num+5,1):
		tu.penup()
		tu.setpos(lines*12-450,0)
		tu.pendown()
		tu.fd(100)
	for lines in range(num+5,num+9,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(300)	
	for lines in range (num+4,num+9,1):
		tu.penup()
		tu.goto(lines*12-450,200)
		tu.pendown()
		tu.fd(100)

def T(num):
	num = num*12
	for lines in range (num,num+3,1):
		tu.penup()
		tu.goto(lines*12-450,200)
		tu.pendown()
		tu.fd(100)
	for lines in range(num+3,num+6,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)
	for lines in range(num+6,num+9,1):
		tu.penup()
		tu.setpos(lines*12-450,200)
		tu.pendown()
		tu.fd(100)
	

def U(num):
	num = num*12
	for lines in range (num,num+2,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)
	for lines in range(num+2,num+7,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(100)
	for lines in range(num+7,num+9,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)
	
def V(num):
	num = num*12
	for lines in range (num,num+2,1):
		tu.penup()
		tu.goto(lines*12-450,-100)
		tu.pendown()
		tu.fd(400)
	for lines in range(num+2,num+7,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(200)
	for lines in range(num+7,num+9,1):
		tu.penup()
		tu.setpos(lines*12-450,-100)
		tu.pendown()
		tu.fd(400)
	
def W(num):
	num = num*12
	for lines in range (num,num+2,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)
	for lines in range(num+2,num+4,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(200)
	for lines in range(num+4,num+5,1):
		tu.penup()
		tu.setpos(lines*12-450,-100)
		tu.pendown()
		tu.fd(300)
	for lines in range(num+5,num+7,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(200)	
	for lines in range (num+7,num+9,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(500)
	
def X(num):
	num = num*12
	for lines in range (num,num+3,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(200)
	for lines in range(num,num+3,1):
		tu.penup()
		tu.setpos(lines*12-450,100)
		tu.pendown()
		tu.fd(200)
	for lines in range(num+3,num+6,1):
		tu.penup()
		tu.setpos(lines*12-450,-100)
		tu.pendown()
		tu.fd(300)
	for lines in range(num+6,num+9,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(200)	
	for lines in range (num+6,num+9,1):
		tu.penup()
		tu.goto(lines*12-450,100)
		tu.pendown()
		tu.fd(200)
	
def Y(num):
	num = num*12
	for lines in range (num,num+3,1):
		tu.penup()
		tu.goto(lines*12-450,0)
		tu.pendown()
		tu.fd(300)
	for lines in range(num+3,num+6,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(300)
	for lines in range(num+6,num+9,1):
		tu.penup()
		tu.setpos(lines*12-450,0)
		tu.pendown()
		tu.fd(300)
	
def Z(num):
	num = num*12
	for lines in range (num,num+3,1):
		tu.penup()
		tu.goto(lines*12-450,-200)
		tu.pendown()
		tu.fd(300)
	for lines in range(num,num+6,1):
		tu.penup()
		tu.setpos(lines*12-450,200)
		tu.pendown()
		tu.fd(100)
	for lines in range(num+3,num+6,1):
		tu.penup()
		tu.setpos(lines*12-450,0)
		tu.pendown()
		tu.fd(100)
	for lines in range(num+3,num+9,1):
		tu.penup()
		tu.setpos(lines*12-450,-200)
		tu.pendown()
		tu.fd(100)	
	for lines in range (num+6,num+9,1):
		tu.penup()
		tu.goto(lines*12-450,0)
		tu.pendown()
		tu.fd(300)
	
name = name.upper()
alphas = list(name)

for num in range(len(name)):
	alpha = alphas[num]
	if alpha == 'A' :
		A(num)
	if alpha == 'B' :
		B(num)
	if alpha == 'C' :
		C(num)
	if alpha == 'D' :
		D(num)
	if alpha == 'E' :
		E(num)		
	if alpha == 'F' :
		F(num)
	if alpha == 'G' :
		G(num)					
	if alpha == 'H' :
		H(num)		
	if alpha == 'I' :
		I(num)		
	if alpha == 'J' :
		J(num)		
	if alpha == 'K' :
		K(num)		
	if alpha == 'L' :
		L(num)		
	if alpha == 'M' :
		M(num)		
	if alpha == 'N' :
		N(num)		
	if alpha == 'O' :
		O(num)		
	if alpha == 'P' :
		P(num)	
	if alpha == 'Q' :
		Q(num)		
	if alpha == 'R' :
		R(num)		
	if alpha == 'S' :
		S(num)		
	if alpha == 'T' :
		T(num)		
	if alpha == 'U' :
		U(num)		
	if alpha == 'V' :
		V(num)		
	if alpha == 'W' :
		W(num)		
	if alpha == 'X' :
		X(num)		
	if alpha == 'Y' :
		Y(num)	
	if alpha == 'Z' :
		Z(num)		

turtle.done()