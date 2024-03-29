CREATE TABLE hotels (
    room_num TEXT NOT NULL,
    ckeck_in TEXT NOT NULL,
    check_out TEXT NOT NULL,
    grade TEXT NOT NULL
);

ALTER TABLE hotels
ADD COLUMN price INTEGER NOT NULL;

ALTER TABLE hotels RENAME COLUMN ckeck_in to check_in;

INSERT INTO hotels
VALUES
    ('B203', '2021-12-31', '2022-01-03', 'suit', 900),
    ('1102', '2022-01-04', '2022-01-08', 'suit', 850),
    ('303', '2022-01-01', '2022-01-03', 'deluxe', 500),
    ('807', '2021-01-04', '2022-01-07', 'superior', 300),
    ('B205', '2022-01-04', '2022-01-07', 'deluxe', 550);

UPDATE hotels
SET check_in = '2022-01-04' WHERE room_num = 807;

SELECT * FROM hotels WHERE room_num LIKE 'B%' OR grade ='deluxe';
