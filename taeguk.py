# 모듈
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Rectangle

# 초기 설정
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

# 그래프
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# 배경
bg = Rectangle((-7, -5), 14, 10, facecolor="white", edgecolor="black", fill=True)
ax.add_artist(bg)

# (1) 윗쪽 빨간색 반원
uB = Wedge((0, 0), 2, 0, 180, facecolor="red", edgecolor="none")
# (2) 아랫쪽 파란색 반원
dB = Wedge((0, 0), 2, 180, 0, facecolor="blue", edgecolor="none")
# (3) 윗쪽 파란색 반원
uS = Wedge((1, -0.1), 1, 0, 180, facecolor="blue", edgecolor="none")
# (4) 아랫쪽 빨간색 반원
dS = Wedge((-1, 0.1), 1, 180, 0, facecolor="red", edgecolor="none")

for wedge in [uB, dB]:
    ax.add_artist(wedge)
for wedge in [uS, dS]:
    ax.add_artist(wedge)

# (5) 좌상단 = 3개
lu1 = Rectangle((-4, 1), 0.3, 2, angle=-30, facecolor="black", edgecolor="black", fill=True)
lu2 = Rectangle((-4.5, 1.2), 0.3, 2, angle=-30, facecolor="black", edgecolor="black", fill=True)
lu3 = Rectangle((-5, 1.4), 0.3, 2, angle=-30, facecolor="black", edgecolor="black", fill=True)
ax.add_artist(lu1)
ax.add_artist(lu2)
ax.add_artist(lu3)
# (6) 좌하단 = 4개
ld1 = Rectangle((-3.2, -3), 0.3, 2, angle=30, facecolor="black", edgecolor="black", fill=True)
ld2 = Rectangle((-4.2, -2.2), 0.3, 0.9, angle=30, facecolor="black", edgecolor="black", fill=True)
ld3 = Rectangle((-3.6, -3.2), 0.3, 0.9, angle=30, facecolor="black", edgecolor="black", fill=True)
ld4 = Rectangle((-4.1, -3.4), 0.3, 2, angle=30, facecolor="black", edgecolor="black", fill=True)
ax.add_artist(ld1)
ax.add_artist(ld2)
ax.add_artist(ld3)
ax.add_artist(ld4)
# (7) 우상단 = 5개
ru1 = Rectangle((3.4, 2), 0.3, 0.9, angle=30, facecolor="black", edgecolor="black", fill=True)
ru2 = Rectangle((4, 0.95), 0.3, 0.9, angle=30, facecolor="black", edgecolor="black", fill=True)
ru3 = Rectangle((4.5, 1.2), 0.3, 2, angle=30, facecolor="black", edgecolor="black", fill=True)
ru4 = Rectangle((4.5, 2.4), 0.3, 0.9, angle=30, facecolor="black", edgecolor="black", fill=True)
ru5 = Rectangle((5, 1.4), 0.3, 0.9, angle=30, facecolor="black", edgecolor="black", fill=True)
ax.add_artist(ru1)
ax.add_artist(ru2)
ax.add_artist(ru3)
ax.add_artist(ru4)
ax.add_artist(ru5)
# (8) 우하단 = 6개
rd1 = Rectangle((3.4, -1.9), 0.3, 0.9, angle=-30, facecolor="black", edgecolor="black", fill=True)
rd2 = Rectangle((2.8, -3), 0.3, 0.9, angle=-30, facecolor="black", edgecolor="black", fill=True)
rd3 = Rectangle((3.9, -2.15), 0.3, 0.9, angle=-30, facecolor="black", edgecolor="black", fill=True)
rd4 = Rectangle((3.3, -3.25), 0.3, 0.9, angle=-30, facecolor="black", edgecolor="black", fill=True)
rd5 = Rectangle((4.4, -2.4), 0.3, 0.9, angle=-30, facecolor="black", edgecolor="black", fill=True)
rd6 = Rectangle((3.8, -3.5), 0.3, 0.9, angle=-30, facecolor="black", edgecolor="black", fill=True)
ax.add_artist(rd1)
ax.add_artist(rd2)
ax.add_artist(rd3)
ax.add_artist(rd4)
ax.add_artist(rd5)
ax.add_artist(rd6)

ax.set_xticks(range(-8, 9))
ax.set_yticks(range(-6, 6))
ax.set_axisbelow(True)
ax.set_aspect("equal", adjustable="box")
ax.axis("off")

plt.show()
