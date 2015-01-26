#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>
# Date:    15.10.2014 10:22:43 CEST
# File:    tbexample.py

import sys
sys.path.append('../')
import z2pack

from common import *

import types
import unittest


class TbExampleTestCase(CommonTestCase):

    def createH(self, t1, t2):

        self.H = z2pack.tb.Hamilton()

        # create the two atoms
        self.H.add_atom(([1, 1], 1), [0, 0, 0])
        self.H.add_atom(([-1, -1], 1), [0.5, 0.5, 0])

        # add hopping between different atoms
        self.H.add_hopping(((0, 0), (1, 1)),
                           z2pack.tb.vectors.combine([0, -1], [0, -1], 0),
                           t1,
                           phase=[1, -1j, 1j, -1])
        self.H.add_hopping(((0, 1), (1, 0)),
                           z2pack.tb.vectors.combine([0, -1], [0, -1], 0),
                           t1,
                           phase=[1, 1j, -1j, -1])

        # add hopping between neighbouring orbitals of the same type
        self.H.add_hopping((((0, 0), (0, 0)), ((0, 1), (0, 1))),
                           z2pack.tb.vectors.neighbours([0, 1],
                                                        forward_only=True),
                           t2,
                           phase=[1])
        self.H.add_hopping((((1, 1), (1, 1)), ((1, 0), (1, 0))),
                           z2pack.tb.vectors.neighbours([0, 1],
                                                        forward_only=True),
                           -t2,
                           phase=[1])

    # this test may produce false negatives due to small numerical differences
    def test_res1(self):
        self.createH(0.2, 0.3)
        # call to Z2Pack
        tb_system = z2pack.tb.System(self.H)
        tb_plane = tb_system.plane(1, 2, 0)
        tb_plane.wcc_calc(verbose=False, num_strings=20, use_pickle=False)
        
        res = {'wcc': [[0.49983964546467036, 0.50016035453532992], [0.49890749383729088, 0.50109250616270928], [0.49641395036486252, 0.50358604963513764], [0.49554883941587446, 0.50445116058412554], [0.49652567629394373, 0.5034743237060566], [0.49035854882904767, 0.50964145117095228], [0.48929271594465651, 0.51070728405534349], [0.48629705364229231, 0.51370294635770786], [0.48121568261281716, 0.51878431738718289], [0.47656990584661874, 0.52343009415338138], [0.46885612423665834, 0.53114387576334154], [0.45994586240888752, 0.54005413759111265], [0.44382468776376022, 0.55617531223623984], [0.42061785313061933, 0.57938214686938083], [0.38301143221824507, 0.61698856778175493], [0.32658906586480302, 0.67341093413519704], [0.24761278897396316, 0.7523872110260369], [0.15963543249220546, 0.84036456750779442], [0.081605641698089357, 0.91839435830191074], [0.0038664353524984706, 0.99613356464750147]], 'lambda_': [array([[ -9.99999492e-01 -9.92567525e-04j,
          1.56195090e-04 -7.44566277e-05j],
       [ -1.56195090e-04 -7.44566277e-05j,
         -9.99999492e-01 +9.92567525e-04j]]), array([[ -9.99976440e-01+0.00685828j,   1.65042418e-04-0.00023731j],
       [ -1.65042418e-04-0.00023731j,  -9.99976440e-01-0.00685828j]]), array([[ -9.99746169e-01+0.02229083j,   9.82852061e-04-0.00312242j],
       [ -9.82852061e-04-0.00312242j,  -9.99746169e-01-0.02229083j]]), array([[ -9.99608936e-01+0.0277925j ,  -8.67704424e-04-0.00296634j],
       [  8.67704424e-04-0.00296634j,  -9.99608936e-01-0.0277925j ]]), array([[-0.99976174+0.01898529j,  0.00679502-0.00835775j],
       [-0.00679502-0.00835775j, -0.99976174-0.01898529j]]), array([[-0.99816565+0.06034263j, -0.00489521+0.00036763j],
       [ 0.00489521+0.00036763j, -0.99816565-0.06034263j]]), array([[ -9.97737833e-01+0.06722225j,  -4.88660382e-04+0.00038147j],
       [  4.88660382e-04+0.00038147j,  -9.97737833e-01-0.06722225j]]), array([[-0.99629584+0.08591383j,  0.00357199-0.00080513j],
       [-0.00357199-0.00080513j, -0.99629584-0.08591383j]]), array([[-0.99304309+0.11754962j, -0.00686562-0.00060986j],
       [ 0.00686562-0.00060986j, -0.99304309-0.11754962j]]), array([[-0.98918334+0.14653749j, -0.00648987-0.00098632j],
       [ 0.00648987-0.00098632j, -0.98918334-0.14653749j]]), array([[-0.98091515+0.19277782j, -0.02529956-0.00145494j],
       [ 0.02529956-0.00145494j, -0.98091515-0.19277782j]]), array([[-0.96849851+0.2487902j , -0.01066998+0.00046992j],
       [ 0.01066998+0.00046992j, -0.96849851-0.2487902j ]]), array([[-0.93835366+0.34552154j, -0.00360836+0.00970883j],
       [ 0.00360836+0.00970883j, -0.93835366-0.34552154j]]), array([[-0.87817028 +4.76122251e-01j, -0.04609146 +3.69386018e-04j],
       [ 0.04609146 +3.69386018e-04j, -0.87817028 -4.76122251e-01j]]), array([[-0.74178995+0.6297605j ,  0.23043221-0.00709817j],
       [-0.23043221-0.00709817j, -0.74178995-0.6297605j ]]), array([[-0.46286388+0.88565229j,  0.03554074-0.01067226j],
       [-0.03554074-0.01067226j, -0.46286388-0.88565229j]]), array([[ 0.01499873+0.99134258j,  0.03654986+0.12521593j],
       [-0.03654986+0.12521593j,  0.01499873-0.99134258j]]), array([[ 0.53775944+0.81909257j,  0.17437561-0.09744377j],
       [-0.17437561-0.09744377j,  0.53775944-0.81909257j]]), array([[ 0.87140197+0.490531j  , -0.00191005-0.00585538j],
       [ 0.00191005-0.00585538j,  0.87140197-0.490531j  ]]), array([[ 0.99970493+0.02151996j, -0.00708934-0.0087574j ],
       [ 0.00708934-0.0087574j ,  0.99970493-0.02151996j]])], 'kpt': [0.0, 0.026315789473684209, 0.052631578947368418, 0.078947368421052627, 0.10526315789473684, 0.13157894736842105, 0.15789473684210525, 0.18421052631578946, 0.21052631578947367, 0.23684210526315788, 0.26315789473684209, 0.28947368421052633, 0.31578947368421051, 0.34210526315789469, 0.36842105263157893, 0.39473684210526316, 0.42105263157894735, 0.44736842105263153, 0.47368421052631576, 0.5], 'gap': [0.0, 0.0, 0.0, 0.0, 2.2204460492503131e-16, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.49999999999999994, 0.5, 0.5]}

        self.assertDictAlmostEqual(tb_plane.get_res(), res)

    def test_res2(self):
        """ test no_iter=True """
        self.createH(0, 0.3)
        # call to Z2Pack
        tb_system = z2pack.tb.System(self.H)
        tb_plane = tb_system.plane(1, 2, 0)
        tb_plane.wcc_calc(verbose=False,
                          num_strings=20,
                          use_pickle=False,
                          no_iter=True)

        res = {'wcc': [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.71428571428571419, 0.71428571428571419], [0.71428571428571419, 0.71428571428571419], [0.71428571428571419, 0.71428571428571419], [0.71428571428571419, 0.71428571428571419], [0.71428571428571419, 0.71428571428571419]], 'lambda_': [array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-0.22252093+0.97492791j,  0.00000000+0.j        ],
       [ 0.00000000+0.j        , -0.22252093+0.97492791j]]), array([[-0.22252093+0.97492791j,  0.00000000+0.j        ],
       [ 0.00000000+0.j        , -0.22252093+0.97492791j]]), array([[-0.22252093+0.97492791j,  0.00000000+0.j        ],
       [ 0.00000000+0.j        , -0.22252093+0.97492791j]]), array([[-0.22252093+0.97492791j,  0.00000000+0.j        ],
       [ 0.00000000+0.j        , -0.22252093+0.97492791j]]), array([[-0.22252093+0.97492791j,  0.00000000+0.j        ],
       [ 0.00000000+0.j        , -0.22252093+0.97492791j]])], 'kpt': [0.0, 0.026315789473684209, 0.052631578947368418, 0.078947368421052627, 0.10526315789473684, 0.13157894736842105, 0.15789473684210525, 0.18421052631578946, 0.21052631578947367, 0.23684210526315788, 0.26315789473684209, 0.28947368421052633, 0.31578947368421051, 0.34210526315789469, 0.36842105263157893, 0.39473684210526316, 0.42105263157894735, 0.44736842105263153, 0.47368421052631576, 0.5], 'gap': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.21428571428571419, 0.21428571428571419, 0.21428571428571419, 0.21428571428571419, 0.21428571428571419]}

        self.assertDictAlmostEqual(tb_plane.get_res(), res)

    def test_res3(self):
        """ test no_neighbour_check=True """
        self.createH(0.1, 0.3)
        # call to Z2Pack
        tb_system = z2pack.tb.System(self.H)
        tb_plane = tb_system.plane(1, 2, 0)
        tb_plane.wcc_calc(verbose=False,
                          num_strings=20,
                          use_pickle=False,
                          no_neighbour_check=True)

        res = {'wcc': [[0.49996369258458911, 0.50003630741541083], [0.49969937950042137, 0.5003006204995788], [0.49921787497304743, 0.50078212502695296], [0.49870591461585301, 0.50129408538414699], [0.49847531395097933, 0.50152468604902101], [0.49764676757501669, 0.50235323242498353], [0.49681898534071861, 0.50318101465928156], [0.49599416659067369, 0.50400583340932625], [0.49472217792911855, 0.50527782207088145], [0.49276712834767228, 0.50723287165232778], [0.49022033200632836, 0.5097796679936718], [0.48587842661714503, 0.51412157338285491], [0.47823278374021649, 0.52176721625978362], [0.46251894588556092, 0.53748105411443925], [0.41753936610692016, 0.58246063389307956], [0.32650477740011102, 0.67349522259988914], [0.22465846442415066, 0.77534153557584962], [0.14764583792827177, 0.85235416207172832], [0.069572386836641423, 0.93042761316335876], [0.00064245928837270067, 0.99935754071162741]], 'lambda_': [array([[ -9.99999974e-01 -2.23545327e-04j,
          4.27619395e-05 -1.55072288e-05j],
       [ -4.27619395e-05 -1.55072288e-05j,
         -9.99999974e-01 +2.23545327e-04j]]), array([[ -9.99998216e-01+0.00188341j,   1.07083012e-05-0.00014284j],
       [ -1.07083012e-05-0.00014284j,  -9.99998216e-01-0.00188341j]]), array([[ -9.99987925e-01+0.00489331j,   8.24964719e-05+0.00044525j],
       [ -8.24964719e-05+0.00044525j,  -9.99987925e-01-0.00489331j]]), array([[ -9.99966944e-01+0.00811047j,  -7.95234595e-05-0.0005704j ],
       [  7.95234595e-05-0.0005704j ,  -9.99966944e-01-0.00811047j]]), array([[-0.99995411+0.00945613j,  0.00100862-0.00115568j],
       [-0.00100862-0.00115568j, -0.99995411-0.00945613j]]), array([[ -9.99890692e-01+0.01478066j,  -3.35399383e-04-0.00015281j],
       [  3.35399383e-04-0.00015281j,  -9.99890692e-01-0.01478066j]]), array([[ -9.99800268e-01 +1.99804456e-02j,
         -4.47837471e-04 +6.63243397e-05j],
       [  4.47837471e-04 +6.63243397e-05j,
         -9.99800268e-01 -1.99804456e-02j]]), array([[ -9.99683268e-01 +2.51647989e-02j,
         -3.11636362e-04 +1.98022133e-05j],
       [  3.11636362e-04 +1.98022133e-05j,
         -9.99683268e-01 -2.51647989e-02j]]), array([[-0.99945021 +3.31354094e-02j, -0.00115054 -7.20833867e-05j],
       [ 0.00115054 -7.20833867e-05j, -0.99945021 -3.31354094e-02j]]), array([[-0.99896753+0.04541153j, -0.00123325-0.00037616j],
       [ 0.00123325-0.00037616j, -0.99896753-0.04541153j]]), array([[-0.99811270 +6.13482024e-02j, -0.00272751 -8.45467378e-06j],
       [ 0.00272751 -8.45467379e-06j, -0.99811270 -6.13482024e-02j]]), array([[-0.99606621 +8.85955763e-02j, -0.00170786 -9.36480651e-05j],
       [ 0.00170786 -9.36480651e-05j, -0.99606621 -8.85955763e-02j]]), array([[ -9.90661901e-01+0.13632467j,  -5.20921706e-04+0.00207586j],
       [  5.20921706e-04+0.00207586j,  -9.90661901e-01-0.13632467j]]), array([[-0.97239770+0.23301292j, -0.01118212-0.00475878j],
       [ 0.01118212-0.00475878j, -0.97239770-0.23301292j]]), array([[-0.86875404+0.48596418j,  0.09509131-0.00792961j],
       [-0.09509131-0.00792961j, -0.86875404-0.48596418j]]), array([[-0.46239437+0.88662158j,  0.00252869-0.00933919j],
       [-0.00252869-0.00933919j, -0.46239437-0.88662158j]]), array([[ 0.15855361+0.98466874j, -0.03463253-0.06394377j],
       [ 0.03463253-0.06394377j,  0.15855361-0.98466874j]]), array([[ 0.5996872+0.79929003j, -0.0283220+0.02661903j],
       [ 0.0283220+0.02661903j,  0.5996872-0.79929003j]]), array([[ 0.90596776+0.42328648j, -0.00274233-0.00659195j],
       [ 0.00274233-0.00659195j,  0.90596776-0.42328648j]]), array([[ 0.99999185-0.00324447j, -0.00104263-0.00216359j],
       [ 0.00104263-0.00216359j,  0.99999185+0.00324447j]])], 'kpt': [0.0, 0.026315789473684209, 0.052631578947368418, 0.078947368421052627, 0.10526315789473684, 0.13157894736842105, 0.15789473684210525, 0.18421052631578946, 0.21052631578947367, 0.23684210526315788, 0.26315789473684209, 0.28947368421052633, 0.31578947368421051, 0.34210526315789469, 0.36842105263157893, 0.39473684210526316, 0.42105263157894735, 0.44736842105263153, 0.47368421052631576, 0.5], 'gap': [0.0, 0.0, 2.2204460492503131e-16, 0.0, 2.2204460492503131e-16, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.99999999999999989, 0.0, 0.50000000000000022, 0.5, 0.50000000000000011, 0.50000000000000011]}

        self.assertDictAlmostEqual(tb_plane.get_res(), res)

    def testkwargcheck1(self):
        """ test kwarg check on wcc_calc """
        self.createH(0.1, 0.3)
        # call to Z2Pack
        tb_system = z2pack.tb.System(self.H)
        tb_plane = tb_system.plane(1, 2, 0)
        self.assertRaises(
            TypeError,
            tb_plane.wcc_calc,
            invalid_kwarg = 3)

    def testkwargcheck2(self):
        """ test kwarg check on __init__ """
        self.createH(0, 0.3)
        # call to Z2Pack
        tb_system = z2pack.tb.System(self.H)
        self.assertRaises(
            TypeError,
            tb_system.plane,
            1, 2, 0, invalid_kwarg = 3)

    # this test may produce false negatives due to small numerical differences
    def test_res1_v2(self):
        self.createH(0.2, 0.3)
        # call to Z2Pack
        tb_system = z2pack.tb.System(self.H)
        tb_plane = tb_system.plane(plane_edge_start=[0, 0, 0], plane_edge_end=[1, 0, 0], string_vec=[0, 1, 0])
        tb_plane.wcc_calc(verbose=False, num_strings=20, use_pickle=False)
        
        res = {'wcc': [[0.49983964546467036, 0.50016035453532992], [0.49641395036486252, 0.50358604963513764], [0.49652567629394373, 0.5034743237060566], [0.48929271594465651, 0.51070728405534349], [0.48121568261281716, 0.51878431738718289], [0.46885612423665834, 0.53114387576334154], [0.44382468776376022, 0.55617531223623984], [0.38301143221824507, 0.61698856778175493], [0.24761278897396316, 0.7523872110260369], [0.081605641698089357, 0.91839435830191074], [0.081626412280110472, 0.91837358771988975], [0.24551244546658102, 0.7544875545334192], [0.37818882309920948, 0.6218111769007908], [0.44448265320552593, 0.55551734679447429], [0.46852472488132335, 0.53147527511867665], [0.4815223617995868, 0.51847763820041326], [0.48880247564436458, 0.51119752435563548], [0.49133310204525971, 0.5086668979547404], [0.49731451892976225, 0.50268548107023769], [0.49970883781246184, 0.50029116218753811]], 'lambda_': [array([[ -9.99999492e-01 -9.92567525e-04j,
          1.56195090e-04 -7.44566277e-05j],
       [ -1.56195090e-04 -7.44566277e-05j,
         -9.99999492e-01 +9.92567525e-04j]]), array([[ -9.99746169e-01+0.02229083j,   9.82852061e-04-0.00312242j],
       [ -9.82852061e-04-0.00312242j,  -9.99746169e-01-0.02229083j]]), array([[-0.99976174+0.01898529j,  0.00679502-0.00835775j],
       [-0.00679502-0.00835775j, -0.99976174-0.01898529j]]), array([[ -9.97737833e-01+0.06722225j,  -4.88660382e-04+0.00038147j],
       [  4.88660382e-04+0.00038147j,  -9.97737833e-01-0.06722225j]]), array([[-0.99304309+0.11754962j, -0.00686562-0.00060986j],
       [ 0.00686562-0.00060986j, -0.99304309-0.11754962j]]), array([[-0.98091515+0.19277782j, -0.02529956-0.00145494j],
       [ 0.02529956-0.00145494j, -0.98091515-0.19277782j]]), array([[-0.93835366+0.34552154j, -0.00360836+0.00970883j],
       [ 0.00360836+0.00970883j, -0.93835366-0.34552154j]]), array([[-0.74178995+0.6297605j ,  0.23043221-0.00709817j],
       [-0.23043221-0.00709817j, -0.74178995-0.6297605j ]]), array([[ 0.01499873+0.99134258j,  0.03654986+0.12521593j],
       [-0.03654986+0.12521593j,  0.01499873-0.99134258j]]), array([[ 0.87140197+0.490531j  , -0.00191005-0.00585538j],
       [ 0.00191005-0.00585538j,  0.87140197-0.490531j  ]]), array([[ 0.87133795-0.49061187j, -0.00318751+0.00774702j],
       [ 0.00318751+0.00774702j,  0.87133795+0.49061187j]]), array([[ 0.0281924-0.99925007j, -0.0264504+0.00220728j],
       [ 0.0264504+0.00220728j,  0.0281924+0.99925007j]]), array([[-0.72113148-0.69246771j, -0.00558576-0.02065586j],
       [ 0.00558576-0.02065586j, -0.72113148+0.69246771j]]), array([[-0.93977470-0.34052194j,  0.02766794+0.01013912j],
       [-0.02766794+0.01013912j, -0.93977470+0.34052194j]]), array([[ -9.80508158e-01-0.19647677j,  -5.12820963e-04+0.00060618j],
       [  5.12820963e-04+0.00060618j,  -9.80508158e-01+0.19647677j]]), array([[-0.99326814-0.11565117j,  0.00656902+0.00021684j],
       [-0.00656902+0.00021684j, -0.99326814+0.11565117j]]), array([[ -9.97526029e-01-0.07028017j,   2.82843154e-06+0.00158727j],
       [ -2.82843154e-06+0.00158727j,  -9.97526029e-01+0.07028017j]]), array([[-0.99851765-0.05427936j, -0.00251287-0.00315152j],
       [ 0.00251287-0.00315152j, -0.99851765+0.05427936j]]), array([[ -9.99857648e-01-0.01686989j,   1.89877858e-04+0.0002335j ],
       [ -1.89877858e-04+0.0002335j ,  -9.99857648e-01+0.01686989j]]), array([[ -9.99998327e-01 +1.81154790e-03j,
         -2.54307031e-04 +2.04406444e-05j],
       [  2.54307031e-04 +2.04406444e-05j,
         -9.99998327e-01 -1.81154790e-03j]])], 'kpt': [0.0, 0.052631578947368418, 0.10526315789473684, 0.15789473684210525, 0.21052631578947367, 0.26315789473684209, 0.31578947368421051, 0.36842105263157893, 0.42105263157894735, 0.47368421052631576, 0.52631578947368418, 0.57894736842105265, 0.63157894736842102, 0.68421052631578938, 0.73684210526315785, 0.78947368421052633, 0.84210526315789469, 0.89473684210526305, 0.94736842105263153, 1.0], 'gap': [0.0, 0.0, 2.2204460492503131e-16, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.50000000000000011, 0.50000000000000011, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}

        self.assertDictAlmostEqual(tb_plane.get_res(), res)

    def test_res2_v2(self):
        """ test no_iter=True """
        self.createH(0, 0.3)
        # call to Z2Pack
        tb_system = z2pack.tb.System(self.H)
        tb_plane = tb_system.plane(plane_edge_start=[0, 0, 0], plane_edge_end=[1, 0, 0], string_vec=[0, 1, 0])
        tb_plane.wcc_calc(verbose=False,
                          num_strings=20,
                          use_pickle=False,
                          no_iter=True)

        res = {'wcc': [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.71428571428571419, 0.71428571428571419], [0.71428571428571419, 0.71428571428571419], [0.71428571428571419, 0.71428571428571419], [0.71428571428571419, 0.71428571428571419], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5]], 'lambda_': [array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-0.22252093+0.97492791j,  0.00000000+0.j        ],
       [ 0.00000000+0.j        , -0.22252093+0.97492791j]]), array([[-0.22252093+0.97492791j,  0.00000000+0.j        ],
       [ 0.00000000+0.j        , -0.22252093+0.97492791j]]), array([[-0.22252093+0.97492791j,  0.00000000+0.j        ],
       [ 0.00000000+0.j        , -0.22252093+0.97492791j]]), array([[-0.22252093+0.97492791j,  0.00000000+0.j        ],
       [ 0.00000000+0.j        , -0.22252093+0.97492791j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]])], 'kpt': [0.0, 0.052631578947368418, 0.10526315789473684, 0.15789473684210525, 0.21052631578947367, 0.26315789473684209, 0.31578947368421051, 0.36842105263157893, 0.42105263157894735, 0.47368421052631576, 0.52631578947368418, 0.57894736842105265, 0.63157894736842102, 0.68421052631578938, 0.73684210526315785, 0.78947368421052633, 0.84210526315789469, 0.89473684210526305, 0.94736842105263153, 1.0], 'gap': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.21428571428571419, 0.21428571428571419, 0.21428571428571419, 0.21428571428571419, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}

        self.assertDictAlmostEqual(tb_plane.get_res(), res)

    def test_res3_v2(self):
        """ test no_neighbour_check=True """
        self.createH(0.1, 0.3)
        # call to Z2Pack
        tb_system = z2pack.tb.System(self.H)
        tb_plane = tb_system.plane(plane_edge_start=[0, 0, 0], plane_edge_end=[1, 0, 0], string_vec=[0, 1, 0])
        tb_plane.wcc_calc(verbose=False,
                          num_strings=20,
                          use_pickle=False,
                          no_neighbour_check=True)

        res = {'wcc': [[0.49996369258458911, 0.50003630741541083], [0.49921787497304743, 0.50078212502695296], [0.49847531395097933, 0.50152468604902101], [0.49681898534071861, 0.50318101465928156], [0.49472217792911855, 0.50527782207088145], [0.49022033200632836, 0.5097796679936718], [0.47823278374021649, 0.52176721625978362], [0.41753936610692016, 0.58246063389307956], [0.22465846442415066, 0.77534153557584962], [0.069572386836641423, 0.93042761316335876], [0.070640757883293409, 0.92935924211670673], [0.22741272684369099, 0.77258727315630904], [0.4177554087429069, 0.58224459125709283], [0.47917835273253484, 0.52082164726746505], [0.49012578802023254, 0.50987421197976768], [0.49482291422743158, 0.50517708577256859], [0.49690235179204773, 0.50309764820795233], [0.49813317792404294, 0.50186682207595723], [0.49929772405232842, 0.5007022759476718], [0.49999165765911974, 0.50000834234088032]], 'lambda_': [array([[ -9.99999974e-01 -2.23545327e-04j,
          4.27619395e-05 -1.55072288e-05j],
       [ -4.27619395e-05 -1.55072288e-05j,
         -9.99999974e-01 +2.23545327e-04j]]), array([[ -9.99987925e-01+0.00489331j,   8.24964719e-05+0.00044525j],
       [ -8.24964719e-05+0.00044525j,  -9.99987925e-01-0.00489331j]]), array([[-0.99995411+0.00945613j,  0.00100862-0.00115568j],
       [-0.00100862-0.00115568j, -0.99995411-0.00945613j]]), array([[ -9.99800268e-01 +1.99804456e-02j,
         -4.47837471e-04 +6.63243397e-05j],
       [  4.47837471e-04 +6.63243397e-05j,
         -9.99800268e-01 -1.99804456e-02j]]), array([[-0.99945021 +3.31354094e-02j, -0.00115054 -7.20833867e-05j],
       [ 0.00115054 -7.20833867e-05j, -0.99945021 -3.31354094e-02j]]), array([[-0.99811270 +6.13482024e-02j, -0.00272751 -8.45467378e-06j],
       [ 0.00272751 -8.45467379e-06j, -0.99811270 -6.13482024e-02j]]), array([[ -9.90661901e-01+0.13632467j,  -5.20921706e-04+0.00207586j],
       [  5.20921706e-04+0.00207586j,  -9.90661901e-01-0.13632467j]]), array([[-0.86875404+0.48596418j,  0.09509131-0.00792961j],
       [-0.09509131-0.00792961j, -0.86875404-0.48596418j]]), array([[ 0.15855361+0.98466874j, -0.03463253-0.06394377j],
       [ 0.03463253-0.06394377j,  0.15855361-0.98466874j]]), array([[ 0.90596776+0.42328648j, -0.00274233-0.00659195j],
       [ 0.00274233-0.00659195j,  0.90596776-0.42328648j]]), array([[  9.03105536e-01-0.42941515j,  -6.77273532e-04-0.00159996j],
       [  6.77273532e-04-0.00159996j,   9.03105536e-01+0.42941515j]]), array([[ 0.14144409-0.98991064j,  0.00676872-0.0049675j ],
       [-0.00676872-0.0049675j ,  0.14144409+0.98991064j]]), array([[-0.86942550-0.49326469j, -0.02803555-0.00180589j],
       [ 0.02803555-0.00180589j, -0.86942550+0.49326469j]]), array([[ -9.91454443e-01 -1.30450266e-01j,
          9.01403957e-04 +5.96931734e-05j],
       [ -9.01403957e-04 +5.96931734e-05j,
         -9.91454443e-01 +1.30450266e-01j]]), array([[ -9.98076043e-01-0.06200083j,   2.84866153e-04+0.00016692j],
       [ -2.84866153e-04+0.00016692j,  -9.98076043e-01+0.06200083j]]), array([[ -9.99470992e-01 -3.25111727e-02j,
          8.71079222e-04 -2.90694116e-05j],
       [ -8.71079222e-04 -2.90694116e-05j,
         -9.99470992e-01 +3.25111727e-02j]]), array([[ -9.99810600e-01-0.01946054j,  -3.41841983e-05+0.00022506j],
       [  3.41841983e-05+0.00022506j,  -9.99810600e-01+0.01946054j]]), array([[ -9.99931209e-01-0.01172664j,  -1.96899057e-04+0.00015513j],
       [  1.96899057e-04+0.00015513j,  -9.99931209e-01+0.01172664j]]), array([[ -9.99990265e-01 -4.41250497e-03j,
          9.46845033e-06 +2.03386485e-06j],
       [ -9.46845033e-06 +2.03386485e-06j,
         -9.99990265e-01 +4.41250497e-03j]]), array([[ -9.99999999e-01 +4.97670566e-05j,
         -2.43895296e-06 -1.62720095e-05j],
       [  2.43895296e-06 -1.62720095e-05j,
         -9.99999999e-01 -4.97670566e-05j]])], 'kpt': [0.0, 0.052631578947368418, 0.10526315789473684, 0.15789473684210525, 0.21052631578947367, 0.26315789473684209, 0.31578947368421051, 0.36842105263157893, 0.42105263157894735, 0.47368421052631576, 0.52631578947368418, 0.57894736842105265, 0.63157894736842102, 0.68421052631578938, 0.73684210526315785, 0.78947368421052633, 0.84210526315789469, 0.89473684210526305, 0.94736842105263153, 1.0], 'gap': [0.0, 2.2204460492503131e-16, 2.2204460492503131e-16, 0.0, 0.0, 0.0, 0.0, 0.99999999999999989, 0.50000000000000022, 0.50000000000000011, 0.50000000000000011, 0.5, 0.99999999999999989, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}

        self.assertDictAlmostEqual(tb_plane.get_res(), res)

    def testkwargcheck1_v2(self):
        """ test kwarg check on wcc_calc """
        self.createH(0.1, 0.3)
        # call to Z2Pack
        tb_system = z2pack.tb.System(self.H)
        tb_plane = tb_system.plane(plane_edge_start=[0, 0, 0], plane_edge_end=[1, 0, 0], string_vec=[0, 1, 0])
        self.assertRaises(
            TypeError,
            tb_plane.wcc_calc,
            invalid_kwarg = 3)

    def testkwargcheck2_v2(self):
        """ test kwarg check on __init__ """
        self.createH(0, 0.3)
        # call to Z2Pack
        tb_system = z2pack.tb.System(self.H)
        self.assertRaises(
            TypeError,
            tb_system.plane,
            plane_edge_start=[0, 0, 0], plane_edge_end=[1, 0, 0], string_vec=[0, 1, 0], invalid_kwarg = 3)

if __name__ == "__main__":
    unittest.main()
