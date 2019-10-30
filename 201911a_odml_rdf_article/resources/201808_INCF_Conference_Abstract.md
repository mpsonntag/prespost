### Comprehensive data annotation and findable data: Mapping odML to RDF

Michael Sonntag1, Yaroslav Shalivskyy1, Achilleas Koutsou1, Christian Garbers1, Jan Grewe2, Thomas Wachtler1

1. German Neuroinformatics Node, Ludwig-Maximilians-Universität München, Martinsried, Germany
2. Institute for Neurobiology, Eberhard-Karls-Universität Tübingen, Tübingen, Germany

Annotation of research data with metadata is vital to provide context for analysis and data re-use. The odML[1] format enables collecting metadata from different sources in an organized, flexible, human and machine-readable fashion[2] and is easy to use for the scientist. odML specifies the format, not the content, so any metadata necessary to describe a given dataset can be stored.

Building on the odML format we present an approach utilizing Semantic Web technologies to effortlessly make even diverse metadata interoperable, findable and accessible according to the FAIR principles[3]. With a small set of terms derived from the odML format (Fig.1) we defined a mapping from the odML data model to a general repesentation in RDF[4] and developed a straightforward conversion pipeline. Thus, metadata collected via the convenient odML format can be fed to a single local or distributed searchable RDF graph. Taking advantage of the powerful OWL language[5], each distinct set of metadata can be subclassed further to the benefit of maintaining the original relations without losing the common structure, achieving interoperability without sacrificing findability.

To enable easy access to large collections of metadata, we further introduce an augmented SPARQL server that offers a convenient search interface for the scientist, including a "fuzzy search" feature, and thus provides findability both by easy to use search terms as well as by using the powerful SPARQL query language.

*Acknowledgments

Supported by BMBF (Grants 01GQ1302 and 01GQ1509)

*References

1. Grewe et al (2011). A bottom-up approach to data annotation in neurophysiology. Front. Neuroinform. 5:16. doi:10.3389/fninf.2011.00016
2. Zehl et al (2016) Handling metadata in a neurophysiology laboratory. Frontiers in Neuroinformatics 10:26. doi:10.3389/fninf.2016.00026
3. Wilkinson et al (2016) The FAIR guiding principles for scientific data management and stewardship. Scientific Data 3:160018. doi:10.1038/sdata.2016.18
4. https://www.w3.org/RDF/
5. https://www.w3.org/TR/owl-features/

[Figure 1: Schema for mapping odML to RDF](201808_INCF_Figure1.jpg)
