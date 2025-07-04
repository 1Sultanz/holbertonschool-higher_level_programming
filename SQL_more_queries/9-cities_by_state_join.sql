-- JOIN TABLE
SELECT cities.id, cities.name, states.name
FROM cities RIGHT JOIN states ON cities.id = states.id
ORDER BY cities.id;
