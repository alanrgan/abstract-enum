class EnumItem(object):
    def __init__(self, enum, name, cls):
        self.cls = cls
        self.enum = enum
        self.name = name

    def __getattr__(self, name):
        return getattr(self.cls, name)

    def __repr__(self):
        return "<{}.{}>".format(self.enum, self.name)

class AbstractEnum(object):
    _items = []
    _item_cls = EnumItem

    @classmethod
    def initialize(cls, *base):
        cls._items = []
        cls.populate(*base)
                    
    class __metaclass__(type):
        def __iter__(self):
            for c in self._items:
                yield c
    
    @classmethod
    def populate(cls, *base):
        flatten = lambda l: [x for sublist in l for x in sublist]
        subclasses = flatten(map(lambda b: b.__subclasses__(), base))
        setattr(cls, '_base', subclasses)
        for sc in subclasses:
            if sc not in base:
                name = getattr(sc, '__alias__', sc.__name__).upper()
                if not hasattr(cls, name):
                    item = cls._item_cls(enum=cls.__name__, name=name, cls=sc)
                    setattr(cls, name, item)
                    cls._items.append(item)
    
    @classmethod
    def register(cls, name, othercls):
        item = Item(name=name, cls=othercls)
        setattr(cls, name, item)
        cls._items.append(item)

    @classmethod
    def set_item_class(cls, item_cls):
        if not issubclass(item_cls, EnumItem):
            raise TypeError('Item class must be a subclass of EnumItem')
        else:
            cls._item_cls = item_cls