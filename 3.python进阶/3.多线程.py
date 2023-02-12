import threading
import time


def test1(msg):
    print(f"hello1 {msg}")
    time.sleep(2)
    print("hello1 end")


def test2(msg):
    print(f"hello2 {msg}")
    time.sleep(2)
    print("hello2 end")


thread_obj = threading.Thread(
    target=test1,
    args=("你好啊1",)
)

thread_obj2 = threading.Thread(
    target=test2,
    kwargs={"msg": "你好啊2"}
)

thread_obj.start()
thread_obj2.start()
