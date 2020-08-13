# Open tools and services for reproducible workflows and efficient data management, collaboration and data publication

Maintaining reproducible analysis workflows while keeping data in sync, backed up, and easily accessible from within and outside the lab is a key challenge in research. The G-Node provides a suite of tools, services and open platforms designed for comprehensive and versioned management of scientific data, seamless integration into automated and reproducible workflows and ease of use collaboration and data publication.
To address reproducibility and data re-usability the lightweight odML[1] metadata format provides users with a flexible option to collect and organize any kind of metadata enabling automated metadata collection and analytic pipelines[2] as well as conversion of diverse metadata to other formats such as RDF to utilize semantic web technologies.
The equally flexible NIX[3] data format takes the concept a step further by combining data and metadata and effectively linking data and corresponding analysis results as well as the associated metadata keeping the whole analysis pipeline in a single file and attached to the relevant metadata. It supports a wide range of data types, including electrophysiology and imaging data. NIX uses the odML metadata format and is integrated with the Neo[4] Python package for electrophysiology, enabling Neo users to store their data in a common open format.
To handle scientific data on a larger scale the GIN[5] services provide data management, collaborative data sharing and data publication.Using established versioning technology [6,7], GIN keeps track of changes and provides secure access, making it convenient to work from multiple workplaces while keeping all data available and in sync. Data can be managed from web and file browsers or a command line client, enabling integration into data acquisition or analysis procedures. The service works with any kind of directory structure and file types, keeping previous versions accessible when datasets are updated. It makes it straightforward to share data within a lab or with off-site collaborators and to work on it together. The microservice architecture of GIN makes it easy to plug in additional services like the GIN-DOI[8] service for persistent data publication identifiers or the GIN-Valid[9] service to automate data format validation and quality control.
The tools presented are easy to use, can be combined with other approaches supporting reproducibility and data sharing[10,11,12], and enable efficient data management that 
supports the FAIR principles[13].


1. odML: http://www.g-node.org/odml 
2. Handling Metadata in a Neurophysiology Laboratory: https://doi.org/10.3389/fninf.2016.00026 
3. NIX: http://www.g-node.org/nix 
4. Neo: http://neuralensemble.org/neo 
5. GIN: https://gin.g-node.org 
6. Git: https://git-scm.com 
7. Git annex: https://git-annex.branchable.com
8. GIN-DOI: https://doi.gin.g-node.org
9. GIN-Valid: https://valid.gin.g-node.org
11. Sumatra: http://neuralensemble.org/sumatra 
10. BIDS: http://bids.neuroimaging.io 
12. DataLad: http://datalad.org 
13. The FAIR Guiding Principles for scientific data management and stewardship: https://doi.org/10.1038/sdata.2016.18 
