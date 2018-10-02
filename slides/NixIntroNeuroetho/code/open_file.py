import nixio as nix

f = nix.File.open("../2018-05-17-ab.nix", nix.FileMode.ReadOnly)

print("file format: %s \t format version: %s, library version %s"
      % (f.format, f.version, nix.__version__))

print("Blocks:")
for b in f.blocks:
    print("\t%s" % b.name)

print("Metadata sections:")
for s in f.sections:
    print("\t%s" % s.name)

f.close()
