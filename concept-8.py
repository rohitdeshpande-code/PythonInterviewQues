import asyncio
import time


def task(name):
    print (f"starting {name}")
    time.sleep(2) #block
    print(f"finished {name}")

# task("QA")
# task("Engineer")

async def task(name):
    print(f"starting {name}")
    await asyncio.sleep(2)
    print(f"finished {name}")

async def main():
    await asyncio.gather(task("QA Engineer"), task("Engineer"))


asyncio.run(main())