# Ati Project

Information to understand challenges of ITA course

## Table of contents

- [Lab 1](#lab-1)
- [Lab 2](#lab-2)
- [Lab 3](#lab-3)
- [Lab 4](#lab-4)
- [Lab 5](#lab-5)
- [Lab 27](#lab-27)

## Lab1 <a name="lab-1"></a>

lab1

## Lab2 <a name="lab-2"></a>

Lab2

## Lab 27 <a name="lab-27"></a>

We have two Workflows. First with pull request to develop branch and the second one that comes from any merge to master.

In the first, the branches are created from develop, the dependencies associated with yarn and python pip are installed and then when we done work on the branch, run_pylint and run_pytest are execute and the branch is pushed to the remote repository and then create pull request.

In the second it is quite similar but with the difference that in the end it ends up performing a content deployment.

File of Workflow can be found [here](/.github/workflows/dev.yaml)
