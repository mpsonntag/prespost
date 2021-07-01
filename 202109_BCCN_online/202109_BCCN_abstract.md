# BCCN 2021     Collaborate and Publish with ease: The G-Node infrastructure services for Research Data Management in Neuroscience and Beyond
Michael Sonntag1 Achilleas Koutsou1 Jan Grewe2 Thomas Wachtler1
G-Node, Department of Biology II, Ludwig-Maximilians-Universität München, Martinsried, Germany
Institute for Neurobiology, Eberhard-Karls-Universität Tübingen, Tübingen, Germany

----

Maintaining reproducible data workflows while keeping data in sync, backed up, and easily accessible from within and outside the lab is a key challenge in research. To minimize the time and effort required for these tasks, we present the GIN services [1], a suite of tools designed for comprehensive, reproducible and versioned management of scientific data.
GIN extends and is fully compatible with established versioning tools (git [2] and git-annex [3]) and offers seamless data access with methods provided by those tools, with common web protocols or third party applications like DataLad [4]. Furthermore, it integrates with tools for data and metadata management [5,6,7] and provides indexing and easy web-based editing of metadata.
GIN offers the power of a repository management service (inspired by GitHub [8]) with easy to use interfaces for data management through a web browser, from the desktop file browser, from the command line, or even by programmatic integration in analysis scripts to further automate data acquisition, analysis and management. The integral version control enables tracking changes and facilitates effortless data sharing and joint manipulation within a lab or with off-site collaborators.
Additional micro-services, including GIN's DOI [9] service provides easy data publication of public GIN datasets with persistent identifiers. GIN-valid [10], a validation service for data formats, support automated quality management of research data. Supported formats include BIDS, odML and NIX and can easily be extended to custom formats. The new GIN tonic [11] micro-service provides a framework to create and automate custom workflows when working with GIN.
The tools presented are easy to use, interoperate with other tools supporting reproducibility and data sharing, and enable efficient data management in line with the FAIR principles [12].

*References

1 GIN (RRID:SCR_015864): https://gin.g-node.org 
2 git: https://git-scm.com
3 git-annex: https://git-annex.branchable.com
4 Datalad (RRID:SCR_003931): http://datalad.org
5 NIX (RRID:SCR_016196): http://www.g-node.org/nix
6 odML (RRID:SCR_001376): http://www.g-node.org/odml
7 BIDS (RRID:SCR_016124): http://bids.neuroimaging.io
8 GitHub https://github.com
9 GIN-DOI https://doi.gin.g-node.org
10 GIN-Valid https://valid.gin.g-node.org
11 GIN-tonic https://github.com/G-Node/tonic
12 Wilkinson et al (2016) The FAIR guiding principles for scientific data management and stewardship. Scientific Data 3:160018, https://doi.org/10.1038/sdata.2016.18


*Acknowledgements 
Supported by BMBF (Grants 01GQ1302 and 01GQ1509)

* Author eMails used
- sonntag@bio.lmu.de
- koutsou@biologie.uni-muenchen.de
- jan.grewe@uni-tuebingen.de
- wachtler@biologie.uni-muenchen.de

