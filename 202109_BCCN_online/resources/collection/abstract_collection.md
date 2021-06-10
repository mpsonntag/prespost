# BCCN 2021     TBD
# NWG 2021      Efficient research data management for reproducible research, collaboration and data publication

# BCCN 2020     Open tools and services for efficient data management, collaboration and data publication
# INCF 2020     GIN: Open platform and services for efficient research data management, collaboration and data publication
# RDA 2020      The G-Node Infrastructure Services: Efficient Research Data Mangagement for Neuroscience and Beyond 

# SfN 2019      Spend your time on science, not on data management: Open tools for efficient data organization, reproducible workflows, and collaboration
                optional: Safe and user friendly data management tools for science
# BCCN 2019     Lightweight tools for safe and efficient data management, processing and validation of research data
# INCF 2019     Microservice infrastructure for continuous validation, processing and indexing of research data on an open platform
# NWG 2019      Achieving reproducible data workflows: Lightweight tools for safe and efficient data management

# 2018 SfN      Achieving reproducible data workflows: Lightweight tools for safe and efficient data management
# 2018 BCCN     Achieving reproducible data workflows: Lightweight tools for safe and efficient data management
# 2018 INCF     Comprehensive data annotation and findable data: Mapping odML to RDF
                The G-Node Infrastructure Services: Safe, efficient and seamless data management for neuroscience

# 2017 SfN      Formats, tools and services for efficient data management, reproducibility and collaboration in neuroscience
# 2017 BCCN     Tools, Formats and services for efficient data management, collaboration and reproducibility in neuroscience
# 2017 INCF     The G-Node Infrastructure Services: Safe and efficient data management for neuroscience
# 2017 NWG      Data organization made easy: Safe and efficient data management for neuroscience

# 2016 SfN      Keeping track of your data with tools for comprehensive data organization
# 2016 BCCN     Keeping track of your data with NIX: tools for comprehensive data organization
# 2016 INCF     Versatile format and tools for comprehensive data organization in neuroscience



# NWG 2021      Efficient research data management for reproducible research, collaboration and data publication
Michael Sonntag, Achilleas Koutsou, Thomas Wachtler
G-Node, Department of Biology II, Ludwig-Maximilians-Universität
München, Martinsried, Germany

Research data management tasks, including organizing reproducible data workflows in the lab, keeping relevant data and metadata accessible, or exchanging data for collaboration or publication, are becoming increasingly demanding. To reduce the workload associated with data management, we present tools and services that are designed to seamlessly integrate with and support the scientist's lab data workflows. Specifically, these tools address key components of efficient data management: Metadata collection, data organization and storage, as well as sharing and publication.
To facilitate the collection of metadata, the lightweight odML[1] format provides a flexible solution to store any kind of metadata, enabling automated metadata collection and analytics[2] as well as conversion to other formats such as RDF for utilizing semantic web technologies.
To organize and integrate data and metadata, the NIX[3] data format offers a unified way of storing and linking data, metadata, and analysis results, which enables keeping all relevant data of a study in a coherent representation. It supports a wide range of data types, including electrophysiology and imaging data. NIX uses the odML metadata format and is integrated with the Neo[4] Python package for electrophysiology, enabling Neo users to store their data in a common
open format.
To manage data and workflows, the GIN[5] services track changes and provide secure access, making it convenient to work from multiple workplaces while keeping all data available and in sync. Data can be managed from web and file browsers or the command line, enabling integration into data acquisition or analysis procedures. GIN works with any kind of directory structure and file types, it uses established versioning technology[6,7] to keep previous versions available when datasets are updated. This makes it straightforward to share data within a lab or with off-site collaborators and to work on it together. GIN can be deployed locally in the lab and its microservice architecture makes it easy to rapidly develop and deploy services to meet new data management requirements. G-Node's public GIN services include data format validation[8] and provide persistent identifiers (DOIs) for dataset publication [9].
The tools presented are easy to use, interoperate with other tools supporting reproducibility and data sharing[10,11,12], and enable efficient data management in line with the FAIR principles[13].

[1] Grewe et al (2011). A bottom-up approach to data annotation in neurophysiology. Front. Neuroinform. 5:16, https://doi.org/10.3389/fninf.2011.00016
[2] Zehl et al (2016) Handling metadata in a neurophysiology laboratory. Front. Neuroinform. 10:26, https://doi.org/10.3389/fninf.2016.00026
[3] NIX, http://www.g-node.org/nix
[4] Neo, https://neuralensemble.org/neo
[5] GIN, https://gin.g-node.org
[6] git, https://git-scm.com/
[7] git-annex, https://git-annex.branchable.com/
[8] GIN-Valid, https://valid.gin.g-node.org/
[9] GIN-DOI, https://doi.gin.g-node.org/
[10] Sumatra, https://neuralensemble.org/sumatra
[11] BIDS, https://bids.neuroimaging.io/
[12] DataLad, https://datalad.org/
[13] Wilkinson et al (2016) The FAIR guiding principles for scientific data management and stewardship. Scientific Data 3:160018, https://doi.org/10.1038/sdata.2016.18


