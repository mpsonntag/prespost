# BCCN 2022     Off- and on-site collaboration and publication: The G-Node Infrastructure Services for research data management
Michael Sonntag1 Achilleas Koutsou1 Thomas Wachtler1
G-Node, Faculty of Biology, Ludwig-Maximilians-Universität München, Martinsried, Germany

----

Maintaining reproducible analysis workflows while keeping data in sync, backed up, and accessible from within and outside the lab is a growing challenge in research. To minimize the time and effort required for these tasks, we present the G-Node Infrastructure (GIN) services [1], a tool suite for comprehensive, reproducible and versioned management of scientific data.
GIN offers the power of a repository management service (inspired by GitHub [2]) with easy to use interfaces for data management through web browser, command line, or programmatic integration in analysis scripts to automate data management, processing and analysis. Integrated version control tracks changes and facilitates effortless data sharing and joint work on data within a lab or with off-site collaborators.
GIN extends and is fully compatible with established versioning tools (git [3] and git-annex [4]) and offers seamless data access with methods provided by those tools as well as with common web protocols or third party applications like DataLad [5]. Furthermore, it integrates with tools for data and metadata management [6,7,8] and provides indexing and easy web-based editing of metadata.
Further features are provided by micro-services that extend the base service. GIN's DOI service [9] offers easy data publication of public GIN datasets with persistent identifiers. GIN-valid [10], a validation service for data formats, supports automated quality management of research data. Supported formats include BIDS, odML and NIX and can easily be extended to custom formats.
While the GIN service hosted by the G-Node provides an open platform for collaboration and publication, the option to set up GIN locally [11] offers the GIN research data management services for use within a lab or research institution.
GIN services are easy to use, interoperate with other tools supporting reproducibility and data sharing, and enable efficient data management in line with the FAIR principles [12].


*References

1 GIN (RRID:SCR_015864): https://gin.g-node.org 
2 GitHub: https://github.com
3 git: https://git-scm.com
4 git-annex: https://git-annex.branchable.com
5 Datalad (RRID:SCR_003931): http://datalad.org
6 NIX (RRID:SCR_016196): https://www.g-node.org/nix
7 odML (RRID:SCR_001376): https://www.g-node.org/odml
8 BIDS (RRID:SCR_016124): https://bids.neuroimaging.io
9 GIN-DOI https://doi.gin.g-node.org
10 GIN-Valid https://valid.gin.g-node.org
11 in-house GIN https://gin.g-node.org/G-Node/in-house-gin
12 Wilkinson et al (2016) The FAIR guiding principles for scientific data management and stewardship. Scientific Data 3:160018, https://doi.org/10.1038/sdata.2016.18


*Acknowledgements 
Supported by BMBF (Grants 01GQ1302 and 01GQ1509) and the Bernstein Center for Computational Neuroscience Munich.

* Author eMails used
- sonntag@bio.lmu.de
- koutsou@biologie.uni-muenchen.de
- wachtler@biologie.uni-muenchen.de

