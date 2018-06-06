
2.1.1 [choose chapter title or devise a different one]
- Regarding the current state of the odML format
- A short description of the odML format 
- ...

[... original text]
odML\footnote{see: \texttt{https://github.com/G-Node/python-odml}} (Open metadata mark up language, RRID:SCR\_001376) 
is a versatile \xml -based hierarchical format for metadata \citep{Grewe_2011} developed by 
the German Neuroinformatics Node (G-Node). While odML was originally designed for electrophysiological metadata, 
its generic structure makes it also applicable to other scientific contexts. In the following, we describe odML in 
its version v1.4\footnote{\texttt{https://github.com/G-Node/python-odml/releases/tag/v1.4.0}}, which includes multiple 
improvements compared to the API described by \citet{Grewe_2011}.
[...]

Since the release of the original version odML has been used in various software projects as plugin to provide
a predefined and available metadata format e.g. in the NIX project or as an integral part as in the odMLtables project
as well as a standalone metadata data pipeline as described by Zehl et al.

The usage in everyday metadata pipelining as well as the integration of the core library in odMLtables lead to the 
discovery of various shortcomings and lead to the demand of new features with respect to the original version
of odML. In addition the re-implementation of odML in other languages than the original implementation e.g. in C++
or Matlab in the NIX project lead to a diversification of the core odML data format.

As the two main shortcomings of the odML core library we identified the need to search across multiple odML files and 
the need to easily visualize and manipulate the content of specific odML files.
To address the first shortcoming we integrated an export to the RDF (Resource Description Framework)
format opening odML to the semantic web. Graphs containing the content of multiple odML files can easily be constructed
and searched using the established SPARQL query language.

To address the need to easily visualize and manipulate odML files Jülich and G-Node started to work more closely 
together to integrate the odMLtables into the previously described odML graphical user interface.

As a first step, the odML graphical user interface was removed from the core library and 


2.1.2 Hierarchical Metadata in the odML format

[... original text continued]
The hierarchical odML structure is flexible and consists of three types of objects (Fig.~\ref{odMLstructure}):


