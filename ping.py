import time
from ping3 import ping
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

target = "google.com"
interval = 1  
max_points = 100  

ping_values = deque(maxlen=max_points)

fig, ax = plt.subplots()
line, = ax.plot([], [], 'r-')
ax.set_xlim(0, max_points - 1)
ax.set_ylim(0, 100)  
ax.set_xlabel('Time')
ax.set_ylabel('Ping (ms)')
ax.set_title(f'Ping to {target}')

text = ax.text(0.8, 0.9, "", transform=ax.transAxes)

def update_plot(frame):
    try:
        ping_time = ping(target, unit='ms')
        if ping_time is None:
            ping_values.append(0)
        else:
            ping_values.append(ping_time)
    except Exception as e:
        ping_values.append(0)
        print(f"Ping error: {e}")

    line.set_data(range(len(ping_values)), list(ping_values))
    
    if ping_values:
        text.set_text(f'Ping: {ping_values[-1]:.2f} ms')

    return line, text

ani = animation.FuncAnimation(fig, update_plot, interval=interval * 1000)
plt.show()