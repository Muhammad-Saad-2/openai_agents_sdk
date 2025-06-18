# import time

# def write():
#     print("hey")
#     time.sleep(1)
#     print("There")


# def write():
#     for _ in range(10):
#         write()

# if __name__ == "__write__":
#     import time 
#     start = time.perf_counter()
#     write()
#     elapsed = time.perf_counter() - start
#     print(f"Executed in {elapsed:0.2f} seconds")


# import asyncio

# async def write():
#     print(f"Hey")
#     await asyncio.sleep(1)
#     print(f"There")


# async def main():
#     await asyncio.gather(
#         write(),write(),write(),write(),write(),write(),write(),write(),write(),write())
    
# if __name__ == "__main__":
#     import time 
#     start = time.perf_counter()
#     asyncio.run(main())
#     elapsed = time.perf_counter() - start
#     print(f"Executed in {elapsed:0.2f} seconds")   


class MyClass:
    x = 0
    y = ""

    def __init__(self, anyNumber, anyString):
        self.x = anyNumber
        self.y = anyString

myObject = MyClass(12345, "Hello")

print(myObject.__str__())
print(myObject.__repr__())
print(myObject)
