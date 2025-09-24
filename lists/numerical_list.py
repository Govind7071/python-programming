for value in range(1,5):
    print(value)
print("\n")
for value in range(6):
        print(value)
print("\n")       
num=list(range(1,6))
print(num)
print("\n")
odd_num=list(range(1,6,2))
print(odd_num)
print("\n")
even_num=list(range(2,6,2))
print(even_num)
print("\n")

squares=[]
for value in range(1,11):
    square=value ** 2
    squares.append(square)

print(squares)
print("\n")
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
print("\n")
squares = [value**2 for value in range(1, 11)]
print(squares)