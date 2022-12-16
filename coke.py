def main():
    amount_due = 50

    while amount_due > 0:
        print(f"Amount due: {amount_due}")
        insert_coin = int(input("Insert Coin: ").strip())
        if insert_coin == 25 or insert_coin == 10 or insert_coin == 5:
            amount_due = amount_due - insert_coin

    if amount_due <= 0:
        print(f"Change Owed: {abs(amount_due)}")


if __name__ == "__main__":
    main()
