## BCCN 2019 Lightweight tools for safe and efficient data management, processing and validation of research data
## INCF 2019 Microservice infrastructure for continuous validation, processing and indexing of research data on an open platform
## NWG 2019 Achieving reproducible data workflows: Lightweight tools for safe and efficient data management
## SfN 2019 Spend your time on science, not on data management: Open tools for efficient data organization, reproducible workflows, and collaboration
## SfN optional Safe and user friendly data management tools for science
## INCF 2020 GIN: Open platform and services for efficient research data management, collaboration and data publication


Abstract BCCN 2019
Maintaining reproducible analysis workflows while keeping data in sync, backed up, and easily accessible from within and outside the lab is a key challenge in research. To minimize time and effort scientists have to spend on these tasks, we provide a suite of tools and services and open platforms designed for comprehensive, reproducible and versioned management of scientific data.

Efficient selection and analysis require that metadata providing information about experimental conditions is available. The odML[1] metadata format is an easy to use method to flexibly collect and organize any kind of metadata. It enables comprehensive collection and automated processing of metadata[2]. Additionally, pre-defined templates and terminologies are available from an online service that also features a forum for usage discussions and exchange of metadata templates within the scientific community.

To keep data and metadata organized, the NIX[3] data format enables to effectively link data and corresponding analysis results as well as the associated metadata. It supports a wide range of data types, including electrophysiology and imaging data. NIX embeds the odML metadata format and integrates with the Neo[4] Python package for electrophysiology, enabling Neo users to store their data in a common open format.

The GIN[5] services provide versioned data management and collaborative data sharing. Using well established version control systems [6,7], GIN keeps track of changes and provides secure access, making it convenient to work from multiple workplaces while keeping all data available and in sync. Data can be managed from web and file browsers or a command line client, enabling integration into data acquisition or analysis procedures. This also makes it straightforward to share data within a lab or with off-site collaborators and to work on it together. The GIN services also feature automated data validation for various data types including the BIDS[8], NIX and odML formats, validation of CSV tables based on goodtables[9] is under development.

The tools presented are easy to use, are compatible with other approaches supporting reproducibility and data sharing [10,11], and enable efficient data management that supports the FAIR principles [12]. Combining them for data annotation, organization, and storage allows streamlining data workflows and efficiently sharing datasets within the lab, among collaborators, or with the larger scientific community.

*References

1. Grewe et al (2011). A bottom-up approach to data annotation in neurophysiology. Front. Neuroinform. 5:16. 
   doi:10.3389/fninf.2011.00016
   (RRID:SCR_001376)
2. Zehl et al (2016) Handling metadata in a neurophysiology laboratory. Frontiers in Neuroinformatics 10:26.
   doi:10.3389/fninf.2016.00026
3. NIX (RRID:SCR_016196): http://www.g-node.org/nix
4. NEO (RRID:SCR_000634): http://neuralensemble.org/neo
5. GIN (RRID:SCR_015864): https://gin.g-node.org
6. git: https://git-scm.com
7. git-annex: https://git-annex.branchable.com
8. BIDS (RRID:SCR_016124): http://bids.neuroimaging.io
9. goodtables: https://goodtables.io/
10. Sumatra: http://neuralensemble.org/sumatra
11. Datalad: http://datalad.org
12. Mark D. Wilkinson et al (2016). The FAIR Guiding Principles for scientific data management and stewardship. Scientific Data volume 3, Article number: 160018
    https://doi.org/10.1038/sdata.2016.18


Abstract INCF 2019
Research requires data to continuously be processed, analyzed and visualized; data needs to be quality checked, verified and backed up. Data and metadata need to be made publicly available in an easy to find and use manner. Many of these tasks can be automated, which usually leads to fewer errors and a higher results quality. To facilitate these tasks, we introduce a suite of microservices for the G-Node data infrastructure (GIN), an open platform for collaboration and sharing of research data and code.

- gin-valid is a service for validating files in GIN repositories based on various format standards. Once a GIN repository is registered with the validation service, every update to the data automatically triggers validators for the supported types and the results are made available to the owner. The service covers the BIDS[2], NIX[3] and odML[4] formats, validation of CSV tables based on goodtables[5] is in development.
- gin-proc automates data processing, based on SnakeMake[6] and Drone CI[7] making workflows reproducible. Much like gin-valid, a registered repository will execute a defined data processing workflow whenever data changes occur.
- gin-dex automatically extracts metadata information from supported file types and provides extensive search across GIN repositories, making data easily findable and accessible.

These new microservices for the GIN framework enable achieving higher quality and FAIRness of data while reducing workload for scientists.

*References

1. GIN (RRID:SCR_015864): https://gin.g-node.org 
2. BIDS (RRID:SCR_016124): http://bids.neuroimaging.io 
3. NIX (RRID:SCR_016196): http://www.g-node.org/nix 
4. odML (RRID:SCR_001376): http://www.g-node.org/odml 
5. goodtables: https://goodtables.io/
6. SnakeMake (RRID:SCR_003475): https://doi.org/10.1093/bioinformatics/bts480
7. DroneCI: https://drone.io/


