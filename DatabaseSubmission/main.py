import sqlite3

fileList = ("information.docx", "Hello.txt", "myImage.png", "myMovie.mpg", "World.txt", "data.pdf", "myPhoto.jpg")

# Connect to database / Create a new database if current database does not exist

conn = sqlite3.connect("myfiles.db")

#Creates a table with two columns
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files (ID INTEGER PRIMARY KEY AUTOINCREMENT, col_filename TEXT)")
    conn.commit()

#Used to loop through fileList to find file names ending in ".txt" and add them to database
for file in fileList:
    if file.endswith(".txt"):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files (col_filename) VALUES (?)", (file,)) #use a one-element tuple
            print(file)
            conn.commit()

conn.close()
