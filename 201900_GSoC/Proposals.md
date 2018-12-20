# Science continuous integration microservice using Snakemake

The G-Node Data Infrastructure (GIN) services[1] provide a platform for
management and sharing of data in neuroscience. Inspired by existing 
continuous integration services like Travis[2] or CircleCI[3] and
recent developed build pipelines for the scientific field like SnakeMake[4] 
this project will aspire to prototype a continuous integration microservice
for scientific data within the scope of the G-Node Data Infrastructure services. 

Scope of the project is
[ToBeDefined]

A successful application will have some experience with either the Python or the 
Go programming language and ideally is already familiar with either git, 
any continuous integration service or SnakeMake

[1] https://gin.g-node.org
[2] https://travis-ci.org/
[3] https://circleci.com/
[4] https://snakemake.readthedocs.io/en/stable/



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




# Enhance the scientific data files validation service in GIN

The G-Node Data Infrastructure (GIN) services[1] provide a platform for
management and sharing of data in neuroscience. To push the quality 
of published and shared scientific data, this project is extended by a 
scientific data files validation microservice. The existing prototype gin-valid[2]
enables validation of BIDS[3] files within a GIN repository.

Goal of the project is to extend this service to support the validation 
of further scientific data formats, NIX[4] and odML[5] in particular, as well 
as to enhance the usability of the existing prototype. 

A successful application will have some experience with the Go programming
language and is familiar with git and github related topics.

[1] https://gin.g-node.org
[2] https://github.com/G-Node/gin-valid
[3] https://bids.neuroimaging.io/
[4] https://github.com/G-Node/nix
[5] https://github.com/G-Node/python-odml

-----
- Enhance the current validation server found at https://github.com/G-Node/gin-valid
- Fix open issues
- add nix validation
- add odML validation
- add ??? validation
-----

# Extended support for NIX file format in GIN

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
is interested in working with ElasticSearch and JavaScript based data visualization.

[1] https://gin.g-node.org
[2] https://github.com/G-Node/python-odml
[3] https://github.com/G-Node/nix


# other GSoC ideas:
- dataframe – req C++ (use proposal from last year)
- data storage for filesystem backend
- odML editor … integrate into nixView, requires nix to write XML/yaml backend, C++ (rather not)

