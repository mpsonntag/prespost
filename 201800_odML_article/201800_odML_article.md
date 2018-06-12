2.1.1 User driven odML adaptations and updates


[... original text]
odML\footnote{see: \texttt{https://github.com/G-Node/python-odml}} (Open metadata mark up language, RRID:SCR\_001376) 
is a versatile \xml -based hierarchical format for metadata \citep{Grewe_2011} developed by the German Neuroinformatics 
Node (G-Node). While odML was originally designed for electrophysiological metadata, its generic structure makes it also 
applicable to other scientific contexts. In the following, we describe odML in its version 
v1.4\footnote{\texttt{https://github.com/G-Node/python-odml/releases/tag/v1.4.0}}, which includes multiple improvements 
compared to the API described by \citet{Grewe_2011}.
[...]

Since the release of the original version, odML has been used in various software projects for storing metadata as they 
become available during data acquisition or analysis [e.g. in the NIX (https://github.com/G-Node/nix) and 
RELACS (http://www.relacs.sourceforge.net) projects], as a part of a metadata data pipeline as described by 
\cite{Zehl_2016}, or as an integral part in the odMLtables project.

This usage of odML in different environments with varying requirements has led to the identification of unused features 
and the need for improvement of the original data model. As examples odML needed to be re-implemented in C++ in the case 
of the NIX and RELACS projects to accommodate a different storage backend than the text-based XML format, in case of the 
odMLtables project, the original internal data representation required only a subset of the complete odML data model. 
These re-implementations did not always stick to the original odML specifications and lead to a diversification of the 
available odML data models. In order to remedy this situation with the latest release of odML version 1.4 (i) unused 
features were removed and (ii) the data model was simplified and adapted to ensure odML compatibility between the 
various project implementations. We will briefly review the changes. 

2.1.2 Removal of unused features:
We dropped support of storing binary data within the values. This feature has, to our knowledge, never been used. 
Approaches combining data and metadata storage (e.g. the NIX project) actually left this feature needless. Dropping it 
allowed us to also remove additional fields in the Value entity that were devoted solely to this purpose. Further, the 
mapping functionality was dropped. The idea behind this feature was to allow to map metadata used according to one 
definition to a different definition. As before, to our knowledge, this functionality has not been used and becomes 
actually obsolete when metadata are converted to formats using semantic web technologies. Again, this allowed us to 
remove now unnecessary fields from the model.

2.1.3 Model simplification:
Several fields were removed due to the dropping of the mapping feature and by removing the support for binary content. 
Another major change was the merge of Value and Property entities of the original data model (compare figure X a and b). 
In principle, it has been possible to store values of completely different types within the same property. For example, 
storing a numeric value (e.g. the temperature) together with a textual value would have been possible. This in turn 
effectively made stored metadata verbose and susceptible to ambiguity between property and value level. In the current 
version, all values stored within a Property must have the same data-type (integer, double, boolean, string…) and must 
have the same physical unit.  This change did not only reduce redundancy and in turn file size, but also reduced the 
chance that core attributes "unit", "uncertainty", "data type" and "reference" of values can be ambiguously defined or 
interpreted. For compatibility with the odML implementation in the NIX project, odML entities now contain a UUID 
(auto-generated unique identifier with extremely low collision probability) that uniquely identifies every single odML 
entity even across unrelated odML files.

2.1.4 Additional features:
On the side of the odML python library, we integrated an export to the RDF (Resource Description Framework) format 
opening odML to the semantic web. With this, the content of multiple odML files exported into the same graph can be can 
be easily searched using the established SPARQL query language. So far, the odML library used xml as a storage format. 
With the new version, XML is still the default storage format, but to support easy consumption through web-based services, 
metadata can now be stored in JSON and Yaml as well and be converted from one to the other formats. 

For easy visualization and manipulation of specific odML files, the groups from Jülich and the G-Node worked more 
closely together to integrate the odMLtables into the previously described odML graphical user interface. To facilitate 
the integration of the core odML library into odMLtables, the odML graphical user interface was removed from the core 
library and moved to its own project odml-ui (https://github.com/G-Node/odml-ui). odml-ui itself was updated to the new 
core odML version and now provides direct access points to the main odMLtables use case features making odml-ui and 
odMLtables even easier to use back to back leaving odml-ui as the file browsing and odMLtables as the file editing part.

2.1.5 Hierarchical Metadata in the odML format


[... original text continued]
The hierarchical odML structure is flexible and consists of three types of objects (Fig.~\ref{odMLstructure}):

Add data model comparison to paper figure 3?

