def main():
    i = 0
    while i < 10:
        print(i)
        i = i + 1
        if i % 3 == 0:
            break

    j = 10
    while j < 100:
        print(j, j % 5)
        j = j + 1
        if j % 5 == 0:
            break

    moji = "a"
    while len(moji) < 5:
        print(moji)
        moji = moji + "a"

if __name__ == "__main__":
    main()