t = input("Please enter your time")

ts = t.split(':')
 
h = int(ts[0]) 
m = int(ts[1]) 
s = int(ts[2]) 

m += h * 60
s += m * 60

print(s)