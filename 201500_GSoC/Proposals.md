odML back-end for NIX to access metadata in XML files

The NIX[1] project aims to standardize methods and models to store
electrophysiology and other neuroscience data together with their
metadata in one common file format based on HDF5. Storing the metadata
in NIX is accomplished by using the odML[2] data model. odML is an
initiative to define and establish an open, flexible and easy-to-use
format to transport metadata based on XML.
The NIX C++ library, which is used to access data from NIX files,
currently only supports metadata stored in HDF5. The goal for this
project would be to implement an additional back-end for the NIX library
that allows to access also metadata stored in XML.

This project requires a good knowledge about C++ and provides a good
opportunity to deepen your C++ skills and to get familiar with some
newer features of the C++11 standard.

[1] https://github.com/G-Node/nix
[2] http://www.g-node.org/projects/odml

