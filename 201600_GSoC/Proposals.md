Python-neuroshare, bringing it into the future together with NIX
================================================

Python-neuroshare[1] is a high level interface to the Neuroshare API, a standardized interface to access electrophysiology data stored in various different file formats. 
One of the "unsung heroes of scientific software" it is in the top 3 of used software in neuroscience[2,3].
The NIX project[4] otoh aims to develop standardized methods and models for storing electrophysiology and other neuroscience data together with their metadata in one common, open file format. 

This GSoC project would be twofold: 1) Refresh and modernize the python-neuroshare code base, e.g. adding Python 3 support. 2) Modify the current neuronshare to hdf5 converter to use NIX instead (via nixpy); having such a converter would mean any proprietary file that can be read with neuroshare could converted with no or little loss of information to an open non-proprietary format. 

[1] https://github.com/G-Node/python-neuroshare
[2] http://www.nature.com/news/the-unsung-heroes-of-scientific-software-1.19100
[3] http://depsy.org/tag/neuroscience
[4] https://github.com/G-Node/nix


NIX Dataframes support
===================

The NIX project aims to develop standardized methods and models for storing electrophysiology and other neuroscience data together with their metadata in one common, open file format. It does so by having a central DataArray object that can hold n-dimensional homogenous data, that is linked with units and other metadata. Although a DataArray can hold any type of data (int, float, etc) it can only hold one type at a time. In recent years working with heterogenous data in form of tables(DataFrames)  has become more and more popular (cf. pandas[2] for Python). The aim of this GSoC project would be to develop a proof-of-concept for such DataFrames to NIX and its python bindings (so pandas DataFrames can be read and written to NIX).

[1] https://github.com/G-Node/nix
[2] http://pandas.pydata.org


NIX filesystem backend support
========================

The NIX project aims to develop standardized methods and models for storing electrophysiology and other neuroscience data together with their metadata in one common, open file format. Currently NIX uses HDF5 files[2] to store the data on-disk. Recently there is concern if H5 is the right format for actively working with files, since that has led to file corruptions[3]. The architecture of the NIX C++ library was designed from the beginning with the idea in mind that different use cases might require different binary file-formats. Therefore NIX has the concept of backends that are responsible for writing and reading the binary data. The basic groundwork has been done for a 'filesystem' backend the would store the data not in an H5 but directly onto the filesystem using the YAML format for metadata and various binary file formats, like e.g. NumPy's npy format, for numeric data. The task for this GSoC project would be to complete the implementation of the 'filesystem' backend to at the same level as the HDF5 backend. Additionally various copy and sync methods have to be developed to be able to copy between different files of possibly different formats. 

[1] https://github.com/G-Node/nix
[2] https://en.wikipedia.org/wiki/Hierarchical_Data_Format
[3] http://cyrille.rossant.net/moving-away-hdf5/
[4] http://docs.scipy.org/doc/numpy/neps/npy-format.html


