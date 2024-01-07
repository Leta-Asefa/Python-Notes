x=10
y=0
try:
    x/y
except ZeroDivisionError as e:
    print('You can not divide by 0')
    print(e)
except Exception as e:
    print('Generall Expections')
    print(e)
finally:
    print("Finally Block")