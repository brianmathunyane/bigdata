def sum_array(array):
    return array[0] + sum_array(array[1:]) if array else 0


    '''Return sum of all items in array'''


sum_array([1,2,3,4,5,6,7,8,9,10])


def fibonacci(n):

    if n<= 1:
        return 1

    else:
        return fibonacci(n- 1) + fibonacci(n- 2)

    '''Return nth term in fibonacci sequence'''


fibonacci (5)


def reverse(word):
    if len(word) == 0:
        return word
    else:
        return reverse(word[1:]) + word[0]
#a = str(input("Enter the string to be reversed: "))
#print(reverse(a))

    '''Return word in reverse'''


reverse("brian")
