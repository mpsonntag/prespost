### From metadata to the semantic web: services for data annotation and findable data

Michael Sonntag1, Achilleas Koutsou1, Jan Grewe2, Thomas Wachtler1

1. German Neuroinformatics Node, Ludwig-Maximilians-Universität München, Martinsried, Germany
2. Institute for Neurobiology, Eberhard-Karls-Universität Tübingen, Tübingen, Germany


Annotation of research data with metadata is crucial to provide context for analysis 
and re-use. The odML[1] format (RRID:SCR_001376) offers a flexible and comprehensive 
solution for the scientist to collect and organize metadata in a structured form that 
is both human readable and machine actionable[2] for documentation and automated 
analysis. To further support the FAIR principles[3], we present tools to export 
metadata from odML to RDF[4], which opens metadata up to semantic web services. 
The G-Node SPARQL server[5] is aimed at providing searchable whole metadata sets 
for meta analyses and also providing links to the actual published scientific 
data set. Scientists can upload their metadata to make their data findable and 
accessible even if it was a data publication or if it is an unpublished data set. 
Furthermore, the GIN[6] data hosting service (RRID:SCR_015864) provides an opt-in 
feature to automatically update the metadata service when changes to a dataset occur, 
to ensure the metadata is always up-to-date.

Finally with a metadata resource service the G-Node hosts a platform providing 
terminologies for metadata annotation and features a forum for general feedback, 
usage discussions and exchange of metadata templates with the scientific community.


*Acknowledgments

Supported by BMBF (Grants 01GQ1302 and 01GQ1509)


*References

1. Grewe et al (2011). A bottom-up approach to data annotation in neurophysiology. Front. Neuroinform. 5:16. doi:10.3389/fninf.2011.00016
2. Zehl et al (2016) Handling metadata in a neurophysiology laboratory. Frontiers in Neuroinformatics 10:26. doi:10.3389/fninf.2016.00026
3. Wilkinson et al (2016) The FAIR guiding principles for scientific data management and stewardship. Scientific Data 3:160018. doi:10.1038/sdata.2016.18
4. https://www.w3.org/RDF/
5. https://meta.g-node.org
6. https://gin.g-node.org


* Author eMails used

- sonntag@bio.lmu.de
- koutsou@bio.lmu.de 
- jan.grewe@uni-tuebingen.de
- wachtler@biologie.uni-muenchen.de
