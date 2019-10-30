odML - RDF project

1) Conversion of odml to RDF and vice versa. We will provide a draft of the RDF data model.
  - Extend the odml data model with the required fields for conversion towards RDF (i.e. adding
    uuids to the entities).
  - Provide a prototype for the conversion from odml to RDF using the provided
    RDF data model draft as reference.
    We will provide example odml files as reference. Use RDFlib or a similar library.
  - Provide a prototype for the import of odml flavored RDF into odml. (optional)
 
2) Test and improve the generic RDF data model
  - Use existing triple stores of your choice to query the created RDF files.
  - Create subclasses and subproperties for the generic RDF data model based on the provided
    example files to increase searchability of the resulting RDF files.
  - Update the odml to RDF conversion prototype to support the additional RDF subclasses and properties.
  - Provide example queries of odml to RDF exports created with generic and specialized RDF data models.
 
3) Explore ways of (i) presenting such knowledge graphs to a user and (ii) drafting of a
   "fuzzy finder" converting non-structured user queries to SPARQL.

Some resources to get started:
- https://en.wikipedia.org/wiki/Semantic_Web (as Christian mentioned)
 
Beginners introductions
- http://www.cambridgesemantics.com/semantic-university/rdfs-introduction
- http://www.cambridgesemantics.com/semantic-university/owl-reference-humans
 
RDF and OWL resources
- http://www.w3.org/TR/rdf11-concepts
- http://www.w3.org/TR/rdf-schema/
- http://www.w3.org/TR/rdf-sparql-query/
- http://www.w3.org/TR/owl-profiles/
 
RDFlib python library and tools
- https://github.com/RDFLib
- http://rdflib.readthedocs.io/en/stable/

----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------

Some questions to discuss.
1) Should we use empty bag for None values.
2) How the terminology can be accessed/stored besides the url in the document.
3) As I read references could be strings to some DB besides url. What do you think of 
   adding a some kind of url validator to diversify such cases? Since different 
   identifiers in rdflib are used (URIRef and Literal) it might be important.
4) Questions about link&include:
    a) Does inheritance work only for properties or other attributes as well?
    b) Should I manage some validation issues e.g. is link from the section to its 
       subsection is considered as mistake?
    c) Are values of links' attributes just name of Sections in the current document? (edited)

----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------

odML - RDF server project

Outline:
Result of the project will be a SPARQL endpoint server providing searches
of G-Node odML files via a triple store RDF graph. The content of the triple
store are odML files provided by the G-Node, converted into the previously
developed RDF format. The server endpoint will support both SPARQL queries
and the also previously developed "fuzzy" queries. The server can be written
in any language, but has to be based on an established RDF library and must
only contain open source components. If the chosen language is not Python,
the previously written "fuzzy" query library has to either be imported via
bindings or reimplemented.

Prerequisite:
- The language decision will be based on RDF library tests and query benchmarks.
- The benchmarks will be based on a triple store RDF Graph containing all
   converted odML files from the gin repositories "gin.g-node.org/G-Node/odmlFiles"
   and "gin.g-node.org/INM6/multielectrode_grasp".
- The benchmark should use the previously defined queries which can be found
   in the python-odml sparql-benchmarking branch.
- The benchmark should provide information about and statistics for
     - the machine the benchmark is executed on.
     - the number of available individual RDF files.
     - the times to load and create the graph of all the available RDF files
       with the different SPARQL libraries.
     - the execution time of the SPARQL queries using the different
       SPARQL libraries.

RDF Query server:
- the primary code will live in a G-Node github repository, any development
   and changes are to be made against this repository. The project will provide a
   BSD license with a G-Node copyright.
- the project consists of three main parts:
     - Handling of an RDF triple store containing the files used during the
       benchmarking. This part also has to handle the addition of new documents
       to the triple store. For now this should be done via the command line and
       not provide web access for this purpose since we do not want to implement
       user management for now.
     - a REST style server querying this triple store via SPARQL or fuzzy queries.
     - a front end providing an entry mask to enter SPARQL or fuzzy queries and
       a sensible display of the retrieved results.

