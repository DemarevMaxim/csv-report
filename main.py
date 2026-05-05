import argparse
import csv
from tabulate import tabulate


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="+", required=True)
    parser.add_argument("--report", required=True)
    return parser.parse_args()


def read_csv(files):
    data = []
    for file in files:
        with open(file, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append({
                    "title": row["title"],
                    "ctr": float(row["ctr"]),
                    "retention_rate": float(row["retention_rate"])
                })
    return data


def filter_data(data):
    return [
        row for row in data
        if row["ctr"] > 15 and row["retention_rate"] < 40
    ]


def sort_data(data):
    return sorted(data, key=lambda x: x["ctr"], reverse=True)


def main():
    args = parse_args()
    data = read_csv(args.files)

    if args.report == "clickbait":
        data = filter_data(data)

    data = sort_data(data)

    if not data:
        print("Нет подходящих данных")
        return

    print(tabulate(data, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()