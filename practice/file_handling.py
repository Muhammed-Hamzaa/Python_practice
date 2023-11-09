# Before we can perform any operations on a file, we must first open it. 
# The mode can be 'r' for reading, 'w' for writing, or 'a' for appending.

# There are various modes in which we can open files.
# read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.
# write (w): This mode opens the file for writing only and creates a new file if the file does not exist.
# append (a): This mode opens the file for appending only and creates a new file if the file does not exist.
# create (x): This mode creates a file and gives an error if the file already exists.
# text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).
# binary (b): used to handle binary files (images, pdfs, etc).
# + : Open a file for updating (reading and writing)

# READING A FILE
f = open('practice/file.txt','r')
text = f.read()
print(text)
# It is important to close a file after you are done with it.
f.close()

# WRITING A FILE
f = open('practice/file.txt', 'a')
f.write('\nHello, world!')
f.close()

# Alternatively, you can use the with statement to automatically close the file after you are done with it.
with open('practice/file.txt', 'a') as f:
  f.write("\nHey I am inside with")

# making a new file
f = open('practice/file2.txt', 'w')
lines = ['89,77,84\n', '77,98,65\n', '98,43,67\n']
f.writelines(lines)
f.close()

#reading the file2.txt
# The readline() method reads a single line from the file. If we want to read multiple lines, we can use a loop.
f = open('practice/file2.txt', 'r')
i=1
while True:
    line = f.readline()
    if not line:
        break
    m1= line.split(",")[0]
    m2= line.split(",")[1]
    m3= line.split(",")[2]
    print(f"\nMarks of student {i} in Maths is: {m1}")
    print(f"Marks of student {i} in Maths is: {m2}")
    print(f"Marks of student {i} in Maths is: {m3}")
    print(line)

# Keep in mind that the writelines() method does not add newline characters between the strings in the sequence.
#  If you want to add newlines between the strings, you can use a loop to write each string separately:
f = open('practice/file.txt', 'w')
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
    f.write(line + '\n')
f.close()


with open('practice/file.txt', 'r') as f:
  # Move to the 10th byte in the file
  f.seek(7)

  # tells the current position  
  print(f.tell())

  # Read the next 5 bytes
  data = f.read(7)
  print(data)


# if you want to truncate the file to a specific size,
#  you can use the truncate function.
with open('practice/sample.txt', 'w') as f:
  f.write('Hello World!')
  f.truncate(5)

with open('practice/sample.txt', 'r') as f:
  print(f.read())

