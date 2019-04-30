Microservice infrastructure for continuous validation, processing and indexing of research data on an open platform

Michael Sonntag1, Achilleas Koutsou1, Christian Garbers1, Jiří Vaněk1, Thomas Wachtler1

1Ludwig-Maximilian-Universität München, Biologie II, Großhaderner Straße 2, 82152 Planegg-Martinsried, Germany 

Research requires data to continuously be processed, analyzed and visualized; data needs to be quality checked, verified and backed up. Data and metadata need to be made publicly available in an easy to find and use manner. Many of these tasks can be automated, which usually leads to fewer errors and a higher results quality. To facilitate these tasks, we introduce a suite of microservices for the G-Node data infrastructure (GIN)[1], an open platform for collaboration and sharing of research data and code.

- gin-valid is a service for validating files in GIN repositories based on various format standards. Once a GIN repository is registered with the validation service, every update to the data automatically triggers validators for the supported types and the results are made available to the owner. The service covers the BIDS[2], NIX[3] and odML[4] formats, validation of CSV tables based on goodtables[5] is in development.
- gin-proc automates data processing, based on SnakeMake[6] and Drone CI[7] making workflows reproducible. Much like gin-valid, a registered repository will execute a defined data processing workflow whenever data changes occur.
- gin-dex automatically extracts metadata information from supported file types and provides extensive search across GIN repositories, making data easily findable and accessible.

These new microservices for the GIN framework will enable achieving higher quality and FAIRness of data while reducing workload for scientists.

References: 
1. GIN: https://gin.g-node.org 
2. BIDS: http://bids.neuroimaging.io 
3. NIX: http://www.g-node.org/nix 
4. odML: http://www.g-node.org/odml 
5. goodtables: https://goodtables.io/
6. Snakemake: https://doi.org/10.1093/bioinformatics/bts480
7. DroneCI: https://drone.io/

Acknowledgements: 
Supported by BMBF (Grants 01GQ1302 and 01GQ1509)

Author emails
sonntag@bio.lmu.de
koutsou@biologie.uni-muenchen.de
garbers@biologie.uni-muenchen.de
vanek@biologie.uni-muenchen.de
wachtler@biologie.uni-muenchen.de
