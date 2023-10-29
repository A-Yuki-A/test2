# 10進数から2進数への変換
def decimal_to_binary(n):
    return bin(n).replace("0b", "")

# 2進数から10進数への変換
def binary_to_decimal(n):
    return int(n, 2)

# テスト
decimal_number = 42
binary_number = "101010"
converted_to_binary = decimal_to_binary(decimal_number)
converted_to_decimal = binary_to_decimal(binary_number)

print(f"10進数 {decimal_number} は2進数 {converted_to_binary} に変換されます。")
print(f"2進数 {binary_number} は10進数 {converted_to_decimal} に変換されます。")
