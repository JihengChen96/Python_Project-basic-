text_input = str(input("enter a phase "))

## the function of split.() is to split the string into 
text_split = text_input.split()

### we need to pre define A before the for loop
a = " "
for i in text_split:
    a = a + i[0].upper()
print(a)