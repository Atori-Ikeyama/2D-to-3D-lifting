import matplotlib.pyplot as plt


def vis2D(data: list) -> None:
    """
    Visualize 2D data
    """

    ims = []
    fig = plt.figure()
    ax = fig.add_subplot(111)

    images1 = ax.scatter(np_data_T[0], np_data_T[1], c='r', marker='o')
    images2 = ax.plot([data[0][0], data[1][0]], [
        data[0][1], data[1][1]], c='g')
    images3 = ax.plot([data[0][0], data[2][0]], [
        data[0][1], data[2][1]], c='g')
    images4 = ax.plot([data[1][0], data[3][0]], [
        data[1][1], data[3][1]], c='g')
    images5 = ax.plot([data[4][0], data[0][0]], [
        data[4][1], data[0][1]], c='g')
    images6 = ax.plot([data[4][0], data[1][0]], [
        data[4][1], data[1][1]], c='g')
    images7 = ax.plot([data[4][0], data[5][0]], [
        data[4][1], data[5][1]], c='b')
    images8 = ax.plot([data[5][0], data[7][0]], [
        data[5][1], data[7][1]], c='b')
    images9 = ax.plot([data[5][0], data[8][0]], [
        data[5][1], data[8][1]], c='b')
    images10 = ax.plot([data[5][0], data[9][0]], [
        data[5][1], data[9][1]], c='b')
    images11 = ax.plot([data[8][0], data[12][0]], [
        data[8][1], data[12][1]], c='c'),
    images12 = ax.plot([data[9][0], data[13][0]], [
        data[9][1], data[13][1]], c='c')
    images13 = ax.plot([data[12][0], data[16][0]], [
        data[12][1], data[16][1]], c='c')
    images14 = ax.plot([data[13][0], data[17][0]], [
        data[13][1], data[17][1]], c='c')
    images15 = ax.plot([data[7][0], data[6][0]], [
        data[7][1], data[6][1]], c='b')
    images16 = ax.plot([data[6][0], data[10][0]], [
        data[6][1], data[10][1]], c='b')
    images17 = ax.plot([data[6][0], data[11][0]], [
        data[6][1], data[11][1]], c='b')
    images18 = ax.plot([data[10][0], data[14][0]], [
        data[10][1], data[14][1]], c='c')
    images19 = ax.plot([data[11][0], data[15][0]], [
        data[11][1], data[15][1]], c='c')
    images20 = ax.plot([data[14][0], data[18][0]], [
        data[14][1], data[18][1]], c='c')
    images21 = ax.plot([data[15][0], data[19][0]],
                       [data[15][1], data[19][1]], c='c')

    ani = animation.ArtistAnimation(fig, ims, blit=True, interval=500)
    ani.save('test.mp4', writer='ffmpeg')


def vis3D(data: list) -> None:
    """
    Visualize 3D data
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter3D(np.ravel(X1), np.ravel(X2), y)
    ax.set_title("Scatter Plot")
    plt.show()
