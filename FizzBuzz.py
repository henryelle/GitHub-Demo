for i in range(1,101):
    z = "FizzBuzz" if i % 3 == 0 and i % 5 == 0 else i
    z = "Fizz" if i % 3 == 0 else i
    z = "Buzz" if i % 5 == 0 else i
    print(z)
