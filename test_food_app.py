import unittest
# 从功能文件导入所有需要测试的类
from food_app import OrderHistory, AddressManager, DishFavorite, CouponManager, DeliveryNote

# 测试订单历史
class TestOrderHistory(unittest.TestCase):
    def test_add_order(self):
        oh = OrderHistory()
        oh.add_order("001", "Burger", 20.0)
        self.assertEqual(len(oh.get_orders()), 1)

    def test_empty_order_history(self):
        oh = OrderHistory()
        self.assertEqual(oh.get_orders(), [])

# 测试地址管理
class TestAddressManager(unittest.TestCase):
    def test_add_delete_address(self):
        am = AddressManager()
        am.add_address("Home", "123 Main St", "13800138000")
        self.assertEqual(len(am.get_addresses()), 1)
        am.delete_address("Home")
        self.assertEqual(len(am.get_addresses()), 0)

# 测试菜品收藏
class TestDishFavorite(unittest.TestCase):
    def test_favorite_operations(self):
        df = DishFavorite()
        df.add_favorite("Burger")
        self.assertTrue(df.is_favorite("Burger"))
        df.remove_favorite("Burger")
        self.assertFalse(df.is_favorite("Burger"))

# 测试优惠券管理
class TestCouponManager(unittest.TestCase):
    def test_coupon_operations(self):
        cm = CouponManager()
        cm.redeem_coupon("满20减5")
        self.assertEqual(cm.get_available_coupons(), ["满20减5"])
        cm.use_coupon("满20减5")
        self.assertEqual(cm.get_available_coupons(), [])

# 测试配送备注
class TestDeliveryNote(unittest.TestCase):
    def test_note_operations(self):
        dn = DeliveryNote()
        dn.add_note("001", "Leave at door")
        self.assertEqual(dn.get_note("001"), "Leave at door")

# 集成测试（功能协作）
class TestIntegration(unittest.TestCase):
    def test_user_order_workflow(self):
        am = AddressManager()
        am.add_address("Home", "123 St", "13800138000")
        cm = CouponManager()
        cm.redeem_coupon("满20减5")
        oh = OrderHistory()
        oh.add_order("001", "Burger", 20.0)
        dn = DeliveryNote()
        dn.add_note("001", "Leave at door")

        self.assertEqual(len(am.get_addresses()), 1)
        self.assertEqual(cm.get_available_coupons(), ["满20减5"])
        self.assertEqual(dn.get_note("001"), "Leave at door")

# 测试执行入口
if __name__ == "__main__":
    unittest.main()