def read_input_file(filename):
    left_list = []
    right_list = []
    with open(filename, 'r') as file:
        for line in file:
            # splits line into two numbers
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    return left_list, right_list


filename = "input.txt"

left_list, right_list = read_input_file(filename)

similarity_score = 0
for num in left_list:
    count_in_right = right_list.count(num)  # counts occurrences in the right list
    similarity_score += num * count_in_right

print("Total similarity score:", similarity_score)
