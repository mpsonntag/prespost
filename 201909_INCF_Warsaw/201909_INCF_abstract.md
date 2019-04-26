Continuous data validation and processing: A scientific microservice infrastructure

Achilleas Koutsou1, Michael Sonntag1, Christian Garbers1, Christian Johannes Kellner1, Jan Grewe2, Thomas Wachtler1

1Ludwig-Maximilian-Universität München, Biologie II, Großhaderner Straße 2, 82152 Planegg-Martinsried, Germany 
2Institute for Neurobiology, University of Tuebingen, Auf der Morgenstelle 28; 72076 Tübingen, Germany


Handling a constant stream of scientific data is challenging work: it needs to be processed, analyzed, refined, visualized and published. On second glance the tasks pile up: raw and processed data needs to be quality checked, verified and backed up; the data pipelines leading to processed data need to be available and metadata about experiments and analysis steps need to be documented to enable reproduction of reported results. Finally all of the above need to be made available to the general public in a manner that is easy to find and consume.
Many of the repetitive tasks from raw to analyzed data can be automated which usually lead to a higher results quality by reducing the input vector of random error.

With the introduction of the GIN (German Neuroinformatics Node Infrastructure) services[1], scientific data (raw or analyzed) can easily be versioned, stored, published and shared together with their metadata as well as any custom software used in the data analysis.

To push data quality, automated data processing and data findability, we introduce the GIN Validation, GIN Processing and GIN Metadata microservices.
- GIN validation (gin-valid) is a Web based Service that currently provides validations of GIN repository files for BIDS[2], NIX[3] and odML[4] file formats out of the box. A prototype to test validity and quality of generic CSV tables based on goodtables.io[] has also been implemented as a proof of concept how easily the validation service can be extended to validate new file formats. If a validation has been added to a GIN repository, every additional or updated data file will lead to a GIN Validation as well, Users will be informed of the results on their GIN repositories.
- GIN Processing (gin-proc) is a Prototype for a generic data processing pipeline based on Drone CI[5] and SnakeMake[6]. User can define a SnakeMake workflow how their data should be processed. As with GIN Validation, if any changes are recorded in a GIN repository thta has GIN Processing enabled, the user defined workflow will be started in the background and the user will automatically receive the results of the processing pipeline.
- GIN Metadata (gin-dex) is another GIN repository plugin service, that will automatically extract metadata information from supported files in a repository, process them and make the information available via a repository wide search to make data more easily findable and accessible.

With the introduction of these new services we hope to achieve higher data quality while at the same time reducing workload for the individual scientist.


References: 
1. GIN: https://gin.g-node.org 
2. BIDS: http://bids.neuroimaging.io 
3. NIX: http://www.g-node.org/nix 
4. odML: http://www.g-node.org/odml 
5. https://drone.io/ 
6. Snakemake—a scalable bioinformatics workflow engine
Johannes Köster Sven Rahmann
Bioinformatics, Volume 28, Issue 19, 1 October 2012, Pages 2520–2522,
https://doi.org/10.1093/bioinformatics/bts480


Acknowledgements: 
Supported by BMBF (Grants 01GQ1302 and 01GQ1509)


(ノ°Д°）ノ︵ ┻━┻

