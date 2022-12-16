def main():
    camel_case = input("camelCase: ").strip()
    # snake_case = convert(camel_case)
    # print(f"snake_case: {snake_case}")

    for letter in camel_case:
        if letter.isupper():
            print("_" + letter.lower(), end="")
        else:
            print(letter.lower(), end="")


# def convert(camel_case):
#     snake_case = ""
#     for letter in camel_case:
#         if letter.isupper():
#             snake_case += "_" + letter.lower()
#             # print("_" + letter.lower(), end="")
#         else:
#             snake_case += letter.lower()
#             # print(letter.lower(), end="")
#     return snake_case


if __name__ == "__main__":
    main()
