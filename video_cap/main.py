import argparse
from video_cap.videocap import VideoCap

available_funcs = list(VideoCap.functions.keys())

parser = argparse.ArgumentParser('Video capture in python using opencv lib')
parser.add_argument('--fun', type=str,
                    choices=available_funcs,
                    help="Available functions: {0}".format(available_funcs), required=True, metavar="FUNC_NAME")
parser.add_argument('-x', type=int, nargs=2, default=[0, 0],
                    help="Region of interest for filter on X axis [-x startcoord endcoord]",
                    metavar='X_RESOLUTIONS'
                    )
parser.add_argument('-y', type=int, nargs=2, default=[0, 0],
                    help="Region of interest for filter on Y axis [-y startcoord endcoord]",
                    metavar='Y_RESOLUTIONS')


def main():
    arguments = parser.parse_args()
    if arguments.x[0] > arguments.x[1] or arguments.y[0] > arguments.y[1]:
        raise AttributeError("First val < Second val!")

    video_cap = VideoCap(arguments.fun, arguments.x[0], arguments.y[0], arguments.x[1], arguments.y[1])
    video_cap.run()
