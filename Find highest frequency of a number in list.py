arr = [1, 2, 2, 3, 3, 3, 4, 2, 3]

max_count = 0
max_element = arr[0]

for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1

    if count > max_count:
        max_count = count
        max_element = arr[i]

print("Element with highest frequency:", max_element)
print("Frequency:", max_count)
