# Split array problem

# In a given integer array A, we must move every element of A to either list B or list C. (B and C
# initially start empty.)
# Return true if and only if after such a move, it is possible that the average value of B is equal to
# the average value of C, and B and C are both non-empty.

# Sample input:
# [1,2,3,4,5,6,7,8]
# Sample output:
# True

# Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have the average
# of 4.5.
# Note:
# The length of A will be in the range [1, 30].
# A[i] will be in the range of [0, 10000].



def split_array_equal_average(array):
    # Special case: if the length of the array is 1, we can't split it into two non-empty lists
    if len(array) == 1:
        return False
    
    total_sum = sum(array)
    len_array = len(array)
    
    # Create a set to store all possible sums that can be made using the first i elements
    # of the array to form a sublist of size j
    list_with_sums = [set() for j in range(len_array // 2 + 1)]
    list_with_sums[0].add(0)
    
    # Loop through each element of the array and update the list_with_sums set for each possible sublist size
    for number in array:
        for i in range(len_array // 2, 0, -1):
            for j in list_with_sums[i - 1]:
                list_with_sums[i].add(j + number)
    
    # Loop through each possible sublist size and check if there is a sum that can form
    # a sublist of that size with an average equal to the overall average
    for i in range(1, len_array // 2 + 1):
        if total_sum * i % len_array == 0 and total_sum * i // len_array in list_with_sums[i]:
            return True
    
    return False


def read_array():
    print("enter the elements of the array and type 'exit' when you are done the length of the array\
          must be between 1 and 30 and the introduced values between 0 and 10 000 including the mentioned values")

    option = ""
    array = []

    while not option == "exit" :
        option = input(">")
        if not option.isdecimal():
            if option != "exit":
                print ("your input won t be considered. it s not an integer or the 'exit' option")
        else:
            array.append(int(option)) 
            
 
    return array


def start():

    array = read_array()
    possible  = split_array_equal_average(array)
    print( possible)



start()