Poster available at
https://www.nwg-goettingen.de/2021/upload/Poster/742/Sonntag_Michael_NWG_Poster.pdf

Video poster pitch available at
https://www.nwg-goettingen.de/2021/upload/Poster/742/Sonntag_Michael_NWG_Poster_pitch_1280x720.mp4



# BCCN 2020     Open tools and services for efficient data management, collaboration and data publication
Achilleas Koutsou1 Michael Sonntag1 Jan Grewe2 Thomas Wachtler1
G-Node, Department of Biology II, Ludwig-Maximilians-Universität München, Martinsried, Germany
Institute for Neurobiology, Eberhard-Karls-Universität Tübingen, Tübingen, Germany

Maintaining reproducible analysis workflows while keeping data in sync, backed up, and accessible from within and outside the lab is a growing challenge in research. To facilitate these tasks, the G-Node provides tools and services for research data management that are designed to seamlessly integrate with and support the scientist's lab data workflows. Specifically, these tools address key components of efficient data management: Metadata collection, data organization and storage, and reproducible data workflows, sharing and publication.

To facilitate the collection of metadata, the lightweight odML[1] format provides a flexible solution to store any kind of metadata, enabling automated metadata collection and analytics[2] as well as conversion to other formats such as RDF for utilizing semantic web technologies.

To organize and integrate data and metadata, the NIX[3] data format offers a unified way of storing and linking data, metadata, and analysis results, which enables keeping all relevant data of a study in a coherent representation. It supports a wide range of data types, including electrophysiology and imaging data. NIX uses the odML metadata format and is integrated with the Neo[4] Python package for electrophysiology, enabling Neo users to store their data in a common open format.

To manage data and workflows, the GIN[5] services track changes and provide secure access, making it convenient to work from multiple workplaces while keeping all data available and in sync. Data can be managed from web and file browsers or the command line, enabling integration into data acquisition or analysis procedures. GIN works with any kind of directory structure and file types, it uses established versioning technology[6,7] to keep previous versions available when datasets are updated. This makes it straightforward to share data within a lab or with off-site collaborators and to work on it together. GIN can be deployed locally in the lab and its microservice architecture makes it easy to rapidly develop and deploy services to meet new data management requirements. G-Node's public GIN services include data format validation[8] and provide persistent identifiers (DOIs) for dataset publication [9].

The tools presented are easy to use, interoperate with other tools supporting reproducibility and data sharing[10,11,12], and enable efficient data management in line with the FAIR principles[13].

1. Grewe et al (2011). A bottom-up approach to data annotation in
neurophysiology. Front. Neuroinform. 5:16
  doi:10.3389/fninf.2011.00016
2. Zehl et al (2016) Handling metadata in a neurophysiology laboratory.
Front. Neuroinform. 10:26
  doi:10.3389/fninf.2016.00026
3. NIX: http://www.g-node.org/nix
4. Neo: https://neuralensemble.org/neo
5. GIN: https://gin.g-node.org
6. Git: https://git-scm.com
7. Git annex: https://git-annex.branchable.com
8. GIN-Valid: https://valid.gin.g-node.org
9. GIN-DOI: https://doi.gin.g-node.org
11. Sumatra: https://neuralensemble.org/sumatra
10. BIDS: https://bids.neuroimaging.io
12. DataLad: https://datalad.org
13. Wilkinson et al (2016) The FAIR guiding principles for scientific data
management and stewardship. Scientific Data 3:160018
  doi:10.1038/sdata.2016.18

Acknowledgements: Supported by BMBF (Grants 01GQ1302 and 01GQ1509)
Topic: Data analysis, machine learning, neuroinformatics
Presentation Type: Poster



# INCF 2020     GIN: Open platform and services for efficient research data management, collaboration and data publication
Achilleas Koutsou, Michael Sonntag, Jiří Vaněk, Thomas Wachtler
German Neuroinformatics Node, Ludwig-Maximilians-Universität München, Germany

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



# RDA 2020      The G-Node Infrastructure Services: Efficient Research Data Mangagement for Neuroscience and Beyond 
Achilleas Koutsou1, Michael Sonntag1, Christian Garbers1, Thomas Wachtler1
1 German Neuroinformatics Node, Department Biologie II, Ludwig-Maximilians-Universität München, Germany

Maintaining reproducible data workflows while keeping data in sync, backed up, 
and easily accessible from within and outside the lab is a key challenge in 
research. To help minimize the time and effort required for these tasks, 
the GIN services provide support for comprehensive, reproducible and versioned 
management of scientific data throughout the data lifecycle.

Resources
GIN (RRID:SCR_015864):
BIDS (RRID:SCR_016124):
NIX (RRID:SCR_016196):
odML (RRID:SCR_001376):
SnakeMake (RRID:SCR_003475):
DroneCI: https://drone.io/
https://gin.g-node.org
http://bids.neuroimaging.io 
http://www.g-node.org/nix 
http://www.g-node.org/odml 
https://snakemake.readthedocs.io
https://drone.io/



