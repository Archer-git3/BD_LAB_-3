

CREATE TABLE game(
	game_id char(50) NOT NULL,
	name_game char(255) NOT NULL,
	developer char(255) NOT NULL,
	release_date date NOT NULL,
	price_for_game float NOT NULL
);

CREATE TABLE gamegenres
(
  game_id     char(50)        NOT NULL ,
  genres_name    char(50)  NOT NULL 
);

CREATE TABLE rating(
	game_id char(50) NOT NULL,
	date_rating date NOT NULL,
	positive_rating int NOT NULL,
	negative_rating int NOT NULL);


ALTER TABLE gamegenres ADD CONSTRAINT PK_gamegenres PRIMARY KEY (game_id, genres_name);
ALTER TABLE game ADD CONSTRAINT PK_game PRIMARY KEY (game_id);
ALTER TABLE rating ADD CONSTRAINT PK_rating PRIMARY KEY (game_id);


ALTER TABLE gamegenres ADD CONSTRAINT FK_GameGenres_Game 
FOREIGN KEY (game_id) REFERENCES game (game_id);

ALTER TABLE rating
ADD CONSTRAINT FK_game_rating FOREIGN KEY (game_id) REFERENCES game(game_id);

