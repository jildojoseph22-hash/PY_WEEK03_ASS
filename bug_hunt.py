count = 1
total = 0

# BUG: The while statement was missing a colon at the end.
# BUG: The condition used < 5, which stopped the loop before adding 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: total is an integer, so I converted it to a string before joining it with text.
print("Sum of 1 to 5 is: " + str(total))