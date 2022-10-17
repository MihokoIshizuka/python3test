def main():
    a, b = 0, 1
    while b < 30:
        print(b)
        # a, b = b, a+b
        temp = a
        a = b
        b = temp + a
if __name__ == "__main__":
    main()