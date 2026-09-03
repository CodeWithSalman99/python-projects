import time 
from datetime import datetime

print("Data logging started press ctrl+c to stop")

while True:

    current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

   # Sensor reading
    temperature = 24.5

    log_entry = f"Time:{current_time} Temp:{temperature}C\n"
    with open("sensor_log.txt", "a") as file:
        file.write(log_entry)

        print(f"Saved: {log_entry.strip()}")
        time.sleep(2)