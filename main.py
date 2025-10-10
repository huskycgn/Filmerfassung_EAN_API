from funcs import ean_lookup, write_db, remove_movies, check_duplicate

running = True

while running:
    mode_select = input("Select mode (1 for adding, 2 for removing, or q to quit): ")
    if mode_select == "1":
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
                except KeyError:
                    print("Ungültige EAN")
                    continue
            else:
                print("Duplikat in DB - nächsten Film scannen!")
                continue
    elif mode_select == "2":
        ean_input = input("Enter an EAN number or type 'q' to quit: ")
        if ean_input == 'q':
            print("Goodbye")
            running = False
        elif not ean_input.isnumeric():
            print("Invalid EAN number")
            continue
        remove_movies(ean_input)
    elif mode_select == "q":
        print("Goodbye")
        running = False

