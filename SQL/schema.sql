-- CREATE TYPE roles AS ENUM ('regular', 'admin');
CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    login varchar(60) NOT NULL,
    password varchar(60) NOT NULL,
    role roles NOT NULL
);

CREATE TABLE IF NOT EXISTS companies (
    company_id SERIAL PRIMARY KEY,
    name VARCHAR(60) NOT NULL,
    description VARCHAR(2000),
    foundation_date DATE NOT NULL,
    ceo VARCHAR(60)
);

CREATE TABLE IF NOT EXISTS games (
    game_id SERIAL PRIMARY KEY,
    company_id INTEGER NOT NULL REFERENCES companies(company_id),
    name VARCHAR(60) NOT NULL,
    description VARCHAR(2000),
    release_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS reviews (
    review_id SERIAL PRIMARY KEY,
    game_id INTEGER NOT NULL REFERENCES games(game_id),
    user_id INTEGER NOT NULL REFERENCES users(user_id),
    content VARCHAR(2000) NOT NULL,
    rating SMALLINT NOT NULL,
    creation_date DATE NOT NULL,
    edit_date DATE
);

CREATE TABLE IF NOT EXISTS screenshots (
    screenshot_id SERIAL PRIMARY KEY,
    game_id INTEGER NOT NULL REFERENCES games(game_id),
    file_name VARCHAR(256) NOT NULL,
    thumnnail_name VARCHAR(256) NOT NULL
);