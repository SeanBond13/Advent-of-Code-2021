inputfile = 'C:\Scripts\_python\Advent of Code 2021\Day_01\day_01_input.txt'
with open(inputfile,'r') as infile:
    depths = [(int(line)) for line in infile]

index = 0
count = 0
for depth in range(0,(len(depths)-1)):
    if depths[index] - depths[index + 1] > 0:
        print(f'{depths[index]} -> {depths[index + 1]} is decreasing')
    elif depths[index] - depths[index + 1] < 0:
        print(f'{depths[index]} -> {depths[index + 1]} is increasing')
        count = count + 1
    index = index + 1
print(f'{count} depths are increasing')