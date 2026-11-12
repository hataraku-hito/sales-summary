"""毎日の売上CSVを集計する小さなツール。

使い方:
    python3 sales_summary.py sample_sales.csv
"""

import csv
import sys
from decimal import Decimal


def load_sales(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(
                {
                    "date": row["date"],
                    "item": row["item"],
                    "quantity": int(row["quantity"]),
                    "unit_price": Decimal(row["unit_price"]),
                }
            )
    return rows


def apply_discount(amount, discount_percent):
    discount = Decimal(str(discount_percent))
    if not discount.is_finite() or discount < 0 or discount > 100:
        raise ValueError("割引率は0〜100の範囲で指定してください")
    return amount * (1 - discount / 100)


def summarize(rows, discount_percent=0):
    if not rows:
        zero = Decimal("0")
        return {
            "count": 0,
            "total": zero,
            "average": zero,
            "tax": zero,
            "grand_total": zero,
        }
    total = Decimal("0")
    for row in rows:
        total += row["quantity"] * row["unit_price"]
    total = apply_discount(total, discount_percent)
    average = total / len(rows)
    tax = total * Decimal("0.1")
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
