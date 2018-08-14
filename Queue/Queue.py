# importing "collections" for deque operations
import collections
class Queue:
# initializing deque
de = collections.deque([])

# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)

# printing modified deque
print("The deque after appending at right is : ")
print(de)

# using appendleft() to insert element at right end
# inserts 6 at the beginning of deque
de.appendleft(6)

# printing modified deque
print("The deque after appending at left is : ")
print(de)

# using pop() to delete element from right end
# deletes 4 from the right end of deque
de.pop()

# printing modified deque
print("The deque after deleting from right is : ")
print(de)

# using popleft() to delete element from left end
# deletes 6 from the left end of deque
de.popleft()

# printing modified deque
print("The deque after deleting from left is : ")
print(de)

print("Please select operation -\n" \
      "1. appendleft\n" \
      "2. appendright\n" \
      "3. popleft\n"
      "4. popleft\n")
InputData=int(input('Enter the data you want to process'))

if select == '1':
    print(number_1, "+", number_2, "=",
          add(number_1, number_2))

elif select == '2':
    print(number_1, "-", number_2, "=",
          subtract(number_1, number_2))

elif select == '3':
    print(number_1, "*", number_2, "=",
          multiply(number_1, number_2))

elif select == '4':
    print(number_1, "/", number_2, "=",
          divide(number_1, number_2))
else:
    print("Invalid input")