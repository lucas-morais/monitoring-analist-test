import matplotlib.pyplot as plt


def line_plot(y, data, title=None, xlabel=None, ylabel=None, markers=None):
    fig, ax = plt.subplots()
    if markers:
        ax.scatter(
            markers, data[y][markers], marker="o", color="red", zorder=2
        )
    ax.plot(data.index, data[y], zorder=-1)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()


def composed_plot(y1, y2, data, title1, title2, markers):
    fig, ax = plt.subplots(3, 1)
    if markers:
        ax.scatter(
            markers, data["today"][markers], marker="o", color="red", zorder=2
        )
        ax.scatter(
            markers, data[y1][markers], marker="o", color="red", zorder=2
        )
        ax.scatter(
            markers, data[y2][markers], marker="o", color="red", zorder=2
        )

    ax[0].plot(data.index, data["today"], zorder=-1)
    ax[0].set_title("HOJE")
    ax[1].plot(data.index, data[y1], zorder=-1)
    ax[1].set_title(title1)
    ax[2].plot(data.index, data[y2], zorder=-1)
    ax[2].set_title(title2)
    # ax.set_xlabel("Hora")
    # ax.set_ylabel("POS")
    plt.xlabel("HORA")
    plt.ylabel("POS")
    plt.show()


# def line_plot(y, data, title=None, xlabel=None, ylabel=None, markers=None):
#     ax, fig = plt.subplot()
#     sns.lineplot(y=data.index)
#     ax.set_title(title)
#     ax.set_xlabel(xlabel)
#     ax.set_ylabel(ylabel)
#     if markers:
#         sns.scatter(markers, data[y][markers], marker="o", color="red")

#     return fig
