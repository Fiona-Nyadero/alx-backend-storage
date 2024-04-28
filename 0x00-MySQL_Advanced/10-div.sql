-- a SQL script that creates a function
-- I didn't even know you could do that

DELIMETER //

CREATE
	FUNCTION [IF NOT EXISTS] SafeDiv(a INT, b INT)
	RETURNS FLOAT
	BEGIN
		DECLARE ret_val INT;

		IF b = 0 THEN
			SET ret_val = 0;
		ELSE
			SET ret_val = a / b;
		END IF;
		
		RETURN ret_val;
	END;

DELIMITER ;
