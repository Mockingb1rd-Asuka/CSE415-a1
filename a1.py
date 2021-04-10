def is_multiple_of_3(n):
    "Return True if n is a multiple of 3; False otherwise."
    return n % 3 == 0


def next_prime(m):
    '''Return an integer p that is prime, and such that
  p > m, and there does not exist any n, with n > m
  and n < p such that n is prime. In other words, return
  the next prime number after m.'''
    p = m + 1
    prime = is_prime(p)
    while prime:
        p += 1
        prime = is_prime(p)
    return p


def is_prime(n):
    if n >= 2:
        for i in range(2, n):
            if (n % i) == 0:
                return True
    else:
        return False


url = "http://courses.cs.washington.edu/courses/cse415/20wi/desc.html"

import wordscraper
import math


def empirical_probabilities(url):
    '''Return a dictionary whose keys are words in a reference vocabulary,
  and whose values are PROBABILITIES of those words, based on the
  number of occurrences on the webpage at the given URL.'''

    bytes = wordscraper.fetch(url)
    word_list = wordscraper.html_bytes_to_word_list(bytes)
    word_dict = wordscraper.make_word_count_dict(word_list)
    word_prob = {}
    for word in word_dict:
        prob = 1.0 - math.exp(- word_dict[word])
        word_prob[word] = prob

    return word_prob
