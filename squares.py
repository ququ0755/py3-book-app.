squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

#列表解析简化
squares = [value**2 for value in range(1,11)]
print(squares)