[1 - Introduction slide / GIN intro]

Hi everyone, I am Michael Sonntag and I am working at the German Neuroinformatics Node, or G-Node. We develop tools and provide services for handling scientific data from raw and metadata over automated workflows to data hosting collaboration and even data publication.

Here I want to give you a brief but hopefully enlightening introduction to the services and tools the G-Node has developed and is maintaining and hosting for your benefit.

At the core of our development we provide free hosting and free publication of neuroscientific data.

The GIN data hosting service give you access to unlimited git based repositories that provides versioning of files and handling of large data files on a central available server, a commandline tool to automate uploading and working on various machines, collaboration in larger and even distributed teams.

[2 - GIN services slide]

Public data sets are eligible request a DOI for data publication to make your research persistently available.
Even though we encourage making data sets public, all repositories can be kept private even for collaborations.

Working with diverse data, settings and paradigms can be overwhelming. The G-Node has developed a format to collect metadata about experiments in a consistent and machine actionable way

[3 - NIX / odML slide]

At the G-Node we are not only concerned with data storage and distribution, we also developed data formats to handle scientific data and metadata.
Again reproducibility in mind we developed the NIX data format that lets you store raw data with all their dimensions and descriptors right next to analysed data and connect them in a meaningful way. By using this approach, data stored in NIX files can be easily interpreted either by collaborators or yourself in a couple of years.
NIX is also developed with integration into automated workflows in mind: you can stream your recorded raw data directly into a NIX file, or easily plug it into an analysis pipeline. To this end it comes with implementations in Python, C++ and Matlab. The eco system further includes NIXView, a graphical user interface that provides viewing and plotting of stored data or metadata out of the box.
Besides storage for scientific data in its various forms of interpretation, NIX implements the odML metadata format, providing users with the means to fully annotate their data at any step of the scientific process e.g. storing animal strains, hardware settings, stimuli or analysis software used right next to data it belongs to in the same file. The full metadata can further be exported to their own files for further analysis across experiments or to share with collaborators.

[4 - Contacts and links slide]

If we have peaked your interest and you have any questions about our tools and services or want to get in touch, contact us at

    info@g-node.org
    sonntag@bio.lmu.de

We'll be happy to get back to you and answer any questions you might have;

take care and see you online!
