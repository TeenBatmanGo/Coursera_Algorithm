
import base


def create_hashtable(nums):
    hashtable = {}
    for num in nums:
        hashtable[num] = True
    return hashtable


def twosum(hashtable, target):
    for num in hashtable.keys():
        if target-num in hashtable and target-num != num:
            return True


if __name__ == '__main__':
    testcase = [-3, -1, 1, 2, 9, 11, 7, 6, 2]

    data = base.load_2sum()
    hash_table = create_hashtable(data)
    cnt = 0
    for i in range(-10000, 10001):
        if twosum(hash_table, i):
            cnt += 1
            print(i)
    print('\nTotal count is', cnt)