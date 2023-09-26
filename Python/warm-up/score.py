"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains n. The second line contains an array A  of n  integers each separated by a space.


"""
#the competitor that does not win first place in a contest. especially : one that finishes in second place is runner-up score

n = int(input())
arr = map(int, input().split())  #2 3 6 6 5
    
new_arr_set = set(arr)
new_arr_list = list(new_arr_set)
new_arr_list.sort()
print(new_arr_list[-2]) 