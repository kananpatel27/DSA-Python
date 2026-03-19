arr = list(map(int, input("Enter array elements (space-separated): ").split()))

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

max_count = 0
max_element = None

for key in freq:
    if freq[key] > max_count:
        max_count = freq[key]
        max_element = key

print("Element with highest frequency:", max_element)
print("Frequency:", max_count)