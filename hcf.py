def find_hcf(a, b):
    hcf = 1
    smaller = min(a, b)
    for i in range(1, smaller + 1):
        if a % i == 0 and b % i == 0:
            hcf = i
    return hcf

# Reading input from the user
input_str = input()
a, b = map(int, input_str.split())

# Calculate HCF
hcf_result = find_hcf(a, b)

# Output the result
print(hcf_result)
