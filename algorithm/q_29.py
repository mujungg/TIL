class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0
        for stone in stones:
            if stone in jewels:
                cnt += 1
        return cnt
    # in list를 통해 cnt를 늘려가는 방식
    def sulution_01(self, jewels: str, stones: str) -> int:
        freqs = {}
        count = 0

        # stone의 빈도 계산
        for char in stones:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1

        # jewels의 빈도수 합산
        for char in jewels:
            if char in freqs:
                count += freqs[char]

        return count
    '''
    해시테이블 이용. 이게 훨 빠름.
    왜냐하면 a in list는 하나하나 비교해가는 방식이라 O(n)의 복잡도임.
    하지만 a in dict는 해시함수를 이용함.
    입력받은 키값을 해시값으로 바꿔 인덱스처럼 이용하는데
    이때 해당 해시값에 연결된 값이 없으면 false임.
    그래서 연산을 한번만 하면 됨. 고로 O(1)
    '''

    def soultion_02(self, jewels: str, stones: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0

        for char in stones:
            freqs[char] += 1

        for char in jewels:
            count += freqs[char]

        return count

    def soultion_03(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(stones)
        count = 0

        for char in jewels:
            count += freqs[char]

        return count