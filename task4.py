
# Finding missing number in an array
arr1 = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11]
sum1 = (1 + len(arr1) + 1) * (len(arr1) + 1) / 2
sum2 = 0
for i in arr1 :
    sum2 += i
print("The given array is : ", arr1)
print("The missing number is : ", int(sum1 - sum2))
print()


# Check for balanced parenthesis
str1 = input("Enter sequence of parenthesis : ")
str2 = ""
flag = True
for i in str1 :
    if(i == '(' or i == '[' or i == '{') :
        str2 += i
    elif(i == ')' or i == ']' or i == '}') :
        if(str2 == "") :
            flag = False
            break
        elif(i == ')' and str2[-1] == '(') :
            str2 = str2[:-1]
        elif(i == ']' and str2[-1] == '[') :
            str2 = str2[:-1]
        elif(i == '}' and str2[-1] == '{') :
            str2 = str2[:-1]
        else :
            flag = False
            break
    else :
        print("Entered wrong character.")
if(flag and str2 == "") :
    print("The paranthesis is balanced.")
else :
    print("The paranthesis is NOT balanced.")
print()


# Longest Word in a sentence
str3 = input("Enter a string to find longest word : ")
word = ""
maxWord = ""
maxLen = 0
for i in str3 :
    if(i != ' ') :
        word += i
    else :
        if(maxLen < len(word)) :
            maxWord = word
            maxLen = len(word)
        word = ""
print("The longest word is :", maxWord, "-> length :", maxLen)
print()


# Count number of words in a sentence
str4 = input("Enter a string to find number of words : ")
wordsArray = str4.split()
wordCount = len(wordsArray)
print("The number of words is :", wordCount)
print()


# Check Pythagorean Triplet
print("Enter numbers to check Pythagorean Triplet.")
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))
if(num1 > num2) :
    if(num1 > num3) :
        num4 = (num2 ** 2) + (num3 ** 2)
        if(num4 == (num1 ** 2)) :
            print("It is Pythagorean Triplet.")
        else :
            print("It is NOT Pythagorean Triplet.")
    else :
        num4 = (num2 ** 2) + (num1 ** 2)
        if(num4 == (num3 ** 2)) :
            print("It is Pythagorean Triplet.")
        else :
            print("It is NOT Pythagorean Triplet.")
else :
    if(num2 > num3) :
        num4 = (num1 ** 2) + (num3 ** 2)
        if(num4 == (num2 ** 2)) :
            print("It is Pythagorean Triplet.")
        else :
            print("It is NOT Pythagorean Triplet.")
    else :
        num4 = (num1 ** 2) + (num2 ** 2)
        if(num4 == (num3 ** 2)) :
            print("It is Pythagorean Triplet.")
        else :
            print("It is NOT Pythagorean Triplet.")
print()


# Bubble sort on list of integers
list3 = [12, 45, 7, 89, 23, 56, 29, 90, 11, 3]
print("Original List is : ", list3)
length1 = len(list3)
for i in range(length1 - 1) :
    for j in range(length1 - 1 - i) :
        if(list3[j] > list3[j + 1]) :
            temp = list3[j]
            list3[j] = list3[j + 1]
            list3[j + 1] = temp
print("The sorted list is : ", list3)
print()


# Find subarray with given sum
arr2 = [2, 4, 5, 5, 7, 2, 3, 9]
print("The array is : ", arr2)
sum3 = 12
print("The subarray is required of sum : ", sum3)
i = 0
index = 0
sum4 = 0
flag = False
while(i < len(arr2)) :
    sum4 += arr2[i]
    if(sum4 == sum3) :
        flag = True
        print("There is subarray with given sum. Indices are from", index, "to", i)
        break
    elif(sum4 > sum3) :
        sum4 -= arr2[index]
        index += 1
        while(sum4 > sum3) : 
            sum4 -= arr2[index]
            index += 1
        if(sum4 == sum3) :
            flag = True
            print("There is a subarray with given sum. Indices are from", index, "to", i)
            break
    i += 1
if(not flag) :
    print("There is NOT a subarray with given sum.")
print()



# Log analysis system

# from collections import defaultdict, Counter

# def parse_log_line(line) :
#     try :
#         parts = line.split()
#         ip = parts[0]
#         url = parts[6]
#         response_code = parts[8]
#         return ip, url, response_code
#     except IndexError :
#         return None, None, None

# def analyze_log_file(file_path) :
#     ip_counter = Counter()
#     url_counter = Counter()
#     response_code_counter = Counter()

#     with open(file_path, 'r') as file :
#         for line in file :
#             ip, url, response_code = parse_log_line(line)
#             if ip and url and response_code:
#                 ip_counter[ip] += 1
#                 url_counter[url] += 1
#                 response_code_counter[response_code] += 1

#     print("\nTop 5 IP addresses : ")
#     for ip, count in ip_counter.most_common(5):
#         print(f"{ip} : {count} times")

#     print("\nTop 5 URLs accessed : ")
#     for url, count in url_counter.most_common(5):
#         print(f"{url} : {count} times")

#     print("\nHTTP Response Codes Count : ")
#     for code, count in response_code_counter.items():
#         print(f"{code} : {count} times")

# # here the file name is given as per file name used in the program
# log_file_path = "..."
# analyze_log_file(log_file_path)
