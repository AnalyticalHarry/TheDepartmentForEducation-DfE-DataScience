/* Creating Attribute Name and Data TyPES*/

CREATE TABLE Student(
  STU_NUM CHAR PRIMARY KEY,
  STU_SNAME VARCHAR(15),
  STU_FNAME VARCHAR(15),
  STU_INITIAL CHAR(1),
  STU_STARTDATE DATE,
  COURSE_CODE CHAR(3),
  PROJ_NUM INT
)

/* Entering first two rows*/
INSERT INTO Student
  (STU_NUM, STU_SNAME, STU_FNAME, STU_INITIAL, STU_STARTDATE , COURSE_CODE, PROJ_NUM)
VALUES
  (01, 'Snow', 'John', 'E', '05-Apr-14', '201', 6),
  (02, 'Stark', 'Arya', 'C', '12-Jul-17', '305', 11);

/* Entering rest of the rows*/
INSERT INTO Student
  (STU_NUM, STU_SNAME, STU_FNAME, STU_INITIAL, STU_STARTDATE , COURSE_CODE, PROJ_NUM)
VALUES
  (03,'Lannister', 'Jamie', 'C', '05-Sep-12','101',2),
  (04, 'Lannister', 'Cercei', 'J', '05-Sep-12', '101',2),
  (05, 'Greyjoy', 'Theon', 'I','09-dEC-15', '402', 14),
  (06, 'Tyrell', 'Margaery', 'Y', '12-Jul-17', '305',10),
  (07, 'Baratheon', 'Tommen', 'R', '13-Jun-19', '201',5);

/*Now we know, which student number 7 has course code of 201, it need to be update to 304*/
SELECT *
FROM Student
WHERE STU_NUM = 7;

UPDATE student
SET COURSE_CODE = '304'
WHERE STU_NUM = 7;

/*Checking dataset*/
SELECT *
FROM student

/*SQL code to delete the row of the person named Jamie Lannister,
who started on 5 September 2012, whose course code is 101 and project
number is 2. Use logical operators to include all of the information given in
this problem.*/

DELETE student 
WHERE STU_FNAME like '%Jamie%' and STU_SNAME like '%Lannister%'
and STU_STARTDATE='05-Sep-12' and COURSE_CODE = 101
and PROJ_NUM =2;


/* Write the SQL code that will change the PROJ_NUM to 14 for all those
students who started before 1 January 2016 and whose course code is at
least 201.
 */
 UPDATE student
 SET PROJ_NUM = 14
 WHERE STU_STARTDATE < '01-Jan-2016' and COURSE_CODE>=201;

 /* SQL code that will delete all of the data inside a table, but not the
table itself.*/
DELETE from student WHERE STU_NUM = 1
DELETE student

/*the SQL code that will delete the Student table entirely*/
SELECT * FROM student
DROP TABLE student

/*Verifying the deleted Student table entirely*/
SELECT * FROM student 