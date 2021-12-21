# numbers = [1, 2, 3, 4, 5]
# result = []
# for n in numbers:
#     if n % 2 == 1:
#         result.append(n*2)
# print(result)

#내포
numbers = [1, 2, 3, 4, 5]
result = []
result = [num * 2 for num in numbers if num % 2 == 1]
print(result)