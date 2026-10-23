'''this can be two pointer or prefix suffix problem 
if the quesition is about find the bounded area or shape of the region'''

def trap(height):
    left=0
    right=len(height)-1
    left_max=0
    right_max=0
    water=0
    while left<right:
        if height[left]<height[right]:
            left_max=max(left_max,left[height])
            water+=(left_max-left[height])
            left+=1
        else:
            right_max=max(right_max,height[right],)
            water-=right_max-height[right]
            right-=1
        return water 
    print(trap([2,3,-2]))
