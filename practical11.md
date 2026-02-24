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
   &nbsp;&nbsp;  
   &nbsp;&nbsp;
   ![](img/VSC_GHC1.png)
3. In the search bar, type "GitHub Copilot" and press Enter, and once you see
   the GitHub Copilot extension in the search results, click on the `Install`
   button.  
   &nbsp;&nbsp;  
   &nbsp;&nbsp;
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
   &nbsp;&nbsp;  
   &nbsp;&nbsp;
   ![](img/VSC_GHC3.png)
2. This will open a popup window in VS Code asking you about what option
   you want to use to sign in to your GitHub account. Click on
   `Continue with GitHub`.  
   &nbsp;&nbsp;  
   &nbsp;&nbsp;
   ![](img/VSC_GHC4.png)
3. This will open a new browser window where you will be asked to sign in to
   your GitHub account, if you have not done it yet, and then authorise VS
   Code to access your GitHub account. Click on `Continue`.  
   &nbsp;&nbsp;  
   &nbsp;&nbsp;
   ![](img/VSC_GHC5.png)
4. In the next web page, you will be asked to authorise VS Code to access your
   GitHub account. Click on `Authorise Visual Studio Code`.  
   &nbsp;&nbsp;  
   &nbsp;&nbsp;
   ![](img/VSC_GHC6.png)
5. Once you have authorised VS Code to access your GitHub account, you should
   see a message in the web page saying `VS Code is now authorised to access
   your GitHub account`. You can now close the web page and go back to VS Code,
   where you may be asked whether you trust the authors of the files in this
   workspace. Click on `Trust Workspace & Continue`.  
   &nbsp;&nbsp;  
   &nbsp;&nbsp;
   ![](img/VSC_GHC7.png)

# Start using GitHub Copilot

If you GitHub acccount is properly linked to VS Code, you should see a tiny
Copilot icon in the bottom right corner of the VS Code window. If this icon
is not visible or is crossed out, it means that GitHub Copilot is not properly
linked to your GitHub account. In such a case, go back to the previous section
and make sure you have properly linked your GitHub account to VS Code.

Sometimes, the extensions may be installed and your GitHub account properly
linked, but VS Code may ask you to either trust the current workspace/file that
you have opened, or to click a the popup window saying `Enable AI features`.

To start using GitHub Copilot, open a new file in VS Code called
`odd_even_numbers.py`, **in the `practical11` directory**, and type the
following two comment lines:

```
## write a program in Python that asks the user for an integer
## number and then prints out whether the number is odd or even.
```
As you type the second comment line, you should see a suggestion from GitHub
Copilot appearing in light grey text, like in the image below. While the
primary supported language for prompts and chatting with GitHub Copilot is
English, you can also use other languages, such as Catalan or Spanish, so
feel free to write the comments in any language you prefer.

![](img/VSC_GHC_odd_even1.png)

This suggestion is the code that GitHub Copilot thinks is the most likely to be
what you want to write based on the comments you have written and the context
of the file. To accept the suggestion, press the `Tab` key, and now save the
file and run it in the shell to see that it works as expected.

**Exercise**: Open in VS Code a new file called `perfect_numbers.py` in the
`practical10` directory and, using GitHub Copilot, write a Python program that
asks the user for an integer number and then prints out whether the number is a
perfect number or not. A perfect number is a positive integer that is equal to
the sum of its proper divisors, i.e., excluding itself from the sum. For
example, 6 is a perfect number because its positive divisors are 1, 2, and 3,
and their sum is 6. Once the program is ready, save the file and run it in the
shell to see that it works as expected.

# Modifying code with GitHub Copilot Chat

Open the Copilot Chat extension (clicking on the right of the
search text box) and ask GitHub Copilot to modify the `perfect_numbers.py`
program to take the input number from the command line instead of asking the
user for it, by typing the following prompt in the chat window:

```
modify this program to take the input number from the command line instead of
asking the user for it.
```
After some thinking, GitHub Copilot will suggest a modified version of the program,
and you can accept the suggestion by clicking on the `Allow` button shown in the
image below.

