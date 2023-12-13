-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT AVG(value) temperature, city FROM temperatures GROUP BY city ORDER BY temperature DESC;
