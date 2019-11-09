def calcu_subsets(objs:list)->list:
    subsets = [[]]  # store subsets
    for obj in objs:
        new_subset_pool = [] # store new subset 
        for old_subset in subsets:
            new_subset = old_subset.copy()
            new_subset.append(obj)
            new_subset_pool.append(new_subset)
        subsets.extend(new_subset_pool)
    return subsets
# ---- calculate subsets ---- #
n = 5
nums = [num for num in range(1,n+1)]
result = calcu_subsets(nums)
print(len(result))  # 2^n
print(result)
