# storing numbers 1 to 100
numRange = range(1, 101)

# iterating for each number and storing in a result
for num in numRange:

    result = ""
    # https://book.pythontips.com/en/latest/ternary_operators.html
    result = "FizzBuzz" if num % 3 == 0 and num % 5 == 0 else num
    if result == "FizzBuzz":
        print(result)
        continue
    result = "Fizz" if num % 3 == 0 else num
    if result == "Fizz":
        print(result)
        continue
    result = "Buzz" if num % 5 == 0 else num
    if result == "Buzz":
        print(result)
        continue
    # if result never becomes FizzBuzz, just print the number
    print(num)
    
