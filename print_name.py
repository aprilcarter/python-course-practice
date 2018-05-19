def print_name(first_name, last_name):
    print(f"Your full name is {first_name} {last_name}")

print_name("April", "Carter")

'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(ls, command, location, value = ""):
    if command == "remove" and location == "end":
        return ls.pop()
    elif command == "remove" and location == "beginning":
        return ls.pop(0)
    elif command == "add" and location == "beginning":
        ls.insert(0, value)
        return ls
    elif command == "add" and location == "end":
        ls.append(value)
        return ls

print(list_manipulation([1,2,3], "remove", "end"))
print(list_manipulation([1,2,3], "remove", "beginning"))
print(list_manipulation([1,2,3], "add", "beginning", 20))
print(list_manipulation([1,2,3], "add", "end", 30))