# SfN 2019      Spend your time on science, not on data management: Open tools for efficient data organization, reproducible workflows, and collaboration
Authors
    A. KOUTSOU1, J. VANĚK1, M. SONNTAG1, C. GARBERS1, C. J. KELLNER1, J. GREWE2, *T. WACHTLER1;
    1G-Node, Dept. of Biol. II, Ludwig-Maximilians-Universität München, Martinsried, Germany; 2Eberhardt-Karls-Universität Tübingen, Tübingen, Germany

Disclosures
    A. Koutsou: None. J. Vaněk: None. M. Sonntag: None. A. Garbers: None. C.J. Kellner: None. J. Grewe: None. T. Wachtler: None.

Abstract
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

Grant Support
    BMBF Grant 01GQ1302
    BMBF Grant 01GQ1509



# SfN 2019      optional: Safe and user friendly data management tools for science
    A. KOUTSOU1, J. VANĚK1, M. SONNTAG1, C. GARBERS1, C. J. KELLNER1, J. GREWE2, *T. WACHTLER1;
    1G-Node, Dept. of Biol. II, Ludwig-Maximilians-Universität München, Martinsried, Germany; 2Eberhardt-Karls-Universität Tübingen, Tübingen, Germany

Disclosures
    A. Koutsou: None. J. Vaněk: None. M. Sonntag: None. A. Garbers: None. C.J. Kellner: None. J. Grewe: None. T. Wachtler: None.

Abstract
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

[1] gin-cli: https://github.com/G-Node/gin-cli
[2] WinGIN: https://github.com/G-Node/WinGIN
[3] WebGIN: https://gin.g-node.org/
[4] gin-doi: https://doid.gin.g-node.org/
[5] NIX: https://www.g-node.org/nix/
[6] odML: https://www.g-node.org/odml/


Grant Support
    BMBF Grant 01GQ1302
    BMBF Grant 01GQ1509


# 2019 BCCN     Lightweight tools for safe and efficient data management, processing and validation of research data
Michael Sonntag1, Achilleas Koutsou1, Jiří Vaněk1, Christian Kellner1, Christian Garbers1, Jan Grewe2, Thomas Wachtler1
1. German Neuroinformatics Node, Ludwig-Maximilians-Universität München, Martinsried, Germany
2. Institute for Neurobiology, Eberhard-Karls-Universität Tübingen, Tübingen, Germany


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

*Acknowledgements 
Supported by BMBF (Grants 01GQ1302 and 01GQ1509)

* Author eMails used
- sonntag@bio.lmu.de
- koutsou@biologie.uni-muenchen.de
- vanek@biologie.uni-muenchen.de
- christian@kellner.me
- garbers@biologie.uni-muenchen.de
- jan.grewe@uni-tuebingen.de
- wachtler@biologie.uni-muenchen.de



# 2019 INCF     Microservice infrastructure for continuous validation, processing and indexing of research data on an open platform
Michael Sonntag1, Achilleas Koutsou1, Christian Garbers1, Jiří Vaněk1, Thomas Wachtler1
1. Ludwig-Maximilians-Universität München, German Neuroinformatics Node, Martinsried, Germany 

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

*Acknowledgements 
Supported by BMBF (Grants 01GQ1302 and 01GQ1509)



# 2019 NWG      Achieving reproducible data workflows: Lightweight tools for safe and efficient data management
Assignment: T27 - Techniques and Demonstrations
Keyword 1:  METADATA
Keyword 2:  METHODS
Keyword 3:  COMPUTER

Achilleas Koutsou1, Michael Sonntag1, Christian Garbers1, Christian Johannes Kellner1, Jan Grewe2, Thomas Wachtler1
1Ludwig-Maximilians-Universität München, Biologie II, Großhaderner Straße 2, 82152 Planegg-Martinsried, Germany 
2Institute for Neurobiology, University of Tuebingen, Auf der Morgenstelle 28; 72076 Tübingen, Germany

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

Acknowledgements: 
Supported by BMBF (Grants 01GQ1302 and 01GQ1509)



# 2018 SfN      Achieving reproducible data workflows: Lightweight tools for safe and efficient data management
Authors
    C. GARBERS1, M. SONNTAG1, A. KOUTSOU1, C. J. KELLNER1, J. GREWE2, *T. WACHTLER1;
    1G-Node, Dept. of Biol. II, Ludwig-Maximilians-Universität München, Planegg, Germany; 2Eberhardt-Karls-Universität Tübingen, Tübingen, Germany

Disclosures
     C. Garbers: None. M. Sonntag: None. A. Koutsou: None. C.J. Kellner: None. J. Grewe: None. T. Wachtler: None.

