# postgresql SELECT, column alias

## 기본 형태

(1) 컬럼 하나만 불러오기

```sql
SELECT column_list1 FROM table_name;
```

(2) 컬럼 여러개 불러오기

```sql
SELECT
	column1,
	column2,
	...
FROM
	table_name;
```

## asterisk(*)

```sql
SELECT * FROM table_name;
```

asterisk(*)는 모든 컬럼은 불러온다. 비효율을 유발하므로 가급적 사용하지 않고 필요한 컬럼들을 특정해주는 것이 좋다.

##  표현식

SELECT에서 연산자같은 표현식을 사용할 수 있다.

ex)

```sql
SELECT 
	first_name || ' ' || last_name,
FROM 
	customer;
```

## 컬럼에 별명 붙이기 - column alias

```sql
SELECT
	old_name AS new_name
FROM
	table_name;
```

기존의 컬럼명(old_name)을 원하는 이름( new_name)으로 바꿀 수 있다. 다만 db의 상태가 변하지는 않고 해당 쿼리가 실행되는 동안만 유효하다.

