class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if stack:  # stack이 비어있지 않을 때
                '''
                stack의 마지막 원소와 s에서 가져온 bracket이
                짝을 이루면 stack.pop(), 짝이 아니면 
                append(bracket)
                '''
                if stack[-1] == '[':
                    if bracket == ']':
                        stack.pop()
                    else:
                        stack.append(bracket)
                elif stack[-1] == '(':
                    if bracket == ')':
                        stack.pop()
                    else:
                        stack.append(bracket)
                elif stack[-1] == '{':
                    if bracket == '}':
                        stack.pop()
                    else:
                        stack.append(bracket)
            else:  # stack이 비어있을 때
                stack.append(bracket)

        if stack:
            return False
        else:
            return True

    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            '''
            table의 키는 다 '닫힌' 괄호임.
            char가 table에 없다는 소리는 '열린' 괄호라는 소리.
            그럼 stack에 넣어줌.
            반대로 char가 table에 있다는 것은 '닫힌' 괄호라는 소리.
            그럼 stack.pop()과 table(char)를 비교.
            '''
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
            '''
            not stack일때 False인 이유:
            elif의 조건문이 실행됐다는 것은 char가 닫힌 괄호라는 뜻.
            그런데 stack이 비어있으면 짝이 없다는 소리.
            
            table[char] != stack.pop()일때 False인 이유:
            char은 닫힌 괄호이므로 table의 key로 사용 가능.
            char를 키로 한 table[key]는 알맞은 짝을 리턴.
            그 알맞은 짝과 stack.pop()이 다르면 당연히 False.
            '''
            return len(stack) == 0
    # 훨씬 빠름