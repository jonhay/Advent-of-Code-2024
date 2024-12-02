# Solution for https://adventofcode.com/2024/day/1
# By Jon Hay

# Setup arrays to hold our two lists
list_1 = []
list_2 = []
distance_list = []
similarity_list = []

# Open file and read data
with open('Day 1/data') as f:    data = [i.strip() for i in f.readlines()]

#print(data)

for index in range(0,len(data)):
    entry = data[index].split("   ")
    list_1.append(int(entry[0]))
    list_2.append(int(entry[1]))


# Part 1 Code:

list_1.sort()
list_2.sort()

for index in range(0,len(list_1)):
    num_1 = list_1[index]
    num_2 = list_2[index]
    if(num_1 > num_2):
        distance_list.append(num_1 - num_2)
    else:
        distance_list.append(num_2 - num_1)

print("Distance Sum: " + str(sum(distance_list)))

# Part 2 Code:

for index in range(0,len(list_1)):
    count_of_num = list_2.count(list_1[index])
    similarity_list.append(list_1[index]*count_of_num)

print("Similarty Sum: " + str(sum(similarity_list)))