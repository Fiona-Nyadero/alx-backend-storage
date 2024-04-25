--trigger resets the attribute valid_emaili
-- when email is changed

CREATE TRIGGER reset_email_trigger
BEFORE UPDATE ON users
FOR EACH ROW
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
