import time

from tas import playback, recorder

def main():
    mode = input("Choose mode: record (r) or play (p): ")

    if mode == 'r':
        input("Press enter to start recording")
        time.sleep(3)
        recorder.record()
    elif mode == 'p':
        input("Press enter to start playback")
        time.sleep(3)
        playback.play()
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()
