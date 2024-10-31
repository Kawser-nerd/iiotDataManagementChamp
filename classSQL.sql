--- drop the table if exits
DROP Table if exists student;

CREATE TABLE student(
	StudentNo Integer not null,
	LastName varchar(20) not null,
	FirstName varchar(20), -- we will accept null values
	Email char(15) not null Unique, -- this column going to accecpt no null value and unique values			
	RegisYear numeric(5,0) not null,
	--- key constraints --
	Constraint std_pk Primary Key(StudentNo)
);

DROP Table if exists Grade;
CREATE Table Grade(
	Term char(7) not null,
	Year numeric(5,0) not null,
	GradePoint decimal(4,2),
	StudentNo Integer not null,
	-- key constraints -- unique key --
	Constraint grade_uk Unique (Term, Year, StudentNo),
	-- Foreign Key
	Constraint grade_fk Foreign Key(StudentNo) REFERENCES student
	
);

-- Modifying the table one created --
ALTER TABLE student ADD Address char(25); -- new attribute is going to be added, with null value acceptable
-- change column name from regisyear to registrationyear
---exec sp_rename 'student.regisyear','registrationyear','COLUMN';
ALTER TABLE student RENAME COLUMN regisyear to registrationyear;
--- change the column datatype 
ALTER TABLE grade ALTER COLUMN Year SET DATA TYPE Integer;
-- delete the attribute from a table
ALTER TABLE student DROP address;

--- change the table name grade to graderecords
ALTER TABLE grade RENAME To graderecords;

-- add a checker to make sure the gradepoint column doesn't have a value less than 0, more than 4
ALTER TABLE graderecords ADD CHECK (GradePoint >=0 and GradePoint <=4);



