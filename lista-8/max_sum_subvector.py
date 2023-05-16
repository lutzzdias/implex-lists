from sys import argv


def max_sum(array, start, end):
    if start == end:
        return start, end, array[start]
    else:
        middle = (start + end) // 2
        left_start, left_end, left_sum = max_sum(array, start, middle)
        right_start, right_end, right_sum = max_sum(array, middle+1, end)
        mid_start, mid_end, mid_sum = max_cross_sum(array, start, middle, end)
        if left_sum > right_sum and left_sum > mid_sum:
            return left_start, left_end, left_sum
        elif right_sum > left_sum and right_sum > mid_sum:
            return right_start, right_end, right_sum
        else:
            return mid_start, mid_end, mid_sum


def max_cross_sum(array, start, middle, end):
    left_sum = float('-inf')
    left_max_index = -1
    sum = 0
    for i in range(middle, start, -1):
        sum += array[i]
        if sum > left_sum:
            left_sum = sum
            left_max_index = i

    right_sum = float('-inf')
    right_max_index = -1
    sum = 0
    for i in range(middle + 1, end, 1):
        sum += array[i]
        if sum > right_sum:
            right_sum = sum
            right_max_index = i

    return left_max_index, right_max_index, left_sum + right_sum


def main():
    file = open(argv[1], 'r')
    output_file = open(argv[1].replace('.txt', '.out'), 'w')

    n = int(file.readline().rstrip())

    for i in range(n):
        array_length = int(file.readline().rstrip())
        array = list(map(int, file.readline().split()))

        # calculate max sum
        _, _, sum = max_sum(array, 0, array_length-1)

        # write to output file
        if i == n - 1:
            output_file.write(f'{sum}')
        else:
            output_file.write(f'{sum}\n')

    file.close()
    output_file.close()


main()