Abstract
    Maintaining reproducible data workflows while keeping data in sync, backed up, and easily accessible from within
    and outside the lab is a key challenge in research. To minimize time and effort scientists have to spend on these
    tasks, we provide a suite of tools designed for comprehensive, reproducible and versioned management of scientific
    data including storage of raw data and metadata annotation.
    Reproducibility and data re-usability require the presence of metadata also providing information about experimental
    conditions. The odML[1] metadata format is a simple and convenient format to flexibly collect and organize any kind
    of metadata. It enables comprehensive collection and automated processing of metadata[2], including conversion to
    other formats such as RDF to utilize semantic web technologies.
    To keep data and metadata organized, the NIX[3] data format enables to effectively link data and corresponding
    analysis results as well as the associated metadata. It supports a wide range of data types, including
    electrophysiology and imaging data. NIX uses the odML metadata format and is integrated with the Neo[4] Python
    package for electrophysiology, enabling Neo users to store their data in a common open format.
    The GIN[5] services provide versioned data management and collaborative data sharing. Using established versioning
    technology[6,7], GIN keeps track of changes and provides secure access, making it convenient to work from multiple
    workplaces while keeping all data available and in sync. Data can be managed from web and file browsers or a command
    line client, enabling integration into data acquisition or analysis procedures. The service works with any kind of
    directory structure and file types, keeping previous versions accessible when datasets are updated. It makes it
    straightforward to share data within a lab or with off-site collaborators and to work on it together.
    The tools presented are easy to use, can be combined with other approaches supporting reproducibility and data
    sharing[8,9,10], and enable efficient data management that supports the FAIR principles[11]. Combining them for
    data annotation, organization, and storage allows streamlining data workflows and efficiently sharing well-annotated
    datasets within the lab, among collaborators, or with the larger scientific community.

    [1] http://www.g-node.org/odml
    [2] https://doi.org/10.3389/fninf.2016.00026
    [3] http://www.g-node.org/nix
    [4] http://neuralensemble.org/neo
    [5] https://gin.g-node.org
    [6] https://git-scm.com
    [7] https://git-annex.branchable.com
    [8] http://neuralensemble.org/sumatra
    [9] http://bids.neuroimaging.io
    [10] http://datalad.org
    [11] https://doi.org/10.1038/sdata.2016.18 

Grant Support
    BMBF Grant 01GQ1302
    BMBF Grant 01GQ1509



# 2018 BCCN     Achieving reproducible data workflows: Lightweight tools for safe and efficient data management
Christian Garbers1, Michael Sonntag1, Achilleas Koutsou1, Christian J. Kellner1, Jan Grewe2, Thomas Wachtler1
1*German Neuroinformatics Node, Ludwig-Maximilians-Universität München, Germany*
2*Institut für Neurobiologie, Universität Tübingen, Germany*

Maintaining reproducible data workflows while keeping data in sync, backed up, and easily accessible from within and outside the lab is a key challenge in research. To minimize time and effort scientists have to spend on these tasks, we provide a suite of tools designed for comprehensive, reproducible and versioned management of scientific data.

Reproducibility and data re-usability require the presence of metadata also providing information about experimental conditions. The odML[1] metadata format is a simple and convenient format to flexibly collect and organize any kind of metadata. It enables comprehensive collection and automated processing of metadata[2], including conversion to other formats such as RDF to utilize semantic web technologies.

To keep data and metadata organized, the NIX[3] data format enables to effectively link data and corresponding analysis results as well as the associated metadata. It supports a wide range of data types, including electrophysiology and imaging data. NIX uses the odML metadata format and is integrated with the Neo[4] Python package for electrophysiology, enabling Neo users to store their data in a common open format.

The GIN[5] services provide versioned data management and collaborative data sharing. Using established versioning technology [6,7], GIN keeps track of changes and provides secure access, making it convenient to work from multiple workplaces while keeping all data available and in sync. Data can be managed from web and file browsers or a command line client, enabling integration into data acquisition or analysis procedures. The service works with any kind of directory structure and file types, keeping previous versions accessible when datasets are updated. It makes it straightforward to share data within a lab or with off-site collaborators and to work on it together.

The tools presented are easy to use, can be combined with other approaches supporting reproducibility and data sharing [8,9,10], and enable efficient data management that supports the FAIR principles [11]. Combining them for data annotation, organization, and storage allows streamlining data workflows and efficiently sharing well-annotated datasets within the lab, among collaborators, or with the larger scientific community.

 - [1] http://www.g-node.org/odml
 - [2] https://doi.org/10.3389/fninf.2016.00026
 - [3] http://www.g-node.org/nix
 - [4] http://neuralensemble.org/neo
 - [5] https://gin.g-node.org
 - [6] https://git-scm.com
 - [7] https://git-annex.branchable.com
 - [8] http://neuralensemble.org/sumatra
 - [9] http://bids.neuroimaging.io
 - [10] http://datalad.org
 - [11] https://doi.org/10.1038/sdata.2016.18

Support
Supported by BMBF (Grants 01GQ1302 and 01GQ1509)



# 2018 INCF     Comprehensive data annotation and findable data: Mapping odML to RDF
Michael Sonntag1, Yaroslav Shalivskyy1, Achilleas Koutsou1, Christian Garbers1, Jan Grewe2, Thomas Wachtler1
1. German Neuroinformatics Node, Ludwig-Maximilians-Universität München, Martinsried, Germany
2. Institute for Neurobiology, Eberhard-Karls-Universität Tübingen, Tübingen, Germany

Annotation of research data with metadata is vital to provide context for analysis and data re-use. The odML[1] format enables collecting metadata from different sources in an organized, flexible, human and machine-readable fashion[2] and is easy to use for the scientist. odML specifies the format, not the content, so any metadata necessary to describe a given dataset can be stored.

