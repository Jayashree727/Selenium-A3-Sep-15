def changecase(func):
  def myinner():
    return func().upper()
  return myinner

class Template:

for i in range(1, 10):
 if 10%2==0:
    print("even")
else:
    print("odd")

def test_login():
    print("login")

def prime_numbers(self):
    for i in range(2, 50):
        for j in range(2, i):
            if i%j==0:
                break
        else:
            print(i)
            