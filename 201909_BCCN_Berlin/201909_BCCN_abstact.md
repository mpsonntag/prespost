## Open lightweight tools for safe and efficient data management, processing and validation


Michael Sonntag1, Achilleas Koutsou1, Jiří Vaněk1, Christian Kellner1, Christian Garbers1, Jan Grewe2, Thomas Wachtler1

1. German Neuroinformatics Node, Ludwig-Maximilian-Universität München, Martinsried, Germany
2. Institute for Neurobiology, Eberhard-Karls-Universität Tübingen, Tübingen, Germany


Maintaining reproducible data workflows while keeping data in sync, backed up, and easily accessible from within and outside the lab is a key challenge in research. To minimize time and effort scientists have to spend on these tasks, we provide a suite of tools and open platforms designed for comprehensive, reproducible and versioned management of scientific data.

Reproducibility and data re-usability require the presence of metadata providing information about experimental conditions. The odML[1] metadata format is an easy to use format to flexibly collect and organize any kind of metadata. It enables comprehensive collection and automated processing of metadata[2]. A hosted metadata resource service provides pre-defined templates and terminologies for metadata annotation and features a forum for usage discussions and exchange of metadata templates within the scientific community.

To keep data and metadata organized, the NIX[3] data format enables to effectively link data and corresponding analysis results as well as the associated metadata. It supports a wide range of data types, including electrophysiology and imaging data. NIX uses the odML metadata format and is integrated with the Neo[4] Python package for electrophysiology, enabling Neo users to store their data in a common open format.

The GIN[5] services provide versioned data management and collaborative data sharing. Using state of the art versioning technology [6,7], GIN keeps track of changes and provides secure access, making it convenient to work from multiple workplaces while keeping all data available and in sync. Data can be managed from web and file browsers or a command line client, enabling integration into data acquisition or analysis procedures. This also makes it straightforward to share data within a lab or with off-site collaborators and to work on it together. The GIN services also feature opt-in automatic data validation of supported data types. The service covers the BIDS[8], NIX and odML formats, validation of CSV tables based on goodtables[9] is under development.

The tools presented are easy to use, are compatible with other approaches supporting reproducibility and data sharing [10,11], and enable efficient data management that supports the FAIR principles [12]. Combining them for data annotation, organization, and storage allows streamlining data workflows and efficiently sharing datasets within the lab, among collaborators, or with the larger scientific community.


*Acknowledgements 

Supported by BMBF (Grants 01GQ1302 and 01GQ1509)


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


* Author eMails used

- sonntag@bio.lmu.de
- koutsou@biologie.uni-muenchen.de
- vanek@biologie.uni-muenchen.de
- christian@kellner.me
- garbers@biologie.uni-muenchen.de
- jan.grewe@uni-tuebingen.de
- wachtler@biologie.uni-muenchen.de
