
num = int(input("Num: "))

a, b = 0, 1

print(f"{a} {b}", end="")
for i in range(num):
    if i >= 2:
        print(f" {a + b}", end="")
        a, b = b, a + b 
print()

    
    