----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------

Outline
Result of the project will be a SPARQL endpoint server providing searches of G-Node odML 
files via a triple store RDF graph. The content of the triple store are odML files 
provided by the G-Node, converted into the previously developed RDF format. 
The server endpoint will support both SPARQL queries and the also previously developed 
"fuzzy" queries. 
The server can be written in any language, but has to be based on an established 
RDF library and must only contain open source components. If the chosen language is not 
Python, the previously written "fuzzy" query library has to either be imported via 
bindings or reimplemented.

Prerequisites
The language decision will be based on RDF library tests and query benchmarks. 
The benchmarks will be based on a triple store RDF Graph containing all converted 
odML files from the gin repositories "gin.g-node.org/G-Node/odmlFiles" and 
"gin.g-node.org/INM6/multielectrode_grasp". 
The benchmark should use the previously defined queries which can be found in the 
python-odml sparql-benchmarking branch. 
The benchmark should provide information about and statistics for - the machine the 
benchmark is executed on. 
the number of available individual RDF files. 
the times to load and create the graph of all the available RDF files with the different 
SPARQL libraries. 
the execution time of the SPARQL queries using the different SPARQL libraries.

Requirements for RDF Query server
the primary code will live in a G-Node github repository, any development and changes 
are to be made against this repository. The project will provide a BSD license with 
a G-Node copyright. 
the project consists of three main parts: 
Handling of an RDF triple store containing the files used during the benchmarking. 
This part also has to handle the addition of new documents to the triple store. For now 
this should be done via the command line and not provide web access for this purpose 
since we do not want to implement user management for now. 
a REST style server querying this triple store via SPARQL or fuzzy queries. 
a front end providing an entry mask to enter SPARQL or fuzzy queries and a sensible 
display of the retrieved results.

