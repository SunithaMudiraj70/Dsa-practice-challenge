def max_product_brute(nums):
    best = nums[0]

    for i in range(len(nums)):
        product = 1

        for j in range(i, len(nums)):
            product *= nums[j]
            best = max(best, product)

    return best
if __name__=="__main__":
    nums=[-2,3,-4]
    print(max_product_brute(nums))
'''
def max_product(nums):
    best = nums[0]
    cur_max = nums[0]
    cur_min = nums[0]

    for x in nums[1:]:
        old_max = cur_max
        old_min = cur_min

        cur_max = max(x, old_max * x, old_min * x)
        cur_min = min(x, old_max * x, old_min * x)

        best = max(best, cur_max)

    return best


print(max_product([-2, 3, -4]))  # 24'''
    