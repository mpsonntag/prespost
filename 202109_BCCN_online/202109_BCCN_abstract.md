# BCCN 2021     Collaborate and Publish with ease: The G-Node infrastructure services for Research Data Management in Neuroscience and Beyond
Michael Sonntag1 Achilleas Koutsou1 Jan Grewe2 Thomas Wachtler1
G-Node, Department of Biology II, Ludwig-Maximilians-Universität München, Martinsried, Germany
Institute for Neurobiology, Eberhard-Karls-Universität Tübingen, Tübingen, Germany

----

Maintaining reproducible data workflows while keeping data in sync, backed up, and easily accessible from within and outside the lab is a key challenge in research. To minimize the time and effort required for these tasks, we present the GIN services [1], a suite of tools designed for comprehensive, reproducible and versioned management of scientific data.
GIN extends and is fully compatible with established versioning tools (git [2] and git-annex [3]) and offers seamless data access with methods provided by those tools or with common web protocols (HTML, WebDAV). Furthermore, it integrates with tools for data and metadata management [4,5,6,7] and provides indexing and easy web-based editing of metadata. GIN offers the power of a repository management service (inspired by GitHub [8]) with easy to use interfaces for data management through a web browser, from the desktop file browser, from the command line, or in analysis scripts. GIN makes it straightforward to share data within a lab or with off-site collaborators and to work on it together. Additional microservices, including GIN-Valid [9], a validation service for data formats, support automation and quality management of research data. GIN’s DOI service provides easy data publication with persistent identifiers.
In summary, GIN offers a convenient and powerful solution  for collaborative data management - open, FAIR, and straightforward.

----

Maintaining reproducible data workflows while keeping data in sync, backed up, and easily accessible from within and outside the lab is a key challenge in research. To minimize the time and effort required for these tasks, we present the GIN services [1], a suite of tools designed for comprehensive, reproducible and versioned management of scientific data.
GIN extends and is fully compatible with established versioning tools (git [2] and git-annex [3]) and offers seamless data access with methods provided by those tools or with common web protocols (HTML, WebDAV). Furthermore, it integrates with tools for data and metadata management [4,5,6,7] and provides indexing and easy web-based editing of metadata. GIN offers the power of a repository management service (inspired by GitHub [8]) with easy to use interfaces for data management through a web browser, from the desktop file browser, from the command line, or in analysis scripts. GIN makes it straightforward to share data within a lab or with off-site collaborators and to work on it together. Additional microservices, including GIN-Valid [9], a validation service for data formats, support automation and quality management of research data. GIN’s DOI service provides easy data publication with persistent identifiers.
In summary, GIN offers a convenient and powerful solution  for collaborative data management - open, FAIR, and straightforward.

----

Access via datalad

----

To manage data and workflows, the GIN[5] services track changes and provide secure access, making it convenient to work from multiple workplaces while keeping all data available and in sync. Data can be managed from web and file browsers or the command line, enabling integration into data acquisition or analysis procedures. GIN works with any kind of directory structure and file types, it uses established versioning technology[6,7] to keep previous versions available when datasets are updated. This makes it straightforward to share data within a lab or with off-site collaborators and to work on it together. GIN can be deployed locally in the lab and its microservice architecture makes it easy to rapidly develop and deploy services to meet new data management requirements. G-Node's public GIN services include data format validation[8] and provide persistent identifiers (DOIs) for dataset publication [9].

----

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

----

