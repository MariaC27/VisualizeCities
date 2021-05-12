# Author: Maria Cristoforo
# Date: November 4, 2020
# Purpose: the functions for Quicksort


# main compare function that takes another function as a parameter
def compare_func(compare_f, x, y):
    if compare_f(x, y):
        return True
        # x is less than y
    else:
        return False
        # x is not less than y


# these two compare functions are just for testing quicksort
# - won't actually be used in sort_cities
def compare_nums(a, b):
    return a < b

def compare_strings(a, b):
    return a.lower() < b.lower()


# these comparison functions used in sort_cities
def compare_city_population(c1, c2):
    return c2.population < c1.population
    # do c2 less c1 so that cities are printed out in order
    # of largest to smallest population

def compare_city_name(c1, c2):
    return c1.name.lower() < c2.name.lower()

def compare_city_latitude(c1, c2):
    return c1.lat < c2.lat


# partitions sublist and returns the index where pivot is placed
def partition(the_list, p, r, compare_func):
    i = p-1
    j = p
    pivot = the_list[r]  #the chosen pivot is always the last element of the list

    while j < r:  # loops stops the second j = r
        if compare_func(pivot, the_list[j]):
            j = j + 1
        else:
            i = i + 1
            the_list[j], the_list[i] = the_list[i], the_list[j] #swap
            j = j + 1

    the_list[i + 1], the_list[r] = the_list[r], the_list[i + 1]
    #swap to get pivot in the right place
    return i + 1


#code to test out the partition function
# mlist = [5, 2, 7, 10, 3, 33, 2, 1, 9, 0, 5]
# id = partition(mlist, 0, len(mlist)-1, compare_nums)
# print("index of pivot:", id)
# print("tested out partition:", mlist)



def quicksort(the_list, p, r, compare_func):

    if (r-p) < 2:
        return
        # base case

    q = partition(the_list, p, r, compare_func)
    quicksort(the_list, p, q-1, compare_func)
    quicksort(the_list, q, r, compare_func)



def sort(the_list, compare_func):
    quicksort(the_list, 0, len(the_list)-1, compare_func)


# code to test out quicksort
# mlist = [5, 0, 7, 10, 3, 33, 2, 1, 9, 1, 5]
# sort(mlist, compare_nums)
# print("sorted:", mlist)



