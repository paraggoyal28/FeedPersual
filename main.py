from rssfeedreader import RssReader
import sys


class Solution:
    def validate_input(self):
        """Checks for input is valid url"""
        if(len(sys.argv) == 1):
            raise SystemError("Must provide at least one url to parse")

    def print_all_feed(self):
        "Print the feeds from all the urls"
        for arg_index in range(1, len(sys.argv)):
            RssReader(sys.argv[arg_index]).print_rss_items()


if __name__ == "__main__":
    solution = Solution()
    solution.validate_input()
    solution.print_all_feed()
