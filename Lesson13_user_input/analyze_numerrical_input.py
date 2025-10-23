
#adding a change so I can commit something to a new branch

numbers = input("Enter a series of numbers separated by spaces for analysis")

number_list = [int(num) for num in numbers.split()]
sums_numbers = sum(map(float, numbers.split()))
#sums_numbers = sum(number_list)
total_numbers = len(number_list)

#average_number = sums_numbers/total_numbers
average_number = round(sums_numbers / total_numbers, 2)
# my solution for calculating frequency of each number, less code, and it still worked except for telling how many times the number appears
#def number_frequency(number_list):
   #return max(number_list, key=number_list.count)


 #Class solution -Calculate the frequency of each number
number_frequency = {}

for number in number_list:
    if number not in number_frequency:
        number_frequency[number] = 1
    else:
        number_frequency[number] += 1

def minmax(number_list):
    min_val = min(number_list)
    max_val = max(number_list)

    return (max_val - min_val)
#added from class solution
most_frequent_number = max(number_frequency, key=number_frequency.get)

print("Number Analysis Results:")
#formatting to separate title from the results
print("-" * 25)
total_numbers = len(number_list)
print(f"Total Numbers: {total_numbers}")
print(f"Sum of Numbers: {sums_numbers}")
#print(f"Most Frequent Numbers: {number_frequency(number_list)}")
print(f"Most Frequent Number: {most_frequent_number} (appears {number_frequency[most_frequent_number]} times)")
print(f"Range of Numbers: {minmax(number_list)}")
print(f"Average Number: {average_number}")