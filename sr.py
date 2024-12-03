import random
import time

TOTAL_FRAMES = 7  # Total number of frames to send
current_frame = 0  # The frame being sent

lost_frames = []  # Set to track frames that were lost

while current_frame < TOTAL_FRAMES:
    print(f"Sending Frame {current_frame}....")
    random_failure = random.randint(0, 7)  # Simulate random loss of a frame
    if random_failure == current_frame:
        print(f"Frame {current_frame} Lost!")
        lost_frames.append(current_frame)
    else:
        print(f"Acknowledgment for Frame {current_frame} received!")
    current_frame += 1

    time.sleep(1)  # Simulate delay

print("\nResending Lost Frames...")
for frame in lost_frames:
    print(f"Resending Frame {frame}...")
    print(f"Acknowledgment for Frame {frame} received!")
