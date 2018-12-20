NIX Dataframe support 
=================== 

The NIX project aims to develop standardized methods and models for storing electrophysiology and other neuroscience data together with their metadata in one common, open file format. It does so by having a central DataArray object that can hold n-dimensional homogeneous data, linked with units and other metadata. Although a DataArray can hold any type of data (int, float, etc) it can only hold one type at a time. In recent years working with heterogenous data in form of tables (DataFrames) has become more and more popular (cf. pandas[2] for Python). The aim of this GSoC project would be to develop a proof-of-concept for such DataFrames in NIX and its python bindings (so pandas DataFrames can be read and written to NIX files). 

Skills needed: C++ (C++11) and Python. 
Mentors: G-Node Developers (Jan Grewe, @jgrewe; Achilleas Koutsou, @achilleas-k) 

[1] https://github.com/G-Node/nix <https://github.com/G-Node/nix> 
[2] http://pandas.pydata.org <http://pandas.pydata.org/> 


NIX filesystem backend support 
======================== 

The NIX[1] project aims to develop standardized methods and models for storing electrophysiology and other neuroscience data together with their metadata in one common, open file format. Currently NIX uses HDF5 files[2] to store the data on-disk, however, the NIX C++ library was designed from the beginning with the idea in mind that different use cases might require different storage solutions. Therefore NIX has the concept of backends that are responsible for writing and reading the  data. The basic groundwork has been done for a ‘filesystem’ backend that  stores the data not in an H5 but directly onto the filesystem using appropriate binary file formats, like NumPy’s npy format[3], for numeric data, and the YAML for metadata. The aim of this GSoC project would be to complete the implementation of the ‘filesystem’ backend to the same level as the HDF5 backend, and to implement copy and sync methods to be able to copy between files of possibly different backends. 

Skills needed: C++ (C++11) 
Mentors: G-Node & NIX Core Team (Jan Grewe, @jgrewe; Achilleas Koutsou, @achilleas-k) 

[1] https://github.com/G-Node/nix <https://github.com/G-Node/nix> 
[2] https://en.wikipedia.org/wiki/Hierarchical_Data_Format
[3] http://docs.scipy.org/doc/numpy/neps/npy-format.html 


odml Editor - Enhancements and Python 3 compatibility
==========================================

The odml[1, 2] data model is designed to store arbitrary experimental metadata in a hierarchical  format. The odml data model is also part of the NIX data format [3] that links metadata and data. We offer a Python implemented GUI for viewing and editing odml data files (XML). So far it has been implemented as part of the core python odml-library for python 2 but it needs to braced for the future, i.e. python 3.x. This project would include separating UI related parts of the codebase to make the editor stand-alone, python 3.x compatible, and allow the editing of metadata originating from NIX files.

Skills needed: Python (2.x and 3.x)
Mentors: G-Node & NIX Core Team (Achilleas Koutsou, @achilleas-k; Jan Grewe, @jgrewe; Michael Sonntag, @mpsonntag) 

[1] https://github.com/G-Node/python-odml <https://github.com/G-Node/python-odml>
[2] Grewe et. al., 2011, Frontiers in Neuroinformatics <http://dx.doi.org/10.3389/fninf.2011.00016>
[3] https://github.com/G-Node/nix <https://github.com/G-Node/nix>

