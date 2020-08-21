'''
:author: Emily Chen
:date:   2019

Any made-up words are marked with an '*'

'''
import unittest
from methods import classify_verb_root, \
                    convert_to_base_form, classify_noun_root

class TestConvert2BaseForm(unittest.TestCase):

    def test_ends_a(self):
        self.assertEqual('anipa', convert_to_base_form("anipa"))

    def test_ends_i(self):
        self.assertEqual('kufi', convert_to_base_form("kufi"))

    def test_ends_u(self):
        self.assertEqual('ulu', convert_to_base_form("ulu"))

    def test_ends_ae(self):
        self.assertEqual('tume', convert_to_base_form("tumae"))

    def test_ends_g(self):
        self.assertEqual('uyghag', convert_to_base_form("uyghak"))

    def test_ends_ghw(self):
        self.assertEqual('saaghw', convert_to_base_form("saaqw"))

    def test_ends_w(self):
        self.assertEqual('kiiw', convert_to_base_form("kiikw"))

    def test_ends_ta(self):
        self.assertEqual('piitute', convert_to_base_form("piituta"))

    def test_ends_n(self):
        self.assertEqual('piitute', convert_to_base_form("piitun"))


class TestClassifyVerbRoot(unittest.TestCase):

    #---------
    # Class 1
    #---------
    def test_ends_a(self):
        self.assertEqual(1, classify_verb_root("ifla"))

    def test_ends_i(self):
        self.assertEqual(1, classify_verb_root("aqii"))

    def test_ends_u(self):
        self.assertEqual(1, classify_verb_root("inghu"))

    #---------
    # Class 2
    #---------
    def test_ends_e_hop_CVCe(self):
        self.assertEqual(2, classify_verb_root("pike"))

    "*"
    def test_ends_e_hop_VCe(self):
        self.assertEqual(2, classify_verb_root("alle"))

    def test_ends_e_noHop_length(self):
        self.assertEqual(2, classify_verb_root("alinge"))

    def test_ends_e_noHop_doubleVowel(self):
        self.assertEqual(2, classify_verb_root("taaqe"))

    def test_ends_e_noHop_eSecondVow(self):
        self.assertEqual(2, classify_verb_root("neghe"))

    "*"
    def test_ends_eg_noHop_threeCns(self):
        self.assertEqual(2, classify_verb_root("qutke"))


    #---------
    # Class 3
    #---------
    def test_ends_w(self):
        self.assertEqual(3, classify_verb_root("aaw"))

    def test_ends_ghw(self):
        self.assertEqual(3, classify_verb_root("qiighw"))

    def test_ends_fullVowelG(self):
        self.assertEqual(3, classify_verb_root("ukig"))

    def test_ends_eg_hop_VCeg(self):
        self.assertEqual(6, classify_verb_root("alleg"))

    "*"
    def test_ends_eg_hop_CVCeg(self):
        self.assertEqual(6, classify_verb_root("talleg"))

    "*"
    def test_ends_eg_noHop_length(self):
        self.assertEqual(7, classify_verb_root("ruguguleg"))

    def test_ends_eg_noHop_doubleVowel(self):
        self.assertEqual(7, classify_verb_root("taaqeg"))

    def test_ends_eg_noHop_eSecondVow(self):
        self.assertEqual(7, classify_verb_root("keleg"))

    "*"
    def test_ends_eg_noDropOrHop_length(self):
        self.assertEqual(3, classify_verb_root("neg"))

    def test_ends_eg_noDropOrHop_threeCns(self):
        self.assertEqual(3, classify_verb_root("mamleg"))

    #---------
    # Class 4
    #---------
    def test_ends_agh(self):
        self.assertEqual(4, classify_verb_root("gaagh"))

    def test_ends_igh(self):
        self.assertEqual(4, classify_verb_root("nengigh"))

    def test_ends_ugh(self):
        self.assertEqual(4, classify_verb_root("mayugh"))

    #---------
    # Class 5
    #---------
    def test_ends_te(self):
        self.assertEqual(5, classify_verb_root("kaate"))

    #---------
    # Class 6 
    #---------
    def test_ends_egh_hop(self):
        self.assertEqual(6, classify_verb_root("itegh"))

    def test_ends_egh_noDropOrHop_threeCns(self):
        self.assertEqual(4, classify_verb_root("unglegh"))

    def test_ends_egh_noDropOrHop_length(self):
        self.assertEqual(4, classify_verb_root("legh"))

    #---------
    # Class 7
    #---------
    def test_ends_egh_noHop_length(self):
        self.assertEqual(7, classify_verb_root("aghyanegh"))

    "*"
    def test_ends_egh_noHop_doubleVowel(self):
        self.assertEqual(7, classify_verb_root("taaqegh"))

    def test_ends_egh_noHop_eSecondVow(self):
        self.assertEqual(7, classify_verb_root("nemegh"))


