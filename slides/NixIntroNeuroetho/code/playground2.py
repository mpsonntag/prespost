import nixio as nix
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)

f = nix.File.open("../2018-05-17-ab.nix", nix.FileMode.ReadOnly)
b = f.blocks[0]

tag = b.tags["ReceptiveField_0"]
mtag = b.multi_tags["ReceptiveField-1"]

eod_array = tag.references["LocalEOD-2"]
time_dimension = eod_array.dimensions[0]
eod = tag.retrieve_data("LocalEOD-2")[:]
time = time_dimension.axis(len(eod)) + tag.position[0]

ax.plot(time[::10], eod[::10], lw=0.5, label=eod_array.name)
ax.set_xlabel("%s [%s]" % (time_dimension.label, time_dimension.unit))
ax.set_ylabel("%s [%s]" % (eod_array.label, eod_array.unit))

for i, (s, e) in enumerate(zip(mtag.positions[:], mtag.extents[:])):
    x_pos = mtag.retrieve_feature_data(i, "ReceptiveField-1_x_pos")[:]
    ax.plot([s, s+e], [2, 2], lw=2, color="red")
    ax.text(s, 2.25, str(x_pos[0]), fontsize=6, color="red")

plt.show()
f.close()
