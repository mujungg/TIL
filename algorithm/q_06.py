from builtins import str


class Solution:
    def my_solution(self, s: str) -> str:
        strs = []
        # 숫자+알파벳 리스트로 변환
        for char in s:
            if char.isalnum():
                strs.append(char)

        print('strs: ', strs)   ##

        for length in range(len(strs),0,-1): # 가장 긴 팰린드롬부터 검증
            print('length: ', length)   ##

            for i in range(len(strs)):  # 시작점을 한칸씩 옮겨가며 팰린드롬 찾기
                print('시작인덱스: ', i) ##
                if i+length > len(strs):    # 범위 벗어나면 끝
                    break
                # pop() 호출 시 기존 strs의 변형을 막고자 임시 리스트를 선언
                # 시작점 + 길이를 슬라이싱 해서 검증하려는 리스트를 따로 떼어옴
                is_palindrom = True
                temp_strs = strs[i:i+length]
                print('이번 루프에서 다루는 리스트 범위: ', temp_strs)    ##

                for j in temp_strs:
                    if j != temp_strs.pop():
                        is_palindrom = False
                        break
                if is_palindrom:
                    return ''.join(strs[i:i+length])
    # Time Limit Exceeded


    def solution_01(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''

        for i in range(len(s) - 1):
            result = max(result,
                         expand(i, i + 1),
                         expand(i, i + 2),
                         key=len)
        return result
    """
    모두 다른 값이 입력으로 들어오면 가장 긴 팰린드롬의 길이가 1이다.(ex: "abcdefg") 이 경우 문자 하나를 리턴해주는데, 
    이 알고리즘의 경우 s[0]을 건너뛰고 s[1]을 리턴해주게됨. 상관은 없지만 만약 문제에서 팰린드롬의 길이가 1인 경우
    s[0]을 리턴하라고 지시할 수도 있으니 그때는 expand()에서 따로 처리해줘야될듯.    
    """ew
c = Solution()
print(c.solution_01(str))

