import math
import time

A = 0
B = 0

# ANSI code to clear screen once at start
print("\x1b[2J", end='')

# Characters and matching color codes (indexed by brightness)
shades = ".,-~:;=!*#$@"
colors = [196, 202, 208, 214, 220, 190, 46, 51, 39, 21, 93, 201]  # rainbow-ish

while True:
    print("\x1b[H", end='')  # Move cursor to top-left

    output = [' '] * 1760
    zbuffer = [0] * 1760

    for j in range(0, 628, 7):  # j from 0 to 2pi
        for i in range(0, 628, 2):  # i from 0 to 2pi
            c = math.sin(i / 100)
            d = math.cos(j / 100)
            e = math.sin(A)
            f = math.sin(j / 100)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i / 100)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(40 + 30 * D * (l * h * m - t * n))
            y = int(12 + 15 * D * (l * h * n + t * m))
            o = int(x + 80 * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if 0 <= o < 1760 and D > zbuffer[o]:
                zbuffer[o] = D
                ch_index = max(0, N)
                color = colors[ch_index % len(colors)]
                output[o] = f"\033[38;5;{color}m{shades[ch_index]}\033[0m"

    for i in range(0, 1760, 80):
        print(''.join(output[i:i + 80]))

    A += 0.04
    B += 0.08
    time.sleep(0)
