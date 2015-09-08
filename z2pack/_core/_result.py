#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>
# Date:    03.09.2015 12:00:27 CEST
# File:    _result.py


class SurfaceResult(object):
    r"""
    Result class for surface calculations.
    """
    def __init__(self, descriptor):
        self._t_points = []
        self._lines = []
        self.descriptor = descriptor

    def __getattr__(self, key):
        if key == 'result':
            return zip(self._t_points, self._lines)

    def __getitem__(self, t):
        try:
            return self._lines[self._t_points.index(t)]
        except ValueError:
            raise KeyError('Line for t={} does not exist'.format(t))

    def __setitem__(self, t, line):
        tval = float(t)
        # this means that lines are effectively "write-protected"
        # except if they are manipulated from within
        if tval in self._t_points:
            raise ValueError('Cannot insert line at t={}: Line exists'.format(tval))
        assert(isinstance(line, LineResult))
        self._t_points.append(tval)
        self._t_points = sorted(self._t_points)
        self._lines.insert(self._t_points.index(tval), line)
    
class LineResult(object):
    r"""
    Result class for line calculations.
    """
    def __init__(self, descriptor):
        self.wcc = None
        self.lambda_ = None
        self.converged = None
        self.max_move = None
        self.num_iter = None
        self.descriptor = descriptor

    def set(self, wcc, lambda_, converged, max_move, num_iter):
        self.wcc = wcc
        self.lambda_ = lambda_
        self.converged = converged
        self.max_move = max_move
        self.num_iter = num_iter

