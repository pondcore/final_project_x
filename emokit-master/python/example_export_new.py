# This is an example of popping a packet from the Emotiv class's packet queue
# Additionally, exports the data to a CSV file.
# You don't actually need to dequeue packets, although after some time allocation lag may occur if you don't.


import platform
import time

from emokit.emotiv import Emotiv
from emokit.packet import EmotivExtraPacket
from emokit.sensors import sensors_mapping
from emokit.util import get_quality_scale_level, system_platform
from emokit.python_queue import Queue
from emokit.tasks import EmotivOutputTask

if platform.system() == "Windows":
    pass


if __name__ == "__main__":
    with Emotiv(display_output=True, verbose=True, write=True) as headset:
        print("Serial Number: %s" % headset.serial_number)
        print("Exporting data... press control+c to stop.")
        file = open("XXX.txt", "w")
        last_sensors = sensors_mapping.copy()
        last_sensors = packet_data.sensors
        
        while headset.running:
            
            try:
                packet = headset.dequeue()
                file.write(',');
                
            except Exception:
                headset.stop()
            time.sleep(0.001)
        file.close()