Building on the odML format we present an approach utilizing Semantic Web technologies to effortlessly make even diverse metadata interoperable, findable and accessible according to the FAIR principles[3]. With a small set of terms derived from the odML format (Fig.1) we defined a mapping from the odML data model to a general repesentation in RDF[4] and developed a straightforward conversion pipeline. Thus, metadata collected via the convenient odML format can be fed to a single local or distributed searchable RDF graph. Taking advantage of the powerful OWL language[5], each distinct set of metadata can be subclassed further to the benefit of maintaining the original relations without losing the common structure, achieving interoperability without sacrificing findability.

To enable easy access to large collections of metadata, we further introduce an augmented SPARQL server that offers a convenient search interface for the scientist, including a "fuzzy search" feature, and thus provides findability both by easy to use search terms as well as by using the powerful SPARQL query language.

*Acknowledgments
Supported by BMBF (Grants 01GQ1302 and 01GQ1509)

*References
1. Grewe et al (2011). A bottom-up approach to data annotation in neurophysiology. Front. Neuroinform. 5:16. doi:10.3389/fninf.2011.00016
2. Zehl et al (2016) Handling metadata in a neurophysiology laboratory. Frontiers in Neuroinformatics 10:26. doi:10.3389/fninf.2016.00026
3. Wilkinson et al (2016) The FAIR guiding principles for scientific data management and stewardship. Scientific Data 3:160018. doi:10.1038/sdata.2016.18
4. https://www.w3.org/RDF/
5. https://www.w3.org/TR/owl-features/

[Figure 1: Schema for mapping odML to RDF](201808_INCF_Figure1.jpg)



# 2018 INCF     The G-Node Infrastructure Services: Safe, efficient and seamless data management for neuroscience
Christian Garbers1, Achilleas Koutsou1, Michael Sonntag1, Thomas Wachtler1
1. German Neuroinformatics Node, Department of Biology II, Ludwig-Maximilians-Universität München, Martinsried, Germany

Maintaining reproducible data workflows while keeping data in sync, backed up, 
and easily accessible from within and outside the lab is a key challenge in 
research. To minimize the time and effort required for these tasks, we present 
the GIN services [1](RRID:SCR_015864), a suite of tools designed for 
comprehensive, reproducible and versioned management of scientific data.

GIN extends and is fully compatible with established versioning tools (git [2] 
and git-annex [3]) and offers seamless data access with methods provided by 
those tools or with common web protocols (HTML, WebDAV). Furthermore, it 
integrates with tools for data and metadata management [4,5,6] and provides 
indexing and easy web-based editing of metadata.

GIN combines the power of a repository management service (inspired by 
GitHub [7]) with data storage and offers easy to use interfaces for data 
management through a web browser, from the desktop file browser, from the 
command line, or in analysis scripts. GIN makes it straightforward to share 
data within a lab or with off-site collaborators and to work on it together. 
Finally, with GIN’s metadata indexing and DOI services any dataset can easily 
be made findable or citable for publication.
In summary, GIN offers a convenient and powerful solution for the demands of 
reliable and efficient data management in the lab, combined with seamless data 
sharing with collaborators and the general scientific community - open, FAIR, and straightforward

*Acknowledgments
Supported by BMBF (Grants 01GQ1302 and 01GQ1509)

*References
1. Grewe et al (2011). A bottom-up approach to data annotation in neurophysiology. Front. Neuroinform. 5:16. doi:10.3389/fninf.2011.00016
2. Zehl et al (2016) Handling metadata in a neurophysiology laboratory. Frontiers in Neuroinformatics 10:26. doi:10.3389/fninf.2016.00026
3. Wilkinson et al (2016) The FAIR guiding principles for scientific data management and stewardship. Scientific Data 3:160018. doi:10.1038/sdata.2016.18
4. https://www.w3.org/RDF/
5. https://www.w3.org/TR/owl-features/



# 2017 SfN      Formats, tools and services for efficient data management, reproducibility and collaboration in neuroscience
Achilleas Koutsou1, Christian Garbers1, Michael Sonntag1, Christian J. Kellner1, Jan Grewe2, Thomas Wachtler1
1 German Neuroinformatics Node, Ludwig-Maximilians-Universität München, Germany
2 Institut für Neurobiologie, Universität Tübingen, Germany

Management of scientific data, including consistent organization and storage of data, is a challenging task. Data
needs to be annotated with metadata to provide information about the underlying experiment to ensure reproducibility.
Accessing and managing data from multiple workplaces while keeping it in sync, backed up, and easily accessible from
within or outside the lab, is even more demanding. To minimize the time and effort scientists have to spend on these
tasks, we here present formats and tools designed for comprehensive and reproducible management of scientific data.
To easily store, select, retrieve and share data using an open format we provide the NIX[1] format, which offers
convenient organization of data and metadata, supporting various data types including electrophysiology and imaging,
and enables to effectively link data and corresponding analysis results as well as the associated metadata. NIX builds
on the odML[2] metadata format and is supported by the Neo[3] Python package for electrophysiology, enabling Neo users
to store their data in a common open format.
Keeping data organized in the lab is made easy via the GIN[4] services. GIN keeps track of changes to the contents and
organization of the files and provides secure remote access, making it convenient to work from multiple workplaces
while keeping all data available and in sync. Data can be managed from web and file browsers or through a command line
interface, enabling even integration into data acquisition and analysis procedures. The system works with any kind of
directory structure and file types, using established technologies to keep previous versions accessible when datasets
are updated. The service furthermore makes it straightforward to share data within a lab or with off-site collaborators
and to work on it together. Any data hosted with the service can easily be made persistently available for publication
using digital identifiers.
Combining GIN and NIX allows streamlining data workflows and eases the sharing of well-annotated datasets within the
lab, among collaborators between labs, or with the public.

