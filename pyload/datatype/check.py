# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from builtins import object
from time import time

from pyload.api import OnlineCheck as OC


class OnlineCheck(object):
    """
    Helper class that holds result of an initiated online check.
    """

    def __init__(self, rid, owner):
        self.rid = rid
        self.owner = owner
        self.result = {}
        self.done = False

        self.timestamp = time()

    def is_stale(self, timeout=5):
        """
        Checks if the data was updated or accessed recently.
        """
        return self.timestamp + timeout * 60 < time()

    def update(self, result):
        self.timestamp = time()
        self.result.update(result)

    def to_api_data(self):
        self.timestamp = time()
        oc = OC(self.rid, self.result)
        # getting the results clears the older ones
        self.result = {}
        # indication for no more data
        if self.done:
            oc.rid = -1

        return oc