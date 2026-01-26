#simple example
def countdown(i):
    print(i)
    if i <= 1:
        return
    else:
        countdown(i-1)

countdown(5)


#How Stack works in recursion
print("\n------------------------------------------")
def greet(name):
    print(f'hello {name} !')
    greet2(name)
    print('im getting ready to say bye')
    bye()

def greet2(name):
    print(f'how are you {name}')

def bye():
    print('ok bye')

greet('alex')

#Another recursion example
print("\n------------------------------------------")
nums = [1,2,3,4,5,6,7,8]

nums_sum = 0
for i in nums:
    nums_sum += i
print(nums_sum)

def func_nums_sum(arr, i=0):
    if i == len(arr):
        return 0
    return arr[i] + func_nums_sum(arr, i + 1)

    
print(f'nums sum recursion: {func_nums_sum(nums)}')

print("\n------------------------------------------")
def count_items(arr, i=0):
    if i == len(arr):
        return 0
    return 1 + count_items(arr, i + 1)

print(f'Counting items using recursion: {count_items(nums)}')