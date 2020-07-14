for x in [1,2,3,4]:
    if x==3:
        break
    print(x)

for y in "hello world":
    print(y)
    print(y.upper())

for x in ["usa","canada","india"]:
        if x =="usa":
            continue
        print(x)

for x in range(2,10,3):
    print(x)

# build exponential logic

def power_number(base_num,pow_num):
    result = 1
    for index in range(pow_num):
        result= result * base_num
    return result

print(power_number(3, 4))
