t = 7
# upper triangle 
for i in range(t):
    print(" "*(t-i)+"*"*(2*i+1))
# lower triangle    
for i in range(t,-1,-1):
    print(" "*(t-i)+"*"*(2*i+1))
