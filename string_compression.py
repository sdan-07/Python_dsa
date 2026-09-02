from collections import Counter

def compress(strs):
    ans=""
    counts = Counter(strs)

    for k,v in counts.items():
        ans += k + str(v)
    return ans

if __name__ == '__main__':
    strs = "aaabccccdd"
    print(compress(strs))