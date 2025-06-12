# Sum of two numbers
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
sum = num1 + num2
print("The sum of two numbers is : ", sum)
print()


# Odd or even number
num3 = int(input("Enter a number to verify even or odd : "))
if(num3 % 2 == 0) :
    print("The number is Even.")
else :
    print("The number is Odd.")
print()

# Factorial of a number
def findFactorial(num4) :
    if(num4 < 0) :
        return "The number is negative."
    elif (num4 == 0) :
        return 1
    else :
        return num4 * findFactorial(num4 - 1)

num4 = int(input("Enter a number to find factorial : "))
factorial = findFactorial(num4)
if(num4 > 0) :
    print(f"The factorial of {num4} is {factorial}.")
else :
    print(factorial)
print()


# Fibonacci Series
f1 = 0
f2 = 1
terms = int(input("Enter number of terms in fibonacci series : "))
if(terms <= 0) :
    print("Number of terms cannot be zero or negative.")
elif(terms == 1) :
    print(f1)
elif(terms == 2) :
    print(f1, f2)
else :
    print(f1, f2, end = " ")
    for i in range(2, terms) :
        f3 = f1 + f2
        print(f3, end = " ")
        f1 = f2
        f2 = f3
print()
print()


# Reverse a String
str1 = input("Enter a string to reverse : ")
reversed_str = ""
for ch in str1 :
    reversed_str = ch + reversed_str
print("The reversed string is ", reversed_str)
print()


# String is palindrome or not
str2 = input("Enter a string to check if palindrome or not : ")
n = len(str2)
i = 0
isPalindrome = True
while(i < n / 2) :
    if(str2[i] != str2[n - i - 1]) :
        isPalindrome = False
        break
    i += 1
if(isPalindrome) :
    print("The string is palindrome.")
else :
    print("The string is not palindrome.")
print()


# Leap year
year = int(input("Enter a year to check whether leap or not : "))
if(year % 400 == 0) :
    print("The year is leap year.")
elif(year % 100 != 0 and year % 4 == 0) :
    print("The year is leap year.")
else :
    print("The year is NOT leap year.")
print()


# Armstrong number
num5 = input("Enter a number to calculate whether armstrong number or not : ")
n1 = len(num5)
answer = 0
for i in num5 :
    answer += (int(i) ** n1)
if(answer == int(num5)) :
    print("The number is Armstrong number.")
else :
    print("The number is NOT Armstrong number.")
print()


# Encryption and Decryption using Substitution Cipher

def create_substitution_map() :
    original = "abcdefghijklmnopqrstuvwxyz"
    shifted =  "defghijklmnopqrstuvwxyzabc"
    mapping = {}
    for i in range(len(original)) :
        mapping[original[i]] = shifted[i]
    return mapping

def encrypt_substitution(text, mapping) :
    result = ""
    for char in text:
        if('a' <= char <= 'z') :
            result += mapping[char]
        elif('A' <= char <= 'Z') :
            lower_char = chr(ord(char) + 32)
            encrypted = mapping[lower_char]
            result += chr(ord(encrypted) - 32)
        else:
            result += char
    return result

def decrypt_substitution(text, mapping) :
    reverse_mapping = {}
    for key in mapping :
        reverse_mapping[mapping[key]] = key
    result = ""
    for char in text :
        if('a' <= char <= 'z') :
            result += reverse_mapping[char]
        elif('A' <= char <= 'Z') :
            lower_char = chr(ord(char) + 32)
            decrypted = reverse_mapping[lower_char]
            result += chr(ord(decrypted) - 32)
        else:
            result += char
    return result

print("Custom Encryption & Decryption Program.")
choice = input("Do you want to (E)ncrypt or (D)ecrypt? : ").lower()
text = input("Enter the message : ")
mapping = create_substitution_map()

if(choice == 'e') :
    substituted = encrypt_substitution(text, mapping)
    print("After substitution : ", substituted)
elif(choice == 'd') :
    decrypted = decrypt_substitution(text, mapping)
    print("Decrypted message : ", decrypted)
else :
    print("Invalid choice.")