In this day and age, instead of focusing on designing and running experiments, scientists 
spend most of their time taming the data beast. Huge amounts of scientific data continuously 
need to be processed, analyzed and visualized; further scientists are need to deal with data 
versioning, backups and reproducibility of their data processing workflows. Most Journals 
require data to be available and easily accessible as prerequisite for a publication. While 
there are already many solutions available from both the scientific as well as the software 
development world to address these issues, most address only a single issue leaving the user 
to find different options for other issues.
The G-Node Infrastructure (GIN) services aim to address issues of data management, versioning, 
backup, sharing and publication as well as automated data quality control and data processing 
pipelines while keeping it user friendly.
At the core of the GIN services is the GIN command line client[1] that enables automating 
data acquisition and versioning workflows. To enable easy data interaction we provide 
WinGIN[2], a graphical user interface specifically targeted for Windows users. It comes 
with a Windows Explorer plugin to make data management available for users that do not 
have a strong programming background. 
To enable collaboration, data sharing and data publication GIN provides an open source and 
free to use data hosting service[3]. The data hosting service keeps track of changes to the 
contents and provides secure remote access, making it convenient to work from multiple 
workplaces and with multiple collaborators while keeping all data available, versioned and 
in sync and provides an option to publish data sets[4].
To foster the use of non-proprietary file formats in neuroscience, the web service 
provides web-browse options for the open source data formats NIX[5] and odML[6].
To further data quality, the GIN services come with an online infrastructure, that 
enables to run custom data processing pipelines as well as automatic data quality controls
as soon as any data changes are uploaded to the service.
All of these services and tools have been developed to reduce the workload for scientists, 
increase data quality to provide free and open source solutions for many stages of 
scientific research, analysis and publication as well as to ease the sharing of data 
within the lab, among collaborators or with the public.

----

The GIN[5] services provide versioned data management and collaborative data sharing. Using well established version control systems [6,7], GIN keeps track of changes and provides secure access, making it convenient to work from multiple workplaces while keeping all data available and in sync. Data can be managed from web and file browsers or a command line client, enabling integration into data acquisition or analysis procedures. This also makes it straightforward to share data within a lab or with off-site collaborators and to work on it together. The GIN services also feature automated data validation for various data types including the BIDS[8], NIX and odML formats, validation of CSV tables based on goodtables[9] is under development.

The tools presented are easy to use, are compatible with other approaches supporting reproducibility and data sharing [10,11], and enable efficient data management that supports the FAIR principles [12]. Combining them for data annotation, organization, and storage allows streamlining data workflows and efficiently sharing datasets within the lab, among collaborators, or with the larger scientific community.

----

Research requires data to continuously be processed, analyzed and visualized; data needs to be quality checked, verified and backed up. Data and metadata need to be made publicly available in an easy to find and use manner. Many of these tasks can be automated, which usually leads to fewer errors and a higher results quality. To facilitate these tasks, we introduce a suite of microservices for the G-Node data infrastructure (GIN), an open platform for collaboration and sharing of research data and code.

- gin-valid is a service for validating files in GIN repositories based on various format standards. Once a GIN repository is registered with the validation service, every update to the data automatically triggers validators for the supported types and the results are made available to the owner. The service covers the BIDS[2], NIX[3] and odML[4] formats, validation of CSV tables based on goodtables[5] is in development.
- gin-proc automates data processing, based on SnakeMake[6] and Drone CI[7] making workflows reproducible. Much like gin-valid, a registered repository will execute a defined data processing workflow whenever data changes occur.
- gin-dex automatically extracts metadata information from supported file types and provides extensive search across GIN repositories, making data easily findable and accessible.

These new microservices for the GIN framework enable achieving higher quality and FAIRness of data while reducing workload for scientists.

----


*References

1 GIN (RRID:SCR_015864): https://gin.g-node.org 
2 git: https://git-scm.com
3 git-annex: https://git-annex.branchable.com
4 odML (RRID:SCR_001376): http://www.g-node.org/odml 
5 NIX (RRID:SCR_016196): http://www.g-node.org/nix
6 BIDS (RRID:SCR_016124): http://bids.neuroimaging.io
7 Datalad (RRID:SCR_003931): http://datalad.org
8 GitHub https://github.com
9 GIN-Valid https://valid.gin.g-node.org



*Acknowledgements 
Supported by BMBF (Grants 01GQ1302 and 01GQ1509)

* Author eMails used
- sonntag@bio.lmu.de
- koutsou@biologie.uni-muenchen.de
- jan.grewe@uni-tuebingen.de
- wachtler@biologie.uni-muenchen.de

