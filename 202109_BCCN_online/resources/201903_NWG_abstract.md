Achieving reproducible data workflows: Lightweight tools for safe and efficient data management

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

