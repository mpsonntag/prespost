Safe and user friendly data management tools for science 

Authors
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


-------------------- optional ---------------------------------------------------


Achieving reproducible data workflows: Lightweight tools for safe and efficient data management

Authors
    A. KOUTSOU1, M. SONNTAG1, C. GARBERS1, C. J. KELLNER1, J. GREWE2, *T. WACHTLER1;
    1G-Node, Dept. of Biol. II, Ludwig-Maximilians-Universität München, Planegg, Germany; 2Eberhardt-Karls-Universität Tübingen, Tübingen, Germany

Disclosures
     M. Sonntag: None. A. Koutsou: None. C. Garbers: None. C.J. Kellner: None. J. Grewe: None. T. Wachtler: None.

Abstract
    Maintaining reproducible data workflows while keeping data in sync, backed up, and easily accessible from within
    and outside the lab is a key challenge in research. To minimize time and effort scientists have to spend on these
    tasks, we provide a suite of tools designed for comprehensive, reproducible and versioned management of scientific
    data including storage of raw data and metadata annotation.
    Reproducibility and data re-usability require the presence of metadata also providing information about experimental
    conditions. The odML[1] metadata format is a flexible format to collect and organize any kind of metadata. It enables
    comprehensive collection and automated processing of metadata[2].
    With the NIX[3] format data can be directly linked to corresponding analysis results and associated metadata using
    odML. It supports a wide range of data types, including electrophysiology and imaging data. NIX is integrated with
    the Neo[4] Python package for electrophysiology, enabling Neo users to store their data in a common open format.
    The GIN[5] services provide versioned data management and collaborative data sharing. Using established versioning
    technology[6,7], GIN tracks changes and provides secure access, making it convenient to work from multiple
    workplaces while keeping all data available and in sync. Data can be managed from web and file browsers or a standalone,
    platform independent command line client, enabling integration into scripted data acquisition, analysis or backup
    procedures. It makes it straightforward to share data within a lab or with off-site collaborators and to work on it
    together. Plugins for the web service enable server-side workflow automization, which comes with the benefit of
    out-of-the-box reproducibility, and data quality control[8] with every recorded data change.
    The tools presented are easy to use, platform independent, can be combined with other approaches supporting
    reproducibility and data sharing[9,10,11], and enable efficient data management that supports the FAIR principles[12].
    Combining them for data annotation, organization, and storage allows streamlining data workflows and efficiently
    sharing well-annotated datasets within the lab, among collaborators, or with the larger scientific community.

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



