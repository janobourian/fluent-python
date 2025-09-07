import unittest
from ch01_data_model.assessment import Deck, Vector2D, Basket, Book

class TestDeck(unittest.TestCase):
    
    def setUp(self):
        self.deck = Deck()
    
    def test_deck_len_is_52(self):
        self.assertEqual(len(self.deck), 52)
    
    def test_indexing_returns_card(self):
        self.assertEqual(self.deck[0], 'A - spades')
        self.assertEqual(self.deck[12], 'K - spades')
        self.assertEqual(self.deck[13], 'A - hearts')
        self.assertEqual(self.deck[25], 'K - hearts')
        self.assertEqual(self.deck[51], 'K - clubs')
    
    def test_slicing_returns_list_of_cards(self):
        self.assertEqual(self.deck[0:3], ['A - spades', '2 - spades', '3 - spades'])
        self.assertEqual(self.deck[12:15], ['K - spades', 'A - hearts', '2 - hearts'])
        self.assertEqual(self.deck[25:28], ['K - hearts', 'A - diamonds', '2 - diamonds'])
        self.assertEqual(self.deck[38:41], ['K - diamonds', 'A - clubs', '2 - clubs'])
        self.assertEqual(self.deck[50:53], ['Q - clubs', 'K - clubs'])
    
    def test_iteration_covers_all_cards(self):
        cards = [card for card in self.deck]
        self.assertEqual(len(cards), 52)
        self.assertEqual(cards[0], 'A - spades')
        self.assertEqual(cards[-1], 'K - clubs')
    
    def test_choice_returns_member_of_deck(self):
        import random
        card = random.choice(self.deck)
        self.assertIn(card, self.deck)

class TestVector2D(unittest.TestCase):
    
    def test_addition(self):
        v1 = Vector2D(2, 3)
        v2 = Vector2D(4, 5)
        v3 = v1 + v2
        self.assertEqual(v3.x, 6.0)
        self.assertEqual(v3.y, 8.0)

    def test_scalar_multiplication(self):
        v = Vector2D(2, 3)
        v2 = v * 3
        self.assertEqual(v2.x, 6.0)
        self.assertEqual(v2.y, 9.0)
    
    def test_magnitude(self):
        v = Vector2D(3, 4)
        self.assertEqual(abs(v), 5.0)
    
    def test_boolean_evaluation(self):
        v1 = Vector2D(0, 0)
        v2 = Vector2D(1, 1)
        self.assertFalse(bool(v1))
        self.assertTrue(bool(v2))
    
    def test_representation(self):
        v = Vector2D(2, 3)
        self.assertEqual(repr(v), 'Vector2D(2.0, 3.0)')
        self.assertEqual(str(v), '(2.0, 3.0)')

class TestBasket(unittest.TestCase):
    
    def setUp(self):
        self.basket = Basket()
    
    def test_empty_basket_is_false(self):
        self.assertFalse(bool(self.basket))
    
    def test_non_empty_basket_is_true(self):
        self.basket.add('apple', 2)
        self.assertTrue(bool(self.basket))
    
    def test_len_reflects_number_of_items(self):
        self.basket.add('apple', 2)
        self.basket.add('banana', 3)
        self.assertEqual(len(self.basket), 5)
        self.basket.add('orange', 1)
        self.assertEqual(len(self.basket), 6)
        self.basket.add('banana', 2)
        self.assertEqual(len(self.basket), 8)
        self.basket.clear()
        self.assertEqual(len(self.basket), 0)

class TestBook(unittest.TestCase):
    
    def setUp(self):
        self.book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    
    def test_str_representation(self):
        self.assertEqual(str(self.book), "The Great Gatsby by F. Scott Fitzgerald (1925)")
    
    def test_repr_representation(self):
        self.assertEqual(repr(self.book), "Book(title='The Great Gatsby', author='F. Scott Fitzgerald', year=1925)")