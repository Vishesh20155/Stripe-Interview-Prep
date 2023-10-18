from shopping_cart import ShoppingCart
from item_database import ItemDatabase
from unittest.mock import Mock
import pytest

def test_add_item():
    cart = ShoppingCart(5)
    cart.add('apple')
    print('hello')
    assert cart.size() == 1
    
def test_overflow():
    cart = ShoppingCart(3)
    
    for i in range(3):
        cart.add('apple')
        
    with pytest.raises(OverflowError):
        cart.add('apple')
        
def test_mock():
    print("Hello")
    cart = ShoppingCart(5)
    cart.add('apple')
    cart.add('orange')

    item_db = ItemDatabase()
    
    def mock_item(item: str) -> float:
        if item == "apple":
            return 1.0
        else:
            return 2.0

    item_db.get = Mock(side_effect=mock_item)
    
    assert cart.get_total_price(item_db) == 3.0