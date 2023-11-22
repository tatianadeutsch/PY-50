# # 3
# division = 5/0
# print(division)


# # 4
# try:
#     division = 5/0
# except ZeroDivisionError:
#     print("На ноль делить нельзя!")


# # 4
# try:
#     a = "1" + 1
# except:
#     raise TypeError ("Значение не соответствует типу данных")

import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")


x = 1
y = "1"

logging.info(f"Значения x и y - {x} и {y}.")
try:
    a = x + y
    logging.info(f"Результат сложения x и y: {x / y}.")
    raise TypeError("Значение не соответствует типу данных")
except:
    logging.error("TypeError, значение не соответствует типу данных", exc_info=True)
    print("Значение не соответствует типу данных")


