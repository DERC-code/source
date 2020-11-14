import numpy as np
import matplotlib.pyplot as plt
import mpu92_forTest

def main():
    print("始まったよ")
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlim(-30, 30)
    ax.set_ylim(-30, 30)
    x=0
    y=0
    print("matlab準備")
    mpu92_forTest.MPU9265_init()
    magnet = mpu92_forTest.get_magnet()
    x = magnet[0] -25
    y = magnet[1] -18
    ax.grid(color='gray')
    lines, = ax.plot(x, y, marker="o")
    while True:
        #点の座標の更新
        magnet = mpu92_forTest.get_magnet()
        x = magnet[0] - 25
        y = magnet[1] - 8
        print(x)
        print(y)
        print()
        #新たな点をプロット
        ax.plot(x,y,marker="o",c="dodgerblue")
        plt.pause(.01)

if __name__ == "__main__":
    main()