DROP TABLE IF EXISTS author_book;
DROP TABLE IF EXISTS book_publisher;
DROP TABLE IF EXISTS library_book;
DROP TABLE IF EXISTS publishers;
DROP TABLE IF EXISTS libraries;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE IF NOT EXISTS authors(
	id SERIAL UNIQUE,
	author_id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	bio TEXT,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS books(
	id SERIAL UNIQUE,
	book_id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
	title VARCHAR(100),
	summary TEXT,
	published_date DATE,
	metadata JSON,
	updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS publishers(
	id SERIAL UNIQUE,
	publisher_id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
	publisher_name VARCHAR(100),
	country CHAR(2),
	founded_year INTEGER,
	details JSON,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS libraries(
	id SERIAL UNIQUE,
	library_id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
	library_name VARCHAR(100),
	location TEXT,
	open_time TIME,
	close_time TIME,
	facilities JSON,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS author_book(
	id SERIAL PRIMARY KEY,
	author_id INTEGER REFERENCES authors(id),
	book_id INTEGER REFERENCES books(id)
);

CREATE TABLE IF NOT EXISTS book_publisher(
	id SERIAL PRIMARY KEY,
	book_id INTEGER REFERENCES books(id),
	publisher_id INTEGER REFERENCES publishers(id)
);

CREATE TABLE IF NOT EXISTS library_book(
	id SERIAL PRIMARY KEY,
	library_id INTEGER REFERENCES libraries(id),
	book_id INTEGER REFERENCES books(id)
);

INSERT INTO authors(first_name, last_name, bio)
VALUES	('Paulo', 'Koelo', '(1947-yil 24-avgustda tugʻilgan) — braziliyalik shoir va yozuvchi.'),
	('Erkin', 'Vohidov', '(1936-2016) taniqli o‘zbek shoiri va jamoat arbobi.');

INSERT INTO books(title, summary, published_date, metadata)
VALUES	('Alkimyogar', 'Oddiy bir cho''pon orzulariga erishish uchun barcha qiyinchiliklarga bardosh berishi, va orzusiga erishishi haqida', TO_DATE('2013', 'yyyy'), '{"janr": "doston", "format": "pdf"}'),
	('Ruhlar isyoni', 'Otashin bengal shoiri Narzul Islom haqida', TO_DATE('2019', 'yyyy'), '{"janr": "qissa, doston", "format": "pdf"}'),
	('O''zbegim', 'Sh''erlar to''plami', TO_DATE('2006', 'yyyy'), '{"janr": "she''rlar, nazm", "format": "pdf"}');

INSERT INTO publishers(publisher_name, country, founded_year, details)
VALUES	('Yangi asr avlodi', 'uz', '2022', '{"web-sayt": "yangiasravlodi.com", "manzil": "Toshkent, Chilonzor 8"}'),
	('G''afur G''ulom', 'uz', '2019', '{"e-mail": "b.rahimov@inbox.ru", "manzil": "Toshkent sh. Shayxontohur tuman, Labzak k. 86"}'),
	('O''zbekiston milliy ensiklopediyasi', 'uz', '2006', '{"manzil": "Toshkent"}');

INSERT INTO libraries(library_name, location, open_time, close_time, facilities)
VALUES	('Ahmad al-Farg''oniy nomidagi viloyat kutubxonasi', 'Farg''ona shahar', '08:00:00', '18:00:00', '{"wi-fi": "kitob123", "oqishxonasi": "12-xona"}');

INSERT INTO author_book(author_id, book_id)
VALUES	(1, 1),
	(2, 2),
	(2, 3);

INSERT INTO book_publisher(book_id, publisher_id)
VALUES	(1, 1),
	(2, 1),
	(1, 2),
	(2, 2),
	(3, 3);

INSERT INTO library_book(book_id, library_id)
VALUES	(1, 1),
	(2, 1),
	(3, 1);

SELECT * FROM author_book
JOIN authors ON authors.id = author_book.author_id
JOIN books ON books.id = author_book.book_id;

SELECT * FROM book_publisher
JOIN books ON books.id = book_publisher.book_id
JOIN publishers ON publishers.id = book_publisher.publisher_id;

SELECT * FROM library_book
JOIN libraries ON libraries.id = library_book.library_id
JOIN books ON books.id = library_book.book_id;
