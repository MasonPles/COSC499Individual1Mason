
## Fizzbuzz
## Comments are cool!

def fizzbuzz(length, first, second, word1, word2):

    output = ""

    for i in range(1,length+1):
        output += str(i)+": "
        if not i % first:
            output += word1
        if not (i % second):
            output += word2
        output += "\n" 

    print(output)


fizzbuzz(100, 3, 5, "Cool", "Beans")
