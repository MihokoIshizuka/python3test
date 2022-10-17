def main():
    for i in range(5):
        print(i)
# 連続した数字を取得、0.5.10.15
    for i in range(0,20,5):
        print(i)

# 連続した数字を取得、10.12.14.16.18
    for i in range(10,20,2):
        print(i)

# 連続した数字を取得、-10.-7.-4.-1.2
    for i in range(-10,5,3):
        print(i)

# 繰り返し処理をスキップして次に移る
    for i in range(5):
        if i == 3:
            continue
        print(i)

if __name__ == "__main__":
    main()