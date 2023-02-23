# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits import mplot3d
#
#
# def plot_surface(domain, fn, grid_samples=100, title=None, **plot_kwargs):
#     x = np.linspace(domain[0][0], domain[0][1], grid_samples)
#     y = np.linspace(domain[1][0], domain[1][1], grid_samples)
#
#     X, Y = np.meshgrid(x, y)
#
#     fn_vectorized = np.vectorize(fn)
#     Z = fn_vectorized(X, Y)
#
#     fig = plt.figure(figsize=(20, 10))
#     ax = plt.axes(projection="3d")
#     ax.plot_surface(X, Y, Z, **plot_kwargs)
#     ax.set(xlabel="x", ylabel="y", zlabel="f(x, y)", title=title)
#     plt.close()
#
#     return fig, ax
#
#
# # now let's try it out!
# def func(x, y):
#     return -np.sin(10 * (x ** 2 + y ** 2)) / 10
#
#
# domain = [(-0.5, 0.5), (-0.5, 0.5)]
# fig, ax = plot_surface(domain, func, rstride=1, cstride=1, cmap='terrain', edgecolor=None)
#
# plt.plot()
