# postgresql  설치, psql, 서버접속, db불러오기

## 설치하고 접속까지

https://dora-guide.com/postgresql-install/

## 환경변수 설정

psql.exe파일이 있는 경로를 path에 추가하면 윈도우 명령프롬프트에서  postgresql을 사용할 수 있다. 내 경우엔 C:\Program Files\PostgreSQL\10\bin

http://www.devkuma.com/books/pages/1426

## 데이터베이스 생성

```sql
CREATE DATABASE db_name
```

## psql 명령어 모음

https://browndwarf.tistory.com/51

## db 불러오기

먼저 bin 파일로 이동한다.

```
C:\Program Files\PostgreSQL\10\bin
```

pg_restore 를 이용해 원하는 .tar 파일을 연다. 

```
pg_restore -U postgres -d (dbname) (.tar파일 경로)
```

이후 비밀번호를 입력하면 완료.

```
Password:
```