Support
Supported by BMBF (Grant 01GQ1302)

References
[1] http://www.g-node.org/nix/
[2] http://www.g-node.org/odml/
[3] http://neuralensemble.org/neo/
[4] https://gin.g-node.org/



# 2017 BCCN     Tools, Formats and services for efficient data management, collaboration and reproducibility in neuroscience
Michael Sonntag1, Achilleas Koutsou1, Christian Garbers1, Christian Johannes Kellner1, Jan Grewe2, Thomas Wachtler1
1. German Neuroinformatics Node, German Neuroinformatics Node, München, Germany
2. Institut für Neurobiologie, Universität Tübingen, Tübingen, Germany

Management of scientific data, including consistent organization and storage of data, is
a challenging task. Data needs to be annotated with metadata to provide information
about the underlying experiment to ensure reproducibility. Accessing and managing data
from multiple workplaces while keeping it in sync, backed up, and easily accessible from
within or outside the lab, is even more demanding. To minimize the time and effort
scientists have to spend on these tasks, we here present formats and tools designed for
comprehensive and reproducible management of scientific data. To easily store, select,
retrieve and share data using an open format we provide the NIX[1] format, which offers
convenient organization of data and metadata, supporting various data types including
electrophysiology and imaging, and enables to effectively link data and corresponding
analysis results as well as the associated metadata. NIX builds on the odML[2] metadata
format and is supported by the Neo[3] Python package for electrophysiology, enabling
Neo users to store their data in a common open format. Keeping data organized in the
lab is made easy via the GIN[4] services. GIN keeps track of changes to the contents
and organization of the files and provides secure remote access, making it convenient to
work from multiple workplaces while keeping all data available and in sync. Data can
be managed from web and file browsers or through a command line interface, enabling
even integration into data acquisition and analysis procedures. The system works with
any kind of directory structure and file types, using established technologies to keep
previous versions accessible when datasets are updated. The service furthermore makes
it straightforward to share data within a lab or with off-site collaborators and to work on
it together. Any data hosted with the service can easily be made persistently available
for publication using digital identifiers. Combining GIN and NIX allows streamlining
data workflows and eases the sharing of well-annotated datasets within the lab, among
collaborators between labs, or with the public.

Acknowledgements
Supported by BMBF (Grant 01GQ1302)

References
1 http://www.g-node.org/nix/
2 http://www.g-node.org/odml/
3 http://neuralensemble.org/
4 https://web.gin.g-node.org/

©(2017) Sonntag M, Koutsou A, Garbers C, Kellner CJ, Grewe J, Wachtler T
Cite as:
Sonntag M, Koutsou A, Garbers C, Kellner CJ, Grewe J, Wachtler T (2017) Tools, Formats and
services for efficient data management, collaboration and reproducibility in neuroscience.
Bernstein Conference 2017
Abstract. doi: 10.12751/nncn.bc2017.0137



# 2017 INCF     The G-Node Infrastructure Services: Safe and efficient data management for neuroscience
Achilleas Koutsou, Christian Garbers, Michael Sonntag, Christian J. Kellner, Thomas Wachtler
German Neuroinformatics Node, Department of Biology II, Ludwig-Maximilians-Universität München, Germany

Managing and accessing data from multiple workplaces while keeping it in sync, backed up, and easily accessible from within or outside the lab is a key challenge for scientists. To minimize the time and effort required for these tasks, we present the GIN [1] (G-Node Infrastructure) services, a free data management system designed for comprehensive and reproducible management of scientific data. At the heart of GIN is the well established and widely used git [2] versioning system and the git-annex [3] extension for handling large files. These two technologies are integrated into the GIN services, together with authentication and user management, making it convenient to use them for collaboration, sharing, and publication.

The GIN workflow provides the power of a web based repository management service (inspired by GitHub [4]) combined with the ease of distributed file storage and sharing of established cloud-based services. The service spans from local workflows starting from your analysis scripts on the workstation to data publication and remote collaboration. It supports workflows compatible with the requirements of the FAIR principles [5] and is interoperable with other tools and services such as NIX [6],  DataLad [7] and DataCite [8].

Thus, GIN provides a much needed solution for the demands of reliable and efficient data management inside the lab and seamless sharing with collaborators and the general scientific community.

Support
Supported by BMBF (Grant 01GQ1302)

