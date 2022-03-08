import matplotlib.pyplot as plt


def jensen(c, t, k):
    L = c * t * pow(k, 1 / 3)
    return L


def relay_graph(c, t, k):
    project_duration = 3 * int(t)
    y = [round(jensen(c, time, k), 5) for time in range(0, project_duration)]

    plt.plot(y, color="blue", linewidth=4, label="Project size respect to time")
    # plt.vlines(
    #     x=td,
    #     ymin=0,
    #     ymax=round(nordan(k, td, td), 5),
    #     color="green",
    #     linestyle="dashed",
    #     linewidth=4,
    #     label=td,
    # )
    # plt.vlines(
    #     x=t,
    #     ymin=0,
    #     ymax=round(nordan(k, td, t), 5),
    #     color="red",
    #     linestyle="dashed",
    #     linewidth=4,
    #     label="t",
    # )
    plt.legend(loc="upper right")
    plt.xlabel("time")
    plt.ylabel("Effort per unit time")
    plt.title("r_curve")
    plt.show()


if __name__ == "__main__":
    print("###################   Jensen formula   ###################")
    # c = float(input("Enter the effective technology  constant:"))
    # t = float(input("Enter the development time: "))
    # k = float(input("Enter the effort needed to develop: "))
    c = 2
    t = 4
    k = 5
    print("\nThe product size(L) is = ", round(jensen(c, t, k), 5), "KLOC")
    relay_graph(c, t, k)

