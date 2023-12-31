INSERT INTO fumos_app_fumomodel (id, fumo_name, release_year, fumo_price, fumo_size, url_img, fumo_serie_id, stock) VALUES
(1, 'FumoFumo Reimu Hakurei Ver 1.0', 2008, 14990, '20cm', 'foto_fumo/fumo_1.jpg', 1, 100),
(2, 'FumoFumo Reimu Hakurei Nendroid Plus', 2010, 2500, '25cm', 'foto_fumo/nendoroid_2.jpg', 2, 50),
(3, 'FumoFumo Reimu Hakurei Puppet', 2009, 39990, '12cm', 'foto_fumo/puppet_1.jpg', 3, 10),
(4, 'FumoFumo Kirisame Marisa Puppet', 2009, 39990, '12cm', 'foto_fumo/puppet_2.jpg', 3, 20),
(5, 'FumoFumo Reimu Hakurei Toy Strap', 2019, 15990, '20cm', 'foto_fumo/strap_1.jpg', 4, 30),
(6, 'FumoFumo Reimu Hakurei Toy Strap Ver 2', 2019, 15990, '12cm', 'foto_fumo/strap_2.jpg', 4, 40),
(7, 'FumoFumo Kirisame Marisa Toy Strap', 2019, 15990, '12cm', 'foto_fumo/strap_3.jpg', 4, 50),
(8, 'FumoFumo Komeiji Satori Toy Strap', 2019, 15990, '12cm', 'foto_fumo/strap_4.jpg', 4, 60),
(9, 'FumoFumo Komeiji Koishi Toy Strap', 2019, 15990, '12cm', 'foto_fumo/strap_5.jpg', 4, 70),
(10, 'FumoFumo Scarlet Remilia Toy Strap', 2019, 15990, '12cm', 'foto_fumo/strap_6.jpg', 4, 80),
(11, 'FumoFumo Scarlet Flandre Toy Strap', 2019, 15990, '12cm', 'foto_fumo/strap_7.jpg', 4, 90),
(12, 'FumoFumo Izayoi Sakuya Toy Strap', 2019, 15990, '12cm', 'foto_fumo/strap_8.jpg', 4, 100),
(13, 'FumoFumo Reimu Hakurei Deka Ver 1', 2009, 40990, '60cm', 'foto_fumo/deka_1.jpg', 5, 15),
(14, 'FumoFumo Kirisame Marisa Deka Ver 1', 2009, 40990, '60cm', 'foto_fumo/deka_2.jpg', 5, 25),
(15, 'FumoFumo Cirno Deka', 2009, 40990, '60cm', 'foto_fumo/deka_3.jpg', 5, 35),
(16, 'FumoFumo Scarlet Remilia Deka', 2009, 40990, '60cm', 'foto_fumo/deka_4.jpg', 5, 45),
(17, 'FumoFumo Scarlet Flandre Deka', 2009, 40990, '60cm', 'foto_fumo/deka_5.jpg', 5, 55),
(18, 'FumoFumo Kirisame Marisa (Kourindou Version) Deka', 2019, 40990, '60cm', 'foto_fumo/deka_6.jpg', 5, 65),
(19, 'FumoFumo Hakurei Reimu (Kourindou Version) Deka', 2019, 40990, '60cm', 'foto_fumo/deka_7.jpg', 5, 75),
(20, 'FumoFumo Kirisame Marisa (Kourindou Version) Ver 2 Deka', 2019, 40990, '60cm', 'foto_fumo/deka_8.jpg', 5, 85),
(21, 'FumoFumo Komeiji Satori Deka', 2019, 40990, '60cm', 'foto_fumo/deka_9.jpg', 5, 95),
(22, 'FumoFumo Komeiji Koishi Deka', 2019, 40990, '60cm', 'foto_fumo/deka_10.jpg', 5, 105),
(23, 'FumoFumo Scarlet Remilia Ver 2 Deka', 2019, 40990, '60cm', 'foto_fumo/deka_11.jpg', 5, 115),
(24, 'FumoFumo Scarlet Flandre Ver 2 Deka', 2019, 40990, '60cm', 'foto_fumo/deka_12.jpg', 5, 125),
(25, 'FumoFumo Izayoi Sakuya Deka', 2019, 40990, '60cm', 'foto_fumo/deka_13.jpg', 5, 135);

INSERT INTO fumos_app_fumoseriesmodel (id, name_series)
VALUES 
(1, 'Fumo'),
(2, 'Nendoroid'),
(3, 'Puppet'),
(4, 'Strap'),
(5, 'Deka');

INSERT INTO usuario_app_regionmodel (id, region_name) VALUES 
(1, 'METROPOLITANA DE SANTIAGO');

INSERT INTO usuario_app_communemodel (id, commune_name, region_id) VALUES
(1, 'SAN BERNARDO',1),
(2, 'PEÑAFLOR',1);