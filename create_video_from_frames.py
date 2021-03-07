import argparse
import os
import glob

import cv2


def do_parsing():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--input_dirs", nargs='*', required=True, type=str,
                        help="Input directory with jpg frames to use for videos")
    parser.add_argument("--output_file", required=True, type=str, help="Output video filepath")
    parser.add_argument("--loops", required=False, default=1, type=int, help="Loop times")
    parser.add_argument("--fps", required=False, default=25, type=int, help="FPS of the video")
    args = parser.parse_args()
    return args


def main():
    args = do_parsing()
    print(args)

    output_dir = os.path.dirname(args.output_file)
    if output_dir != "":
        os.makedirs(os.path.dirname(args.output_file), exist_ok=True)

    image_files = []
    for loop in range(args.loops):
        for input_dir in args.input_dirs:
            image_files.extend(sorted(glob.glob(input_dir + "/*.jpg")))

    first_image = cv2.imread(image_files[0])

    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    videowriter= cv2.VideoWriter(args.output_file, fourcc, args.fps, first_image.shape[:2][::-1])

    for image_file in image_files:
        print(image_file)
        frame = cv2.imread(image_file)
        videowriter.write(frame)

    print(f"Video saved in {args.output_file}")


if __name__ == "__main__":
    main()
