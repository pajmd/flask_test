import codecs


def test_string():

    # https://docs.python.org/dev/howto/unicode.html

    # the UNICODE codepoint goes up yo 0x10FFFF,
    # representing/enconding a character with 32 bits would be very inefficient as
    # most of the time we use character from 0-128 so enconding strategy where invented
    # like latin1 mostly for western languages and utf-8 wich supports all languages
    # code each character with 1 (western simple), 2, 3, or 4 bytes and 0 is excluded.
    ch = "漢字"

    # in Python 3 str and unicode are the same, and the python 2 str becaome byte()

    # s1 and s2 are just a representaion on the screen but if saved to a file
    # that was intended for a different system while saving one should specify
    # the encoding and while reading it the system should know in adavance
    # the encoding to read it correctly
    s1 = str("j'étais fatigué")
    s2 = u"j'étais fatigué"

    # en fait in python s1 would encoded in utf8 and s2 in lantin1
    # using two differents encoding shows different array contents
    b1 = bytearray(s1,encoding="utf-8")
    b2 = bytearray(s2,encoding="latin-1")
    print("\nbyte string s1 len %d b1 size %d" % (len(s1), len(b1)))
    print("unicode s2 len %d b2 size %d" % (len(s2), len(b2)))

    # for c in s1:
    #     print(c)
    # for c in s2:
    #     print(c)
    with open('/home/pjmd/tmp/temp1.txt', mode='w', encoding='utf-8') as f1:
        f1.write(s1)
    with open('/home/pjmd/tmp/temp2.txt', mode='w', encoding='latin-1') as f2:
        f2.write(s2)
    with open('/home/pjmd/tmp/temp1.txt', mode='r', encoding='latin-1') as f1:
        garbled = f1.read()
    # the 2 files have different lengths
    print("Garbled sring because the write and read encodings don't natch %s" % garbled)