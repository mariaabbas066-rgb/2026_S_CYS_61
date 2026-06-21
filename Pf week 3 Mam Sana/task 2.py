find_max = lambda x, y: x if x > y else y


def table_print(num, range_limit):
    for i in range(1, range_limit + 1):
        print(num, "x", i, "=", num * i)

num1 = int(input("first number: "))
num2 = int(input("second number: "))
limit = int(input("Table kahan tak chahiye? "))

bada_num = find_max(num1, num2)
print("Bada number hai:", bada_num)
print("--- Table ---")
table_print(bada_num, limit)