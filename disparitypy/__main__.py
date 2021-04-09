import argparse
import sys


from .comparators.comparator import UComparator


"""
    Definition of the main function body
"""
def main():
    """
        Argument parsing and initial test
    """
    parser = argparse.ArgumentParser('disparity')
    parser.add_argument('folder1')
    parser.add_argument('folder2')
    arguments = parser.parse_args()

    ccc = UComparator.from_paths(arguments.folder1,
                                 arguments.folder2)

    print(ccc.compare())

    return 0


"""
    Python binding for main script
"""
if __name__ == "__main__":
    sys.exit(main())
