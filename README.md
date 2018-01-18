# Fast-Trips Tutorial

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/Fast-Trips/fast-trips-tutorial/master)


## Requirements

**Operating System:** This has been tested with Windows 10 and Mac OS Sierra (v10.12.3).  There is no reason that it wouldn't work on LINUX, but we have not pre-compiled the binaries so you will have to build from source.

**Memory:** Fast-Trips does use some RAM, so don't try and run full-scale regional transit demand without 48GB or similar.  This can be somewhat throttled by using the "chunking" feature.

**Software:** Requirements and setup instructions are discussed in the next section.  

**Prerequisites:** It is helpful to have a foundation in Python and understanding of the Pandas package.  

## Software Setup

This tutorial uses [Jupyter Notebooks](https://jupyter.readthedocs.io/en/latest/index.html) (formerly known as iPython Notebooks) to interactively run and explore Fast-trips.  This is not really a suitable solution for running a full-scale regional network, but it is useful for running these small examples and looking at the results interactively.

There are two main parts to setup for the tutorial:  

  * Installing Fast-Trips and other required software  
  * Downloading this tutorial repository with the tutorial and supporting data and scripts

### Required Software

This tutorial requires a a Python 2.7x setup with the following packages (and their respective supporting packages):  

  * [Jupyter Notebooks >=4.3.1](http://jupyter.org/) notebooks for controlling workflow and serving as the UI  
  * [Pandas v0.19.2](http://pandas.pydata.org/) for data wrangling  
  * [MatPlotLib](https://matplotlib.org/), [Seaborn](http://seaborn.pydata.org/) and [Bokeh v0.12.4](http://bokeh.pydata.org/en/latest/) for plotting results  
  * [Folium v0.2.1 - not v0.3!](https://github.com/python-visualization/folium) for mapping in leaflet  
  * [Fast-Trips](https://github.com/metropolitantransportationcommission/fast-trips) for the actual transit simulation 
  
If you are interested in installing a development version of Fast-Trips where you have the full GitHub repository and updates you make to the code are reflected in the tutorial, you should following the directions on the [Fast-Trips README](https://github.com/metropolitantransportationcommission/fast-trips).

### Installing Required Software + Fast-Trips into a Virtual Environment Using Anaconda (Recommended Method)

The easiest way to setup the all of this software is use virtual environments so as to not disturb any other Python installations you may have, but you can also choose to use `pip install <package name>` to install all of these packages [ although we haven't tested it in your environment to verify that it will work! ]

  1.  **Install Anaconda**  An easy way to use virtual environments is to download and install the [Anaconda package for Python 2.7](https://www.continuum.io/downloads).  

  2.  **Import Virtual Environment**  Once you have installed Anaconda, you can use the [Anaconda Navigator](https://docs.continuum.io/anaconda/navigator) to install a [virtual environment](https://conda.io/docs/using/envs.html).  Working within a virtual environment will ensure that you don't 'mess up' any other python installations on your computer with settings that are specific for Fast-Trips.  

The easiest way is to import the virtual environment `ft_environment.yml` that is included in this repository using Anaconda Navigator.

![Importing Virtual Environment](/img/anaconda-import-environment.png?raw=true "Importing a Virtual Environment")<!-- .element width="300px" -->

**Alternate Plan: Create Virtual Environment** If for some reason the virtual environment import doesn't work, you can create a new virtual environment and install the following packages on to it either [interactively via the GUI](https://docs.continuum.io/anaconda/navigator-tutorial#step-1-create-and-activate-a-new-environment-for-the-package-you-want-to-use) or by launching a terminal from the virtual environment and using `pip install` as shown below:

![Importing Virtual Environment](/img/terminal-open.png?raw=true "Opening a terminal from a virtual environment")<!-- .element width="300px" -->

```bash
pip install notebook
pip install pandas
pip install matplotlib
pip install seaborn
pip install bokeh==0.12.4
pip install folium==0.2.1
pip install fasttrips
```

### Downloading or Cloning Tutorial Repository

You can either download or clone this repository to run the tutorial on your own computer.  

If you have a [GitHub](https://github.com) account (free) and Git installed on your computer, please consider [`forking`](https://help.github.com/articles/fork-a-repo/) and then [`cloning`](https://help.github.com/articles/cloning-a-repository/) this repository so that you can save your updates and potentially submit them back to this main tutorial.  It makes things easier to have [GitHub Desktop](https://desktop.github.com/) installed, but this is optional.

If you want to download, you can just click the green `clone or download` button in the top-right of the main page for this repository and select `Download zip`.   Make sure and unzip the file and remember where you put it.  

## Starting the Tutorial  

The tutorial can be started by firing up a Jupyter notebook session in your browser from your virtual environment.  This will bring up a file manager.  

![Opening Notebook from Virtual Environment in Anaconda](/img/anaconda-open-notebook.png?raw=true "Opening Notebook from Virtual Environment in Anaconda")<!-- .element height="50%" width="50%" -->

Navigate to where wherever you downloaded or cloned this repository and click on `Tutorial #1` to start.  When you are done with this tutorial, you can select the next one, etc.

{
  width: 70%;
  border: none;
  background: none;
}
![Navigate to tutorial](/img/navigate-to-tutorial.png?raw=true "Navigate to Tutorial")<!-- .element height="50%" width="50%" -->

## Tutorial Contents

At this time, there are five completed [ or near complete ] lessons and several more planned ones.

  1. Exploring the input formats, running a simple scenario, and reviewing output   
  2. Capacity constraints, iterations, and adding new capacity  
  3. User classes  
  4. Building your own scenario from a GTFS feed
  5. Exploring trip-based-hyperpath parameters: overlap and dispersion 
  
There are an accompanying presentation and lecture notes that will be made available shortly.
