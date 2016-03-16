sqlite3 site.db

CREATE TABLE `users` (
    `uid` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    `name` varchar(255) NOT NULL
);

CREATE TABLE `messages` (
    `uid` INTEGER NOT NULL,
    `msg` TEXT
);

SELECT `name`, COUNT(`msg`)  FROM `users`, `messages` WHERE `users`.`uid` = `messages`.`uid`;