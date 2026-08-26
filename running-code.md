---
layout: page
title: 💻 Running Code
description: Instructions for running code in Math 124.
nav_order: 5
---

# 💻 Running Code
{:.no_toc}

{% include floating-toc.html %}

Many homework assignments and some labs will have an accompanying Jupyter Notebook. Jupyter Notebooks allow us to write and run code within a single document, while also including explanations, images, and interactive visualizations. You will learn more about them in Lab 1.

All of the code in this class will be written in Python, a popular language for engineering applications (and in general). This is not a class about Python – instead, we will use Python to further your understanding of linear algebra and how it is applied in engineering. Much of the code you will see in assignments will be provided by us, but we may ask you to write small pieces of code yourself. Code will **never** appear on quizzes or exams.

We will use [Google Colab](https://colab.research.google.com/) to run Jupyter Notebooks in this class. Google Colab is a freely-hosted service by Google that you can access from your web browser, so you do not need to install anything on your computer. You should sign in using your `@umich.edu` Google account.

---

## Opening a Notebook

Any lab or homework with a code component will include a **🪄 magic link 🪄** that opens its notebook directly in your browser. Let's walk through how to use that magic link. For this walkthrough, we will use Lab 1's notebook as an example, but the same steps apply for all notebooks (just with a different file name).

1. Click the magic link for the assignment. For labs, this link will appear directly on the course homepage, [math124.org](./); for homeworks, this will appear in the homework writeup under the corresponding problem.
1. Make sure that the top-right corner of your screen shows that you are logged into your `@umich.edu` account, not a personal Google account. You can switch accounts at this stage if need be, without needing to re-click the magic link.
1. Now, the notebook should be open. Think of the opened notebook as a template – it has all of the instructions we want to provide you with, but you still need to run the code and write some yourself too. Once the notebook opens in Google Colab and you are signed in with the correct account, click **Copy to Drive**. **This is the most important step:** it creates your own editable copy and prevents you from losing your work.
1. Rename the file from `Copy of lab01.ipynb` to `yourlastname-lab01.ipynb`, e.g. `rampure-lab01.ipynb`. (`.ipynb` is the file extension for Jupyter Notebooks.) Make sure to save the updated notebook.

Now, your renamed copy of the notebook is yours, and any changes you make will be saved there. This copied notebook will be saved in a folder in your Google Drive called `Colab Notebooks`. To open this folder, click `File > Locate in Drive` after renaming the notebook.

When you want to return to a notebook after you closed its window in your browser, **don't click on the magic link again** – this will lead you to the same template you started with, without any of your work. Instead, open the `Colab Notebooks` folder in your Google Drive and double click on the renamed notebook. This will bring you back to the version with your changes.

Tips:
1. Star the `Colab Notebooks` folder in your Drive to make it easier to find. To do this, once you've navigated to the `Colab Notebooks` folder, click the name of the folder, then `Organize > Add to starred`. Then, to open the `Colab Notebooks` folder moving forward, just open Google Drive, click `Starred` on the left side, and `Colab Notebooks` will be there for quick access.
1. **Save your notebooks frequently!** Don't rely on Colab's autosaving.


---

## Running Code in a Notebook

A **cell** is the basic building block of a Jupyter Notebook. Cells can contain either code or writing (called Markdown, which is a language for formatting text). Run a code cell by pressing the `Shift` and `Enter` keys on your keyboard at the same time (preferred), or by pressing the play button next to a cell.

One of the first cells in every notebook we provide will download the files and images needed for that assignment. Other early cells may import Python packages or perform additional setup. Run these cells in order from the top of the notebook and wait for each to finish.

The notebook remembers the results of cells you have already run during the current session, so the order in which you run cells matters! If you close the notebook or reconnect after being idle, it's a good idea to:
1. Click the triangle dropdown next to `Run all`, and click `Restart session`.
1. Manually re-run all of the cells in the notebook, starting with the first code cell and stopping at the point you are currently working on.

---

This page with Colab instructions is new. If anything is confusing or you have tips to share, let us know on Ed!