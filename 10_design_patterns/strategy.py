from abc import ABC, abstractmethod
from collections.abc import Sequence
from decimal import Decimal
from typing import NamedTuple, Optional

class Customer(NamedTuple):
    name: str
    fidelity: int

class LineItem(NamedTuple):
    product: str
    quantity: int
    price: Decimal
    
    def total(self) -> Decimal:
        return self.price * self.quantity

class Order(NamedTuple):
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional['Promotion'] = None
    
    def total(self) -> Decimal:
        return sum(item.total() for item in self.cart)
    
    def due(self) -> Decimal:
        if self.promotion is None:
            discount = Decimal('0')
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount
    
    def __repr__(self) -> str:
        return f'<Order total: {self.total():.2f} due: {self.due():.2f}>'

class Promotion(ABC):
    @abstractmethod
    def discount(self, order: Order) -> Decimal:
        """Return discount as a positive dollar amount"""
        pass

class FidelityPromo(Promotion):
    def discount(self, order: Order) -> Decimal:
        if order.customer.fidelity >= 1000:
            return order.total() * Decimal('0.05')
        return Decimal('0')

class BulkItemPromo(Promotion):
    def discount(self, order: Order) -> Decimal:
        discount = Decimal('0')
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * Decimal('0.1')
        return discount

class LargeOrderPromo(Promotion):
    def discount(self, order: Order) -> Decimal:
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * Decimal('0.07')
        return Decimal('0')