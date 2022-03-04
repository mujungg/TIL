# ORDER BY
## ORDER BY
SELECT로 받아온 결과물을 원하는 기준에 따라 정렬할 수 있다. 이때 사용하는 것이 ORDER BY이다. 문법은 다음과 같다.
```sql
SELECT 
    select_list
FROM
    table_name
ORDER BY
    sort_expression1 [ASC | DESC],
    ...
    sort_expression2 [ASC | DESC];
```
* ASC(default) : ascending order(오름차순)  
DESC : descending order(내림차순)
* `FROM` -> `SELECT` -> `ORDER BY` 순으로 평가한다.
* 정렬 컬럼을 여러개로 지정한 경우, 앞에 오는 컬럼부터 평가한다. 중복이 있을 경우 뒤에 오는 컬럼을 다시 평가한다.

## NULL
정렬 기준 컬럼에 NULL값이 포함될 경우 NULL을 앞에 정렬할지, 뒤에 정렬할지 결정해주는 키워드가 NULLS FIRST, NULLS LAST이다.
* ASC(오름차순): NULLS LAST가 디폴트
* DESC(내림차순): NULLS FIRST가 디폴트
