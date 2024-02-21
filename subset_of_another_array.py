def subset_of_another_array(a1,a2):
#subset of another array
    for i in a2:
        if i in a1:
            a1.remove(i)
        else:
            return 'No'
    return 'Yes'