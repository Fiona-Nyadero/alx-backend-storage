-- triggers a reduction in quantity of an object
-- after adding a new order

CREATE TRIGGER dec_trigger AFTER INSERT ON orders 
FOR EACH ROW
	UPDATE items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
