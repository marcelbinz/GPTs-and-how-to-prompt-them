import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = np.array([
    [3, 5, 3, 4, 4, 2, 4],
    [2, 4, 6, 7, 9, 13, 4],
    [4, 3, 4, 4, 1, 4, 2],
    [18, 11, 6, 9, 8, 9, 8],
    [3, 3, 4, 5, 6, 7, 1],
    [3, 2, 2, 3, 1, 4, 3],
    [0, 0, 0, 0, 4, 4, 0],
    [5, 4, 3, 3, 7, 3, 2],
    [2, 0, 0, 1, 1, 4, 4],
    [3, 5, 3, 5, 1, 1, 0],
    [0, 1, 0, 0, 3, 2, 1],
    [8, 3, 3, 3, 0, 3, 5],
    [4, 3, 0, 1, 0, 0, 0],
    [8, 2, 1, 3, 5, 4, 6],
    [5, 1, 1, 0, 3, 3, 0],
    [14, 11, 13, 16, 7, 5, 10],
    [4, 1, 1, 0, 1, 0, 0],
    [2, 3, 1, 3, 3, 3, 3],
    [2, 1, 1, 3, 1, 2, 2],
])

times = np.array([
    [550, 530, 420, 420, 430, 402, 382],
    [620, 420, 325, 420, 360, 360, 345],
    [560, 570, 545, 515, 480, 455, 470],
    [482, 470, 420, 360, 420, 300, 302],
    [1020, 810, 770, 680, 735, 650, 605],
    [800, 710, 715, 700, 695, 655, 785],
    [600, 560, 510, 465, 465, 468, 455],
    [456, 390, 325, 329, 368, 320, 310],
    [420, 360, 450, 450, 450, 480, 470],
    [641, 630, 608, 640, 550, 545, 475],
    [460, 375, 362, 307, 297, 243, 240],
    [560, 520, 540, 440, 500, 390, 385],
    [590, 420, 360, 350, 345, 330, 360],
    [750, 720, 605, 600, 650, 550, 500],
    [420, 680, 470, 495, 435, 434, 410],
    [870, 840, 795, 630, 610, 600, 530],
    [840, 750, 690, 675, 700, 645, 630],
    [690, 625, 580, 510, 560, 555, 470],
    [866, 680, 725, 595, 590, 580, 529],
])

fig, ax1 = plt.subplots()

ax1.plot(data.mean(0), color='tab:blue')
ax1.set_ylabel('Number of mistakes', color='tab:blue')
ax1.set_xlabel('Block')
ax1.set_ylim(0, 5)
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()
ax2.plot(times.mean(0), color='tab:red')
ax2.set_ylabel('Time', color='tab:red')
ax2.set_ylim(0, 700)
ax2.tick_params(axis='y', labelcolor='tab:red')

ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)
plt.tight_layout()

plt.show()