-- 1. Vazifa

DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS categories;

CREATE TABLE IF NOT EXISTS categories(
	category_id SERIAL PRIMARY KEY,
	category_name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS products(
	product_id SERIAL PRIMARY KEY,
	product_name VARCHAR(100),
	price INTEGER,
	category_id INTEGER DEFAULT NULL REFERENCES categories(category_id) 
);

INSERT INTO categories(category_name)
VALUES	('Telefonlar'),
	('Noutbooklar'),
	('Planshetlar'),
	('Akksesuarlar'),
	('Telefon ehtiyot qismlari');

INSERT INTO products(product_name, price, category_id)
VALUES	('iPad Pro', 800, 3),
	('iPhone 13 Pro Max', 670, 1),
	('Samsung S22', 290, 1),
	('iPhone 12 original display', 70, NULL),
	('Airpods Pro 2', 300, 4),
	('Samsung Tab S9', 900, 3),
	('Samsung S20 display', 140, NULL),
	('Redmi Note 14 Pro', 350, 1),
	('iWatch Series 10', 480, 4),
	('PlayStation 5', 430, NULL),
	('Redmi zaryadnik 67W', 15, 4),
	('iPhone zaryadnik 20W', 30, 4),
	('Redmi Pad Pro', 280, 3),
	('Metoo klaviatura va sichqoncha', 20, NULL),
	('Monitor Samsung Essential S3', 150, NULL);

SELECT * FROM products
INNER JOIN categories ON categories.category_id = products.category_id;

SELECT * FROM products
RIGHT JOIN categories ON categories.category_id = products.category_id;

SELECT * FROM products
LEFT JOIN categories ON categories.category_id = products.category_id;

SELECT * FROM products WHERE category_id IS NULL;

SELECT * FROM products
RIGHT JOIN categories ON categories.category_id = products.category_id
WHERE products.category_id IS NULL;

SELECT * FROM products
FULL JOIN categories ON categories.category_id = products.category_id;

SELECT * FROM products
FULL JOIN categories ON categories.category_id = products.category_id
WHERE products.category_id IS NULL;

SELECT * FROM products CROSS JOIN categories;

SELECT * FROM products NATURAL JOIN categories;

-- 2. Vazifa

DROP TABLE IF EXISTS admins;

CREATE TABLE IF NOT EXISTS admins(
	id SERIAL PRIMARY KEY,
	full_name VARCHAR(80),
	admin_id INTEGER REFERENCES admins(id)
);

INSERT INTO admins(full_name, admin_id)
VALUES	('Ne''matjon Rasulov', NULL),
	('Shavkat Hakimov', 1),
	('Ikrom Akramov', 1),
	('Ziyodullo Toshpo''latov', 2),
	('Abdullo Sobirjonov', 2),
	('Shoxrux Abdusamatov', 3),
	('Saizazimxon Mamurxonov', 3),
	('Fayzullo Muxtorov', 3);

SELECT admins.full_name, users.full_name FROM admins JOIN admins as users ON admins.id = users.admin_id;

-- 3. Vazifa

DROP TABLE IF EXISTS film_actor;
DROP TABLE IF EXISTS actors;
DROP TABLE IF EXISTS films;

CREATE TABLE IF NOT EXISTS films(
	film_id SERIAL PRIMARY KEY,
	film_name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS actors(
	actor_id SERIAL PRIMARY KEY,
	actor_name VARCHAR(80)
);

CREATE TABLE IF NOT EXISTS film_actor(
	film_actor_id SERIAL PRIMARY KEY,
	film_id INTEGER REFERENCES films(film_id),
	actor_id INTEGER REFERENCES actors(actor_id)
);

INSERT INTO films(film_name)
VALUES	('Uylanish'),
	('Zamonaviy sovchilar'),
	('Oling quda bering quda');
	
INSERT INTO actors(actor_name)
VALUES	('Alisher Uzoqov'),
	('Muhammadiso Abdulxairov'),
	('Matyoqub Matchonov');

INSERT INTO film_actor(film_id, actor_id)
VALUES	(1, 1),
	(1, 3),
	(2, 1),
	(2, 2),
	(3, 1),
	(3, 2),
	(3, 3);
	
SELECT film_name, actor_name FROM film_actor
JOIN films ON films.film_id = film_actor.film_id
JOIN actors ON actors.actor_id = film_actor.actor_id;

-- 4. Vazifa

SELECT category_name, count(product_name) FROM categories
JOIN products ON products.category_id = categories.category_id
GROUP BY category_name;

SELECT actor_name, count(film_name) FROM film_actor
JOIN actors ON actors.actor_id = film_actor.actor_id
JOIN films ON films.film_id = film_actor.film_id
GROUP BY actor_name;