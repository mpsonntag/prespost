## Problemset introduction
- diverse metadata
- how to generalize for search
- how to make available for linkback


## A brief introduction to the odML data format

As previously reported (Grewe et al., 2011)[Grewe] odML[odML] is a data format 
designed to thoroughly document diverse metadata. Developed by the
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

While odML has shown to document experiments even 
through diverse fields due to its flexibility, there is a growing need to search
across multiple experiments and even across multiple fields. As recently 
published (Sprenger et al., 2019)[odMLtables], the odML data format has been 
developed further to also address this growing demand.

Due to this growing demand the odML implementation has been
furthered to include a conversion of odML to an odML flavored
version of the RDF (Resource Description Framework)[3] format.
Data in RDF can easily loaded into graph databases and queried
using the RDF specific SPARQL ([xxx])[] query language.
Using the odML format in RDF enable to search across multiple
documents and even unrelated fields of science.

- brief description of features + data model, mentioning of update compared to 
  first paper and mention of odmltables

[Grewe] Grewe J., Wachtler T., and Benda J. (2011). A bottom-up approach to data annotation in neurophysiology. Front. Neuroinform. 5:16, doi:10.3389/fninf.2011.00016
[odML] https://github.com/G-Node/python-odml, RRID:SCR_001376
[odMLtables] Sprenger J, Zehl L, Pick J, Sonntag M, Grewe J, Wachtler T, Grün S and Denker M (2019). odMLtables: A User-Friendly Approach for Managing Metadata of Neurophysiological Experiments. Front. Neuroinform. 13:62. doi: 10.3389/fninf.2019.00062


## Introduction to RDF to deal with querying diverse datasets

## Project outlines
- mapping of odml -> RDF to make diverse datasets queryable via the same graph
- providing a common server for searchable metadata
- figure: proposed workflow; adopted from 1st publication @ INCF conf -> get doi?
- how to make the data useful and findable? -> datacite!

# Implementation

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
