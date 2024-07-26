data = {}
print(type(data))
# Remember floor division : making it equivalent to the math.floor() function
# The result of regular division (using the / operator) is 15/4 = 3.75, but using // has floored 3.75 down to 3


print(-10//3)
print(11//3)

# print(''conversation - He said, "Shantanu's explanation is very good" and I subscribed channel"")
print("""conversation - He said, "Shree`s explanation is very good" and I subscribed to his blog""")
print("\"""conversation - He said, \"Shree\'s explanation is very good\" and I subscribed to his blog\"""")


name = "shantanu" # from yt
print(name[2:8:-2])

my_dict = {"a":100,"v":300,"j" :"32"}
print(len(my_dict))

## Merge 3 lists
a = [1,2,3]
b = [4,5,7]
c = [3,6,9]
print(a+b+c)
print(list(zip(a,b,c)))