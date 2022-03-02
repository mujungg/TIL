## typescript를 사용하는 이유

1. 런타임 에러 방지  
2. 코드 하이라이트 및 자동완성 (intellisense)  

vscode는 typescript의 intellisense를 훌륭하게 지원한다. js는 타입의 불확실성 때문에 자동완성이 안되는 경우가 있다. 
```javascript
function sum(a, b) {
    return a + b;
}

let total = sum(10,20);
total.toLocalString();
```
위 코드에서 total은 정수이므로 toLocalString()메소드를 사용할 수 있다. 하지만 js는 sum() 함수가 항상 정수형을 리턴한다는 보장이 없으므로 자동완성을 섣불리 수행하지 않는다.

## TypeScript 설치
정확히 말하자면 타입스크립트 컴파일러를 설치한다.   
준비물: node.js  
```
// global로 설치
npm install -g typescript
```
(npm은 node.js의 명령어. 파이썬의 pip와 비슷한데 pip는 패키지의 설치를 담당하는 반면 npm은 설치뿐 아니라 전반적인 관리를 담당한다.)
```
tsc -v
```
위 명령어를 통해 정상적으로 설치가 되었나 확인한다.

## tsc
타입스크립트 컴파일러는 ts파일을 js파일로 컴파일해준다. 결국 ts는 개발 편의를 위한 눈속임이라고 볼 수 있고 실제로는 js가 동작한다. 
```
tsc filename.ts
```
위 명령어를 실행하면 동명의 js파일이 생성된다. js파일은 node를 이용해 실행한다.
```
node filename.js
```

## tsconfig
tsconfig.json의 역할  
1. vscode의 intellisense 커스텀    
2. tsc의 컴파일 방식 제어

반드시 프로젝트의 루트 디렉토리에 위치해야 한다. </br></br>
tsconfig.json에서 다룰 수 있는 속성은 광범위하기 때문에 나중에 다시 자세히 공부하자. 또한 이를 손쉽게 설정할 수 있는 기능이 리액트에 있다고 한다. (Spring Boot같은...?) 아무튼 이런게 있구나 정도만 알고 넘어가자!
