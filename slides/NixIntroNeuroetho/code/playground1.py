import nixio as nix
import matplotlib.pyplot as plt
import numpy as np

f = nix.File.open("../2018-05-17-ab.nix", nix.FileMode.ReadOnly)
b = f.blocks[0]

eod = b.data_arrays["EOD"]
dim = eod.dimensions[0]

plt.plot(dim.axis(1000), eod[:1000], label=eod.name)
plt.xlabel("%s [%s]" % (dim.label, dim.unit))
plt.ylabel("%s [%s]" % (eod.label, eod.unit))
plt.legend()
plt.show()

f.close()
