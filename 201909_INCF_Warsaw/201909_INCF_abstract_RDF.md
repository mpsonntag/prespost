### Towards a FAIR semantic web: services for data annotation and findable data

Michael Sonntag1, Achilleas Koutsou1, Jan Grewe2, Thomas Wachtler1

1. German Neuroinformatics Node, Ludwig-Maximilians-Universität München, Martinsried, Germany
2. Institute for Neurobiology, Eberhard-Karls-Universität Tübingen, Tübingen, Germany

A critical point in science is the annotation of research data with metadata 
to provide context for analysis and re-use. The odML[1] format provides a flexible and comprehensive 
option to annotate scientific data in a structured form that is both human and machine
consumable[2] for documentation and automated analysis.
To fully comply with the FAIR principles[3] published scientific data foremost of 
all needs to be findable and accessible. To contribute to this end, the G-Node
provides an OWL terminolgoy[4] to export odML data to RDF[5] which opens any metadata in
odML format to any service that supports semantic web technology.
Further the G-Node hosts its own dedicated semantic web[6] server open to the public
where anyone can browse the metadata of available datasets and find the links to 
where the data is actually hosted. To enable anyone to contribute to this common
database, the G-Node defined a minimally required set of information along the
datacite guidelines and provides on the one hand a dedicated metadata upload service[7] 
where any interested party can upload metadata about their experiments to make their 
published data findable. On the other hand the G-Nodes own data hosting service GIN[8]
provides an option to make their published data findable via the metadata
service and keep the metadata automatically up to date.
Finally with a metadata resource service[9] the G-Node hosts a platform that provides
terminologies and templates for metadata annotation and provides a forum for anyone 
to give feed back and share their own templates with the scientific community.

*Acknowledgments

Supported by BMBF (Grants 01GQ1302 and 01GQ1509)

*References

1. Grewe et al (2011). A bottom-up approach to data annotation in neurophysiology. Front. Neuroinform. 5:16. doi:10.3389/fninf.2011.00016
2. Zehl et al (2016) Handling metadata in a neurophysiology laboratory. Frontiers in Neuroinformatics 10:26. doi:10.3389/fninf.2016.00026
3. Wilkinson et al (2016) The FAIR guiding principles for scientific data management and stewardship. Scientific Data 3:160018. doi:10.1038/sdata.2016.18
4. https://www.w3.org/TR/owl-features/
5. https://www.w3.org/RDF/
6. https://meta.g-node.org
7. https://metup.g-node.org
8. https://gin.g-node.org
9. https://resources.g-node.org
