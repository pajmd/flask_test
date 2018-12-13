import pytest
import sys


def test_attributes():
    # object doesn't have a dictionary nor it's instances
    o = object()
    assert '__dict__' not in dir(object)
    assert '__dict__' not in dir(o)

    # therefore adding and atttibute on the fly will raise an exception
    with pytest.raises(AttributeError):
        o.stuff = 'stuff'

    class Stuff(object):
        pass

    # a class derived from obect receives a dictionay
    assert '__dict__' in dir(Stuff)

    # an instance of a class having a dictionay __dict__
    # receives its own dictionary __dict__
    a = Stuff()
    assert '__dict__' in dir(a)

    # to add an attibute one can use the dot notation
    # or the api function setattr(x,y,z)
    a.new_atr = 'xyz'
    setattr(a, 'other_attr', 'abc')
    assert a.other_attr == 'abc'

    # Adding an attribute to the instance puts it
    # in the instance dictionry
    a.stuff = "stuffy"

    # dictionary of a class differs fron an instance
    assert a.__dict__['stuff'] == 'stuffy'
    assert 'stuff' in a.__dict__
    assert 'stuff' not in Stuff.__dict__

    # stuff attribute is in the lists of attribute of the instance
    # not the class
    assert 'stuff' in dir(a)
    assert 'stuff' not in dir(Stuff)

    # dir(instance) lists all attribute on the
    # class and the instance
    assert '__class__' in dir(a)
    assert '__class__' in dir(Stuff)
    assert a.__class__ != Stuff.__class__

    # adding an attribute to the class
    Stuff.stuff2 = 'stuff2'

    # stuff2 attribute shows on both the class and the instance
    assert 'stuff2' in dir(Stuff)
    assert 'stuff2' in dir(a)

    # the stuff2 attribute shows only in the class dictionary
    assert 'stuff2' in Stuff.__dict__
    assert not 'stuff2' in a.__dict__

    print("Stuff attributes: \n%s" % dir(Stuff))
    print("a attributes: \n%s" % dir(a))
    a.__dict__['stuffz'] = 'stuffyz'
    assert a.stuffz == 'stuffyz'
    print("a dictionary: \n%s" % a.__dict__)

    # we can set an attribute to an object only if it allows it
    # i.e. it has a __dict__
    setattr(a, 'stuff3', 'astuff3')
    assert a.__dict__['stuff3'] == 'astuff3'
    with pytest.raises(AttributeError):
        setattr(o, 'some_attr', 'attrval')

    print("Stuff dictionary: \n%s" % Stuff.__dict__)
    print("Stuff attributes: \n%s" % dir(Stuff))

    # __getitem__, __setitem__ are implemented by container classes

    #print("a.getitem('stuff')" % a.__getitem__('stuff'))
    # print("Stuff.getitem('stuff3')" % Stuff.getitem('stuff3'))

    att = getattr(a, 'stuff')

    assert a.stuff == "stuffy"


def _test_container_item():
    # container being list, tuple,dict, set
    class Cont(dict):
        def __setitem__(self, key, value):
            pass

    c = Cont()

    # This notation [] uses __setitem__
    # raises an exception because setitem is overriden with pass
    #
    c[1] = 'un'
    with pytest.raises(KeyError):
        un = c[1]
    # assert c[1] == 'un'

    class Cont2(dict):
        pass

    c = Cont2()
    c.deux = 2
    assert c.deux == 2
    assert c['deux'] == 2
    print("c['deux'] = %d" % c['deux'])

    d = dict()
    # We can't call __setitem__ on a dict
    # but we can on a object that derives a dict
    with pytest.raises(AttributeError):
        d.trois = 3
    d[4] = 'quatre'
    assert d[4] == 'quatre'

    print("Cont attibutes: \n%s"%dir(Cont))
    print("dict attibutes: \n%s"%dir(dict))


def test_using_slots():
    class Dicty(object):
        pass

    class Slotty(object):
        __slots__ = ['stuff']

    s = Slotty
    s.stuff = 'stuff'
    assert s.stuff == 'stuff'
    print("size of slotty: %d" % sys.getsizeof(s))
    d = Dicty()
    d.stuff = 'stuff'
    print("size of dicty: %d" % sys.getsizeof(d))
