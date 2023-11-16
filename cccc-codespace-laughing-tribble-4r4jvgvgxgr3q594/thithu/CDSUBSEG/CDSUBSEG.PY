def find_largest_divisible_subarray(arr):
    def find_common_divisor(n):
        for i in range(2, n + 1):
            if n % i == 0:
                return i
        return 1

    max_subarray_start = -1
    max_subarray_end = -1

    for i in range(len(arr)):
        common_divisor = find_common_divisor(arr[i])
        if common_divisor > 1:
            subarray_start = i
            subarray_end = i
            while subarray_end + 1 < len(arr) and arr[subarray_end + 1] % common_divisor == 0:
                subarray_end += 1

            if subarray_end - subarray_start > max_subarray_end - max_subarray_start:
                max_subarray_start = subarray_start
                max_subarray_end = subarray_end

    if max_subarray_start == -1:
        return -1
    else:
        return max_subarray_end - max_subarray_start + 1

# Example usage:
arr = [2,6,12,15,27,1,81,5]
result = find_largest_divisible_subarray(arr)
print(result)
