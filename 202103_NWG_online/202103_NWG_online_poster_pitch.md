[1 - Introduction slide / GIN intro]

Hi everyone, I am Michael Sonntag and I am working at the G-Node. We develop tools and provide services for handling scientific data, metadata over automated workflows to data hosting, collaboration and data publication.

Here I want to give you a brief introduction to the services and tools the G-Node has developed and is maintaining and hosting for your benefit.

[2 - GIN services slide]

At the center of our efforts we provide free hosting and free publication of neuroscientific data.

The GIN data hosting service is a free web-based repository platform for neuroscientists to upload any kind of data independent of format or size and share them with the lab or with off site collaborators. The data is versioned using git for large files and any changes to files can be traced and reversed. This enables safe data handling even for large teams working on the same data from distributed workplaces, be it at the office, recording stations or from home.

Repositories can be kept private or made public and shared with as many collaborators as required.

Data can be up- and downloaded by using the web interface as well as by a command line client available for all major operating systems.
The command line client provides more options to tightly control and document the data flow and enables GIN to become an integral part in automated data workflows for example by automatically uploading data files to a GIN repository immediately once they are recorded.

While the G-Node provides free space and access via its hosting service, the GIN server software is open source and can be set up and used by anyone in their own lab or institution. If you are interested, feel free to get in touch, we are happy to help you set up your own instance of GIN.

Besides data hosting of repositories, GIN also provides you with the option to persistently publish any of your data sets. For public GIN repositories, you will always have the option to request a DOI for the full dataset. To this end, GIN is a data publishing service recommended by Nature, PLOS and eLife.

[3 - NIX / odML slide]

At the G-Node we are not only concerned with data storage and distribution, we also developed data formats to handle scientific data and metadata.
With reproducibility in mind we developed the NIX data format that stores raw data besides analysed data and their full metadata with all their dimensions and descriptors in the same file. By using this approach, data stored in NIX files can be easily interpreted either by collaborators or long after an experiment took place.
NIX is also developed with integration into automated workflows in mind: recorded data can be streamed directly into a NIX file, or easily integrated into an analysis pipeline. To this end it comes with implementations in Python, C++ and Matlab. The rich eco system further includes NIXView, a graphical user interface that provides viewing and plotting of stored data or metadata out of the box.
Besides storage for scientific data in its various forms of interpretation, NIX implements the odML metadata format, providing users with the means to fully annotate their data at any step of the scientific process for example by storing animal strains, stimuli or hardware settings right next to data it belongs to in the same file.

[4 - Contacts and links slide]

With this I hope I gave you a concise but intriguing overview of the services and tools the G-Node has to offer. Please check our poster for more details and additional services I was not able to discuss in this brief presentation.

If we have peaked your interest and you have any questions about our projects or want to get in touch, contact us at info@g-node.org. We'll be more than happy to get back to you and answer any questions you might have;

take care and see you online!
