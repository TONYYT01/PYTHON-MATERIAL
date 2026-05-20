##### Table of Contents

- [What is thread](#what-is-thread)
- [What is Process](#process)

#### What is thread 
- So the thread is the lightweight multiple parts or unit's of work are doing concurrently (same time or overlapping)
- Example 
    1. Think and imagine Program(process) is an restaurant
    - So the program(process) is whole restaurant
    - Thread is an waiter in the restaurant doing the specific task or work
    - 👉 One restaurant (process) can have multiple waiters (threads) working at the same time. 
##### Why do we need threads
- Actually in real world application we are not doing single work or thing 
- We are doing multiple things
- What are they
- Example Take the whatsapp 
    - Sending messages
    - Receiving messages
    - Downloading messages
- This are the things we are actully doing at the time

- Without threads the app would be freeze like a low-end phone
- It is like we are telling to our program see me i will make you the multiworking program ,no need the other program for me with you only i will do 
- In an old days by the single program we are doing the single task.bore and slow
- But we need the
    1. multitasking
    2. Better cpu usage
    3. Fast performance
- `Processes` -> Isolation + Safety
- `Threads` -> Speed + MultiTasking

```python
import threading

def Task():
    print("Hello")
t1=threading.Thread(target=Task)
t1.start()
t1.join()
``` 
```python
What actually happens step-by-step
Program starts
Thread object is created (but not running yet)
.start() → thread begins execution
task() runs inside that thread
.join() → main program waits
Thread finishes → program ends cleanly
```

#### Process
- Process is the program that is running
- For example opening the google chrome that is a process actually
- Thread is a smallest unit inside the program 
- For example we are opening the google chrome inside the tab 

#### Stracture
- Process Contains
    - It contains Own Memory (heap,Stack)
    - Own Data
    - Own program
    - Os Resources
- Thread Contains
    - Stack
    - Program Counters
    - Registers
    - But Shares
        - memory
        - Variables
        - Resources
### Creating Threads (core syntax)
```python
import threading
def Taks():
    print("Hiiii")
t1=threading.Thread(target=Task)
t1.start()
```
### Why multithreading
- So with one example you understand it clearly
```python
import time
def Task():
    print("Started")
    time.sleep(3)
    print("Ended")
Task()
Task()
```
- For above one o/p is
```python
started
ended
started
ended
```
- For this one we actually doing the Task completing for 2 it will took the 6 seconds of time 
- By using the Threads we make it 3 seconds 
```python
started
started
ended
ended
```
- It will do like this actully
- Threads are used to run the task at the same time
- Best for apis,file,db ->i/o tasks

- Remember this one threads are always faster ? ->No
- for cpu usage  heavy tasks python GIL sucks
- Threads = good for waiting tasks, not heavy calculations
