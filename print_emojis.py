#print(U0001f600)
for s in range(1,11):
    print('#' * s)

s = 1
while s < 11:
    print('#' * s)
    s += 1

for t in range(1, 22, 2):
    spaces = int((21 - t) / 2)
    spacer = " " * spaces
    print(spacer + ("#" * t))
