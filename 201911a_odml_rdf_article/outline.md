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

### Mapping of odML entities to RDF classes

[TableDocument]: mapping of odML `Document` to RDF. (a) The document root is mapped to an 
RDFS class of type `odml:Document`. (b) The uuid of the odML `Document` is used as
Name of the created `odml:Document` RDF node to uniquely identify the document if it is 
merged with a graph database. (c) RDF export of repositories: linked terminologies are
downloaded on conversion and exported additional RDF document connected via the `odml:Hub` 
RDF node. This additional document is linked via `odml:hasTerminology` to the original
document. If the terminology cannot be imported, its URL will be kept as is and its
value is provided as an RDF leaf via the predicate `odml:hasExternalTerminology` in
the original document. See [TableHub] and [TableTerminology] for more detailed descriptions 
[xxx check if this actually works as described] (d) As provenance from where the RDF 
odml:Document was created from, the filename of the original odML file is documented via 
the non-odML predicate `odml:hasFilename` 

    odml                    RDF                                 xsd type
    ------------------------------------------------------------------------------
    odml (a)                odml:Document                       -

    id (b)                  RDF node instance name              -
    author                  odml:hasAuthor                      xsd:string
    date                    odml:hasDate                        xsd:date
    version (odml)          odml:hasVersion                     xsd:float
    version (document)      odml:hasDocVersion                  xsd:string
    repository (c)          odml:hasTerminology                 -
                            odml:hasExternalTerminology         xsd:string
    Sections                odml:hasSection                     -
    - (d)                   odml:hasFilename                    xsd:string


[TableSection]: mapping of odML `Section` to RDF. (a) Any odML `Section` entity is mapped 
to an RDFS class of type `odml:Section`. (b) The uuid of an odML `Section` entity is used 
as Name of the created `odml:Section` RDF node to uniquely identify the section if it is 
merged with a graph database. If this node already exists in the graph, it will not 
add a duplicate entry, but will add only any predicates that the graph with respect to
this Section node does not already contain. [xxx Move to another part or remove?] 
(c) cf. `repository` description in [TableDocument]. (d) A `reference` can either be be a 
URL to an external reference or a string pointing to an id in a Database. (e) Unspecific
Sections are exported using the `odml:Section` class and the `odml:hasSection` predicate.
We also provide a set of 'specialized' RDF classes that are subclasses of Section. cf. 
[subclassing] for details.

    odml            RDF                             xsd type
    ------------------------------------------------------------------------------
    Section (a)     odml:Section                    -

    id (b)          RDF node instance name          -
    name            odml:hasName                    xsd:string
    type            odml:hasType                    xsd:string
    definition      odml:hasDescription             xsd:string
    repository (c)  odml:hasTerminology             -
                    odml:hasExternalTerminology     xsd:string
    reference (d)   odml:hasReference               xsd:string
    Sections (e)    odml:hasSection                 -
    Properties      odml:hasProperty                -


[TableProperty]: mapping of odML `Property` to RDF. (a) Any odML `Property` entity is mapped 
to an RDFS class of type `odml:Property`. (b) The uuid of an odML `Property` entity is used 
as Name of the created `odml:Property` RDF node to uniquely identify the section if it is 
merged with a graph database. (c) cf. `reference` description in [TableSection]. (d) odML
supports multiple values. On the export to RDF the order of these values need to be 
respected as well. Values are connected to the RDF document via the `odml:hasValue` 
predicate to an `rdf:Seq` node. This `rdf:Seq` node in turn contains numbered rdf:li 
items which in turn contain the individual odml.Value entries. This construct enables 
RDF searches for individual values rather then searching for lists of values.
 
    odml            RDF                             xsd type
    ------------------------------------------------------------------------------
    Property (a)    odml:Property                   -
    
    id (b)          RDF node instance name          -
    name            odml:hasName                    xsd:string
    definition      odml:hasDefinition              xsd:string
    reference (c)   odml:hasReference               xsd:string
    unit            odml:hasUnit                    xsd:string
    dtype           odml:hasDtype                   xsd:string
    uncertainty     odml:hasUncertainty             xsd:float
    values (d)      odml:hasValue                   -
                    rdf:Seq                         -
                    rdf:_#                          xsd:string
    value_origin    odml:hasValueOrigin             xsd:string