References
[1] https://gin.g-node.org/ 
[2] https://git-scm.com/ 
[3] https://git-annex.branchable.com/
[4] https://github.com 
[5] https://www.force11.org/group/fairgroup/fairprinciples
[6] http://www.g-node.org/nix 
[7] http://datalad.org/
[8] https://www.datacite.org/



# 2017 NWG      Data organization made easy: Safe and efficient data management for neuroscience
Michael Sonntag1, Achilleas Koutsou1, Christian Garbers1, Christian J. Kellner1, Adrian Stoewer1 , Jan Grewe2, Thomas Wachtler1
1German Neuroinformatics Node, Ludwig-Maximilians-Universität München, Germany
2Institut für Neurobiologie, Universität Tübingen, Germany

Management of scientific data, including consistent organization, annotation and storage of data, is a challenging task. Accessing and managing data from multiple workplaces while keeping it in sync, backed up, and easily accessible from within or outside the lab is even more demanding. To minimize the time and effort scientists have to spend on these tasks, 
we here present the GIN (G-Node Infrastructure) services [1], a free data management system designed for comprehensive and reproducible management of scientific data. It keeps track of changes to the contents and organization of the files and provides secure remote access to the data. More specifically, once a directory has been put under GIN control, the contents will be synced to a dedicated GIN server. With proper authorization, data can be accessed and changed from remote clients, making it easy to work from multiple workplaces while keeping all data at hand and in sync. Data can be managed from web and file browsers as well as through a command line interface, which enables integrating data management and access into the data acquisition and analysis procedures. The system handles any kinds of directory structures and file types, and tracks all changes, using Git [2] tracking mechanisms. This supports reproducible data workflows and in particular keeps previous versions accessible when datasets are updated. The service furthermore makes it straightforward to share any data within a lab or with off-site collaborators and to work on it in parallel.

A special feature of the GIN services is support for the NIX (Neuroscience information exchange) data format [3]. This file format is specifically designed to store recorded data, analysis results and annotations (metadata) in a single file, supporting the concept that all information about an experiment is kept in one place. The contents of NIX files managed by a GIN repository are indexed, providing fast search for specific datasets or data analysis.
NIX files can be created and accessed by a variety of programming languages, including Python [4], Matlab [5] and Java [6], and through the Neo package [7] to specifically support working with electrophysiological data.

Comprehensive organization and reproducible management of scientific data is challenging, in particular with complex experiments and heterogeneous data. The GIN services in combination with the NIX format enable to streamline the lab data workflows and reduce the efforts involved in sharing data with collaborators or the community.

Support
Supported by BMBF (Grant 01GQ1302)

References
[1] https://gin.g-node.org/
[2] https://git-scm.com/
[3] https://github.com/G-Node/nix
[4] https://github.com/G-Node/nixpy
[5] https://github.com/G-Node/nix-mx
[6] https://github.com/G-Node/nix-java
[7] https://github.com/G-Node/python-neo-nixio



# 2016 SfN      Keeping track of your data with tools for comprehensive data organization
Christian J Kellner(1), Adrian Stoewer(1), Michael Sonntag(1), Achilleas Koutsou(1), Andrey Sobolev(1), Jan Benda(2), Thomas Wachtler(1), Jan Grewe(2)
(1) German Neuroinformatics Node, Ludwig-Maximilians-Universität München, Großhaderner Straße 2, Planegg-Martinsried, 82152, Germany
(2) Institut für Neurobiologie, Universität Tübingen, Tübingen, Germany

Making sense of complex neuroscience data requires integration of information from multiple sources. Recorded data needs to be joined with metadata describing experimental conditions and analyses. A tight link between data and metadata helps during offline analysis by easing data identification and data retrieval. We previously developed a format for storing of metadata, the odML[1], and here present a data format and tools to link data and metadata meaningfully for easy data exploration, selection, retrieval, and sharing. The NIX[2] format can store various kinds of scientific data, like electrophysiological, imaging, or other recorded or derived data, together with the metadata and including relationships between data items. Data are stored with units and dimension information, for direct interpretation. The format allows specifying regions of interest, such as areas in an image or events in a recorded signal, and references between data items. Integration into the recording or ana
lysis software is made possible through libraries for different languages, including C++, Python, Matlab, and Java. Installable packages exist for the major platforms, together with documentation, examples, and tutorials. The NixView program[3] can be used to explore, plot and export the stored data in a user friendly and convenient way. An I/O backend for the Neo Python objects for electrophysiology [4,5] enables conversion of data from various proprietary formats to the open NIX format. Moreover, results of data analysis done with Neo, for example using the Elephant[6] toolkit, can be saved in the very same format. The NIX project thus facilitates data integrity and reproducibility through comprehensive annotation and efficient organization of neuroscience data, during everyday lab work.

[1] http://dx.doi.org/10.3389/fninf.2011.00016
[2] https://github.com/G-Node/nix
[3] http://bendalab.github.io/NixView
[4] http://neuralensemble.org/neo
[5] https://github.com/G-Node/python-neo-nixio
[6] http://neuralensemble.org/elephant



