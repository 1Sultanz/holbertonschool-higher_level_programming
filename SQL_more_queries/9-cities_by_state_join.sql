-- JOIN TABLE
SELECT cities.id, cities.name, states.name
FROM cities CROSS JOIN states ON cities.id = states.id
ORDER BY cities.id;
