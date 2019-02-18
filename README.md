[![Build Status](https://travis-ci.org/Esme-Sudria-Database/lab-spark.svg?branch=master)](https://travis-ci.org/Esme-Sudria-Database/lab-spark)

This repository contains scripts to create a virtual machine to experiments on spark.

General information
===================

* [website](esme.farcellier.com)
* [public chat](https://gitter.im/esme-farcellier-com)

Requirement 1 : installation to perform on your computer
========================================================

3 softwares are required on your computer :

* [Virtual box](https://www.virtualbox.org/)
* [Vagrant](https://www.vagrantup.com/)
* [Git](https://git-scm.com/)

On linux
---------

```
sudo apt-get install git
```

I recommand to setup the last version of vagrant and virtualbox from their website

* [Vagrant](https://www.vagrantup.com/)
* [Virtual box](https://www.virtualbox.org/)

On windows
-----------

Download and install the 3 softwares above.

On mac
-------

```
brew install git
```

Install by hand :

* [Vagrant](https://www.vagrantup.com/)
* [Virtual box](https://www.virtualbox.org/)

Step 1 : install the environment
================================

1. clone this repository :

```
git clone https://github.com/Esme-Sudria-Database/lab-spark.git
```

To create the virtual machine, use the command

    cd lab-spark
    vagrant up

This script will use image from ubuntu 18.04. Ansible will pull spark ans install on it.

Resources
=========

the lab use implementations from [Advanced Analytics with Spark](https://github.com/sryza/aas), by Sandy Ryza, Uri Laserson, Sean Owen, and Josh Wills.
