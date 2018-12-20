NIX filesystem backend support 
======================== 

The NIX project aims to develop standardized methods and models for storing electrophysiology and other neuroscience data together with their metadata in one common, open file format. Currently NIX uses HDF5 files[2] to store the data on-disk, however, the NIX C++ library was designed from the beginning with the idea in mind that different use cases might require different storage solutions. Therefore NIX has the concept of backends that are responsible for writing and reading the binary data. The basic groundwork has been done for a ‘filesystem’ backend that would store the data not in an H5 but directly onto the filesystem usingappropriate binary file formats, like NumPy’s npy format, for numeric data, and the YAML format for metadata. The aim of this GSoC project would be to complete the implementation of the ‘filesystem’ backend to the same level as the HDF5 backend, and to implement copy and sync methods to be able to copy between different files of possibly different formats. 

Skills needed: C++ (C++11) 
Mentors: G-Node & NIX Core Team (Jan Grewe, @jgrewe; Christian Kellner, @gicmo) 

[1] https://github.com/G-Node/nix <https://github.com/G-Node/nix> 
[2] https://en.wikipedia.org/wiki/Hierarchical_Data_Format <https://en.wikipedia.org/wiki/Hierarchical_Data_Format> 
[3] http://cyrille.rossant.net/moving-away-hdf5/ <http://cyrille.rossant.net/moving-away-hdf5/> 
[4] http://docs.scipy.org/doc/numpy/neps/npy-format.html <http://docs.scipy.org/doc/numpy/neps/npy-format.html>

