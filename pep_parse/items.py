from scrapy import Field, Item


class PepParseItem(Item):
    number = Field()
    name = Field()
    status = Field()
