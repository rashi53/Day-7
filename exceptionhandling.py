def kelvintofahrenheit(Temperature):
    assert(Temperature>=0),"Colder than absolute zero"
    res=((Temperature-273)*1.8)+32
    return res
try:
    print(kelvintofahrenheit(273))
    print(kelvintofahrenheit(505.78))
    print(kelvintofahrenheit(-5))
except AssertionError as ob:
    print(ob)
    print("thank you")
          
