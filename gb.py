import random

FRAME_COUNT = 8
WINDOW_SIZE = 3
frame = 0

while frame < FRAME_COUNT:
    window = []
    # fill the window...
    for i in range(WINDOW_SIZE):
        if frame + i < FRAME_COUNT:
            window.append(frame + i)

    print("Sending frames in Window--->", window)

    success = True

    for currentframe in window:
        if random.randint(0, 7) < 2:
            print("Frame", currentframe, "is lost!")
            success = False
            break
        else:
            print("Acknowledgement received for frame:", currentframe)

    if success:
        frame += WINDOW_SIZE
    else:
        print("Resending Frames from frame number", frame)

