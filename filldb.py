from sqlalchemy import create_engine
db_string = "postgresql://rqsmbzyanmedhj:af8823e6051abe7570a25ce8a0f37d65141a3d4b61ef10755cc57b7b8552657d@ec2-3-211-221-185.compute-1.amazonaws.com:5432/d204uhq85b0b5b"
db = create_engine(db_string)
# Create 

db.execute("DROP TABLE course_info")
db.execute("DROP TABLE section")
db.execute("DROP TABLE reviews")

db.execute("CREATE TABLE IF NOT EXISTS course_info (course_name text, department text, number integer, description text)")  
db.execute("INSERT INTO course_info (course_name, department, number, description) VALUES ('Intro to Web Development', 'COMP SCI', 396,'Projects suggested by faculty and approved by the department. Equivalent to 397 but intended to apply toward courses for the computer science major and its project requirement.')")

db.execute("CREATE TABLE IF NOT EXISTS section (course_name text, professor text, review_id integer)")  
db.execute("INSERT INTO section (course_name, professor, review_id) VALUES ('Intro to Web Development','Sarah Van Wart',1)")

db.execute("CREATE TABLE IF NOT EXISTS reviews (review_id integer, reviews text)")  
db.execute("INSERT INTO reviews (review_id, reviews) VALUES (1,'good')")



# Read
result_set = db.execute("SELECT * FROM course_info")  
for r in result_set:  
    print(r)