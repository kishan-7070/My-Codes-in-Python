str1=input("Enter string: ")
v=['a','e','i','o','u']
count =0
for vowel in v:
   for char in str1:
       if(vowel==char):
           print(vowel)
           count+=1
print("Total number of vowels in str1 is:",count)
