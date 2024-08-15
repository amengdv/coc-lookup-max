import os


def get_col_at(th, csv):
    lines = csv.split("\n")
    townhall = lines[0].split(",")

    column_index = townhall.index(str(th))

    result = f"TOWNHALL {th}\n"

    for line in lines:
        words = line.split(",")
        if words[0] == "TOWNHALL" or words[0] == "":
            continue


        result += f"{words[0]}: {words[column_index]}\n"


    return result


def get_csv_content(category):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "..", "data")

    category += ".csv"
    with open(os.path.join(data_dir, category)) as csv:
        return csv.read()



