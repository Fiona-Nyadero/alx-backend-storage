-- a SQL script that creates a function
-- I didn't even know you could do that

DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
BEGIN
	RETURN IF(b = 0, 0, a / b);
END //
DELIMITER ;
