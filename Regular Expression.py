from ast import pattern
import re
from nltk.tokenize import word_tokenize;

text = "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure 7558313179 Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem +91-7558313179Ipsum comes from sections 1.10.32 and 1.10.33 of \"de Finibus Bonorum et Malorum\" (The Extremes of Good and Evil) 9022231583 by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first 7218462529 line of Lorem Ipsum, \"Lorem ipsum dolor sit amet..\", comes from a line in section 1.10.32"

# Here we will be finding the phone number from the given text using the text matching technique

pattern = '\+\d{2}-\d{10}|\d{10}'

ans = re.findall(pattern,text);
print(ans)


text = '''note-1: Ram had empire\n Contrary to 19 BC popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure 7558313179 Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem +91-7558313179Ipsum comes from sections 1.10.32 and 1.10.33 of \"de Finibus Bonorum et Malorum\" (The Extremes of Good and Evil) 9022231583 by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first 7218462529 line of Lorem Ipsum, \"Lorem ipsum dolor sit amet..\", comes from a line in section 1.10.32 \n
note-2: Chhatrapati shivaji Maharaj had empire\n Contrary to 19 BC popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure 7558313179 Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem +91-7558313179Ipsum comes from sections 1.10.32 and 1.10.33 of \"de Finibus Bonorum et Malorum\" (The Extremes of Good and Evil) 9022231583 by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first 7218462529 line of Lorem Ipsum, \"Lorem ipsum dolor sit amet..\", comes from a line in section 1.10.32\n
note-3: I will be having the empire\n Contrary to 19 BC popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure 7558313179 Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem +91-7558313179Ipsum comes from sections 1.10.32 and 1.10.33 of \"de Finibus Bonorum et Malorum\" (The Extremes of Good and Evil) 9022231583 by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first 7218462529 line of Lorem Ipsum, \"Lorem ipsum dolor sit amet..\", comes from a line in section 1.10.32'''

pattern = 'note\-\d\:'

result = re.findall(pattern, text)
print(result)


# To print any character except the character that we want to specify we give the ^ symbol

pattern = '[^n]' #Here we have left the value of  from the text file
print(re.findall(pattern, text))

# Now we will be having only the header of each of the topic
# To match this type of character pattern we will be having the character sequence as the pattern as given and then only till we find the new line

pattern = "note-\d:[^\n]*"
print(re.findall(pattern, text))

#Now we want to print the data where number is follwed by BC
pattern = '\d\d BC'
print(re.findall(pattern, text))

#if we want our data to have any range of data from any digit then the numbers can be put into the square brackets
#Here only data values between the range of [1-2]follwed by any numbers is accepted
pattern = '[1-2][0-9] BC'
print(re.findall(pattern, text))

pattern = "([1-2][0-9]) BC"
print("Years of the BC",re.findall(pattern, text, flags=re.IGNORECASE))

text ="""FY2021 Q1 $4.85
FY2020 Q4 $3.00"""

pattern1 = "FY[\d{4}]*"
pattern2 = '\$[\d\.\d\d]*'

print(re.findall(pattern1, text), " has the money of ", re.findall(pattern2,text))

text1 = "Hello, I am having an issue with my order #412889912."
text2 = "My order 412889912 is having an issue, I was charged 50$ when online it says 40$"
text3 = "I have a problem with my order number 412889912"
pattern = "\#d{9}|\d{9}|\d{9}"
print("For text number 1: ",re.findall(pattern,text1))
print("For text number 2: ",re.findall(pattern,text2))
print("For text number 3: ",re.findall(pattern,text3))