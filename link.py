with open('test.txt', encoding='utf-8') as f:
    for line in f:
        
        new_mass = line.split(";")
        with open("onlylink.txt", "a", encoding='utf-8') as us:
            us.write(f'{new_mass[0]}\n')