Technologies
Apache Jena (https://jena.apache.org/index.html) 
Robust and developed Java framework for Semantic Web and Linked data.

Advantages
Complete stack of solutions for building Semantic Web apps including Jena Fuseki, TDB, 
Ontology API, Inference API.
Extensive and updated documentation.
Well known organization.
Open Source.

Core technologies for the project
Jena Fuseki (https://jena.apache.org/documentation/fuseki2/index.html)
Apache Jena Fuseki is a SPARQL server. It can run as a operating system service, as a 
Java web application (WAR file), and as a standalone server. It provides security (using 
Apache Shiro) and has a user interface for server monitoring and administration.

Jena TDB (https://jena.apache.org/documentation/tdb/index.html)
TDB is a component of Jena for RDF storage and query. It support the full range of 
Jena APIs. TDB can be used as a high performance RDF store on a single machine. 

Useful technologies to add later
Jena Inference API (https://jena.apache.org/documentation/inference/index.html)
Additional facts to be inference from instance data and class descriptions using RDF and OWL.
Application of generic rules for many RDF processing or transformation tasks. 
As I understand also possible to use for validating graphs with specific OWL ontology.

Jena Ontology API (https://jena.apache.org/documentation/ontology/)
Advanced tool to build and manage OWL ontologies. 

Jena Eyeball (https://jena.apache.org/documentation/tools/eyeball-getting-started.html)
New tool, not released yet to inspect common problems in RDF models (including OWL)

Jena Elaphas (https://jena.apache.org/documentation/hadoop/)
Beta module. Apache Jena Elephas is a set of libraries which provide various basic 
building blocks which enable you to start writing Apache Hadoop based applications 
which work with RDF data.

Link to the image, to zoom and comment
https://drive.google.com/file/d/1x9g2RYKtogVxvVGQGsacjd71H8OqNPNZ/view?usp=sharing

Description
Fuseki support various running options and I am still considering the best one for our 
use case. https://jena.apache.org/documentation/fuseki2/fuseki-run.html
Standalone server is the most straightforward solution. However, since processing fuzzy 
queries requires separate module, I can consider running Fuseki from java application. 
Option 1. Standalone servers. Diagram draft above
In the case we develop every part as standalone applications which communicate with each 
other through HTTP. Java app as shown in the draft can be Python server in the case. 
Benchmarks will be executed on the standalone app side.
Option 2. One Spring application with embedded Fuseki server
One application with embedded server, one API for invoking SPARQL. 
https://jena.apache.org/documentation/fuseki2/fuseki-embedded.html
Better benchmarks since there is no additional http layer and everything gathered in one app.

It looks more easier and promising to me but I need some time to research the option. 
Will add to this part soon.

Jena Fuseki demo app
Jena Fuseki is powerful service for executing SPARQL queries and manage datasets. Fuseki 
UI is enhanced with various features and can serve as example, or can be reused for Fuzzy 
queries app.
I ran it and tested it locally. It supports Apache Shiro (https://shiro.apache.org/) for 
authentication. With the UI and auth there is not many  reasons to have command line 
interface to manage the dataset and interact with TDB. 

I deployed Fuseki Server on my Amazon account to the EC2 instance, so you can also test 
it right away. It contains the persistent dataset with drosophila graph which consist of 
100k triples. I added authentication configuration so you would need admin rights to load 
new files or update existing graph with `insert` queries. Querying and looking the graph 
does not require any auth.

----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------

# Fuzzy sparql
POST
http://meta.g-node.org:8000/api/fuzzy-query/
{
    "query": "FIND sec(name, type) prop(name) HAVING Recording, Date",
        "dataset": "<http://meta.g-node.org:3030/odml-tdb/data/drosophila>"
}

Benchmarking
Creating various from basic tree
Change 
Width
height (level),
Amount of change (amount of change)
Size (n of elements)
Distance, difference ?? ( do not understand =)) ) 

Things to research 
Jena Full text search with Apache Lucene 
    https://jena.apache.org/documentation/query/text-query.html

Analogous to NCBI search

https://www.ncbi.nlm.nih.gov/books/NBK3837/

Arthur[sec.name] AND Human[prop.value] (edited)
rickskyy
4:38 PM
select sec.name where doc(..) sec(type:sometype) prop(..) prop(..)

hi @U1FMV8NLT @dumdribille, working with benchmarking for fuzzy finder. 
Now I use SQLAlchemy plugin for rdflib with MySQL db as triple store, because loading 
over 200 files (drosophila files from gin repo) in memory every time is quite time-consuming. 
How do you like me to organize jupyter documentation with the benchmarking so you can manually test queries yourself.
1) The straightforward solution is just add gin ttl files (5 Mb) to the doc folder and load the graph every time, it takes from 1 to 2 minutes on average to load 100k triples.
2) More complex way is set up the db in the cloud somewhere so everyone can connect to it and test.
The first way is not too bad also since I can load the graph only once and work with it in memory for some time without closing, so here jupyter becomes really useful.
In any way I plan to finish all the work by tomorrow and present the results to you. Also we can set up a hangout either tomorrow or during the next week. (edited)
Some edits, just tried running queries on SQL db and noticed that the difference between in memory tests and db tests is too huge, smth like quering the db is 60 times slower :sweat_smile: than the same query in memory (I do not count the graph loading time). Gave up using db for now.
Also I looked for some storage services yesterday and find out some rankings https://db-engines.com/en/ranking/rdf+store. The first one is commercial so I do not think it would work for us. Jena is only compatible with Java but it looks impressive with great documentation and so on. In addition it is open source. Also I want to try it and see the difference in speed of queries compare to python rdflib. Have not looked to virtuoso yet.

@dumdribille @jgrewe some review tips. In `FuzzyFinder` class there are implemented 
2 main functions `FuzzyFinder.find()` and `FuzzyFinder.find_fuzzy()`. The second is more 
fuzzy than first and I assume it's more relevant to requirements we were discussing earlier. 
Basically, `FuzzyFinder.find_fuzzy()` is an extension to the previous one, but I left 
first find() to see your comments.
You can test them in jupyter notebook on part of drosophila database which consist of 17k 
triples. I added this ttl files just for testing purposes and to show difference of speed 
between queries with various complexity. Definitely they might not be added to python-odml 
repo and there are ways to load them from external service. (edited)

----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------

We needed the odml to RDF export for a specific joint project with a group in the us, the 
crcns, with the goal to make metadata from experiments available and searchable. This we 
already achieved now we are in turn waiting for a response from the crcns which from past 
experience can take some time.
Other than that we don't have any active users for the RDF data. If we can set up a proper 
server where our data can be searched via SPARQL or our easier variant of it, this might 
be an additional interesting service within the G-Node, but I cannot guarantee, that many 
people will use it. In any case, I think there are no objections whatsoever to use the 
code in your thesis other than it has to stay open source.

----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------

Benchmarking

Frankly, results are controversial. Fuseki starts falling sometimes on 10M. Sometimes it is fast ~ 5 seconds on 10 M, in other situations it is just not responding at all on quite a similar query. (edited)

SELECT ?s ?s_name ?p_name ?value
FROM <http://meta.g-node.org:3030/odml-gen/data/test-put>
FROM <http://meta.g-node.org:3030/odml-gen/data/files3-7>
FROM <http://meta.g-node.org:3030/odml-gen/data/odml-perfomance-test>
WHERE {
    ?s odml:hasProperty ?p .
    ?s odml:hasName ?s_name .
    ?p rdf:type odml:Property .
    ?p odml:hasName ?p_name .
    FILTER regex(?p_name, "^name-lv-250-5") .
}

the one thing I noticed that it is usually falling when there is no limit in search. 
So for example above search goes infinite on 10M  (error: no response from endpoint), 
but with a limit of 10 it is 5 sec, limit of 20 is 12 sec
These happens in many situations
Trivial: searches for deeper levels are more time consuming, but not more than 2 times for 10 M
I wrote in the thesis is kind of good and the speed I have is nice comparing to other 
cases e.g. https://www.sciencedirect.com/science/article/pii/S1045926X1730246X
sciencedirect.com
Performance assessment of RDF graph databases for smart city services
Smart cities are providing advanced services aggregating and exploiting data from 
different sources. Cities collect static data such as road graphs, s…
But I feel we need to test more. Not sure that server can handle 100M, will try soon, 
for diploma results I limit myself to 10M.
I am trying to get the job in one local company so I have a test task from the employer 
for these week so I switch my work there, and come back in a week or so, to prepare good 
report for you, because the benchmarks I added to the thesis are not too representative 
for you I think (edited)

the example that I had on multiple tests - average on 50 tests on each 60 and 270 level +- 10 levels
although it is the simple query but it nice to see the tendency when the graph grows 
and also it is returning all results even when it is the biggest width (returning > 25k rows result) (edited)
however, more specific queries like the one I sent earlier or even super specific like 
finding one unique value is usually falling on 10M (edited)

While testing query performance got first result - exponential grow of the executing time to number of triples for merged graphs.
(< 1000 triples = < 2 sec) (2500 = 60 sec)
Besides in memory tests tried SQLAlchemy stores such as SQlite and MySQL. As I understood there is no significant correlation between performance and storage usage.
However, I had some problems with reading data from MySQL database
The problem might be in:
Poorly optimized queries
*Odml RDF architecture (For now I trying to read more about query optimization)

q1 = prepareQuery("""SELECT ?p ?value
           WHERE {
              ?d rdf:type odml:Document .
              ?d odml:hasSection ?s .
              ?s rdf:type odml:Section .
              ?s odml:hasType "Recording" .
              ?s odml:hasProperty ?p .
              ?p odml:hasName "Recording duration" .
              ?p odml:hasValue ?v .
              ?v rdf:type rdf:Bag .
              ?v rdf:li ?value .
           }""", initNs={"odml": Namespace("https://g-node.org/projects/odml-rdf#"),
                         "rdf": RDF})

q2 = prepareQuery("""SELECT ?s
           WHERE {
              ?d rdf:type odml:Document .
              ?d odml:hasSection ?s .
              ?s odml:hasType "Recording"
           }""", initNs={"odml": Namespace("https://g-node.org/projects/odml-rdf#"),
                         "rdf": RDF})


Performance: 100k triples = 182 sec execution, (rdflib SQlite in memory test)


----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
