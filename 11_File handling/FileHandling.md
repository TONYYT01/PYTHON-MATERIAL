- So file handling is the one of the process of storing the data in permently in disk
- In that files we managing like delete and create and update all those things are coming under the file handling
- There are 2 types of files 
1. Text file
2. Binary file
- test files are like we can simple open that content should be human can understand 
- Like python txt and csv this files and all
- Binary files content the know charactures that should understand by some tooles to get that one
- We can't only directly
- This are the images and video and the extenctions this thing are in binay files
- We can't open those directly


### Main opertions in file
- Open
- Read
- Write
- Close 

- This are main opertaions we can do in the files some operations are also there 

### Do pratical Examples

```python
file=open("Data.txt","x")
```
- it will create the file inside the your working directory location

```python
file=open("file.txt","w")
```
- for with this one also we can create the new file
- Better use the "w" because you run the above code no error

```python
file=open("Data.txt","r")
data=file.read()
print(data)
```
- Open the file and the read the content in that pirticular file

- Default mode is Read mode

```python
file=open("Data.txt","w")
file.write("Name : KOla")
```

- When you run this code it automatically over writen the entair data and new data added in that place
- When you run like for example file_1.txt has some data
so now you runded this code file= Open("file_1.txt","w") it automatically remove tha content in that file 
- Always backup the files 


```python
file=open("Data.txt","r+")
```
- This actually the read and write operations perform so when the file does not exist it will through tha error and not create the new file 

> R+

```python
file=open("Data.txt","r+")
data=file.read()
file.write("Age : 21")
data1=file.read()
print(data1)
```
- When you run this it will print the null 
- Why ? Because of the the file pointer in the write time in the Eof so thats why it will not read the file

- Thats why you need to move the pointer at the first

```python
file=open("Data.txt","r+")
data=file.read()
file.write("Age : 21")
file.seek(0)
data1=file.read()
print(data1)
```

- Practice with better approch

```python
with open("Data.txt","r+") as File:
    data=File.read()
    print(data)
```

- Above operation we can done simply


### Pointer location function

> tell()

- It will show the where the pointer would be

```python
with open("Data.txt","r+") as file:
    print(file.tell())
    file.write("Hello Everyone")
    print(file.tell())
    print(file.tell())
    data=file.read()
    print(data)

```

> seek(any index number) 
- we can move the pointer where you want easyly

```python
with open("Data.txt","r+") as file:
    print(file.tell())
    file.write("Hello Everyone")
    print(file.tell())
    file.seek(0)
    print(file.tell())
    data=file.read()
    print(data)
```

> append (a)

- it will open the file if exists and append the data at end of the content in the file
- If not exist it automatically create the file and write the content in that
- This is only append ,read does't work hear

```python
with open("Data.txt","a") as file:
    file.write("\nHello")
```

> (a+)
- It supports the read and the append operation 

```python
with open("Data.txt","a+") as file:
    print(file.read())
```
- when you open the file with the append mode (a+) it will the pointer would waiting in the last so thats why if you start it self if you want read just move the pointer to the first

```python
with open("Data.txt","a+") as file:
    file.seek(0)
    print(file.read())
```

