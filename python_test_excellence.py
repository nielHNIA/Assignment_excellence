"""Question1
Use python lists and make an list of numbers.
Write a function which returns sum of the list of numbers"""


def sum_of_list(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

""""Question2"""

def greater_than_rest(dict1):
    dict2 = {}
    max_key = 'a'
    max_value = 0
    for key, value in dict1.items():
        if value >= max_value:
            max_key = key
            max_value = value
    dict2[max_key] = max_value
    return dict2
            
"""Question 3"""
def max_consecutive_ones(lst):
    max = 0
    count = 0
    for i in range(len(lst)):
        if lst[i] != 1:
            count = 0
        else:
            count += 1
            if count > max:
                max = count

    return max
        

        
      
            


print(sum_of_list([1,2,3,4,5]))
print(greater_than_rest({
   "1" : 50,
   "2" : 60,
   "3" : 70
}
))
print(max_consecutive_ones([0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]))
