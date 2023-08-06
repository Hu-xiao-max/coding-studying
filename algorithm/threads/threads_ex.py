import threading

# 定义一个打印数字的线程任务
def print_numbers(thread_name, start, end):
    for i in range(start, end + 1):
        print(f"{thread_name}: {i}")

# 创建两个线程
thread1 = threading.Thread(target=print_numbers, args=("Thread 1", 1, 5))
thread2 = threading.Thread(target=print_numbers, args=("Thread 2", 6, 10))

# 启动线程
thread1.start()
thread2.start()

# 等待线程执行完毕
thread1.join()
thread2.join()

print("All threads finished.")