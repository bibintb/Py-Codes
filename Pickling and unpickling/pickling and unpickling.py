# pickling and unpickling
import pickle
numbers = [1,2,3,4,5,6,7,8,9]
filename = '/home/shad/Documents/file.txt'
f1 = open(filename, 'wb')
pickle.dump(numbers, f1)
f1.close()

filename = '/home/shad/Documents/file.txt'
f2 = open(filename, 'rb')
new_list = pickle.load(f2)
print(new_list)
print(new_list==numbers)


