#!/usr/bin/env python
#-*- coding:utf-8 -*-

def quick_sort(lists,left,right):
    """
    Quick Sort
    """
    length = len(lists)
    if length == 0 or left > right:
        return lists
    j = left

    for i in range(left,right):
        if lists[i] < lists[right]:
            lists[i],lists[j] = lists[j],lists[i]
            j = j+1

    lists[j],lists[right] = lists[right],lists[j]

    if left < j-1:
        quick_sort(lists,left,j-1)
    if right > j+1:
        quick_sort(lists,j+1,right)

    return lists

def insert_sort(lists):
    """
    Insert Sort
    """
    length = len(lists)
    if length == 0:
        return lists
    for i in range(1,length):
        j = i-1
        key = lists[i]
        while j>=0 and lists[j]>key:
            lists[j+1] = lists[j]
            lists[j] = key
            j = j-1

    return lists

def shell_sort(lists):
    """
    Shell Sort
    """
    length = len(lists)
    if length == 0:
        return lists
    dist = length//2
    while dist>=1:
        for i in range(dist,length):
            j = i-1
            key = lists[i]
            while j>=0 and lists[j]>key:
                lists[j+1] = lists[j]
                lists[j] = key
                j = j-1
       
        dist = dist//2

    return lists
    
def bubble_sort(lists):
    """
    Bubble Sort
    """
    length = len(lists)
    if length == 0:
        return lists
    for i in range(length-1):
        for j in range(1,length-i):
            if lists[j]<lists[j-1]:
                lists[j],lists[j-1] = lists[j-1],lists[j]

    return lists

def select_sort(lists):
    """
    Selection Sort
    """
    length = len(lists)
    if length == 0:
        return lists
    for i in range(length):
        minIndex = i
        for j in range(i,length):
            if lists[j]<lists[minIndex]:
                minIndex = j
        lists[i],lists[minIndex] = lists[minIndex],lists[i]

    return lists

if __name__ == "__main__":
    lists = [23,4,1,45,2,56,25,76,25,68,45,16]
    print(quick_sort(lists,0,(len(lists)-1)))
    lists = [23,4,1,45,2,56,25,76,25,68,45,16]
    print(insert_sort(lists))
    lists = [23,4,1,45,2,56,25,76,25,68,45,16]
    print(shell_sort(lists))
    lists = [23,4,1,45,2,56,25,76,25,68,45,16]
    print(bubble_sort(lists))
    lists = [23,4,1,45,2,56,25,76,25,68,45,16]
    print(select_sort(lists))
