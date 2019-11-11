# FAIR from metadata to the Semantic Web: open source services for data annotation and findable data

## Abstract

Annotation of research data with metadata is crucial to provide context for analysis and 
re-use. The odML[Grewe] format offers a flexible and comprehensive solution for the 
scientist to collect and organize metadata in a structured form that is both human readable 
and machine actionable for documentation and automated analysis. To further support the 
FAIR[FAIR] principles, we present tools to export metadata from odML to RDF[RDF], which 
opens any metadata to Semantic Web[SemWeb] services. The open source G-Node SPARQL server 
is aimed at providing searchable whole metadata sets for meta analyses and also providing 
links to the actual published scientific data set. Scientists can upload their metadata 
to make their data findable and accessible even if it was a data publication or if it is 
an unpublished data set. 

## Introduction

According to the FAIR principles[FAIR], (meta)data is supposed to be Findable, Accessible,
Interoperable, Reusable. Metadata, data about experimental data, play a special role in
this context. Not only do they accurately describe the experimental setup but ideally also
the dataset involved. If handled properly, a collection of metadata is the first step to
solving the FAIR principles for a dataset. As previously shown[Interop2017] Interoperability 
between even diverse metadata can be achieved by using the common and flexible 
Semantic Web RDF technology.
Expanding on this idea, we show how Findability and Accessibility of large collections of 
metadata can be achieved by the use of open source software. Interoperability between 
different types of metadata is achieved by a minimal set of common RDF terms.
This way diverse sets of metadata can be easily converted and imported into a common 
searchable data graph. Taking advantage of the powerful OWL feature of RDF, each distinct 
set of metadata can be subclassed to the benefit of maintaining the original structure 
without losing the common generic structure keeping Interoperability without sacrificing 
Findability.
To make large collections of merged metadata in RDF format easily Accessible, we introduce 
an augmented version of the open source SPARQL server Apache Fuseki[ApacheJena]. This 
software provides access to the metadata by both custom, easy to use search terms as well 
as the powerful SPARQL query language.

### The odML data format

As previously reported (Grewe et al., 2011)[Grewe] odML[odML] is a data format 
designed to thoroughly document diverse metadata that comes with a freely available
reference implementation in Python. Developed by the
German Neuroinformatics Node, its design was oriented along the needs
of Neuroscientific metadata, but its generic approach makes it applicable
to any scientific field and is able to store heterogenic metadata to fully document
even complex experimental setups and conditions[Zehl].

As a brief introduction to the odML concept is to store metadata in a 
generic but hierarchical structure. Fig[odmlModelA] provides an overview of the 
general odml data model with all its available attributes while Fig[odmlModelB] 
shows an abstraction of how the model can be used to store metadata. 

Fig[odmlModel]. Fig[odmlModelA] The odML data model. Fig[odmlModelB] The two main concept 
entities are nested *Sections* that provide a single *Document* with its general
structure an make such a document navigate- and searchable. *Sections*
can contain *Properties* that in turn contain metadata values.

Metadata organized using the odML data model can be stored in multiple
different file formats: XML, JSON and YAML. See Fig[formatExamples] for examples.
While both XML and JSON are well used in data processing and automation, YAML
provides an option for both human readability and machine consumption.

Fig[formatExamples]. Metadata organized in odML and stored using the XML[formatExamplesA],
JSON[formatExamplesB] and YAML[formatExamplesC] storage formats.

