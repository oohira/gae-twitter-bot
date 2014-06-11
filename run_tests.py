import argparse
import os.path
import sys
import unittest

DIR_PATH = os.path.dirname(__file__)


def main():
    parser = argparse.ArgumentParser(description='Run the test suite.')
    parser.add_argument(
        'sdk_path',
        help='The path to the GAE SDK directory.')
    parser.add_argument(
        'tests', nargs='*',
        help='The fully qualified names of the tests to run. '
        'If not given then the full test suite will be run.')
    args = parser.parse_args()
    sys.path.extend([
        DIR_PATH,
        os.path.join(DIR_PATH, 'lib'),
        os.path.join(args.sdk_path, 'lib', 'yaml-3.10')
    ])

    loader = unittest.TestLoader()
    if args.tests:
        tests = loader.loadTestsFromNames(args.tests)
    else:
        tests = loader.discover(DIR_PATH, '*_test.py')
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(tests)

if __name__ == '__main__':
    main()
