import unittest
import wroc
import random

class TestProbaAda(unittest.TestCase):

    #def test_p(self):
    #    self.assertTrue(True)

    def test_p1(self):
        w=wroc.f1(0)
        self.assertEqual(w,0)

    def test_p2(self):
        w=wroc.f1(1)
        self.assertEqual(w,1)

    def test_p3(self):
        w=wroc.f1(2)
        self.assertEqual(w,4)

    def test_p4(self):
        w=wroc.f1(2,1)
        self.assertEqual(w,5)

    def test_p5(self):
        w=wroc.f1(2,3)
        self.assertEqual(w,7)

    def test_p6(self):
        w=wroc.f2("ala")
        self.assertEqual(w,"a")

    def test_p7(self):
        w=wroc.f2([1,2,3])
        self.assertEqual(w,1)

    def test_p8(self):
        w=wroc.f2([])
        self.assertEqual(w,"BUUUUM")

    def test_p9(self):
        w=wroc.f3(1)
        self.assertEqual(w,"jeden")

    def test_p10(self):
        w=wroc.f3(2)
        self.assertEqual(w,"dwa")

    def test_p11(self):
        w=wroc.f3(3)
        self.assertEqual(w,"trzy")

    def test_p12(self):
        w=wroc.f3(random.choice(range(4,1000)))
        self.assertEqual(w,"other")

    def test_p13(self):
        w=wroc.f4("ala")
        self.assertEqual(w,"ala ma kota")

    def test_p14(self):
        w=wroc.f4("kot")
        self.assertEqual(w,"kot ma kota")

    def test_p15(self):
        w=wroc.f4("kot","psa")
        self.assertEqual(w,"kot ma kota i psa")

    def test_p16(self):
        w=wroc.f4("kot","mysz")
        self.assertEqual(w,"kot ma kota i mysz")

    def test_p17(self):
        w=wroc.f5(0)
        self.assertEqual(w,[])

    def test_p18(self):
        w=wroc.f5(1)
        self.assertEqual(w,[0])

    def test_p19(self):
        w=wroc.f5(2)
        self.assertEqual(w,[0,1])

    def test_p20(self):
        w=wroc.f5(7)
        self.assertEqual(w,[0,1,2,3,4,5,6])

    def test_p21(self):
        w=wroc.f5(7,2)
        self.assertEqual(w,[0,2,4,6])

    def test_p22(self):
        w=wroc.f5(17,2)
        self.assertEqual(w,[0,2,4,6,8,10,12,14,16])

    def test_p23(self):
        w=wroc.f5(17,5)
        self.assertEqual(w,[0,5,10,15])

    def test_p24(self):
        w=wroc.f6(1,"*")
        self.assertEqual(w,"*")

    def test_p25(self):
        w=wroc.f6(7,"*")
        self.assertEqual(w,"*******")

    def test_p26(self):
        w=wroc.f6(4,"A")
        self.assertEqual(w,"AAAA")

    def test_p27(self):
        w=wroc.f7("ala")
        self.assertEqual(w,"slowo")

    def test_p28(self):
        w=wroc.f7("1")
        self.assertEqual(w,"cyfra")

    def test_p29(self):
        w=wroc.f7("11111")
        self.assertEqual(w,"liczba")

    def test_p30(self):
        w=wroc.f7("-11111")
        self.assertEqual(w,"liczba ze znakiem")

    def test_p31(self):
        w=wroc.f7("Ala ma kota.")
        self.assertEqual(w,"zdanie")

    def test_p32(self):
        w=wroc.f7("<taaag>")
        self.assertEqual(w,"tag poczatkowy")

    def test_p33(self):
        w=wroc.f7("</taaag>")
        self.assertEqual(w,"tag koncowy")

if __name__ == '__main__':
    unittest.main()
