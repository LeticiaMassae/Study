print('Hello, World!')
print(len('Hello, World!'))

print()
print('for x in range(10): print(x)')
for x in range(10): print(x)

print()
print("sorted('abracadabra')")
sorted('abracadabra')
print(sorted('abracadabra'))

print()
print("reversed(sorted('abracadabra'))")
reversed(sorted('abracadabra'))
print(reversed(sorted('abracadabra')))

print()
print("list(reversed(sorted('abracadabra')))")
list(reversed(sorted('abracadabra')))
print(list(reversed(sorted('abracadabra'))))

print()
print("''.join(reversed(sorted('abracadabra')))")
''.join(reversed(sorted('abracadabra')))
print(''.join(reversed(sorted('abracadabra'))))

print()
print("''.join(reversed(sorted(['Alice', 'Daniel', 'Bob', 'Charlie'])))")
''.join(reversed(sorted(['Alice', 'Daniel', 'Bob', 'Charlie'])))
print(''.join(reversed(sorted(['Alice', 'Daniel', 'Bob', 'Charlie']))))

print()
print("'This is a long string'.split(" ")")
print('This is a long string'.split(" "))

print()
print("a_string = 'Apples, oranges, and bananas'")
print("a_string.find('an')")
a_string = 'Apples, oranges, and bananas'
print(a_string.find('an'))

print()
print("a_string[10:]")
print(a_string[10:])

print()
print("Hello, {0}, and welcome to {1}".format("Robin", "Python"))

print()
a_list = "This is a long string".split(" ")
a_list.remove("long")
print(a_list)
