import subprocess
import json

def speed_color():
	out = subprocess.check_output(['speedtest-cli', '--json'])

	print("OUT: ", out)

	data = json.loads(out.decode('utf-8'))

	print("SPEED: ", data['download'])

	colors = ["FF0000", "FF3300", "ff6600", "ff9900", "FFCC00", "FFFF00", "ccff00", "99ff00", "66ff00", "33ff00", "00FF00"]

	step = 4.5 # 50 / 11

	color = int(data['download']) / 1000000 / 4.5

	if color > 10:
		color = 10

	ans = colors[color]

	print ans
	return ans