[V#] we used parts of the datacite schema as an example since it will serve later on as 
one of the main search criteria to find and link back to published or otherwise
available datasets. We provide a full DataCite odML terminology [DataCiteTerminology], 
two specific odML templates [DataCiteTemplates] as reference usage implementation and
a Python conversion script from XML Datacite files to odML [DataCiteToODML].  

### Further development to open odML to graph database searches

While odML has shown to document experiments even through diverse fields due to its 
flexibility, there is a growing need to search metadata across multiple experiments 
and even across multiple fields. As recently published (Sprenger et al., 2019)[odMLtables], 
the odML data format has been developed further to also address this growing demand.

Even though searches within even extensive odML documents were always part of the
implementation and even imports from linked, external sources into individual documents
are possible, the option to easily search across multiple documents was still lacking.
To this end we chose to open the odML data format to the Semantic Web[SemWeb] via 
conversion to the RDF (Resource Description Framework)[RDF] format.

The Semantic Web offers a large technology stack fit to meet the requirements:
A suite of various graph database tools to merge individual documents in the RDF format 
into a single graph even if the content of the documents are not uniform. 
SPARQL (SPARQL Protocol and RDF Query Language), a full fledged query language that can 
be used to extract information from such a graph.
Another feature is OWL (Web Ontology Language)[OWL] which enables the definition of a 
vocabulary extension of the basic RDF terminology to enable more elaborate and domain 
specific SPARQL searches. The broad range of freely available open source tools can be 
adapted to fit more specific use cases. 

# Implementation

In the following we will describe how we mapped the versatile odML data format to
its RDF equivalent and document the specific OWL ontology we devised. We will also 
show how metadata can be exported from odml to its rdf equivalent, how different 
documents can be loaded into a single graph and how it can be searched via SPARQL.
We will show how the basic structure can be furthered with indidual subclasses to
make searches more specific.
Finally we will present an open web service that enables metadata searches across multiple
documents and present a suggestion based on the widely accepted DataCite[DataCite] 
publication standard to enable backlinks from metadata sets to the original, published data. 

## Implementation of odML to RDF mapping

First step was mapping the odML entities `Document`, `Section` and `Property` to RDF 
classes and provide the respective RDF predicates and xsd types.

### Namespace

We chose the RDF namespace `https://g-node.org/projects/odml-rdf` to identify all RDF 
odML entities. [xxx should we change this namespace? if yes to what should we change it
and we need to provide the odML OWL ontology at this namespace in any case, cf. related section below] 

- Schema and description of odml and the RDF mapping
- ontology
- description of usage -> rdf example with 
- description of subclassing, idea behind it, how to use it
- description convenience conversion scripts
- description convenience datacite conversion script?

- fuzzy queries?

## Implementation of SPARQL server: meta.g-node.org

- why fuseki
- adoption
- availability of data

Fuseki is an open source SPARQL query server from the Apache Jena[ApacheJena] 
Semantic Web tools suite that we adopted to support odml style RDF.
We provide an instance that is publicly available under https://meta.g-node.org.
Here we provide a metadata database of all Datasets that have been published by 
CRCNS[CRCNS] and G-Node[GIN].
The server provides example queries how the contained database can be queried.
The service is free to use and free to contribute, any additions to the database
are welcome.

- availability for in house serving

## Suggested workflow

-- should we add a suggested workflow? Could be an adopted figure from 
   INCF 2018/2019 from recording to graph server. 


## odML for backlink
- datacite port to odML template
- other odML templates for making datasets findable via the server


# References

[FAIR] The FAIR Guiding Principles for scientific data management and stewardship. 10.1038/sdata.2016.18
[Interop2017] Towards interoperability of neurophysiology data repositories. 10.12751/incf.ni2017.0017
[ApacheJena] Jena 2006, A semantic web framework for Java, http://jena.apache.org/
[Grewe] Grewe J., Wachtler T., and Benda J. (2011). A bottom-up approach to data annotation in neurophysiology. Front. Neuroinform. 5:16, doi:10.3389/fninf.2011.00016
[odML] https://github.com/G-Node/python-odml, RRID:SCR_001376
[Zehl] Zehl L, Jaillet F, Stoewer A, Grewe J, Sobolev A, Wachtler T, Brochier G, Riehle A, Denker M, Grün S (2016) Handling Metadata in a Neurophysiology Laboratory. Frontiers in Neuroinformatics 10:26, doi: 10.3389/fninf.2016.00026
[odMLtables] Sprenger J, Zehl L, Pick J, Sonntag M, Grewe J, Wachtler T, Grün S and Denker M (2019). odMLtables: A User-Friendly Approach for Managing Metadata of Neurophysiological Experiments. Front. Neuroinform. 13:62, doi: 10.3389/fninf.2019.00062
[SemWeb] https://www.w3.org/standards/semanticweb/
[RDF] https://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/
[SPARQL] https://www.w3.org/TR/sparql11-query/
[OWL] https://www.w3.org/TR/owl-ref/
[DataCite] https://datacite.org/
[CRCNS] https://crcns.org/
[GIN] https://doid.gin.g-node.org

[DataCiteTerminology] V#
[DataCiteTemplates] V#
[DataCiteToODML] V#
