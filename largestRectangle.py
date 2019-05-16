def largestrectangle(height):

    # given a histogram [], find the largest rectangle.
    # rectangle can be large area cover across the histogram

    # iterate through the array when array is not empty and current array is larger or equal to previous array

    height.append(0)
    stack = [-1]
    ans = 0
    for i in range(len(height)):
        print('i:{}'.format(i))
        print('stack: {}'.format(stack))
        while height[i] < height[stack[-1]]:
            h = height[stack[-1]]
            stack.pop()
            w = i - stack[-1] -1
            ans = max(ans, h*w)

        stack.append(i)

    return ans




if __name__ == '__main__':

    his = [1,2,6,8,5,3,1,2,3,4]
    print('largestrectangle(his):{}'.format(largestrectangle(his)))

