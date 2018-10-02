
- If there is already a well defined data format that can be easily accessed and manipulated by a programming language - great. use it. don't add work unless you have too.
    e.g. Judi dataset nifti files -> can be opened, processed and analysed using e.g. the NiBabel python library.
- If there are any files that cannot be accessed by an existing library and are normal timeseries or other data, put them in nix and annotate them accordingly e.g. Judi dataset files Sub_xxx/*.txt -> they are not self explanatory since there is no format documentation. When putting it into a nix file, you can add metadata via section/properties and link them to the actual data. when doing analysis e.g. together with the nifit files, just access both if required and you can add the results to the same nix file as well.

- nix sections can be copied to another nix file to serve as templates 

- workshop: make a single piece of current data structure easier to understand for other people / future self



Workshop provide:
gin-cli for gin@home for RTGVenice


Workshop requirements for the students:

python3

virtualenv

(provide install scripts and example howtos)


Distribute required software packages

- Use a relocatable virtual environment where nixpy and odml are installed including all required packages.
- Additional can also contain odml-ui and odmltables





# Readme

# G-Node Workshop: Data and Metadata management

Workshop 4 will address two main fields of data management:
- how can experimental data be organised in projects and handled in collaborations
- what is metadata, why should anyone care about them and how can they be collected, organized and used

We want to try addressing these questions mainly through hands on sessions, ideally with YOUR data
so you get an immediate benefit. Either bring your data to the workshop or even better upload it 
with a short description to this PRIVATE repository so we can have a look at it and use your data 
to prepare our hands on sessions.

We will present the software we have developed at the G-Node: NIX and gin for data management
and odML for metadata handling.

For the hands on session we'll ask you to do some light python coding! You can either join up with someone
or use your own laptop. In this case please make sure you have Python3 and the following two packages installed:

    pip install nixio
    pip install python-odml

We are also happy to prepare an introduction to other solutions you might be interested in.

If that is the case or you have a general question, either [create an issue](https://web.gin.g-node.org/RTGVenice/GNodeWorkshop/issues/new) 
on this repository or just edit this readme and leave a note. You can easily edit and save the document online. 
Don't worry, everything is versioned, you cannot break anything.

---------------------------------------

### Questions and Suggestions

I would like you to talk about:
- How do I load Matlab files in Python
  

