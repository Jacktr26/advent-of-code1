with open('input.txt', 'r') as file:
    lines = file.readlines()
total_dist = 0
for line in lines:

    line = line.strip()
    left = line[:5].strip()
    right = line[8:].strip()

    # only numbers used
    left_nums = [int(char) for char in left if char.isdigit()]
    right_nums = [int(char) for char in right if char.isdigit()]

    iteration = 0

    # Calculate the distance and remove smallest number
    while left_nums and right_nums:  # Make sure both lists aren't empty
        iteration += 1

        dist = 0
        if min(left_nums) - min(right_nums) < 0:
            dist += min(right_nums) - min(left_nums)
            left_nums.remove(min(left_nums))
            right_nums.remove(min(right_nums))
        else:
            dist += min(left_nums) - min(right_nums)
            left_nums.remove(min(left_nums))
            right_nums.remove(min(right_nums))

        # print every 5th output as this is the total distance
        if iteration % 5 == 0:
            total_dist += dist
            print(dist)

print(f"your total distance is {total_dist}")
