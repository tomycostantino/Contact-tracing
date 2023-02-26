import time
from modules.tracker import Tracker

def main():
    running = False
    tracker = Tracker()

    while True:
        if running:
            pass
        else:
            tracker.run()
            running = True

if __name__ == '__main__':
    main()