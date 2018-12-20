Python-neuroshare, bringing it into the future together with NIX 
================================================ 

Python-neuroshare[1] is a high-level interface to the Neuroshare API, a standardized interface to access electrophysiology data stored in various different file formats. One of the "unsung heroes of scientific software" it is in the top 3 of used software in neuroscience[2,3]. 
Currently python-neuroshare provides only a limited custom format for storing the data. The NIX project[4] otoh aims to develop standardized methods and models for storing electrophysiology and other neuroscience data together with their metadata in one common, open file format. 

This GSoC project would be twofold: 1) Refresh and modernize the python-neuroshare code base, e.g. adding Python 3 support. 2) Modify the current neuronshare to hdf5 converter to use the NIX format instead (via nixpy[5]); having such a converter would mean any proprietary file that can be read with neuroshare could converted with no or little loss of information to an open non-proprietary format. 

Skills needed: Python and C. 
Mentors: G-Node Developers (Christian Kellner, @gicmo) 

[1] https://github.com/G-Node/python-neuroshare <https://github.com/G-Node/python-neuroshare> 
[2] http://www.nature.com/news/the-unsung-heroes-of-scientific-software-1.19100 <http://www.nature.com/news/the-unsung-heroes-of-scientific-software-1.19100> 
[3] http://depsy.org/tag/neuroscience <http://depsy.org/tag/neuroscience> 
[4] https://github.com/G-Node/nix <https://github.com/G-Node/nix> 
[5] https://github.com/G-Node/nixpy <https://github.com/G-Node/nixpy>


NIX Dataframes support 
=================== 

The NIX project aims to develop standardized methods and models for storing electrophysiology and other neuroscience data together with their metadata in one common, open file format. It does so by having a central DataArray object that can hold n-dimensional homogeneous data,linked with units and other metadata. Although a DataArray can hold any type of data (int, float, etc) it can only hold one type at a time. In recent years working with heterogenous data in form of tables (DataFrames) has become more and more popular (cf. pandas[2] for Python). The aim of this GSoC project would be to develop a proof-of-concept for such DataFrames in NIX and its python bindings (so pandas DataFrames can be read and written to NIX files). 

Skills needed: C++ (C++11) and Python. 
Mentors: G-Node Developers (Christian Kellner, @gicmo) 

[1] https://github.com/G-Node/nix <https://github.com/G-Node/nix> 
[2] http://pandas.pydata.org <http://pandas.pydata.org/> 


NIX filesystem backend support 
======================== 

The NIX project aims to develop standardized methods and models for storing electrophysiology and other neuroscience data together with their metadata in one common, open file format. Currently NIX uses HDF5 files[2] to store the data on-disk, however, the NIX C++ library was designed from the beginning with the idea in mind that different use cases might require different storage solutions. Therefore NIX has the concept of backends that are responsible for writing and reading the binary data. The basic groundwork has been done for a ‘filesystem’ backend that would store the data not in an H5 but directly onto the filesystem usingappropriate binary file formats, like NumPy’s npy format, for numeric data, and the YAML format for metadata. The aim of this GSoC project would be to complete the implementation of the ‘filesystem’ backend to the same level as the HDF5 backend, and to implement copy and sync methods to be able to copy between different files of possibly different formats. 

Skills needed: C++ (C++11) 
Mentors: G-Node & NIX Core Team (Jan Grewe, @jgrewe; Christian Kellner, @gicmo) 

[1] https://github.com/G-Node/nix <https://github.com/G-Node/nix> 
[2] https://en.wikipedia.org/wiki/Hierarchical_Data_Format <https://en.wikipedia.org/wiki/Hierarchical_Data_Format> 
[3] http://cyrille.rossant.net/moving-away-hdf5/ <http://cyrille.rossant.net/moving-away-hdf5/> 
[4] http://docs.scipy.org/doc/numpy/neps/npy-format.html <http://docs.scipy.org/doc/numpy/neps/npy-format.html>
