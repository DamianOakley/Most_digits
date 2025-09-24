#Most digits
#https://www.codewars.com/kata/58daa7617332e59593000006

nums = [742, 8201, -17, 819, -99021, 7209]

def most_digits(numbers):
    return max(numbers, key=lambda x: len(str(abs(x))))

print(most_digits(nums)) 

#We set "nums" as a variable, and include a list of digits for it to equate to. 
#We use "max" to find the number with the highest amount of characters, using "numbers" as a key.
#For said key, we use "lambda" to return the result, and use "len" to count the digits in each number.
#Finally, we use "str(abs)(x)" to remove any negative signs when counting digits, and then convert the result into a string before it is revealed.
