# Fast-Trips Tutorial


## Software Setup

This tutorial uses iPython Jupyter Notebooks to interactively run and explore Fast-trips.  This is not really a suitable solution for running a full-scale regional network, but it is useful for running these small examples and looking at the results interactively.

The easiest way to setup the software is to download and install the [Anaconda package for Python 2.7](https://www.continuum.io/downloads).  

While Anaconda is downloading and installing, you can [clone or download](https://help.github.com/articles/cloning-a-repository/) this repository.  Cloning will maintain a link to this repository and allow you to seamlessly use any updates when they are published, but it requires that you install Git or [GitHub Desktop](https://desktop.github.com/).

You will also need to either clone or download [Fast-Trips](https://github.com/MetropolitanTransportationCommission/fast-trips) and follow its installation instructions.  Note that in the future we hope Fast-Trips is available as a pre-compiled binary.

Once you have installed Anaconda, you can use the [Anaconda Navigator](https://docs.continuum.io/anaconda/navigator) to install a [virtual environment](https://conda.io/docs/using/envs.html).  Working within a virtual environment will ensure that you don't 'mess up' any other python installations on your computer with settings that are specific for Fast-Trips.  The easiest way is to import the virtual environment `ft_environment.yml` that is included in this repository using Anaconda Navigator.

Finally, you will need to install your local verion of Fast-Trips into this virtual environment.  This is easiest to do using the command line via `conda` 
