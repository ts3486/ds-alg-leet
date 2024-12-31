# put stirng into array. then, reverse the array by adding the elements of the array from last to frsit in another array. conacatenate the elements and return the string.

#this will have a bigO of o(n) and space complexity of o(n) as well.

#is input type always string? if not, we need to check the type of input and return if it is not string.

def reverse_string(string):
    string_array = list(string)
    reversed_array = []
    for i in range(len(string_array) - 1, -1, -1):
        reversed_array.append(string_array[i])
    return ''.join(reversed_array)

print(reverse_string("hello")) #result: olleh

def reverse_string2(string):
    return string[::-1]

print(reverse_string2("hello2")) #result: olleh