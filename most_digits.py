#Most digits
#https://www.codewars.com/kata/58daa7617332e59593000006

nums = [742, 8201, -17, 819, -99021, 7209]

def most_digits(numbers):
    return max(numbers, key=lambda x: len(str(abs(x))))

print(most_digits(nums)) 

#This function browses the numbers in a list. 
#It then finds the number with the highest amount of digits, regardless of sign.
#It returns that number as the output.