# Exercise 1
print("\n+++++++Excercise1+++++++")
a = [1,2,3,4,5,6,7,8,9]

# Printing item in index 4 using bracket notation
print("\nPrinting item in index 4 using bracket notation")
print(a[3])

# Printing item in index 5 using [-1] index
print("\nPrinting item in index 5 using [-1] index")
print(a[-5])

# Printing every second item from the list
print("\nPrinting every second item from the list")
for i  in a:
    if i%2 == 0:
        print(i)

# Printing items from 3rd to 5th
print("\nPrinting items from 3rd to 5th")
for i in range(len(a)):
    if (i>1):
        print(a[i])
    if(i>3):
        break

# Exercise 2
print("\n+++++++Excercise2+++++++")
# Printing all names
print("\nPrinting all names")
names  = {'foo': {'name': 'Foo', 'lastname': 'Fooer'}, 'bar': {'name': 'Bar', 'lastname': 'Baer'}, 'Baz': None}

for k in names:
    print(k)

# Printing value of name key of bar
print("\nPrinting value of name and lastname keys of bar")
print(f"Firstname is {names['bar']['name']} and lastname is {names['bar']['lastname']}")

# Printing all names values of non empty keys of the dictionary
print("\nPrinting all names values of non empty keys of the dictionary")

for k in names:
    if not names[k] is None:
        print(names[k]["name"]) 

print("\n+++++++Excercise3+++++++")
# Sum function
def summer(a,b):
    return a + b

# Invoking summer with parameters 2,4
print(f"Invoking summer with parameters 2,4:  {summer(2,4)}\n")


# Sum function refactored with default values
def summer2(a=2,b=4):
    return a + b

# Invoking summer with parameters 2,4
print(f"Invoking summer with default parameters 2,4:  {summer2()}\n")


def summer3(**kwargs):
    a = kwargs['a']
    b = kwargs['b']
    if b<0:
        if (a+b)>0:
            return -1*(a+b)
    return a + b

print(f"Invoking summer with keyword arguments a=2,b=5: {summer3(a=2,b=5)}\n")


print("\n+++++++Excercise4+++++++")
words = ['python', 'and', 'data', 'science', 'is', 'awesome']

# words with len greater than 5
words_gt_5 = [word for word in words if len(word)>5]
print(f"Printing words with len greater than 5:  {words_gt_5}\n")

# dictionary from words with word index as key and word as value
words_dict = {words.index(word):word for word in words}
print(f"Printing dictionary from words with word index as key and word as value:  {words_dict}\n")

# add next item with value = "!"
words_dict[len(words_dict)] = "!"
print(f"Adding item with key = count of dict and value ='!':  {words_dict}\n")

print("\n+++++++Excercise4+++++++")
def only_ints_reversed(input_list = []):
    only_ints = [num for num in input_list if isinstance(num,int) and not isinstance(num,bool)]
    only_ints.sort(reverse=True)
    return only_ints

input_list = ['x', -0.1, 'foo', True, 'bar', 10, 1.1, '8', 5, None, 12]
print(f"Returning {input_list} with only integers in reversed order\n")
print(only_ints_reversed(input_list = input_list))