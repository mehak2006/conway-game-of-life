import argparse
from rplife import __version__, patterns, view

def get_command_line_args():
    parser = argparse.ArgumentParser(
        prog="rplife",
        description="Conway's Game of Life in your terminal",
    )
    parser.add_argument(
        "-p",
        "--pattern",
        choices = [pat.name for pat in patterns.get_all_patterns()],
        default="blinker",
        help = "take a pattern for the Game of Life (default: %(default)s)",
    )
    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="show all available patterns in a sequence",
    )
    parser.add_argument(
        "-v",
        "--view",
        choices = view.__all__,
        default="CursesView",
        help="view for displaying the Game of Life (default: %(default)s)",
    )
    parser.add_argument(
        "-g",
        "--gen",
        metavar="NUM_GENERATIONS",
        type=int,
        default=10,
        help="number of generations to display (default: %(default)s)",
    )
    parser.add_argument(
        "-f",
        "--fps",
        metavar="FRAMES_PER_SECOND",
        type=int,
        default=7,
        help="frames per second (default: %(default)s)",
    )
    return parser.parse_args()