colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
sentence = "The quick brown fox jumped over the lazy dog."
modifiers = ["Dark", "Light", "Brownish"]

#slice
print('-= Slice =-')
print(sentence[0])
print(sentence[4])
print(sentence[-1])
print()
print(colors[1])
print(colors[1:4])

#split
print(' -= Split =-')
print(sentence.split(' '))

print('')
print('-= For =-')
modifiers = ["Dark", "Light", "Brownish"]
for c in colors:
    for m in modifiers:
        print(m + ' '+ c)

print('')
print('-= While =-')
countdown = 10
while countdown >= 0:
    print(str(countdown))
    countdown -= 1

print('')
print('-= Iterating =-')
names = ["Daniel", "James", "Peter", "Sean"]
while names:
    print('Welcome, Mr. ' + names.pop())

print(names)
names.append('Larry')
while names:
    print('Welcome, Mr. ' + names.pop())