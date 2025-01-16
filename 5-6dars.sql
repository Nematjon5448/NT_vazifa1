DROP TABLE IF EXISTS kitob_sharhlari;
DROP TABLE IF EXISTS kitoblar;
DROP TABLE IF EXISTS nashriyotlar;
DROP TABLE IF EXISTS mualliflar;

CREATE TABLE IF NOT EXISTS mualliflar(
	muallif_id SERIAL PRIMARY KEY,
	ism VARCHAR(50) NOT NULL,
	tugilgan_sana DATE,
	mamlakat VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS nashriyotlar(
	nashriyot_id SERIAL PRIMARY KEY,
	nashriyot_nomi VARCHAR(100) NOT NULL UNIQUE,
	shahar VARCHAR(50),
	asos_solingan_yil INT CHECK(asos_solingan_yil <= 2024)
);

CREATE TABLE IF NOT EXISTS kitoblar(
	kitob_id SERIAL PRIMARY KEY,
	kitob_nomi VARCHAR(100) NOT NULL,
	muallif_id INTEGER REFERENCES mualliflar(muallif_id) ON DELETE CASCADE,
	nashriyot_id INTEGER DEFAULT 1 REFERENCES nashriyotlar(nashriyot_id) ON DELETE SET DEFAULT,
	janr VARCHAR(100),
	nashr_sanasi DATE,
	narx INTEGER
);

CREATE TABLE IF NOT EXISTS kitob_sharhlari(
	kitob_sharhlari_id SERIAL PRIMARY KEY,
	kitob_id INTEGER REFERENCES kitoblar(kitob_id) ON DELETE SET NULL,
	sharh TEXT,
	baho INT CHECK(baho >= 1 AND baho <= 10),
	sharh_sanasi DATE DEFAULT CURRENT_DATE
);

INSERT INTO mualliflar(ism, tugilgan_sana, mamlakat)
VALUES	('Alisher Navoiy', TO_DATE('09.02.1441', 'dd.mm.yyyy'), 'Hirot'),
	('O''kir Hoshimov', TO_DATE('05.08.1941', 'dd.mm.yyyy'), 'O''zbekiston'),
	('Aleksandr Pushkin', TO_DATE('06.06.1799', 'dd.mm.yyyy'), 'Rassiya'),
	('Mixail Lermontov', TO_DATE('15.10.1814', 'dd.mm.yyyy'), 'Rassiya'),
	('Abdulla Qodiriy', TO_DATE('10.04.1894', 'dd.mm.yyyy'), 'O''zbekiston');

INSERT INTO nashriyotlar(nashriyot_nomi, shahar, asos_solingan_yil)
VALUES	('Sharq', 'Toshkent', 2018),
	('Yangi asr avlodi', 'Toshkent', 2009),
	('Yangi kitob', 'Toshkent', 2014),
	('G''afur G''ulom', 'Toshkent', 1957),
	('O''zbekiston', 'Toshkent', 1990);

INSERT INTO kitoblar(kitob_nomi, muallif_id, nashriyot_id, janr, nashr_sanasi, narx)
VALUES	('O''tkan kunlar', 5, 1, 'Roman', TO_DATE('12.03.2020', 'dd.mm.yyyy'), 50000),
	('Mehrobdan Chayon', 5, 1, 'Roman', TO_DATE('10.10.2019', 'dd.mm.yyyy'), 55000),
	('Yevgeniy Onegin', 3, 2, 'Roman, hikoya', TO_DATE('05.08.2014', 'dd.mm.yyyy'), 43000),
	('Kapitan qizi', 3, 2, 'Roman, hikoya', TO_DATE('23.01.2017', 'dd.mm.yyyy'), 48000),
	('Ikki eshik orasi', 2, 3, 'Roman', TO_DATE('18.09.2017', 'dd.mm.yyyy'), 50000),
	('Daftar hoshiyasidagi bitiklar', 2, 4, 'Roman', TO_DATE('12.05.2019', 'dd.mm.yyyy'), 30000),
	('Saddi Iskandariy', 1, 4, 'Doston', TO_DATE('01.05.2020', 'dd.mm.yyyy'), 70000),
	('Farhod va Shirin', 1, 4, 'Doston', TO_DATE('03.06.2020', 'dd.mm.yyyy'), 65000),
	('Zamonamiz qahramoni', 4, 5, 'Ma''lumotga oid adabiyot, fan va ta''lim', TO_DATE('29.05.2016', 'dd.mm.yyyy'), 40000),
	('Qora ko''zlar', 4, 5, 'sh''er, ertak, qissa', TO_DATE('13.03.2019', 'dd.mm.yyyy'), 44000);

INSERT INTO kitob_sharhlari(kitob_id, sharh, baho, sharh_sanasi)
VALUES	(1, 'Judayam ta''sirli sevgi haqidagi kitob ekan', 5, TO_DATE('12.03.2024', 'dd.mm.yyyy')),
	(2, NULL, 5, TO_DATE('13.03.2024', 'dd.mm.yyyy')),
	(3, 'Kitob menga yoqdi', 4, TO_DATE('16.06.2024', 'dd.mm.yyyy')),
	(4, 'Unchalik qiziq kitob emas ekan', 2, TO_DATE('20.03.2024', 'dd.mm.yyyy')),
	(5, 'O''tkir Hoshimov doim zo''r kitoblar yozadi, bu kitob ular ichida eng zo''ri', 5, TO_DATE('01.07.2024', 'dd.mm.yyyy')),
	(6, 'Bu kitob judayam hayotiy, bu kitobdan ancha narsa o''rgandim', 5, TO_DATE('23.11.2024', 'dd.mm.yyyy')),
	(7, NULL, 5, TO_DATE('12.12.2024', 'dd.mm.yyyy')),
	(8, 'Kitob menga yoqdi', 5, TO_DATE('15.11.2024', 'dd.mm.yyyy')),
	(9, 'Ajoyib ilmiy kitob ekan', 4, TO_DATE('21.07.2024', 'dd.mm.yyyy')),
	(10, NULL, 3, TO_DATE('01.05.2024', 'dd.mm.yyyy'));

SELECT * FROM kitob_sharhlari;

SELECT ism || ' - ' || mamlakat FROM mualliflar;

SELECT * FROM kitoblar ORDER BY kitob_nomi;

SELECT * FROM kitoblar WHERE janr = 'Roman';

SELECT * FROM mualliflar FETCH FIRST 4 ROW ONLY;
SELECT * FROM mualliflar OFFSET 3 LIMIT 6;

SELECT * FROM kitoblar WHERE janr IN ('Doston', 'Roman');

SELECT * FROM kitoblar 
WHERE narx BETWEEN 45000 AND 60000;

SELECT * FROM mualliflar WHERE ism LIKE '%Navoiy';

SELECT * FROM kitob_sharhlari
WHERE sharh IS NULL;

SELECT * FROM mualliflar 
JOIN kitoblar ON kitoblar.muallif_id = mualliflar.muallif_id
JOIN nashriyotlar ON nashriyotlar.nashriyot_id = kitoblar.nashriyot_id
JOIN kitob_sharhlari ON kitob_sharhlari.kitob_id = kitoblar.kitob_id;

