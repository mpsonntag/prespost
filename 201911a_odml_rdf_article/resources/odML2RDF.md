## Exporting odML to RDF

## Mapping odML to RDF terms

Looked up all the different resources for odML that are still out there and came up with the following existing
classes and properties - I am sure many of them can be removed, but then they should also be removed from the
resources to reduce confusion.

ALL of the properties can be fine grained into subproperties to give more semantic meaning to the connection
between nodes.

e.g.
    section hasSection section
 could become
    section hasExperimenter section
    
 here hasExperimenter is a subclass of `hasSection` ... a search for `hasExperimenter` would return only sections connected
 via this specific property, a search for hasSection would return all sections connected by `hasSection` and `hasExperimenter`.

### The odml namespace:
odML ... namespace should be a URL pointing to where the RDF definition of odML can be found. 
Main part of the url will be http://g-node.org, the secondary hierarchical part has not been determined yet.

### Naming guidelines:
Custom RDF Node and Property names should be in line with rdf best practices.
Check the corresponding [github issue](https://github.com/G-Node/python-odml/issues/112).

### Hub
I think this is something we would need, to merge different odML documents into an existing graph.
Because we start from a hierarchical document it is ok to connect them via a central hub node.

    odml                        RDF                             xsd type        RDF alternative
    -------------------------------------------------------------------------------------------
    -                           odml:Hub                        -               RDF type odml:Hub
    -                           odml:hasDocument                -
    -                           odml:hasTerminology             -

### Root section

    odml                        RDF                             xsd type        RDF alternative
    -------------------------------------------------------------------------------------------
    odml                        odml:Document                   -               RDF type odml:Document
    
    id                          use uuid as instance name       -
    author                      odml:hasAuthor                  xsd:string
    date                        odml:hasDate                    xsd:date
    version (odml)              odml:hasVersion                 xsd:float
    version (document)          odml:hasDocVersion              xsd:string
    repository                  odml:hasTerminology             -               * see description below
                                odml:hasExternalTerminology     xsd:string
    Sections                    odml:hasSection                 -
    -                           odml:hasFilename                xsd:string      + see description below

 
* RDF export of repositories: 
Export terminology to an additional rfd document with proper ID and add it to the hub node and reference 
the terminology doc ID in the main document (and all others that use the terminology).
Otherwise, if pointing to external url (publicly available): keep the url as leaf.

+ As provenance to follow up on where this particular odml:Document was created from, add the
  filename of the original odML file.

### Terminology

Terminologies from an odml document should live at the same hierarchy level as the original document 
(directly beneath the odml:Hub) and should be referenced via odml:Terminolgy by the odml:Document or 
odml:Section it was taken from.
It should have its own id, but I am not sure, if it should have author, date and document version as an 
odml:Document has. I would leave this for now and introduce it later if we find a case where we actually need it.

    odml                        RDF                             xsd type        RDF alternative
    -------------------------------------------------------------------------------------------
    odml                        odml:Terminology                -
    
    id                          use uuid as instance name       -
    Sections                    odml:hasSection                 -


### Section

    odml                        RDF                             xsd type        RDF alternative
    ---------------------------------------------------------------------------------------
    Section                     odml:Section                    -               RDF type odml:Section
    
    id (to be implemented)      RDF Section instance name       -
    name                        odml:hasName                    xsd:string      RDFS:label
    type                        odml:hasType                    xsd:string
    definition                  odml:hasDescription             xsd:string      RDFS:comment
    repository                  odml:hasTerminology             -               see root:repository
                                odml:hasExternalTerminology     xsd:string
    include                     * see below                     -
    link                        * see below                     -
    reference                   odml:hasReference               -/xsd:string    + see below
    Sections                    odml:hasSection                 -               ~ see below
    Properties                  odml:hasProperty                -

    mapping (deprecated)        will be removed in future versions of odml

 
* Resolving include and link (i.e. adding all information inherited from the respective resources, should be handled [needs to be confirmed] by the python-odml lib)
 
Links (allow for a more compact tree, models an inheritance pattern, links to sections of the same type within the very same file): 
-- document: doc_1
-- section global_foo
    amp = 1
    dur  = 2
-- section bar
    -- section local_foo (link: global_foo)
        amp = 1.4
    -- section local_foo2 (link: global_foo)
        amp = 1.3
 
local_foo.properties → [amp = 1.4, dur = 2]
local_foo2.properties → [amp = 1.3, dur = 2]
 
Include (same as Links but for resources in external files):
-- document: global_doc
-- section global_foo
    amp = 1
    dur  = 2
 
-- document: bar_1
    --section local_foo (include: global_doc/global_foo)
        amp = 1.7
 
-- document: bar_2
    section local_foo (include: global_doc/global_foo)
        amp = 1.8
 
bar_1.local_foo.properties → [amp = 1.7, dur = 2]
bar_2.local_foo.properties → [amp = 1.8, dur = 2]
 
+ Resolving a reference can be a URL to an external reference or a string pointing to an id in a Database.

~ should this be specified to hasSubSection and already be a subclass of hasSection?
there are already different connectors between sections/property 
and section which could not be distinguished otherwise e.g. mapsToSection


### Property

    odml                        RDF                             xsd type        RDF alternative
    -------------------------------------------------------------------------------------------
    Property                    odml:Property                   -               RDF type odml:Property
    
    id (to be implemented)      RDF Property instance name      -
    name                        odml:hasName                    xsd:string      RDFS:label
    definition                  odml:hasDefinition              xsd:string      RDFS:comment
    reference                   odml:hasReference               - / xsd:string  see below #

    unit                        odml:hasUnit                    xsd:string      si:unit
    dtype                       odml:hasDtype                   xsd:string      + see below
    uncertainty                 odml:hasUncertainty             xsd:float
    Values                      odml:hasValue                   xsd:string      * see below
    value_origin                odml:hasValueOrigin             xsd:string

    mapping                     will be removed in future versions of odml
    synonym                     will be removed in future versions of odml
    dependency                  will not be exported
    dependencyValue             will not be exported

'# Resolving a reference can be a URL to an external reference or a string pointing to an id in a Database.

+ This could be a problem to link, if its not a basic type, but one defined in a terminology; 
    It has to be different from Section/type.

* use RDF:Bag with RDF:li or similar for values since odml supports multiple values.

### Value

    Value as a concept will be removed, in particular the following value fields
    will not be removed from the odml concept:

    filename
    encoder
    checksum
    reference
    defaultFilename


## RDF libraries

## RDF libraries
- [RDFlib](https://github.com/RDFLib/rdflib) 
    - Actively developed, many RDF project seem to converge on RDFlib
    - Comes with decent documentation
    - py2 and py3.
- [librdf](http://librdf.org/): C library with bindings to various language bindings including Python.


## odML Resources that are out there:
A lot of the resources that can still be found have very conflicting content. This makes it quite difficult to
properly discuss even within teams, if everyone has different "base of knowledge" about odML.

### Documents, Documentation, Tutorials
- [odML Roadmap (google doc)](https://docs.google.com/document/d/16usqrMgk6muqgkSmQ0qonXsGrC0S9nhyHdzgWAJyoFg/edit#heading=h.ycmlvplf2l2s)
- odML metadata future document
- [python-odml documentation + tutorial](https://g-node.github.io/python-odml/)
- [odML terminologies](http://portal.g-node.org/odml/terminologies/v1.0/terminologies.xml)
- [odML Schema](http://www.g-node.org/projects/odml/odMLSchema.png/view)

### Papers
- [A bottom-up approach to data annotation in neurophysiology](http://journal.frontiersin.org/article/10.3389/fninf.2011.00016/full)
- [Handling Metadata in a Neurophysiology Laboratory](http://journal.frontiersin.org/article/10.3389/fninf.2016.00026/full)

### Projects using odML
- [python-odml](https://github.com/G-Node/python-odml)
- [odml-ui](https://github.com/G-Node/odml-ui)
- [odml-terminologies](https://github.com/G-Node/odml-terminologies)
- [odML Tables](https://github.com/INM-6/python-odmltables)

### RDF resources

#### Introduction
- http://www.cambridgesemantics.com/semantic-university/rdfs-introduction
- http://www.cambridgesemantics.com/semantic-university/owl-reference-humans

#### RDF and OWL resources
- http://www.w3.org/TR/rdf11-concepts
- https://www.w3.org/TR/2004/REC-rdf-concepts-20040210/
- http://www.w3.org/TR/rdf-schema/
- https://www.w3.org/TR/rdf11-primer/
- http://www.w3.org/TR/rdf-sparql-query/
- http://www.w3.org/TR/owl-profiles/
- [OWL tutorial](http://owl.cs.manchester.ac.uk/publications/talks-and-tutorials/protg-owl-tutorial/)

#### Related RFCs
- [rfc2396 - Uniform Resource Identifiers (URI): Generic Syntax](http://www.ietf.org/rfc/rfc2396.txt)


## Unsorted notes:
Check out which RDFs:xxx would fit for "subset" and check, how this would be stored in "normal" odML 
... would this break existing files? 

Conversion RDF -> odML ... how to root the graph? Here a single RootSection node would help!

- what are specific datatypes can be used for objects in a triple?  which xsd type schema to use for property values?
    MS: I am not sure how we should add data types directly to values , since this is handled via property.dtype. 
            The type defined there applies to all values in the bag. Maybe if dtype is a basic datatype, then 
            add the corresponding datatype, otherwise add xsd:string.

- how the terminology can be accessed / stored besides the url in the document
    MS: This is touches actually an interesting, more general point: Are `Terminology` and `Document` the same?
        As far as I understand it so far, they are actually two different concepts. Maybe we should therefore 
        Also keep them semantically separate. So I would suggest using odml:Document and odml:Terminology as 
        rdf types respectively.
        Arbitrary example: an exported document could have one odml:Document and e.g. two different odml:teminologies,
        connected via an odml:Hub:
        odml:Hub - hasDocument - odml:Document (id:1)
        odml:Hub - hasTerminology - odml:Terminology (id:2)
        odml:Hub - hasTerminology - odml:Terminology (id:3)
        odml:Document - hasSection - odml:Section (id:4)
        odml:Document - terminology - odml:Terminology(3)
        odml:Section(4) - terminology - odml:Terminology(2)


- as I read references could be strings to some DB beside url. should we add a url validator to diversify cases, 
    since different identifiers are used in rdflib (URIRef and Literal)
        MS: I would export the content as is to a Literal only for now.
Issues:

- Subclassing for Sections and Properties Examples
        Subclass Sections and Properties according to the type of available terminologies
        Start with the Section and Property types in our current example files
        e.g. odml:Person subclass odml:Section; odml:Electrode subclass odml:Section
        Update the current odML ontology with these terms as new subclasses
        to sections and properties. That way A Section of type "Electrode" can be
        found either by "isSection" and "hasType=Electrode" or directly by
        "isElectrode" which should make the queries more efficient when they become
        more complex.

- Generic Subclass exporter prototype
refactor the current exporter to
    - [ ] Implement a generic list filled with the newly added Section and
            Property subclasses mapped to the corresponding type. This
            list should be easily updatable with additional Section and
            Property Subclasses.
    - [ ] during the export, add a Section or Property check for type. If a Section or Property
            is of a type in the list of subclasses, export them as the corresponding subclass
            Otherwise export as plain Section or Property.
            e.g.

- Test queries for subclassing
    Transform the queries created during the first round of testing into the
        new version and add new specific queries against a couple of merged
        documents.

- Update import from RDF to odML of Subclass RDF documents
    Refactor the importer so that it correctly interprets all subclasses of
    Section as Section and subclasses of Property as Property during the
    import process.

- Port all documented odML Terminology terms to odML Ontology
    Once the subclassing prototype works and the queries run
    satisfyingly, include all described Sections and Properties from
    the G-Node odML Terminology into the odML Ontology and make
    them available to the rdf_exporter.

