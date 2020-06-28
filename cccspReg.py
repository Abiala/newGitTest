import re, pyperclip
# Create regex for phone numbers
PhoneRegex = re.compile(r'\d{11}')
# Copy from clipboard
text = pyperclip.paste()
# Extract phone numbers from text
AllNumbers = PhoneRegex.findall(text)
# Save in a text file
Numbers = []
for number in AllNumbers:
    Numbers.append(number)
print(Numbers) 
result =  '\n'.join(Numbers)
newText = open('june.txt', 'a')
newText.write(result)