[TableHub]: The custom RDF type of class `odml:Hub` has no odML entity equivalent. It is 
introduced to merge Documents and Terminologies into a single RDF graph: the `Hub` is 
used to root a graph that might contain multiple documents to enable searches across 
unrelated and inhomogenious metadata content.

    odml            RDF                             xsd type
    ------------------------------------------------------------------------------
    -               odml:Hub                        -
    -               odml:hasDocument                -
    -               odml:hasTerminology             -


[TableTerminology]: odML documents can link to external Terminology documents. To make 
these available for searches within a connected RDF graph besides the odML documents they 
are referenced by, linked terminologies are imported and converted into RDF documents.
They are connected via the `odml:hasSection` predicate to their referencing documents.
Conversely the odml:Section in an odml:Document references the Terminology via the 
`odml:hasTerminology` predicate.

    odml            RDF                             xsd type
    -------------------------------------------------------------------------------------------
    -               odml:Terminology                -
    Sections        odml:hasSection                 -

Fig [odmlRDFDataModel]

### Subclassing of Sections

ALL of the properties can be fine grained into subproperties to give more semantic 
meaning to the connection between nodes.

e.g.
    section hasSection section
 could become
    section hasExperimenter section
    
 here hasExperimenter is a subclass of `hasSection` ... a search for `hasExperimenter` 
 would return only sections connected via this specific property, a search for hasSection 
 would return all sections connected by `hasSection` and `hasExperimenter`.

### odML RDF ontology

To make use of the RDF feature of validating individual RDF files, we created an odML
RDF ontology which includes the basic set of odml RDF terms and included all currently
supported Section subclasses. This list of subclasses should not be seen as permanent and
will probably increase in the future.

[odmlOntology][odml-ontology.ttl] cf file. [xxx how to best include this file in the article]


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
Semantic Web tools suite that was adopted to support odML specific RDF.
An publicly accessible instance is available at https://meta.g-node.org.
The service provides a metadata graph searchable by SPARQL containing all scientific 
Datasets that have been published by CRCNS[CRCNS] and G-Node[GIN].
The server provides example SPARQL queries how the available database can be used.
The service is free to use and free to contribute, any additions to the database
are welcome and encouraged.

The SPARQL server including all example queries has been Dockerized. Both source 
code[ODMLQuery] and docker container[ODMLQueryDocker] are freely available and free to use.

## Suggested workflow

-- should we add a suggested workflow? Could be an adopted figure from 
   INCF 2018/2019 from recording to graph server. 

Fig [workFlowSchema]


## odML for backlink
- datacite port to odML template
- other odML templates for making datasets findable via the server

# odml RDF mapping difficulties


Another problemset was that there is no order within a graph which from our point of view was only an issue with the actual property values that have to be kept in order. For all other entities order of same-level entities like Sections or Properties in an odml document are by definition not relevant and do not have to be taken into consideration when converting to a graph representation, as long as the hierarchical structure is still observerved. To this end we had to ensure, that identical entities like Sections or Properties could be uniquely identfied to keep the hierarchical structure intact. To this end, we used the ID, that each odML entity already has to uniquely identify itself within and even across odML documents, to identify the entities in the graph as well. The following two examples describe the Problem and how it was solved:

    In the following document structure
    Document - uniqueID_A
    - Section - name_A - uniqueID_B 
    - Section - name_B - uniqueID_C
      - Section - name_A - uniqueID_D

    In a graph without 

## Challenges in converting hierarchical documents to a graph based representation

After reviewing the general structure of odML entities there were two main points to consider: odML entities (Document, Section, Property) and the entities Attributes (e.g. Section.name or Property.value). To approach the issue, as a general concept, odML entities where considered as Graph nodes while odML entity attributes where considered graph leaves. In this Scenario, mapping entity attributes to RDF was straightforward. As an example, Section.name="Experiment_A"" would be converted to the straightforward RDF triple `odml:Section odml:hasName Experiment_A`.

