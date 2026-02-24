---
layout: page
title: Practical 11
permalink: /practical11/
---

# Objectives

The learning objectives for this practical are:

  * Configure Visual Studio (VS) Code for AI pair programming with GitHub
    Copilot.
  * Learn using GitHub Copilot for AI pair programming.
  * Learn how to give context to GitHub Copilot to get better code
    suggestions.

# Setup and background

To do this practical you need an installation of the text editor VS Code, R and
RStudio. You can find the instructions in the [setup](/setup/) link
on how to install, VS Code, R and RStudio in your system. Make a
directory called `practical11` for this practical.

# Adding the GitHub Copilot extension to Visual Studio Code

To add the GitHub Copilot extension to VS Code, follow these steps:

1. Open VS Code.
2. Click on the Extensions icon in the left sidebar (or press `Ctrl+Shift+X`).
![](img/VSC_GHC1.png)
3. In the search bar, type "GitHub Copilot" and press Enter, and once you see
   the GitHub Copilot extension in the search results, click on the `Install`
   button.
![](img/VSC_GHC2.png)

This will install in fact two extensions, GitHub Copilot and GitHub Copilot
chat. The first one allows you to get in-line code suggestions as you type,
while the second one is a conversational AI assistant that allows you to have
a chat with GitHub Copilot to help you with your coding-specific tasks.

# Link your GitHub account to Visual Studio Code

Once the GitHub Copilot extension is installed, you need to authenticate your
GitHub account in VS Code. This will only work if your GitHub account has
access to GitHub Copilot. If you don't have access to GitHub Copilot, you can
request access as a student by following the instructions in this
[link](https://docs.github.com/en/education/about-github-education/github-education-for-students/apply-to-github-education-as-a-student).

To authorise VS Code to access your GitHub account, follow these steps:

1. Click on the GitHub Copilot icon in the bottom right corner of the VS Code
   window, and then click on `Sign in to use AI Features`.
![](img/VSC_GHC3.png)
2. This will open a popup window in VS Code asking you about what option
   you want to use to sign in to your GitHub account. Click on
   `Continue with GitHub`.
![](img/VSC_GHC4.png)
3. This will open a new browser window where you will be asked to sign in to
   your GitHub account, if you have not done it yet, and then authorise VS
   Code to access your GitHub account. Click on `Continue`.
![](img/VSC_GHC5.png)
4. In the web page, you will be asked to authorise VS Code to access your
   GitHub account. Click on `Authorise Visual Studio Code`.
![](img/VSC_GHC6.png)
5. Once you have authorised VS Code to access your GitHub account, you should
   see a message in the web page saying `VS Code is now authorised to access
   your GitHub account`. You can now close the web page and go back to VS Code,
   where you may be asked whether you trust the authors of the files in this
   workspace. Click on `Trust Workspace & Continue`.
![](img/VSC_GHC7.png)

# Start using GitHub Copilot

If you GitHub acccount is properly linked to VS Code, you should see a tiny
Copilot icon in the bottom right corner of the VS Code window. If this icon
is not visible or is crossed out, it means that GitHub Copilot is not properly
linked to your GitHub account. In such a case, go back to the previous section
and make sure you have properly linked your GitHub account to VS Code.

Sometimes, the extensions may be installed and your GitHub account properly linked,
but VS Code may ask you to either trust the current workspace/file that you have
opened, or to click on the popup window saying `Enable AI features`.

To start using GitHub Copilot, open a new file in VS Code called `odd_even_numbes.py`
and type the following two comment lines:

```
## write a program in Python that asks the user for an integer
## number and then prints out whether the number is odd or even.
```
As you type the second comment line, you should see a suggestion from GitHub Copilot
appearing in light grey text, like in the image below.

![](img/VSC_GHC_odd_even1.png)

This suggestion is the code that GitHub Copilot thinks is the most likely to be
what you want to write based on the comments you have written and the context
of the file.

To accept the suggestion, press the `Tab` key, and now save the file and run it
in the shell to see that it works as expected.

**Exercise**: Using GitHub Copilot, write a Python program that asks the user
for an integer number and then prints out whether the number is a perfect
number or not. A perfect number is a positive integer that is equal to the sum
of its proper divisors, i.e., excluding itself from the sum. For example, 6 is
a perfect number because its positive divisors are 1, 2, and 3, and their sum
is 6.

## How to get explanations from GitHub Copilot

Open a new file in VS Code called `prime_numbers.py` and type the
following comment line:

```
## write a program in Python that asks the user for an integer
## number and then prints out whether the number is prime or not.
```
As you type the second comment line, you should see a suggestion from GitHub
Copilot appearing in light grey text consisting of a single line of code,
press tab to accept it. A second line will be suggested, press tab to accept it,
and so on until you see two yellow stars appearing next to the one of the
suggested lines, as in the image below. Click on the yellow stars, and then click
on the option `Explain`.

![](img/VSC_GHC_prime1.png)

Try to understand the explanation given by GitHub Copilot and then accept the rest
of the suggested code. Run the program to see that it works as expected.
