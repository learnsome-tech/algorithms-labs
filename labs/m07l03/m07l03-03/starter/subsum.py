nodes = 0

def sub_pruned(nums, target, i=0, cur=0):
    global nodes
    nodes += 1
    if cur == target: return True
    if cur > target or i == len(nums): return False
    return (sub_pruned(nums, target, i+1, cur+nums[i]) or
            sub_pruned(nums, target, i+1, cur))

def sub_noprun(nums, target, i=0, cur=0):
    global nodes
    nodes += 1
    if i == len(nums): return cur == target
    return (sub_noprun(nums, target, i+1, cur+nums[i]) or
            sub_noprun(nums, target, i+1, cur))

nums, target = [10, 20, 30, 40, 50], 15
nodes = 0; sub_pruned(nums, target); pn = nodes
nodes = 0; sub_noprun(nums, target); un = nodes
print('pruned nodes:', pn)
print('unpruned nodes:', un)
