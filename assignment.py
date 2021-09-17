
## Fizzbuzz

def fizzbuzz(length):

    output = ""

    for i in range(1,length+1):
        output += str(i)+": "
        if not i % 3:
            output += "fizz"
        if not (i % 5):
            output += "buzz"
        output += "\n" 

    print(output)


fizzbuzz(100, 3, 5)
