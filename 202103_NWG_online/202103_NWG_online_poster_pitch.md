[1 - Introduction slide / GIN intro]

Hi everyone, I am Michael Sonntag and I am working at the G-Node, the German Neuroinformatics Node. We develop tools and provide services for handling scientific data from raw and metadata over automated workflows to data hosting collaboration and even data publication.

Here I want to give you a brief but hopefully enlightening introduction to the services and tools the G-Node has developed and is maintaining and hosting for your benefit.

At the center of our efforts we provide free hosting and free publication of neuroscientific data.

The GIN data hosting service is a free web-based repository platform for neuroscientists to upload any kind of data independent of format and size and share them with the lab or with off site collaborators. The data is versioned using git for large files and any changes to files can be traced and reversed, enabling safe access to and manipulation of data even for large teams working on the same data from distributed workplaces, be it the office, recording stations or from home.

Repositories can be kept private or made public and shared with as many collaborators as required.

[2 - GIN services slide]

Data can be up- and downloaded by using the web interface as well as a command line client available for all major operating systems. The command line client provides more options to tightly control and document the data flow and enables GIN to become an integral part in automated data workflows e.g. by automatically uploading data files to a GIN repository immediately once they are recorded.

While the G-Node provides free space and access via its own hosted service at gin.g-node.org, the GIN server software is open source and can set up and used by anyone. Data can be kept in house and repositories can easily also be uploaded to GIN if you want to publish. If this is interesting for you, feel free to get in contact, we are happy to help you set get set up with your own instance of GIN.

Besides data hosting of repositories, GIN also provides you with the option to persistently publish any of your repositories. Once you make a repository public, you will get to option to acquire a DOI for such datasets. To this end, GIN is a data publishing service recommended by Nature, PLOS and eLife.


[3 - NIX / odML slide]

At the G-Node we are not only concerned with data storage and distribution, we also developed data formats to handle scientific data and metadata.
Again reproducibility in mind we developed the NIX data format that lets you store raw data with all their dimensions and descriptors right next to analysed data and connect them in a meaningful way. By using this approach, data stored in NIX files can be easily interpreted either by collaborators or yourself in a couple of years.
NIX is also developed with integration into automated workflows in mind: you can stream your recorded raw data directly into a NIX file, or easily plug it into an analysis pipeline. To this end it comes with implementations in Python, C++ and Matlab. The eco system further includes NIXView, a graphical user interface that provides viewing and plotting of stored data or metadata out of the box.
Besides storage for scientific data in its various forms of interpretation, NIX implements the odML metadata format, providing users with the means to fully annotate their data at any step of the scientific process e.g. storing animal strains, hardware settings, stimuli or analysis software used right next to data it belongs to in the same file. The full metadata can further be exported to their own files for further analysis across experiments or to share with collaborators.

[4 - Contacts and links slide]

With this I hope I gave you an concise but interesting overview of the services and tools the G-Node has to offer. Please view our poster for more details, additional services I was not able to discuss in this brief presentation and links to all resources.

If we have peaked your interest and you have any questions about our tools and services or want to get in touch, contact us at

    info@g-node.org
    sonntag@bio.lmu.de

We'll be more than happy to get back to you and answer any questions you might have;

take care and see you online!
