def interpreter():
    expression = input("Please type expresiion: ").strip()
    x, y, z = expression.split(" ")

    match y:
        case "+":
            result = float(x) + float(z)
            print(f"{result:.1f}")
        case "-":
            result = float(x) - float(z)
            print(f"{result:.1f}")
        case "*":
            result = float(x) * float(z)
            print(f"{result:.1f}")
        case "/":
            if int(z) == 0:
                print(f"You can't divide by zero")
            else:
                result = float(x) / float(z)
                print(f"{result:.1f}")


interpreter()
