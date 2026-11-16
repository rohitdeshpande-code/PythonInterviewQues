
with open("test.txt", "w") as f:
    f.write("Hello QA Engineers..!!!!")

try:
    with open("test.txt", "r") as f:
        content = f.read()
        print(content)

except FileNotFoundError as e:
    print(e)

finally:
    print('clean up any resources')