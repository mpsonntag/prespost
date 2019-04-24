Continuous data validation and processing: A scientific microservice infrastructure

Achilleas Koutsou1, Michael Sonntag1, Christian Garbers1, Christian Johannes Kellner1, Jan Grewe2, Thomas Wachtler1

1Ludwig-Maximilian-Universität München, Biologie II, Großhaderner Straße 2, 82152 Planegg-Martinsried, Germany 
2Institute for Neurobiology, University of Tuebingen, Auf der Morgenstelle 28; 72076 Tübingen, Germany


Handling a constant stream of scientific data is hard work: it needs to be processed, analyzed, refined, visualized and published. On a second look there are even more tasks that need to be done: raw and processed data needs to be quality checked and verified and backed up and the data pipelines leading to processed data need to be available and metadata about any experiments and analysis steps need to be documented to reproduce reported results. Finally results, raw data and analysis methods need to be made available to the general public in a manner that is easy to find and consume.
Many of the repetitive tasks from raw to analyzed data can be automated and usually leads to a higher results quality by reducing the input vector of random error.

With the introduction of the GIN (German Neuroinformatics Node Infrastructure) services[1], the G-Node presented a solution
on how to version, store, publish and share any scientific related data (raw or analyzed) together with their metadata as well as any custom software used in the data analysis.

To push data quality, automated data processing and data findability, we introduce the GIN Validation, GIN Processing and GIN Metadata microservices.
- GIN validation is a Web based Service that currently provides validations of GIN repository files for BIDS[], NIX[] and odML[] file formats out of the box. A prototype to test validity and quality of generic CSV tables based on goodtables.io[] has also been implemented as a proof of concept how easily the validation service can be extended to validate new file formats. If a validation has been added to a GIN repository, every additional or updated data file will lead to a GIN Validation as well, Users will be informed of the results on their GIN repositories.
- GIN Processing is a Prototype for a generic data processing pipeline based on Drone CI[] and SnakeMake[]. User can define a SnakeMake workflow how their data should be processed. As with GIN Validation, if any changes are recorded in a GIN repository thta has GIN Processing enabled, the user defined workflow will be started in the background and the user will automatically receive the results of the processing pipeline.
- GIN Metadata is another GIN repository plugin service, that will automatically extract metadata information from supported files in a repository, process them and make the information available via a repository wide search to make data more easily findable and accessible.







References: 


Acknowledgements: 
Supported by BMBF (Grants 01GQ1302 and 01GQ1509)





Achieving reproducible data workflows: Lightweight tools for safe and efficient data management

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


