-- JOIN TABLE
SELECT cities.id, cities.name, states.name
FROM cities FULL OUTER JOIN states ON cities.id = states.id
ORDER BY cities.id;
