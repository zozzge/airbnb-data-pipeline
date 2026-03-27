-- İlk 10 Satır
SELECT * FROM airbnb LIMIT 10;

--Sadece belirli sütunlar
SELECT host_id, name, neighbourhood_group FROM airbnb LIMIT 10;

-- Fiyatı 2002den büyük olanlar
SELECT name, price FROM airbnb WHERE price > '200';

-- Minimum nights 5'ten büyük olanlar
SELECT name, minimum_nights FROM airbnb WHERE minimum_nights > '5';

--En pahalı 10 listing
SELECT name, price, neighbourhood_group FROM airbnb ORDER BY price DESC LIMIT 10;

--En ucuz 10 listing
SELECT name, price, neighbourhood_group FROM airbnb ORDER BY price ASC LIMIT 10;

-- Fiyatı 100'den düşük ve review sayısı 50'den fazla olanlar
SELECT name, price, reviews_per_month FROM airbnb WHERE price < 100 AND number_of_reviews > 50;

--Manhattan'da olup fiyatı 150'den büyük olanlar
SELECT name, neighbourhood_group, price FROM airbnb WHERE neighbourhood_group = 'Manhattan' AND price > 150;

-- Manhattan veya Brooklyn'de olanlar
SELECT name, neighbourhood_group FROM airbnb WHERE neighbourhood_group = 'Manhattan' OR neighbourhood_group = 'Brooklyn';

--IN kullanımı
SELECT name, neighbourhood_group FROM airbnb WHERE neighbourhood_group IN ('Manhattan','Brooklyn');

--LIKE kullanımı 
SELECT name, room_type FROM airbnb WHERE name LIKE '%Private%';

--IS NULL kontrolü
SELECT name, last_review FROM airbnb WHERE last_review IS NULL LIMIT 10;

--Ortalama price
SELECT AVG(price) AS avg_price  FROM airbnb;

--En çok review alan 10 listingi getir
SELECT reviews_per_month FROM airbnb ORDER BY reviews_per_month DESC LIMIT 10;

--Price > 200 ve number_of_reviews > 20 olan listingleri getir
SELECT price, number_of_reviews FROM airbnb WHERE price >200 AND number_of_reviews>20;

--Hangi bölgeler pahalı (GROUP BY aggregation)
SELECT neighbourhood_group, COUNT(*) AS listing_count, AVG(price) AS avg_price, MAX(price) AS max_price
FROM airbnb
GROUP BY neighbourhood_group
ORDER BY avg_price DESC;

--HAVING (GROUP BY için WHERE clause) where satır filtrler, having grup fltreler
SELECT neighbourhood_group, AVG(price) AS avg_price
FROM airbnb
GROUP BY neighbourhood_group
HAVING AVG(price) > 150;

--CASE WHEN (if else gibi)
SELECT name, price,
				CASE 
							WHEN price < 100 THEN 'Cheap'
							WHEN price < 200 THEN 'Medium'
							ELSE 'Expensive'
				END AS price_category
FROM airbnb;

--Aynı hostları tekrar tekrar saymaz
SELECT COUNT (DISTINCT host_id)
FROM airbnb;

--Window functions (veriyi gruplamadan, satır satır ama grup bağlamında analiz yapmanı sağlar)
--RANK()
SELECT name, price,
				RANK() OVER ( ORDER BY price DESC) AS price_rank
FROM airbnb;

--PARTITION BY
SELECT 
    name, 
    price,
    RANK() OVER (
        PARTITION BY neighbourhood_group 
        ORDER BY price DESC
    ) AS rank
FROM airbnb;

--Subquery
SELECT name, price
FROM airbnb
WHERE price > (
				SELECT AVG(price)
				FROM airbnb
);

--LIMIT + OFFSET en pahalı 10'u atlar sonraki 10'u getirir.
SELECT name, price
FROM airbnb
ORDER BY price DESC
LIMIT 10 OFFSET 10;

--NULL
SELECT name, price
FROM airbnb
WHERE last_review IS NULL;

--coalesce NULL değerleri başka değerle değiştirir
SELECT 
				name, 
				price,
				
				COALESCE(reviews_per_month, 0)
FROM airbnb;

--NULL değeri ortalamayla değiştirme
SELECT 
    name, 
    price,
    COALESCE(
        reviews_per_month, 
        (SELECT AVG(reviews_per_month) FROM airbnb)
    ) AS reviews_per_month
FROM airbnb;