Mapping the connection of entities amongst themselves was another issue. 
Uniquely identifying an entity and its connections within a graph is essential to maintain and reconstruct an underlying hierarchical structure. RDF knows the feature of "blank nodes" to uniquely identify a graph node within an rdf graph and provides it out of the box, if no unique identifier for an entity has been provided. The downside of blank nodes in RDF are, that they are not persistent. Whenever the same RDF file is loaded into a different graph, the blank node IDs will differ keeping the underlying structure intact but potentially making identification of a specific node problematic. Furthermore, if the same document would be uploaded again into the same graph, the blank nodes would differ again, potentially leading to duplicate entries in the graph.
odML already provides all its main entities, Documents, Sections, Properties, with its own unique IDs that uniquely identifies them within and even across different odML documents. These IDs where now used as identifiers for the nodes. With this approach, when loaded into different graphs or even loaded into the same graph twice, the odML entities are always uniquely identifiable and duplicate entries do not occur.

The abstract example in Figure[TODO] shows the problemset and the chosen approach. The unique IDs are in detail UUID strings as specified in RFC 4122\footnote{\url{https://tools.ietf.org/html/rfc4122}} with an extremely low collision probability.

    odML document
    Document - uniqueID_01
    - Section - name_A - uniqueID_02
    - Section - name_B - uniqueID_03
      - Section - name_A - uniqueID_04

    Document converted to odML RDF in the nice to read turtle[todo link] notation:
    @prefix odml: <https://g-node.org/odml-rdf#> .

    odml:uniqueID_01 a odml:Document ;
        odml:hasSection odml:uniqueID_02, odml:uniqueID_03 .

    odml:uniqueID_02 a odml:Section ;
        odml:hasName "name_A" .

    odml:uniqueID_03 a odml:Section ;
        odml:hasName "name_B" .
        odml:hasSection odml:uniqueID_04 .

    odml:uniqueID_04 a odml:Section ;
        odml:hasName "name_A" .


    - connecting the documents at a common root to retain document separation - introduction of the Hub
    - why care has to be taken in the conversion
    - tree vs graph
    - address not easy to go back from rdf
    - add readthedocs link to paper
    - compare to HBP knowledge graph


# Discussion / Comparison

A problemset in finding data in unfamiliar data structures is navigation. While JSON already provides strictness in creating a valid, parsable document, odML provides a simple, underlying structure. Groupings are done in sections that can be nested. Values and connected metadata like uncertainty as well as further links are constrained to properties that can only be contained by sections. Once one knows this underlying structure, searching through such a document is fairly easy once the section-property relationship is known while not sacrificing storing metadata fairly unrestricted and expand them if required.

Ebrains/knowledge graph
https://www.re3data.org/repository/r3d100013325
https://nfdi-neuro.de/files/2020-02-10_Zehl_EBRAINS.pdf
EBRAINS Knowledge Graph (https://kg.ebrains.eu)
EBRAINS Knowledge Graph (RRID:SCR_017612)

Compared to the HBP knowledge graph the odML RDF version is designed for a different audience; it is meant for in house or across house use - everyone that is using odML can make their data searchable and while making use of the custom SPARQL server can even be shared across labs to make metadata searchable and datasets discoverable. The labs themselves are responsible to curate the metadata, convert it and make useful search queries available.

Further its a low access point to publish metadata and link to already published datasets since its not hard to export to RDF, create a cross-platform and cross-lab database that can host even diverse metadata.

The option for multiple query endpoints make it easy to temporarily set up a large common dataset from multiple locations and take it down after its job is done.





# Outlook

Custom subclassing
Integration into GIN for automatic upload

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
[ODMLQuery] https://github.com/G-node/odml-query
[ODMLQueryDocker] https://hub.docker.com/r/gnode/meta

[DataCiteTerminology] V#
[DataCiteTemplates] V#
[DataCiteToODML] V#
