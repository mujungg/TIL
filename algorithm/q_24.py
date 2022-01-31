class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        #output이 없으면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return self.input == [] and self.output == []
        '''
        A and B
        - A,B 둘 다 참이면 B 를 출력
        - A,B 둘 다 거짓이면 A 를 출력
        - A, B 둘 중에 하나만 참이면 거짓인 값을 출력
        '''
