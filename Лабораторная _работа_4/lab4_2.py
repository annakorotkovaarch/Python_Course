# TODO импортировать необходимые молули
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла

    f = open(INPUT_FILENAME, "r")
    columns = f.readline().strip().split(",")
    lout = []
    for l in f.readlines():
        lout.append(dict(zip(columns, l.strip().split(","))))



    ...  # TODO Сериализовать в файл с отступами равными 4

    json.dump(lout, open(OUTPUT_FILENAME, "w"), indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
