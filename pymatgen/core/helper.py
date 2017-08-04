from pymatgen import vis
from monty.serialization import loadfn
import matplotlib as mpl
mpl.use("TkAgg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import os, itertools, re

colors = loadfn(os.path.join(os.path.dirname(vis.__file__), "ElementColorSchemes.yaml"))
color_dict = {el:[j / 256. for j in colors["Jmol"][el]] for el in colors["Jmol"].keys()}


def vis_struct(structure, res=100, show_unit_cell=True):
    """
    Visualizes structure using 3d matplotlib plot
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_aspect('equal')
    #plot unit cell
    if show_unit_cell:
        vecs = structure.lattice.matrix
        for vec in vecs:
            ax.plot(*zip([0, 0, 0], vec), 'k-', zorder=0)
        for (vec1, vec2) in itertools.permutations(vecs, 2):
            ax.plot(*zip(vec1, vec1+vec2), 'k-', zorder=0)
        for (vec1, vec2, vec3) in itertools.permutations(vecs, 3):
            ax.plot(*zip(vec1+vec2, vec1+vec2+vec3), 'k-', zorder=0)
    phi = np.linspace(0, 2*np.pi, res)
    theta = np.linspace(0, np.pi, res)
    regex = re.compile('[^a-zA-Z]')
    for site in structure.sites:
        rad = float(site.specie.atomic_radius)
        loc = site.coords
        xm = rad * np.outer(np.cos(phi), np.sin(theta)) + loc[0]
        ym = rad * np.outer(np.sin(phi), np.sin(theta)) + loc[1]
        zm = rad * np.outer(np.ones(np.size(phi)), np.cos(theta)) + loc[2]
        color = color_dict[regex.sub('', site.species_string)]
        ax.plot_surface(xm, ym, zm, color=color, linewidth=0, zorder=1)
    return fig
