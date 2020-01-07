# Extended support for NIX file format in GIN

The G-Node Data Infrastructure (GIN) services[1] provide a platform for management and sharing of data in neuroscience.  Inspired by GitHub, the platform uses git and git-annex for versioning and sharing of scientific data, offering the power of a web-based repository management service combined with distributed version control.  It addresses the range of research data workflows from data processing and analysis on the local workstation to remote collaboration and data publication.  GIN also provides indexing services for convenient searching of data and metadata, including information in well-defined formats like the odML[2] metadata format and the NIX[3] format for scientific data.

In this project we want to enhance the GIN data management services by making use of specific features of the NIX format, such as the comprehensive organization of metadata and the representation of relationships between the data.  This would materialize as a set of features on the GIN web frontend for extended search, visualization and exploration of data stored on GIN.

Outcomes of this project would be the ability to search for and extract structural properties and metadata from files and to present and visualize the results.

A successful applicant will have some experience with Python and Go as well as git and will be interested in working with ElasticSearch and JavaScript based data visualization.

Mentors: G-Node & NIX Core Team (Achilleas Koutsou, @achilleas-k; Jan Grewe, @jgrewe; Michael Sonntag, @mpsonntag)

[1] https://gin.g-node.org
[2] https://github.com/G-Node/python-odml
[3] https://github.com/G-Node/nix

# NIX file system backend support

The NIX[1] project aims to develop standardized methods and models for storing electrophysiology and other neuroscience data together with their metadata in a common, open file format.  Currently implementations of NIX use HDF5[2] to store data, however the NIX specification does not define a storage format.  Instead, NIX was designed to be file format agnostic, so that storage formats can be chosen based on the usage requirements.

The current libraries were developed to allow alternate storage backends to be implemented with little modifications to the existing code.  This project will aim to implement a filesystem-based backend for storing NIX data.  Some preliminary work has already been done on this backend, which stores data in multiple files in a nested directory tree, using appropriate binary file formats for data, like NumPy's npy format[3] for numeric data, and YAML for metadata.

The aim of this GSoC project would be to complete the implementation of the file system backend such that it is at feature-parity with the HDF5 backend and to implement methods for copying data between files of possibly different backends.  Skills needed: C++ (C++11).

Mentors: G-Node & NIX Core Team (Achilleas Koutsou, @achilleas-k; Jan Grewe, @jgrewe; Michael Sonntag, @mpsonntag)

[1] https://github.com/G-Node/nix
[2] https://en.wikipedia.org/wiki/Hierarchical_Data_Format
[3] http://docs.scipy.org/doc/numpy/neps/npy-format.html
