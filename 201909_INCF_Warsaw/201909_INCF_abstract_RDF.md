### Towards a FAIR semantic web: services for data annotation and findable data

Michael Sonntag1, Achilleas Koutsou1, Jan Grewe2, Thomas Wachtler1

1. German Neuroinformatics Node, Ludwig-Maximilians-Universität München, Martinsried, Germany
2. Institute for Neurobiology, Eberhard-Karls-Universität Tübingen, Tübingen, Germany

A crucial aspect in current science is the annotation of research data with metadata 
to provide context for analysis and re-use. The odML[1] format provides a flexible and 
comprehensive solution to annotate scientific data in a structured form that is both 
human readable and machine consumable[2] for documentation and automated analysis.
To fully comply with the FAIR principles[3], published data needs to be findable and 
accessible. To this end, the G-Node developed tools to export any metadata to odML 
termed RDF[4] which opens metadata up to any service that supports semantic web 
technologies. Further the G-Node hosts its own semantic web server[5] aimed at providing 
searchable whole metadata sets for meta analyses and also providing a link to the actual 
published scientific data set. Any interested party can upload[6] their own metadata to 
the service to make their data findable and accessible even if it was a data publication 
or if it is an unpublished data set. To make the process more convenient the G-Nodes' 
own scientific data hosting service GIN[7] provides an opt-in feature to automatically 
update the metadata service with any change in a public dataset to ensure any data is 
always easily findable.
Finally with a metadata resource service[8] the G-Node hosts a platform providing
terminologies for metadata annotation and features a forum for general feed back, 
usage debate and exchange of custom re-usable metadata templates with the 
scientific community.

*Acknowledgments

Supported by BMBF (Grants 01GQ1302 and 01GQ1509)

*References

1. Grewe et al (2011). A bottom-up approach to data annotation in neurophysiology. Front. Neuroinform. 5:16. doi:10.3389/fninf.2011.00016
2. Zehl et al (2016) Handling metadata in a neurophysiology laboratory. Frontiers in Neuroinformatics 10:26. doi:10.3389/fninf.2016.00026
3. Wilkinson et al (2016) The FAIR guiding principles for scientific data management and stewardship. Scientific Data 3:160018. doi:10.1038/sdata.2016.18
4. https://www.w3.org/RDF/
5. https://meta.g-node.org
6. https://metup.g-node.org
7. https://gin.g-node.org
8. https://resources.g-node.org
