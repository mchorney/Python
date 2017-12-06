USE world;
-- QUESTION 1
SELECT name, language, percentage FROM countries
LEFT JOIN languages
ON country_id = countries.id
WHERE language = 'Slovene'
ORDER by percentage DESC;
-- QUESTION 2
SELECT countries.name, COUNT(cities.id) as num_cities FROM countries
JOIN cities
ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY num_cities DESC;
-- QUESTION 3
SELECT cities.name, cities.population FROM countries
JOIN cities
ON cities.country_id = countries.id
WHERE countries.name = 'Mexico'
ORDER BY population DESC;
-- QUESTION 4
SELECT countries.name, languages.language, languages.percentage FROM countries
JOIN languages
ON languages.country_id = countries.id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;
-- QUESTION 5
SELECT name, surface_area, population from countries
WHERE surface_area < 501 and population > 100000;
-- QUESTION 6
SELECT name, government_form, capital, life_expectancy from countries
WHERE government_form = 'Constitutional Monarchy' and capital > 200 and life_expectancy > 75;
-- QUESTION 7
SELECT countries.name, cities.name, cities.district, cities.population FROM countries
JOIN cities
ON cities.country_id = countries.id
WHERE countries.name = 'Argentina' and cities.district = 'Buenos Aires' and cities.population > 500000;
-- QUESTION 8
SELECT region, COUNT(id) as num_of_countries FROM countries
GROUP BY region
ORDER BY num_of_countries DESC;