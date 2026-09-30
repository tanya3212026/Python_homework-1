from address import Address
from mailing import Mailing

from_addr = Address(
    code="154320",
    city="Рига",
    street="Квыжановски",
    building="1",
    apt="20",
)

to_addr = Address(
    code="356782",
    city="Москва",
    street="Пречистенка",
    building="17",
    apt="5",
)

mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=1550,
    track="RU123456789",
)

print(mailing)
