# #방법 1
# import theater_module
# theater_module.price(3)  # 3명 영화 가격
# theater_module.price_morning(4)  # 4명 조조 영화 가격
# theater_module.price_soldier(5)  # 5명 군인 영화 가격

# #방법 2
# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# #방법 3
# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# #방법 4
# from theater_module import price, price_morning
# price(5)
# price_morning(6)
# #price_soldier(7) #오류 발생

# 방법 5
from theater_module import price_soldier as price
price(5)
