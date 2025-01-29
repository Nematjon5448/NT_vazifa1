DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS genres;

CREATE TABLE IF NOT EXISTS genres(
	genre_id SERIAL PRIMARY KEY,
	genre_name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS books(
	book_id SERIAL PRIMARY KEY,
	book_name VARCHAR(100),
	author_name VARCHAR(100),
	price INTEGER,
	genre_id INTEGER REFERENCES genres(genre_id)
);

INSERT INTO genres(genre_name)
VALUES	('Sarguzashtlar'),
		('Roman');

INSERT INTO books(book_name, author_name, price, genre_id)
VALUES	('Alkimyogar', 'Paulo Koelo', 19000, 1),
		('O''tkan kunlar', 'Abdulla Qodiriy', 22000, 2),
		('Mehrobdan chayon', 'Abdulla Qodiriy', 18000, 2),
		('Sariq devni minib', 'Xudoyberdi To''xtaboev', 20000, 1);

SELECT * FROM books;

UPDATE books SET price = 25000 WHERE book_id = 1;
UPDATE books SET genre_id = 1 WHERE book_id = 2;

DELETE FROM books WHERE book_id = 3;
DELETE FROM books WHERE book_id = 2;






