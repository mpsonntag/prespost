## Problemset introduction
- diverse metadata
- how to generalize for search
- how to make available for linkback


## A brief introduction to the odML data format

As previously reported (Grewe et al., 2011)[Grewe] odML[odML] is a data format 
designed to thoroughly document diverse metadata that comes with a freely available
reference implementation in Python. Developed by the
German Neuroinformatics Node, its design was oriented along the needs
of Neuroscientific metadata, but its generic approach makes it applicable
to any scientific field.

### The odML data format

As a brief introduction to the odml concept is to store metadata in a 
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

### Further development to open odml to interconnected searches

While odML has shown to document experiments even through diverse fields due to its 
flexibility, there is a growing need to search metadata across multiple experiments 
and even across multiple fields. As recently published (Sprenger et al., 2019)[odMLtables], 
the odML data format has been developed further to also address this growing demand.

Even though searches within even extensive odML documents were always part of the
implementation and even imports from linked, external sources into individual documents
are possible, the option to easily search across multiple documents was still lacking.
To this end we chose to open the odML data format to the Semantic Web[SemWeb] via conversion to 
the RDF (Resource Description Framework)[RDF] format.

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

- Schema and description of odml and the RDF mapping
- ontology
- description of usage -> rdf example with 
- description of subclassing, idea behind it, how to use it
- description convenience conversion scripts
- description convenience datacite conversion script?

- fuzzy queries?

## Implementation of sparql server

- why fuseki
- adoption
- availability of data

- availablility for in house serving

## odML for backlink
- datacite port to odML template
- other odML templates for making datasets findable via the server


# References

[Grewe] Grewe J., Wachtler T., and Benda J. (2011). A bottom-up approach to data annotation in neurophysiology. Front. Neuroinform. 5:16, doi:10.3389/fninf.2011.00016
[odML] https://github.com/G-Node/python-odml, RRID:SCR_001376
[odMLtables] Sprenger J, Zehl L, Pick J, Sonntag M, Grewe J, Wachtler T, Grün S and Denker M (2019). odMLtables: A User-Friendly Approach for Managing Metadata of Neurophysiological Experiments. Front. Neuroinform. 13:62. doi: 10.3389/fninf.2019.00062
[SemWeb] https://www.w3.org/standards/semanticweb/
[RDF] https://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/
[SPARQL] https://www.w3.org/TR/sparql11-query/
[OWL] https://www.w3.org/TR/owl-ref/
[DataCite] https://datacite.org/
