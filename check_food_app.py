# 尝试导入并检查所有类
try:
    from food_app import OrderHistory, AddressManager, DishFavorite, CouponManager, DeliveryNote
    print("✅ 所有类导入成功！")
    
    # 检查每个类是否可实例化
    classes = [OrderHistory, AddressManager, DishFavorite, CouponManager, DeliveryNote]
    for cls in classes:
        obj = cls()
        print(f"✅ {cls.__name__} 类实例化成功")
except ImportError as e:
    print(f"❌ 导入失败：{e}")
    print("请检查food_app.py是否包含缺失的类，或文件是否保存正确")
except Exception as e:
    print(f"❌ 实例化失败：{e}")