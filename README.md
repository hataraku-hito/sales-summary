# sales-summary

毎日の売上CSVを集計する小さなPythonツールです。

## 使い方

```bash
python3 sales_summary.py sample_sales.csv
python3 sales_summary.py sample_sales.csv 10   # 割引率10%を指定
```

CSVの形式: `date,item,quantity,unit_price`
