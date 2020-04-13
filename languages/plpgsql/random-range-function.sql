-- returns random integers in a given range

CREATE OR REPLACE FUNCTION random_range(low INT, high INT) 
    RETURNS INT AS
$$
BEGIN
    RETURN floor(random() * (high - low + 1) + low);
END;
$$ language 'plpgsql' STRICT; 
