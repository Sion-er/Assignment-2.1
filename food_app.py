# 订单历史类
class OrderHistory:
    def __init__(self):
        self.orders = []
    def add_order(self, order_id, dish, price):
        self.orders.append({"id": order_id, "dish": dish, "price": price})
    def get_orders(self):
        return self.orders

# 地址管理类
class AddressManager:
    def __init__(self):
        self.addresses = []
    def add_address(self, name, detail, phone):
        self.addresses.append({"name": name, "detail": detail, "phone": phone})
    def get_addresses(self):
        return self.addresses
    def delete_address(self, name):
        self.addresses = [a for a in self.addresses if a["name"] != name]

# 菜品收藏类
class DishFavorite:
    def __init__(self):
        self.favorites = []
    def add_favorite(self, dish):
        self.favorites.append(dish)
    def remove_favorite(self, dish):
        self.favorites.remove(dish)
    def is_favorite(self, dish):
        return dish in self.favorites

# 优惠券管理类
class CouponManager:
    def __init__(self):
        self.coupons = []
    def redeem_coupon(self, coupon):
        self.coupons.append(coupon)
    def get_available_coupons(self):
        return self.coupons
    def use_coupon(self, coupon):
        self.coupons.remove(coupon)

# 配送备注类
class DeliveryNote:
    def __init__(self):
        self.notes = {}
    def add_note(self, order_id, note):
        self.notes[order_id] = note
    def get_note(self, order_id):
        return self.notes.get(order_id, "")