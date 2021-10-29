INSERT INTO users VALUES
    (DEFAULT, 'user1', 'pass1', 'regular'),
    (DEFAULT, 'user2', 'pass2', 'regular'),
    (DEFAULT, 'user3', 'pass3', 'admin');

INSERT INTO companies VALUES
    (DEFAULT, 'Ubisoft', 'text', '2021-10-10', 'text'),
    (DEFAULT, 'Electronic Arts', null, '2021-10-10', null),
    (DEFAULT, 'Rockstar', null, '2021-10-10', null);

INSERT INTO games VALUES
    (DEFAULT, 1, 'Far Cry 6', 'text', '2021-10-10'),
    (DEFAULT, 2, 'Battlefiled 6', null, '2021-10-10'),
    (DEFAULT, 3, 'Grand Theft Auto 5', null, '2021-10-10');

INSERT INTO reviews VALUES
    (DEFAULT, 1, 1, 'review', 76, '2021-11-11', '2021-11-12'),
    (DEFAULT, 1, 3, 'review', 84, '2021-11-11', null),
    (DEFAULT, 2, 2, 'review', 95, '2021-11-11', null);

INSERT INTO screenshots VALUES
    (DEFAULT, 1, 'screenshot1', 'thumbnail1'),
    (DEFAULT, 1, 'screenshot2', 'thumbnail2'),
    (DEFAULT, 1, 'screenshot3', 'thumbnail3');