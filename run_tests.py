#!/usr/bin/env python3

import unittest

from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.discover(
        "/autograder/source/instructor/tests"
    )
    with open("/autograder/results/results.json", "w") as f:
        JSONTestRunner(visibility="visible", stream=f).run(suite)
