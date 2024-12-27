1 - vazifa

DROP TABLE IF EXISTS foydalanuvchilar;

CREATE TABLE IF NOT EXISTS foydalanuvchilar(
	foydalanuvchi_id SERIAL NOT NULL UNIQUE,
	ism VARCHAR(25) NOT NULL,
	yosh INTEGER,
	manzil VARCHAR(20)
);

INSERT INTO foydalanuvchilar(ism, yosh, manzil)
VALUES('Nematjon',  22, 'Margilon'),
('Azizbek', 23, 'Rishton'),
('Alisher', 23, 'Quvasoy'),
('Otabek', 22, 'Fargona');

SELECT * FROM foydalanuvchilar;

2 - vazifa

CREATE TABLE IF NOT EXISTS mahsulotlar(
	mahsulot_id SERIAL NOT NULL UNIQUE,
	nom VARCHAR(30) NOT NULL,
	narx INTEGER,
	tavsif VARCHAR(60)
);

INSERT INTO mahsulotlar(nom, narx, tavsif)
VALUES('Pepsi', 12000, 'Gazlangan 1,5 litr'),
('Chortoq', 4000, 'Gazlanmagar 1 litr'),
('Fanta', 14000, 'Gazlangan 1,5 litr');

SELECT * FROM mahsulotlar;

3 - vazifa

CREATE TABLE IF NOT EXISTS buyurtmalar(
	buyurtma_raqami SERIAL NOT NULL UNIQUE,
	foydalanuvchi VARCHAR(25),
	mahsulot VARCHAR(40),
	miqdor INTEGER
);

INSERT INTO buyurtmalar(foydalanuvchi, mahsulot, miqdor)
VALUES('Muhammadrasul', 'Kitob', 120),
('Shoxrux', 'Daftar', 500),
('Abror', 'Albom', 200);

SELECT * FROM buyurtmalar;

4 - vazifa

CREATE TABLE IF NOT EXISTS xodimlar(
	xodim_id SERIAL NOT NULL UNIQUE,
	ism VARCHAR(25) NOT NULL,
	lavozim VARCHAR(30),
	tavsif VARCHAR(60)
);

INSERT INTO xodimlar(ism, lavozim, tavsif)
VALUES('Nematjon', 'Dasturchi', 18000),
('Azizbek', 'Hissobchi', 15000),
('Diyorbek', 'Qorovul', 4000);

SELECT * FROM xodimlar;

5 - vazifa

CREATE TABLE IF NOT EXISTS yetkazib_beruvchi(
	id_raqami SERIAL NOT NULL UNIQUE,
	kompaniya_nomi VARCHAR(40) NOT NULL,
	telefon_raqami VARCHAR(15),
	manzil VARCHAR(50)
);

INSERT INTO yetkazib_beruvchi(kompaniya_nomi, telefon_raqami, manzil)
VALUES('Uzum Market', '+99878 1501115', 'Fargona sh. Qomus kochasi'),
('EMU pochta', '+99893 3819151', 'Fargona sh. B.Al-Margiloniy'),
('BTS pochta', '+99871 2070809', 'Fargona sh. Yuksalish kochasi');

SELECT * FROM yetkazib_beruvchi;



