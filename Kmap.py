#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script defines a function to simplify boolean algebra expressions,
inspired by Karnaugh Map.
"""

from Kmap.utils import (
    Term,
    find_essential_prime_implicants,
    find_prime_implicants,
)


class Minterms(object):
    """ Minterms stores expressions for 1s and "don't care". """

    def __init__(
        self, minterms_str=None, not_cares_str=None,
    ):
        if minterms_str is None:
            minterms_str = []
        if not_cares_str is None:
            not_cares_str = []

        self.minterms = [Term(term) for term in minterms_str]
        self.not_cares = [Term(term) for term in not_cares_str]

    def simplify(self):
        prime_implicants = find_prime_implicants(self.minterms, self.not_cares)
        result = find_essential_prime_implicants(prime_implicants, self.minterms)
        return result


if __name__ == "__main__":
    str_terms = ["0100", "1000", "1010", "1011", "1100", "1111"]
    terms_not_care = ["1001", "1110"]
    t_minterms = [Term(term) for term in str_terms]
    not_cares = [Term(term) for term in terms_not_care]

    minterms = Minterms(t_minterms, not_cares)
    minterms.simplify()
