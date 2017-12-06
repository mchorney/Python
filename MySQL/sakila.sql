USE Sakila;
-- Question 1
SELECT customer.first_name, customer.last_name, customer.email, address.address 
FROM customer
JOIN address
ON address.address_id = customer.address_id
JOIN city 
ON city.city_id = address.city_id
WHERE city.city_id = 312;
-- Question 2
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name as genre
FROM film 
JOIN film_category 
ON film_category.film_id = film.film_id
JOIN category
ON category.category_id = film_category.category_id
WHERE category.name = 'Comedy';
-- Question 3
SELECT actor.actor_id, actor.first_name, actor.last_name, film.title, film.description, film.release_year
FROM actor
JOIN film_actor 
ON film_actor.actor_id = actor.actor_id
JOIN film
ON film.film_id = film_actor.film_id
WHERE actor.actor_id = 5;
-- QUESTION 4
SELECT customer.store_id, customer.first_name, customer.last_name, customer.email, address.address
FROM customer
JOIN address
ON address.address_id = customer.address_id
JOIN city 
ON city.city_id = address.city_id
WHERE customer.store_id = 1 and city.city_id IN (1, 42, 312, 459);
-- Question 5
SELECT film.title, film.description, film.release_year, film.rating, film.special_features
FROM film 
JOIN film_actor 
ON film_actor.film_id = film.film_id
JOIN actor 
ON actor.actor_id = film_actor.actor_id
WHERE actor.actor_id = 15 and film.rating = 'G' and film.special_features LIKE '%behind the scenes%';
-- QUESTION 6
SELECT film.film_id, film.title, actor.actor_id, actor.first_name, actor.last_name
FROM film 
JOIN film_actor
ON film_actor.film_id = film.film_id
JOIN actor
ON actor.actor_id = film_actor.actor_id
WHERE film.film_id = 369;
-- QUESTION 7 
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name as genre
FROM film 
JOIN film_category 
ON film_category.film_id = film.film_id
JOIN category
ON category.category_id = film_category.category_id
WHERE film.rental_rate = 2.99 and category.name = 'drama';
-- QUESTION 8 
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name as genre, CONCAT(actor.first_name," ", actor.last_name) as actor_name
FROM film 
JOIN film_category 
ON film_category.film_id = film.film_id
JOIN category
ON category.category_id = film_category.category_id
JOIN film_actor
ON film_actor.film_id = film.film_id
JOIN actor
ON actor.actor_id = film_actor.actor_id
WHERE category.name = 'action' and CONCAT(actor.first_name," ", actor.last_name) = 'SANDRA KILMER';