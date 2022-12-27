DO $$
 DECLARE
     game_id   gamegenres.game_id%TYPE;
     genres_name gamegenres.genres_name%TYPE;

 BEGIN
     game_id := 000;
     genres_name := 'genres_name_';
     FOR counter IN 10...20
         LOOP
            INSERT INTO gamegenres (game_id, genres_name)
             VALUES (game_id || counter, genres_name || counter);
         END LOOP;
 END;
 $$
 