class TestClassifyNounRoot(unittest.TestCase):

    #---------
    # Class 1
    #---------
    def test_ends_a(self):
        self.assertEqual(1, classify_noun_root("anipa"))

    def test_ends_i(self):
        self.assertEqual(1, classify_noun_root("kufi"))

    def test_ends_u(self):
        self.assertEqual(1, classify_noun_root("ulu"))

    #---------
    # Class 2
    #---------
    def test_ends_w(self):
        self.assertEqual(2, classify_noun_root("aaw"))

    def test_ends_ghw(self):
        self.assertEqual(2, classify_noun_root("qiighw"))

    def test_ends_fullVowelG(self):
        self.assertEqual(2, classify_noun_root("panig"))

    "*"
    def test_ends_eg_hop_VCeg(self):
        self.assertEqual(7, classify_noun_root("alleg"))

    def test_ends_eg_hop_CVCeg(self):
        self.assertEqual(7, classify_noun_root("pilleg"))

    "*"
    def test_ends_eg_noHop_length(self):
        self.assertEqual(8, classify_noun_root("ruguguleg"))

    def test_ends_eg_noHop_doubleVowel(self):
        self.assertEqual(8, classify_noun_root("laageg"))

    def test_ends_eg_noHop_eSecondVow(self):
        self.assertEqual(8, classify_noun_root("kemeg"))

    def test_ends_eg_noDropOrHop_length(self):
        self.assertEqual(2, classify_noun_root("veg"))

    def test_ends_eg_noDropOrHop_threeCns(self):
        self.assertEqual(2, classify_noun_root("akleg"))

    #---------
    # Class 3
    #---------
    def test_ends_weak_agh(self):
        self.assertEqual(3, classify_noun_root("aghnagh"))

    def test_ends_weak_igh(self):
        self.assertEqual(3, classify_noun_root("aligh"))

    def test_ends_weak_ugh(self):
        self.assertEqual(3, classify_noun_root("nayugh"))

    #---------
    # Class 4
    #---------
    def test_ends_markedStrong_agh(self):
        self.assertEqual(4, classify_noun_root("afsengagh*"))

    def test_ends_markedStrong_igh(self):
        self.assertEqual(4, classify_noun_root("ayumigh*"))

    def test_ends_markedStrong_ugh(self):
        self.assertEqual(4, classify_noun_root("nanugh*"))

    #---------
    # Class 5
    #---------
    def test_ends_strong_aagh(self):
        self.assertEqual(5, classify_noun_root("neghqwaagh"))

    def test_ends_strong_iigh(self):
        self.assertEqual(5, classify_noun_root("kaviigh"))

    def test_ends_strong_uugh(self):
        self.assertEqual(5, classify_noun_root("suugh"))

    #---------
    # Class 6
    #---------
    def test_ends_te(self):
        self.assertEqual(6, classify_noun_root("riigte"))

    #---------
    # Class 7
    #---------
    def test_ends_egh_hop(self):
        self.assertEqual(7, classify_noun_root("alegh"))

    def test_ends_egh_noDropOrHop_length(self):
        self.assertEqual(5, classify_noun_root("megh"))

    def test_ends_egh_noDropOrHop_threeCns(self):
        self.assertEqual(5, classify_noun_root("naangnegh"))

    #---------
    # Class 8
    #---------
    def test_ends_egh_noHop_length(self):
        self.assertEqual(8, classify_noun_root("pukanegh"))

    "*"
    def test_ends_egh_noHop_doubleVowel(self):
        self.assertEqual(8, classify_noun_root("piinegh"))

    def test_ends_egh_noHop_eSecondVow(self):
        self.assertEqual(8, classify_noun_root("kenegh"))

    #---------
    # Class 9
    #---------
    def test_ends_e_hop_VCe(self):
        self.assertEqual(9, classify_noun_root("iye"))

    def test_ends_e_hop_CVCe(self):
        self.assertEqual(9, classify_noun_root("maye"))

    #----------
    # Class 10
    #----------
    def test_ends_e_noHop_length(self):
        self.assertEqual(10, classify_noun_root("piislaye"))

    def test_ends_e_noHop_doubleVowel(self):
        self.assertEqual(10, classify_noun_root("huuse"))

    def test_ends_e_noHop_eSecondVow(self):
        self.assertEqual(10, classify_noun_root("neqe"))




if __name__ == '__main__':
    unittest.main()
