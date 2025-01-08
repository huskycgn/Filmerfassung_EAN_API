from funcs import ean_lookup, write_db, check_duplicate

running = True

while running:
    ean_input = input("Enter an EAN number or type 'q' to quit: ")
    if ean_input == 'q':
        print("Goodbye")
        running = False
    elif not ean_input.isnumeric():
        print("Invalid EAN number")
        continue
    else:
        if not check_duplicate(ean_input):
            try:
                title = ean_lookup(ean_input)
                write_db(title, ean_input)
            except:
                print("Ungültige EAN")
                continue
        else:
            print("Duplikat in DB - nächsten Film scannen!")
            continue



