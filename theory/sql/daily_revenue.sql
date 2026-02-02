SELECT SUM(amount)
FROM {{ params.table }}
WHERE transaction_timestamp BETWEEN '{{ ds }}' AND '{{ data_interval_end.strftime("%Y-%m-%d") }}'