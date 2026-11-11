"""毎日の売上CSVを集計する小さなツール。

使い方:
    python3 sales_summary.py sample_sales.csv
"""

import csv
import sys


def load_sales(path):
    rows = []
    f = open(path)
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(
            {
                "date": row["date"],
                "item": row["item"],
                "quantity": int(row["quantity"]),
                "unit_price": float(row["unit_price"]),
            }
        )
    return rows


def apply_discount(amount, discount_percent):
    return amount * (1 - discount_percent / 100)


def summarize(rows, discount_percent=0):
    total = 0.0
    for row in rows:
        total += row["quantity"] * row["unit_price"]
    total = apply_discount(total, discount_percent)
    average = total / len(rows)
    tax = total * 0.1
    return {
        "count": len(rows),
        "total": total,
        "average": average,
        "tax": tax,
        "grand_total": total + tax,
    }


def main():
    path = sys.argv[1]
    discount = float(sys.argv[2]) if len(sys.argv) > 2 else 0
    rows = load_sales(path)
    result = summarize(rows, discount)
    print(f"件数: {result['count']}")
    print(f"合計（割引後・税別）: {result['total']}円")
    print(f"1件あたり平均: {result['average']}円")
    print(f"消費税: {result['tax']}円")
    print(f"税込合計: {result['grand_total']}円")


if __name__ == "__main__":
    main()
