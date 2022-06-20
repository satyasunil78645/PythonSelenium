import array as arr

int_val = arr.array('i', [1, 2, -3, 4, 5])  # i --> type code for integer, mention accordingly for other data type
print(int_val.buffer_info())  # return the length

for i in range(len(int_val)):
    print(int_val[i], end=" ")
print()

char_val = arr.array('u', ['a', 'e', 'i'])
for i in range(len(char_val)):
    print(char_val[i], end=" ")

# creating new array with the same values
new_array = arr.array('i', [1, 2, -3, 4, 5])
new_array1 = new_array(new_array.typecode, (a for a in new_array))
for e in new_array1:
    print(e)