Abstract INCF 2020
Maintaining reproducible data workflows while keeping data in sync, backed up, and easily accessible from within and outside the lab is a key challenge in research. To minimize the time and effort required for these tasks, we present the GIN services [1], a suite of tools designed for comprehensive, reproducible and versioned management of scientific data.
GIN extends and is fully compatible with established versioning tools (git [2] and git-annex [3]) and offers seamless data access with methods provided by those tools or with common web protocols (HTML, WebDAV). Furthermore, it integrates with tools for data and metadata management [4,5,6,7] and provides indexing and easy web-based editing of metadata. GIN offers the power of a repository management service (inspired by GitHub [8]) with easy to use interfaces for data management through a web browser, from the desktop file browser, from the command line, or in analysis scripts. GIN makes it straightforward to share data within a lab or with off-site collaborators and to work on it together. Additional microservices, including GIN-Valid [9], a validation service for data formats, support automation and quality management of research data. GIN’s DOI service provides easy data publication with persistent identifiers.
In summary, GIN offers a convenient and powerful solution  for collaborative data management - open, FAIR, and straightforward.

Supported by BMBF (Grant 01GQ1302)

References
1 GIN (RRID:SCR_015864): https://gin.g-node.org 
2 git: https://git-scm.com
3 git-annex: https://git-annex.branchable.com
4 odML (RRID:SCR_001376): http://www.g-node.org/odml 
5 NIX (RRID:SCR_016196): http://www.g-node.org/nix
6 BIDS (RRID:SCR_016124): http://bids.neuroimaging.io
7 Datalad (RRID:SCR_003931): http://datalad.org
8 GitHub https://github.com
9 GIN-Valid https://valid.gin.g-node.org

Abstract MWG 2019
Maintaining reproducible data workflows while keeping data in sync, backed up, and easily accessible from within and outside the lab is a key challenge in research. To minimize time and effort scientists have to spend on these tasks, we provide a suite of tools designed for comprehensive, reproducible and versioned management of scientific data. 
Reproducibility and data re-usability require the presence of metadata also providing information about experimental conditions. The odML[1] metadata format is a simple and convenient format to flexibly collect and organize any kind of metadata. It enables comprehensive collection and automated processing of metadata[2], including conversion to other formats such as RDF to utilize semantic web technologies. 
To keep data and metadata organized, the NIX[3] data format enables to effectively link data and corresponding analysis results as well as the associated metadata. It supports a wide range of data types, including electrophysiology and imaging data. NIX uses the odML metadata format and is integrated with the Neo[4] Python package for electrophysiology, enabling Neo users to store their data in a common open format. 
The GIN[5] services provide versioned data management and collaborative data sharing. Using established versioning technology [6,7], GIN keeps track of changes and provides secure access, making it convenient to work from multiple workplaces while keeping all data available and in sync. Data can be managed from web and file browsers or a command line client, enabling integration into data acquisition or analysis procedures. The service works with any kind of directory structure and file types, keeping previous versions accessible when datasets are updated. It makes it straightforward to share data within a lab or with off-site collaborators and to work on it together. 
The tools presented are easy to use, can be combined with other approaches supporting reproducibility and data sharing [8,9,10], and enable efficient data management that supports the FAIR principles [11]. Combining them for data annotation, organization, and storage allows streamlining data workflows and efficiently sharing well-annotated datasets within the lab, among collaborators, or with the larger scientific community. 

References: 
1. odML: http://www.g-node.org/odml 
2. Handling Metadata in a Neurophysiology Laboratory: https://doi.org/10.3389/fninf.2016.00026 
3. NIX: http://www.g-node.org/nix 
4. Neo: http://neuralensemble.org/neo 
5. GIN: https://gin.g-node.org 
6. Git: https://git-scm.com 
7. Git annex: https://git-annex.branchable.com 
8. Sumatra: http://neuralensemble.org/sumatra 
9. BIDS: http://bids.neuroimaging.io 
10. DataLad: http://datalad.org 
11. The FAIR Guiding Principles for scientific data management and stewardship: https://doi.org/10.1038/sdata.2016.18 

Abstract SfN2019
Scientists experience increasing demands on research data management, such as 
organizing data workflows in the lab, data exchange for collaboration, or preparing 
data for publication. To reduce the workload associated with data management, we 
provide a suite of tools for key tasks including metadata collection, data organization, 
and data sharing.
With the odML[1] format, metadata can be collected from various sources in an experiment 
into a unified representation, which helps keeping information about experimental 
conditions available and enables automated project management tasks such as analyzing 
and selection of recording sessions[2], as well as conversion of metadata to other 
formats such as RDF to utilize semantic web technologies.
To keep data and metadata organized, the NIX[3] data format enables effectively linking 
data and analysis results as well as the associated metadata. The format supports a wide 
range of data types, including electrophysiology and imaging data. NIX uses the odML 
metadata format and is integrated with the Neo[4] Python package for electrophysiology, 
enabling Neo users to store their data in a common open format.
The GIN[5] services help keeping track of data workflows and support collaborative data 
sharing. Using established versioning technology[6,7], GIN tracks changes and keeps 
previous versions accessible when datasets are updated. It makes it convenient to work 
from multiple workplaces while keeping data available and in sync. The service works 
with any kind of directory structure and file types, supporting the scientist's data 
organization while making it straightforward to share data within a lab or with off-site 
collaborators and to work on it together. Plugins offer extended features including 
configurable workflow automation or automated format validation with every recorded 
data change.
The tools presented are easy to use, can be combined with other approaches supporting 
reproducibility and data sharing[9,10,11], and enable efficient data management that 
supports the FAIR principles[12].

[1] http://www.g-node.org/odml
[2] https://doi.org/10.3389/fninf.2016.00026
[3] http://www.g-node.org/nix
[4] http://neuralensemble.org/neo
[5] https://gin.g-node.org
[6] https://git-scm.com
[7] https://git-annex.branchable.com
[8] https://github.com/G-Node/gin-valid
[9] http://neuralensemble.org/sumatra
[10] http://bids.neuroimaging.io
[11] http://datalad.org
[12] https://doi.org/10.1038/sdata.2016.18
