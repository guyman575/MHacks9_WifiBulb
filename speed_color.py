import subprocess
import json

def speed_color():
	out = subprocess.check_output(['speedtest-cli', '--json'])

	print("OUT: ", out)

	data = json.loads(out.decode('utf-8'))

	print("SPEED: ", data['download'])

	colors = [0xFF0000, 0xFF3300, 0xff6600, 0xff9900, 0xFFCC00, 0xFFFF00, 0xccff00, 0x99ff00, 0x66ff00, 0x33ff00, 0x00FF00]

	step = 4.5 # 50 / 11

	color = int(data['download']) / 1000000 / 4.5

	if color > 10:
		color = 10

	color = colors[color]

	print color
	return color
