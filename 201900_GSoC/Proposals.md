# Continuous integration for research data

The G-Node Data Infrastructure (GIN) services[1] provide a platform for
management and sharing of data in neuroscience. Inspired by
GitHub, the platform uses a git/git-annex backend for versioning and
sharing of scientific data, offering the power of a web based repository
management service combined with a distributed file storage. It addresses the range of
research data workflows starting from data analysis on the local workstation
to remote collaboration and data publication. GIN also provides indexing
services for convenient searching of data and metadata, including information in
well-defined formats like the odML[2] metadata format and the NIX[3] format for
scientific data.

Considering existing continuous integration services like Travis[4] or CircleCI[5] 
and build pipelines for the scientific field like SnakeMake[6] this project aims 
to prototype a continuous integration microservice for research data within 
the scope of the G-Node Data Infrastructure services. 

Scope of the project is to set up a microservice for automated organization and 
processing of data and metadata using established CI technology. The development will
be performed based on a use case of electrophysiological data.

A successful application will have some experience with the Python or the 
Go programming languages and ideally is familiar with git, continuous integration 
services and/or SnakeMake

[1] https://gin.g-node.org
[2] https://github.com/G-Node/python-odml
[3] https://github.com/G-Node/nix
[4] https://travis-ci.org/
[5] https://circleci.com/
[6] https://snakemake.readthedocs.io/en/stable/


## whats our goal with this
    - test code
    - test analysis pipeline
    - test result files
    - use as analysis pipeline

## general structure
    git repository with
    - code
    - data
    - tests
      - snakemake file
      - standard_data
      - (test code)

## Project outline
- server written in go or python; if possible re-use validation server (https://github.com/G-Node/gin-valid)
- clone gin/git repository
- identify snakemake file from root and start snakemake process
- provide latest snakemake build status for every repository
- provide example workflow


# Enhancing the scientific data format validation service in GIN

The G-Node Data Infrastructure (GIN) services[1] provide a platform for
management and sharing of data in neuroscience. Inspired by
GitHub, the platform uses a git/git-annex backend for versioning and
sharing of scientific data, offering the power of a web based repository
management service combined with a distributed file storage. It addresses the range of
research data workflows starting from data analysis on the local workstation
to remote collaboration and data publication. GIN also provides indexing
services for convenient searching of data and metadata, including information in
well-defined formats like the odML[2] metadata format and the NIX[3] format for
scientific data.
 
To push the quality of published and shared scientific data, a microservice for 
validation of scientific data formats is being established. The gin-valid[4] service 
currently enables validation of BIDS[5] files within a GIN repository.

Goal of the project is to extend this service to support the validation 
of further scientific data formats, e.g. NIX, odML, PyNN[6] or NeuroML[7], as well 
as to enhance the usability of the existing prototype. 

A successful candidate will have experience with the Go programming
language and is familiar with git and github related topics.

[1] https://gin.g-node.org
[2] https://github.com/G-Node/python-odml
[3] https://github.com/G-Node/nix
[4] https://github.com/G-Node/gin-valid
[5] https://bids.neuroimaging.io/
[6] https://neuralensemble.org/PyNN/
[7] https://www.neuroml.org/


# Extended support for the NIX file format in GIN

The G-Node Data Infrastructure (GIN) services[1] provide a platform for
management and sharing of data in neuroscience. Inspired by
GitHub, the platform uses a git/git-annex backend for versioning and
sharing of scientific data, offering the power of a web based repository
management service combined with a distributed file storage. It addresses the range of
research data workflows starting from data analysis on the local workstation
to remote collaboration and data publication. GIN also provides indexing
services for convenient searching of data and metadata, including information in
well-defined formats like the odML[2] metadata format and the NIX[3] format for
scientific data.

In this project we want to enhance the GIN data management services
by making use of specific features of the NIX format, such as the comprehensive
organization of metadata and the representation of relationships
between the data. This would materialize as a set of features on the GIN web
frontend for extended search, visualization and exploration of data stored on GIN.

Outcomes of this project would be the ability to extract structural properties and
metadata from files and to present and visualize the results as statistical summaries.

A successful applicant will have some experience with Python and Go as well as git and
is interested in working with ElasticSearch and JavaScript-based data visualization.

[1] https://gin.g-node.org
[2] https://github.com/G-Node/python-odml
[3] https://github.com/G-Node/nix


# other GSoC ideas:
- dataframe – req C++ (use proposal from last year)
- data storage for filesystem backend
- odML editor … integrate into nixView, requires nix to write XML/yaml backend, C++ (rather not)

