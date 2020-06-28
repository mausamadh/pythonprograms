'''

Write a Python program to sum all the items in a list.
'''
given_list = [1,2,3,4,5,6,7,8,9]
another_list = ["akabar",'rajesh','Hisenberg']

def sum_list(summ_all_my_items):
    return sum(summ_all_my_items)
print(sum_list(given_list))
#print(sum_list(another_list)) #sum  function doesnot operate on strings 

print(" ".join(another_list)) # for strings we use join method as it concatinates(join) strings 