# Problemset
- diverse metadata
- how to generalize for search
- how to make available for linkback

As previously presented, odML[1] is a data format to document
metadata. It is able to accommodate diverse metadata. As reported
as part of the odML tables publication[2] the data format has been
developed further.
While odML has shown to document experiments even through diverse
fields due to its flexibility, there is a growing need to search
across multiple experiments and even across multiple fields.

Due to this growing demand the odML implementation has been
furthered to include a conversion of odML to an odML flavored
version of the RDF (Resource Description Framework)[3] format.
Data in RDF can easily loaded into graph databases and queried
using the RDF specific SPARQL ([xxx])[] query language.
Using the odML format in RDF enable to search across multiple
documents and even unrelated fields of science.
  

## Introduction odML how to deal with diverse metadata
- Paper
- brief description of features + data model, mentioning of update compared to 
  first paper and mention of odmltables

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
