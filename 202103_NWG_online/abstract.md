# 202103 NWG abstract

Efficient research data management for reproducible research, collaboration and data publication

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
