# ♦️ STRING MANIPULATION EXERCISES
# 1. CREATE A FUNCTION THAT RECIEVES A STRING AND RETURN THE INVERTED STRING
def invert_string(string):
    inverted_string = ""
    for char in string:
        inverted_string = char + inverted_string
    return inverted_string
# print(invert_string("Federico"))

# 1.1 ⬆️ OPTIMIZED USING JOIN AND REVERSED
def reversed_string_converter(string):
    return "".join(reversed(string))
# print(reversed_string_converter("This is a optimized way"))

# 1.2 ⬆️ SHORT SYNTAX USING SLICING [::-1]
def reversed_string_slicing (string):
    return  string[::-1]
# print(reversed_string_slicing("Shorter and optimized approach"))

# 2. COUNT VOCALS IN STRING
string = "Fedeaawweweei"
vocals = ["a","e","i","o","u"]
vocalsCount = 0
vocalsFounded = []
for char in string.lower():
    if char in vocals:
        vocalsCount +=1
        vocalsFounded.append(char)
# print(vocalsCount)
# print(vocalsFounded)

# 3. DELETE WHITE SPACES USING REPLACE
sentence = "Python its a languaje multiplatform"
# sentenceFormated = sentence.replace(" ", "")
# print(sentenceFormated)

# 3.1 ⬆️ DELETING WHITE SPACES USING JOIN AND SPLIT
sentenceFormated = "".join(sentence.split())
# print(sentenceFormated)

# 4. CREATE A FUNCTION THAT DETECT FOR PALINDROMES
possiblePalindrome = "federico"
def checkPalindrome(posiblePalindrome):
    rever = "".join(reversed(posiblePalindrome))
    if posiblePalindrome == rever:
        return True
    else:
        return False
# print(checkPalindrome(possiblePalindrome))

# 4.1 ⬆️⬆️ USING SLICING SYNTAX [::-1] REDUCED
def check_palindrome(word):
    return word == word[::-1]
# print(check_palindrome("reconocer"))

# 5. CREATE A FUNCTION THAT DELETE ALL OCURRENCES
my_string = "Me gusta Python"
def replace_word(text,old_world, new_world):
    return text.replace(old_world, new_world)
# print(replace_word(my_string, "Python", "Java"))

# 6. WORDS COUNTER 
word_counter = sentence.split()
# print(len(word_counter))

# 7. INTERLEAVE CHARACTERS
def separete_characters(string):
    return "-".join(string).lower()
# print(separete_characters(sentence))

# 8. EXTRACT NUMBERS FROM STRING
clean_string = []
numbers_detected = []
def extract_numbers(string):
    for char in string:
        if not char.isdigit():
            clean_string.append(char)
        else:
            numbers_detected.append(char)
    return "Clean string: ",clean_string, "Numbers detected: ",numbers_detected
# print(extract_numbers("F3Der1c0"))

# 9. TITLE FORMAT
# CONVERT FIRST LETTER OF EVERY WORD IN UPPERCASE
def title_text (text):
    return text.title()
# print(title_text("fe fe fe ef ef"))


# 10. CONVERT LETTER TO LEET SPEAK
# EXAMPLE: "Hello world" → "H3110 W0r1d"
def leet_speak_converter (string):
    string = string.lower()
    string = string.replace("a", "4")
    string = string.replace("e", "3")
    string = string.replace("i", "1")
    string = string.replace("o", "0")
    return string
# print(leet_speak_converter("Federico")) 


# EXERCISE Create a program that receive weight and choose if are kgs or lbs inserting the letter k, K or l,L
# print("First i need your weight")
# weight = float(input("Weight: "))
# unit = input("(K)gs or (L)bs ").lower()
# if unit == "k":
#     print("Your weight converted to Lbs: ", weight/0.45)
# else:
#     print("Your weight converted to Kgs: ",weight*0.45)
    

# LIST
# Store indexed data [0]
# We can change, add and remove items 
# Allow duplicates
# numbers = [1,2,3,4,5,6]
# add value to the end of list
# numbers.append(6)

# Remove value
# numbers.remove(3)

# Remove all items 
# numbers.clear()

# insert index and value to add
# numbers.insert(0,-2)

# Check if a value exist on list using in operator
# print(2 in numbers) 
# print(len(numbers))


# FOR LOOPS
# fruits = ["apple", "orange", "watermelon", "peach"]
# for item in fruits:
#     print(item)


# RANGE FUNCTION
# Generate a range of numbers
# numbs = range(0,11)
# for number in numbs:
#     print(number)

# We can add a third parameter to step
# n = range (0, 11, 2)
# for number in n:
#     print(number)

# We can use range() inside for when we dont need to store the result in a separate value
# for number in range (0, 11, 2):
#     print(number)

# We can REVERSE range
# for x in reversed(range(1,11)):
#     print(x)
# print("Happy new Year!")


# TUPLAS (inmutables)
# values = (1,3,5,20,20.2,3)
# COUNT
# print(values.count(3))
# INDEX (First coincidence only)
# print(values.index(20.2))

# ENUMERATE FUNCTION (to acces index and value)
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
# for index, color in enumerate(colors):
#     print(index, color)

# EXCEPTIONS 
# - Occurs when syntactically correct code result in an error.
# - Occurs in the execution, errors are detected by the parser.
# - Program comes to a halt.

# Raising an error
# credit_card = "2021-2040-3040-2244"
# if len(credit_card)>= 19:
#     raise Exception("The credit card number might have 18 digits it has", len(credit_card))
# Not executed
# print(len(credit_card))
# print(type(credit_card))

# ASSERT
# - Used for debuggin.
# - Test that a condition is met (True).
# - Not use it in production (optimized mode -o -oo)
# - Program comes to a halt.

# CASE 1 TRUE ASSERT
# phone_number = "1134883456"
# assert(len(phone_number) == 10),"The phone number might contains 10 digits"
# print("We can continue the process")

# CASE 2 FALSE ASSERT
# phone_number = "11348834562"
# assert(len(phone_number) == 10),"The phone number might contains 10 digits"
# Not executed
# print("We can continue the process")

# HANDLING ERRORS - TRY AND EXCEPT
# EXAMPLE
# def linux_interaction():
#     import sys
#     # print(sys.platform)
#     if "linux" not in sys.platform:
#         raise RuntimeError("Function can only run on linux systems.")
#     # condition is true so this not executed
#     print("Doing linux things.")

# SORTING PRODUCTION OPTIMIZED MOD THAT IGNORES RAISED STATEMENT
# # Calling 
# try:
#     linux_interaction()
#     # Catching and refer the error
# except RuntimeError as error:
#     print(error)
#     print("The linux_interaction() function wasn't executed.")

# # EXAMPLE 2 
# try:
#     with open("file.log") as file:
#         read_data = file.read()
#         print(read_data)
# except:
#     print("Couldn't open file.log")

# Handling file not found with a built-up exception 
# try:
#     with open("files.log") as file:
#         read_data = file.read()
#         print(read_data)
# except FileNotFoundError as fnf_error:
#     print(fnf_error)
# # Adding ELSE statment no exception? run else clause
# else:
#     print("Doing even more Linux things.")

# FUNCTIONS:
# All you need to know about is the function’s interface:
# What arguments (if any) it takes
# What values (if any) it returns
# Abstractions and reusability
# Modules
# ANY() Takes iterable as it argument returns True if any of the item are truthy and false otherwise.
# print(any([False, False, False])) #False
# print(any([len('foo') == 3, 8 >=5 , False])) #True


