# Find mean, median, mode for the given set of numbers in a list.

# import statistics

data = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 8, 9, 10]
my_mean = sum(data) / len(data)
sorted_data = sorted(data)
n = len(sorted_data)
if n % 2 == 1:
    my_median = sorted_data[len(sorted_data) // 2]
else:
    my_median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
mode = {}
for i in data:
    mode[i] = data.count(i)
my_mode = list(mode.keys())[list(mode.values()).index(max(mode.values()))]

# my_mean = statistics.mean(data)
# my_median = statistics.median(data)
# my_mode = statistics.mode(data)

print("Mean:", my_mean)
print("Median:", my_median)
print("Mode:", my_mode)
