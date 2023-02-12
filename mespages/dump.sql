CREATE TABLE IF NOT EXISTS posts (
id INTEGER PRIMARY KEY,
title varchar(255),
content text,
user_id integer,
date date
);
CREATE TABLE IF NOT EXISTS scripts (
id INTEGER PRIMARY KEY,
title varchar(255),
content text,
user_id integer,
date date);
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY,
email varchar(256),
password varchar(256)
);
