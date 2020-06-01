CREATE DATABASE xuan_test_db;

USE xuan_test_db;

-- List available tables (excludes views)
SELECT * FROM xuan_test_db.INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE';

----------------------------------------------------------------

CREATE TABLE dept(
	ID INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,
	NAME VARCHAR(40)
);

DROP TABLE dept;

SELECT * FROM dbo.dept;

INSERT INTO dbo.dept values('Computer Science');
INSERT INTO dbo.dept values('Artifical Intelligence');
INSERT INTO dbo.dept values('Network Research');
INSERT INTO dbo.dept values('Linux Research');
INSERT INTO dbo.dept values('Bussiness Academy');
---------------------------------------------------------------
CREATE TABLE employee(
	NO INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,
	NAME VARCHAR(20),
	GENDER VARCHAR(8) DEFAULT 'Male',
	BIRTH DATE,
	PROVINCE VARCHAR(20),
	DEPT VARCHAR(30),
	SALARY FLOAT DEFAULT '5000',
	PHOTO VARBINARY(MAX), 
	MEMO NTEXT,
)

DROP TABLE dbo.employee;

SELECT * FROM dbo.employee;

INSERT INTO dbo.employee values('John', 'Male', '1983-05-20', 'ZheJiang', 'CS', 5000, 
(SELECT * FROM OPENROWSET(BULK N'C:\Users\Administrator\Workspace\xuan_work\programming\test\database\img\piggy_0.png', SINGLE_BLOB) as T1),
'This is a line of blob type uplaoding in sql server')

INSERT INTO dbo.employee values('Anna', 'Male', '1983-05-20', 'ZheJiang', 'CS', 5000, 
(SELECT * FROM OPENROWSET(BULK N'C:\Users\Administrator\Workspace\xuan_work\programming\test\database\img\bot_0.png', SINGLE_BLOB) as T2),
'This is a line of blob type uplaoding in sql server')


INSERT INTO dbo.employee values('Anna1', 'Male', '1983-05-20', 'ZheJiang', 'CS', 5000, 
(SELECT * FROM OPENROWSET(BULK N'C:\Users\Administrator\Workspace\xuan_work\programming\test\database\img\bot_0.png', SINGLE_BLOB) as T2),
'This is a line of blob type uplaoding in sql server')


INSERT INTO dbo.employee values('Anna2', 'Male', '1983-05-20', 'ZheJiang', 'CS', 5000, 
(SELECT * FROM OPENROWSET(BULK N'C:\Users\Administrator\Workspace\xuan_work\programming\test\database\img\bot_0.png', SINGLE_BLOB) as T2),
'This is a line of blob type uplaoding in sql server')

--DELETE FROM dbo.employee; 
---------------------------------------------------------------

CREATE TABLE majors(
	ID INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,
	MAJOR VARCHAR(40),
	DEPTid INT
)

SELECT * FROM dbo.majors;

INSERT INTO dbo.majors VALUES('Biology', 2);
INSERT INTO dbo.majors VALUES('Software', 1);
INSERT INTO dbo.majors VALUES('Network Security', 3);
INSERT INTO dbo.majors VALUES('Linux Kernel', 4);
INSERT INTO dbo.majors VALUES('Bussiness Management', 5);
------------------------------------------------------------------
CREATE TABLE stu_ifo(
	ID INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,
	NAME VARCHAR(20),
	GENDER VARCHAR(8),
	DEPTid INT,
	MAJORid INT
)

SELECT * FROM dbo.stu_ifo;

INSERT INTO dbo.stu_ifo VALUES('George Carlin', 'Male', 5, 5);
INSERT INTO dbo.stu_ifo VALUES('Kite Smith', 'Female', 1, 1);
INSERT INTO dbo.stu_ifo VALUES('william Birkin', 'Male', 2, 2);
INSERT INTO dbo.stu_ifo VALUES('John Strong', 'Male', 4, 4);
INSERT INTO dbo.stu_ifo VALUES('Linus Torvalds', 'Male', 3, 3);

DELETE FROM dbo.stu_ifo;

