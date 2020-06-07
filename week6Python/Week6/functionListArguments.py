

''' Your solution goes here '''
def swap(value):
    intermediare_value = value[0]
    value[0] = value[len(value) - 1]
    value[len(value) - 1] = intermediare_value
values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
swap(values_list)

print(values_list)