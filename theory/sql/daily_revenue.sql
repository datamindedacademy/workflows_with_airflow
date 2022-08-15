SELECT SUM(amount)
FROM {{ params.table }}
WHERE transaction_timestamp BETWEEN '{{ ds }}' AND '{{ next_ds }}'