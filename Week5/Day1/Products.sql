SELECT *
FROM products
WHERE price > (SELECT AVG(price) FROM products);

SELECT product_name, price*stock_quantity AS total_value
FROM products
WHERE price*stock_quantity < 100000
ORDER BY supplier ASC, total_value DESC