# 2016 BCCN     Keeping track of your data with NIX: tools for comprehensive data organization
    Christian J Kellner1 Adrian Stoewer1 Michael Sonntag1 Achilleas Koutsou1 Andrey Sobolev1 Jan Benda2 Thomas Wachtler1 Jan Grewe2
    Department Biologie II, Ludwig-Maximilians-Universität München, 82152 Planegg-Martinsried, Germany
    Institut für Neurobiologie, Eberhard-Karls-Universität Tübingen, 72076 Tübingen, Germany

Managing neuroscience data requires the integration of information from multiple sources. Information about stimuli, animals, protocols, and other background information about the experiment, together often called "metadata", are necessary to interpret the resulting data correctly. Storing such information consistently alongside the recoded data is therefore an essential part of experimental research and depends crucially on available file formats. Many existing formats provide only limited support for storing metadata along with the data. Here we present the NIX project, consisting of an open format and software tools to store, organize, and link data and metadata. The format[1] can represent various kinds of recorded and derived data in conjunction with all the metadata and links between data entities to facilitate data organization and data retrieval, as well as data sharing. Units and dimension information is stored directly with the data, for immediate correct interpretation. The NIX software libraries support direct, fine-grained access to the data and the linked metadata. This enables selecting specific subsets of the data, such as signals recorded from a certain electrode channel, or spike trains from a certain single unit in trials with a given stimulus. Efficient use of NIX format features is facilitated by software libraries for different languages, including C++, Python [2], Matlab [3], and Java [4]. Installable packages exist for different platforms, together with documentation, examples, and tutorials [5]. The NixView program [6] can be used to explore, plot and export the stored data in a user-friendly and convenient way. The NIX project includes tools that link to other open data format projects like Neo [7,8] and Neuroshare [9]. This enables seamless integration of data access with data analysis, and creates a route for the conversion of raw data from various proprietary formats to the open NIX format. Moreover, results of data analysis done with Neo, e.g. using the Elephant [10] toolkit, can be saved in the very same format. The NIX project thus supports comprehensive annotation and efficient organization of neuroscience data, and the variety of libraries makes it easy to integrate access to data and metadata in the lab data collection and analysis workflow.
Acknowledgements

Supported by the German Federal Ministry of Education and Research (BMBF Grant 01GQ1302)
References

http://www.g-node.org/projects/nix
https://github.com/G-Node/nixpy
https://github.com/G-Node/nix-mx
https://github.com/G-Node/nix-java
http://g-node.github.io/nixpy
http://bendalab.github.io/NixView/
http://neuralensemble.org/neo/
https://github.com/G-Node/python-neo-nixio
http://www.g-node.org/projects/neuroshare-tools/
http://neuralensemble.org/elephant/

Citation: Kellner CJ, Stoewer A, Sonntag M, Koutsou A, Sobolev A, Benda J, Wachtler T, Grewe J (2016) Keeping track of your data with NIX: tools for comprehensive data organization. Bernstein Conference 2016.
Copyright: © (2016) Kellner CJ, Stoewer A, Sonntag M, Koutsou A, Sobolev A, Benda J, Wachtler T, Grewe J
doi: 10.12751/nncn.bc2016.0121



# 2016 INCF     Versatile format and tools for comprehensive data organization in neuroscience
Christian J Kellner(1), Adrian Stoewer(1), Michael Sonntag(1), Achilleas Koutsou(1), Andrey Sobolev(1), Jan Benda(2), Thomas Wachtler(1), Jan Grewe(2)
(1) German Neuroinformatics Node, Ludwig-Maximilians-Universität München, Großhaderner Straße 2, Planegg-Martinsried, 82152, Germany
(2) Institut für Neurobiologie, Universität Tübingen, Tübingen, Germany

Managing neuroscience data requires the integration of information from multiple sources. Background information, or metadata, about the experiment is necessary to interpret the resulting data correctly. Storing such information consistently is an essential part of experimental research and depends crucially on available file formats. Many existing formats provide only limited support for storing metadata along with the data. Here we present the NIX project[1], consisting of an open format and software tools to store and organize data and metadata. The format can store recorded or derived data together with the meta-information, including relationships between data items. Units and dimension information is stored alongside the data, to make quick interpretation possible. The format further allows specifying regions of interest, such as areas in an image or events in a recorded signal. Efficient use of NIX features is facilitated by software libraries for different languages, including C++, Python, Matlab , and Java. Installable packages exist for different platforms, together with documentation, examples, and tutorials. Additionally the NixView program[2] can be used to explore, plot and export the stored data in a user friendly and convenient way. An I/O backend for NEO[3,4] has been implemented, creating a route for raw data in various proprietary formats to be converted to the open NIX format via the NEO data structures. Moreover the results of data analysis done with NEO, e.g. using the Elephant[5] toolkit, can be saved in the same format. The NIX project thus supports comprehensive annotation and efficient organisation of neuroscience data, and the variety of libraries makes it easy to integrate access to data and metadata in the lab data collection and analysis workflow.

Acknowledgements
Supported by the Federal Ministry of Education and Research (BMBF Grant 01GQ1302)

[1] https://github.com/G-Node/nix
[2] http://bendalab.github.io/NixView/
[3] http://neuralensemble.org/neo/
[4] https://github.com/G-Node/python-neo-nixio
[5] http://neuralensemble.org/elephant/


