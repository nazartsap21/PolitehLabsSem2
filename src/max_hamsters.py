def max_hamsters(s: int, c: int, hamsters: list[list]) -> int:
    high = c - 1
    low = 0
    counted_hamsters = [0] * c
    while True:
        if high == low:
            mid = high
        else:
            mid = int((high + low) / 2)
        temp_array = sorted([x[0] + x[1] * mid for x in hamsters])
        if sum(temp_array[:mid+1]) == s:
            result = mid + 1
            break
        elif sum(temp_array[:mid+1]) > s:
            high = mid - 1
            counted_hamsters[mid] = sum(temp_array[:mid+1])
        elif sum(temp_array[:mid+1]) < s:
            low = mid + 1
            counted_hamsters[mid] = sum(temp_array[:mid+1])
            if counted_hamsters[mid + 1] > s:
                result = mid + 1
                break

    return result
