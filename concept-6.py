

def add1(x, y):
    return x+y

res = add1(2,5)
print(res) #7

add = lambda x,y: x+y
print(add(1,2)) #3


#how map works
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x:x*2, numbers)
print(list(squared_numbers)) #[2, 4, 6, 8, 10]

#how filter works
even_numbers = filter(lambda x:x%2 == 0, numbers)
print(list(even_numbers)) #[2, 4]

num = [3, 2, 6, 1]
print(sorted(num)) #[1, 2, 3, 6]

print(num[::-1]) #[1, 6, 2, 3]