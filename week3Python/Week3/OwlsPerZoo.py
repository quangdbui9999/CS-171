avg_owls = 0.0

num_owls_zooA = int(input())
num_owls_zooB = int(input())
num_owls_zooC = int(input())
num_zoos = int(input())

''' Your solution goes here '''
avg_owls = (num_owls_zooA + num_owls_zooB + num_owls_zooC) / num_zoos
print('Average owls per zoo:', int(avg_owls))