# You are given two integers a and b.
# Start with x = 0.
# In every iteration, add a to x.
# After each addition, calculate:
# x // b
# Check whether the quotient is exactly 1.
# Continue doing this until the condition becomes true.

# Example 1
# a = 3
# b = 5
# x = 0
#
# Iterations:
#
# x = 0 + 3 = 3
# 3 // 5 = 0   ❌
#
# x = 3 + 3 = 6
# 6 // 5 = 1   ✅
#
# So the answer is reached when x = 6.
# It takes 2 iterations (answer=2)
#
# Example 2
# a = 4
# b = 10
# x = 0
# x = 4
# 4 // 10 = 0  ❌
#
# x = 8
# 8 // 10 = 0  ❌
#
# x = 12
# 12 // 10 = 1 ✅
#
# So here, it takes 3 additions.
# answer = 3

def solve(a,b,x):
    count=0
    while(True):
        x = x + a
        count+=1
        if x // b == 1:
            return count

if __name__ == '__main__':
    a,b,x = 4,10,0
    print(solve(a,b,x))