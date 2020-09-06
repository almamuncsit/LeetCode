SELECT c.Name as Customers
FROM Customers c
LEFT JOIN Orders o ON c.id = o.CustomerId
WHERE o.CustomerId IS NULL
