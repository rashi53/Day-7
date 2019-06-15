def div(a,b):
    assert(b!=0),"Division by zero is not defined"
    return a/b
try:
  print(div(20,3))
  print(div(100,20))
  print(div(55,0))
except AssertionError as ob:
    print(ob)
print('thank you')




























































































