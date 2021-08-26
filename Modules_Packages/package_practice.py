# import travle.thailand #import~에서는 class는 불러올 수 x
# trip_to = travle.thailand.ThailandPackage()
# trip_to.detail()

# from travle.thailand import ThailandPackage #from~import~에서는 class 불러올 수 o
# trip_to = ThailandPackage()
# trip_to.detail()

# from travle import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

from Modules_Packages.travle import thailand
from travle import *
trip_to = vietnam.VietnamPackage()  # __init__.py에 적어 공개된 파일
# trip_to = thailand.ThailandPackage() #공개되지 않은 파일 -> 오류 발생
trip_to.detail()
