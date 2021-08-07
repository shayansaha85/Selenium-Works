def generate_csv(list, animal):
    s = ""
    for x in list:
        s += x + "\n"
    file = open(f"spreadsheets/{animal}_details.csv", "w")
    file.write(s)
    file.close()
    print("===================================================")
    print(f"{animal}_details.csv saved")
    print("===================================================")
    