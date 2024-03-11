
import collections
from collections import defaultdict

# collections defaultdict()

d = {
    "красные утята": 0,
    "Зеленые утята": 0,
    "желтые утята": 0
}

d["красные утята"] += 1 # так прибавляется 1 к значению по ключу красные утята
d["синий утенок"] = 1 # так присваиваем дефолт значение неизвестному ключу
d["синий утенок"] += 1 # так не добавится сразу по неизвестному ключу пока мы не присвоим дефолт значение - например 0, чтобы к нему прибавлять.

# позволяет с этим справиться функция defaultdict(int)

d = defaultdict(int)

d["какой-то неизвестный утенок"] += 1 #тут не надо заранее присваивать дефолт, будет присваиваться само

print(d)


from collections import namedtuple

region_city_pair = namedtuple("region_city_pair", ["region", "city"])

ekb = region_city_pair(region=66, city="Екатеринбург")
print(ekb) # можем обращаться через точку ekb.city или ekb.region
print(tuple(ekb))

from dataclasses import dataclass #тоже самое будет что и выше про namedtuple но это посовременнее

@dataclass
class RegionCityPair:
    region: int
    city: str

# collections.OrderDict

from collections import OrderedDict

d = OrderedDict()
d["key"] = "value"
d["other"] = "123"

# Теперь можно просто dict использовать, теперь всегда сортируется по порядку - orderDict использовали в старых версиях питона

