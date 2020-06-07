
index = 1
weight = ""
list_weights = []
for index in range(1, 5):
    weight = input(f"Enter weight {index}:\n")
    list_weights.append(float(weight))
print(f"Weights: {list_weights}\n")

sum_weight = 0
for index in list_weights:
    sum_weight += index
average_weight = sum_weight / len(list_weights)
print("Average weight: %.2f" %average_weight)
print("Max weight: %.2f\n" %max(list_weights))

index_list = int(input("Enter a list index (1 - 4):\n"))
print("Weight in pounds: %.2f" %list_weights[index_list - 1])
print("Weight in kilograms: %.2f\n" %(list_weights[index_list - 1] / 2.2))

sorted_list_weights = sorted(list_weights)
print(f"Sorted list: {sorted_list_weights}")