![](img/VSC_GHC_modify_perfect1.png)

GitHub Copilot will modify the program as you have asked, and will give you the
option to keep the modified code or undo the suggested edits. Click on the button
`Keep` shown in the image below.

![](img/VSC_GHC_modify_perfect2.png)

Now save the file, go to the Unix command line and verify that the modified program
works as expected by calling it as follows:

```
$ python perfect_numbers.py 6
```

# How to get explanations from GitHub Copilot

GitHub Copilot can also provide explanations for the code it suggests. For
instance, in the previous example, type in the Copilot Chat window the following
prompt, selecting the first option that appears in the dropdown menu as shown
in the image below.:

```
/explain the function is_perfect_number
```

![](img/VSC_GHC_explain_perfect.png)

# How to give context to GitHub Copilot

**Before we start this section, close all files you have opened in VS Code, and
close VS Code itself.**

To get suggestions from GitHub Copilot adapted to your needs, you should give it
context about what you want to do and how you want to do it. The first step to
enable GitHub Copilot to learn the context in which you want to work is to create
a directory specific for the project you want to work on, and then open that
directory with VS Code. For instance, let's say we want to learn how to write simple
programs in Python using only while and if statements, avoiding the use of the
`range()` function and the `+=` adding notation. Let's create a directory called
`my_first_python_programs` **outside** the `practical11` directory, and then open that directory with VS Code by typing on the shell:

```
$ code my_first_python_programs
```
VS Code will ask you whether you trust the authors of the files in this directory, and you should click on `Yes, I trust the authors` as shown in the image below.

![](img/VSC_GHC_context1.png)

Now, open the GitHub Copilot Chat extension and type the following prompt in
the chat window and press `Enter`.

```
/init help writing simple programs in Python to learn programming, using only
while and if statements, avoid using the range() function and the += adding
notation. Write code outside a function.
```

VS Code will start scanning the files in the directory, which is empty, and will
ask you whether it should scan other files in your system, click on `Skip` as shown in
the image below.

![](img/VSC_GHC_context2.png)

GitHub Copilot should have created a hidden directory called `.github`
with a Markdown file called `copilot-instructions.md` in it, and will ask you
whether you want to keep that file, click on `Keep` as shown in the image below.

![](img/VSC_GHC_context3.png)

Using the file explorer on the left, navigate to the file `copilot-instructions.md` and
open it to see the first draft of the instructions that GitHub Copilot has created for
you. You should see something similar to the image below.

![](img/VSC_GHC_context4.png)

To see how GitHub Copilot uses these instructions, create a new file called
`perfect_numbers.py` in the `my_first_python_programs` directory and type the
following comment line in it:

```
## write a Python program that asks the user to enter an integer number
## and prints out whether the number is perfect or not.
```
As you type the second comment line, you should see a suggestion from GitHub
Copilot appearing in light grey text, like in the image below, with a yellow
stars icon next to it, click on it and select the option `Fix` as shown in the
image below.

![](img/VSC_GHC_context5.png)

Finally, you should see that the code suggestion from GitHub Copilot has been
modified to adapt to the context you have given it, and now it uses only while and
if statements, and does not use the `range()` function or the `+=` adding notation, as shown in the image below. Click on the `Keep` button to keep the modified code.

![](img/VSC_GHC_context6.png)

**Exercise**: Create a new file called `prime_numbers.py` in the `my_first_python_programs`
directory and, using GitHub Copilot, write a Python program that takes a number from
the command line and prints out whether the number is prime or not.

**Exercise**: Create a new file called `relatively_primes.py` in the
`my_first_python_programs` directory and, using GitHub Copilot, write a Python
program that takes two numbers from the command line and prints out whether they
are relatively primes or not.

# Using GitHub Copilot with R and RStudio

In this [link](https://docs.posit.co/ide/user/ide/guide/tools/copilot.html)
you can find instructions on how to use GitHub Copilot with R and RStudio.
