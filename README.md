# MP Workshop 2017
Assets for the Materials Project workshop on August 10-11, 2017 (and Python/Jupyter primer August 9) in Berkeley, CA.

To get the most out of the workshop, if you are rusty with programming skills or not fluent with programming in the Python language and not familiar with the Jupyter notebook environment for writing and running programs, we highly recommend attendance at our optional "Python/Jupyter primer" the day before the workshop, Wednesday, August 9th.

At the workshop, you can expect to gain competency in:

* Exploring MP's web interface to search for materials and properties, apply filters to searches, and use "apps" to gain insight into ensembles of materials (e.g. phase diagrams).

* Using the core primitives and modules of our open-source software package for materials analysis, pymatgen.

* Using our Application Programming Interface (API) to download data in order to do more flexible and complex analyses than those available through our website.

* Walking through case studies of using pymatgen tools to do analyses, especially using MP data via our API.

* Understanding how to use our growing library of workflow software (Atomate) to predict material properties by running multi-step calculations automatically.

* Walking through a couple detailed case studies for Atomate workflows.

* Contributing data to MP in a way that associates it with our library of compounds so that users can include data from external sources into their analysis.

# Exercises
Some additional exercise notebooks can be found at: https://jupyterhub.materialsproject.org/

# Agenda

Breakfast arrives on Thursday and Friday mornings at 09:00.

Wed morning -- Python/Jupyter primer (optional)
* 09:30-10:00 [Jupyter basics](python-primer/episodes/Introduction%20and%20Jupyter%20Use.ipynb); [Python variables and arithmetic](python-primer/episodes/Variables%20and%20built-in%20functions.ipynb)
* 10:00-10:15 [Built-in functions and libraries; getting help](python-primer/episodes/Variables%20and%20built-in%20functions.ipynb)
* 10:15-10:55 Control flow: [conditionals](python-primer/episodes/Conditionals.ipynb), [for loops](python-primer/episodes/For%20loops.ipynb)
* 10:55-11:10 (break)
* 11:10-11:50 Data structures: [lists](python-primer/episodes/Lists.ipynb) and [dictionaries](python-primer/episodes/Dictionaries.ipynb)
* 11:50-12:30 Data collection: [comprehensions](python-primer/episodes/Comprehensions.ipynb), [writing functions](python-primer/episodes/Writing%20Functions.ipynb)

Thu morning
* 09:30-09:45 [Intro](Intro_Persson.pdf)
* 09:45-11:00 [Web site - walk through apps and material detail pages](website/website_walkthrough.ipynb)
* 11:00-11:15 coffee break
* 11:15-12:30 [Pymatgen core use](pymatgen/core/pymatgen_core.ipynb) – going over useful functionality
* 12:30-13:30 lunch

Thu afternoon
* 13:30-13:45 catch-up/debugging
* 13:45-15:00 [API basics](API_use/api_use_2017.ipynb) - MPRester methods, query() syntax, mapidoc repo
* 15:00-15:15 coffee
* 15:15-16:30 Pymatgen adventures - [several](pymatgen/Thermochemistry.ipynb) [case](pymatgen/Electronic%20Structure.ipynb) [studies](pymatgen/Epitaxial%20Analysis.ipynb), including use of MP API

Fri morning
* 09:30-09:45 catch-up/debugging
* 09:45-11:00 [Software tools for calculating materials properties in high-throughput](Atomate/Intro_Session_Lecture.pdf)
* 11:00-11:15 coffee break
* 11:15-12:30 [Workflow](Atomate/Overview.ipynb) [walk](Atomate/ElectronicStructure.ipynb) [through](Atomate/ElasticTensor.ipynb)
* 12:30-13:30 lunch

Fri afternoon
* 13:30-13:45 catch-up/debugging
* 13:45-15:00 [Contributing data to MP](mpcontribs/mpcontribs.ipynb)
* 15:00-15:15 coffee
* 15:15-16:30 Integrative case studies based on participant feedback, including a MongoDB primer ([intro](mongo-primer/mongo-primer.pdf), [walkthrough](mongo-primer/mongo-primer.ipynb))

## Contributing

If you have push access to the repository, feel free to add assets / works in
progress to share here. The preferred format is *.ipynb for tutorial material.
For planning, feel free to examine/edit this
repository's [wiki](https://github.com/materialsproject/workshop-2017/wiki).
