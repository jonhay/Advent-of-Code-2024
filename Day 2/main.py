# Solution for https://adventofcode.com/2024/day/2
# By Jon Hay

# Setup variables to hold our counts
safe_count = 0
unsafe_count = 0


# Open file and read data
with open('Day 2/data') as f:    data = [i.strip() for i in f.readlines()]

#print(data)

for index in range(0,len(data)):
    entry = data[index].split(" ")
    safe = True
    direction = "Flat"
    prior_direction = "Flat"
    for reading in range(0,len(entry)-1):
        first_num = int(entry[reading])
        second_num = int(entry[reading+1])
        if first_num > second_num:
            prior_direction = direction
            direction = "Down"
        if first_num < second_num:
            prior_direction = direction
            direction = "Up"
        if first_num == second_num:
            prior_direction = direction
            direction = "Flat"
        if direction is "Up":
            change_from_prior = second_num - first_num
        if direction is "Down":
            change_from_prior = first_num - second_num
        if abs(change_from_prior > 3):
            prior_direction = direction
            safe = False
        if reading >= 1 and direction is not prior_direction:
            safe = False
    #print(str(entry) + " safe: " + str(safe))
    if safe:
        safe_count += 1
    if not safe:
        unsafe_count += 1

print("Safe Count: " + str(safe_count))
