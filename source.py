import json

f = open('aabdelwahed3_input.json',)
data = json.load(f)
f.close()

p = data['p']
q = data['q']
g = data['g']
h = int(data['h'], base=16)
y = data['y']
r = data['r']
s = data['s']
k = -1

for i in range(pow(2,16)):
    if r == (pow(g,i,p) % q):
      k = i
      break

  
if k == -1:
  print('no k found')
  exit()

x = ((s*k-h)*pow(r,-1,q) % q)

def test():
  testY = pow(g,x,p)
  testR = pow(g,k,p) % q
  testS = (pow(k, -1, q) * (h + (x*r))) % q

  print('correct y') if testY == y else print('wrong y:', testY)
  print('correct r') if testR == r else print('wrong r:', testR)
  print('correct s') if testS == s else print('wrong s:', testS)


print('k:',k)
print('x:', x)

# test()
