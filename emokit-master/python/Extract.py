import platform
import time

from emokit.emotiv import Emotiv

if platform.system() == "Windows":
    pass

if __name__ == "__main__":
    with Emotiv(write_decrypted=True) as headset:
        print("Serial Number: %s" % headset.serial_number);
        time.sleep(0.001)
