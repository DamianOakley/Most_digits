#Most digits
#https://www.codewars.com/kata/58daa7617332e59593000006

nums1 = [742, 8201, -17, 819, -99021, 7209]

def most_digits(numbers):
    max_digits_found = 0
    number_with_max_digits = 0

    for num in numbers:
        digits = len(str(abs(num)))
        if digits > max_digits_found:
           max_digits_found = digits
           number_with_max_digits = num

    return number_with_max_digits

print(most_digits(nums1)) 


nums2 = [-1922, 2839201, 92678322, 4, 64, -929019]

def most_digits(numbers):
    max_digits_found = 0
    number_with_max_digits = 0

    for num in numbers:
        digits = len(str(abs(num)))
        if digits > max_digits_found:
           max_digits_found = digits
           number_with_max_digits = num

    return number_with_max_digits
print(most_digits(nums2)) 

#This function browses the numbers displayed in a list. 
#It then counts the digits in each number and selects the one with the highest amount of digits, regardless of sign.
#It then returns that number as the output.