
## Fizzbuzz

def fizzbuzz(length, first, second):

    output = ""

    for i in range(1,length+1):
        output += str(i)+": "
        if not i % first:
            output += "fizz"
        if not (i % second):
            output += "buzz"
        output += "\n" 

    print(output)


fizzbuzz(100, 3, 5)
