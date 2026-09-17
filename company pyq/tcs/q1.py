# you are given a word in which the letters are only lower case.you need to remove one letter from the word such it makes the count of each letter is same.
# eg:yummy
# on removing u we get 2 y and 2 m which makes it true.

from collections import Counter
def solve(s):
    cnt = Counter(s)

    for k in cnt:
        cnt[k] -= 1
        lst=[v for v in cnt.values() if v>0]
        if len(set(lst)) == 1:
            return True
        cnt[k] += 1
    return False

def main():
    s="yummy"
    print(solve(s))
main()