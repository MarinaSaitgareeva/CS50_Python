def main():
    class Counter(dict):
        def __missing__(self, key):
            return 0

    grocery = Counter()

    while True:
        try:
            item = input().upper().strip()
            grocery[item] += 1

        except EOFError:
            grocery = dict(sorted(grocery.items()))

            print()
            for item in grocery:
                print(f"{grocery[item]} {item}")

            break

        # except KeyError:
        #     pass


if __name__ == "__main__":
    main()
