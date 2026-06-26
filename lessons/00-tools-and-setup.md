# Setup Guide – Tools and Environment

> Complete this guide before your first hands-on coding session (**Lesson 3, Night 2**). In **Lesson 3**, we cover how data is structured — features, labels, preprocessing, and feature engineering. This guide sets up the tools you'll use to load, explore, and model that data in Python.

---

## What You'll Learn

By the end of this guide, students will be able to:

- Explain why **Python**, **Anaconda**, and **Jupyter Notebook** are used in this course.
- Install Anaconda and launch Jupyter Notebook on their machine.
- Verify that **NumPy**, **Pandas**, and **Scikit-learn** import correctly.
- Load a CSV in a notebook and explore it with `head()`, `describe()`, and `value_counts()`.
- Know where the bootcamp datasets and code live in this repository.

---

## The Core Tools

To build Machine Learning models, you need the right tools. In this course, **Python** is our programming language of choice, supported by a set of industry-standard libraries.

In **Lesson 1**, we previewed the data science toolkit. This guide walks through how to **install and run** that toolkit so you're ready to write code alongside the rest of the bootcamp.

---

### Python

Python is the most popular language for Data Science and Machine Learning. It is easy to read, easy to write, and has a massive ecosystem of pre-built tools for data manipulation and modeling.

---

### Anaconda

**Anaconda** is a free distribution of Python specifically geared towards data science. It comes with Python and the necessary libraries pre-installed, so you don't have to worry about complex dependency setups.

---

### Jupyter Notebook

**Jupyter Notebook** is a web-based interactive coding environment. Unlike traditional scripts where you run an entire file at once, Jupyter lets you run code in small **cells** one at a time. This makes it easy to experiment and see results immediately.

---

## Installation Guide

The easiest route for this course is to use Anaconda.

### Step 1: Download Anaconda

Head to the official Anaconda website and download the installer for your operating system:

- [anaconda.com/download](https://www.anaconda.com/download)

Choose the installer for **Windows**, **macOS**, or **Linux** as appropriate.

---

### Step 2: Install

Run the installer and follow the default prompts. No special configuration is required for this course.

---

### Step 3: Launch Anaconda Navigator

Once installation is complete, open the **Anaconda Navigator** application on your computer.

---

### Step 4: Open Jupyter Notebook

Inside Anaconda Navigator, find the **Jupyter Notebook** tile and click **Launch**. This opens a terminal window — **keep that window open** while you work. Jupyter will automatically open in your web browser.

> If you close the terminal, Jupyter stops running. Re-launch it from Anaconda Navigator when you need it again.

---

## Verify Your Setup

Create a new notebook in Jupyter and run this cell to confirm everything is installed:

```python
import numpy as np
import pandas as pd
import sklearn

print("NumPy:", np.__version__)
print("Pandas:", pd.__version__)
print("Scikit-learn:", sklearn.__version__)
print("Setup OK!")
```

If all three libraries print a version number and you see `Setup OK!`, your environment is ready.

---

## The Core Libraries

Almost every ML project in this bootcamp relies on three foundational Python libraries. Anaconda installs them automatically. Here is what each one does:

---

### NumPy (`numpy`)

**Numerical Python** — used for fast mathematical operations on large multi-dimensional arrays and matrices. Think of it as the core calculator for data science. Pandas and Scikit-learn both depend on NumPy under the hood.

---

### Pandas (`pandas`)

Your main tool for **data manipulation**. Use it to:

- Load datasets into tables (DataFrames)
- Clean and transform data
- Explore data with printed output

If you know Excel, think of Pandas as Excel on steroids. In this course you'll explore data using:

- `head()` — first few rows
- `describe()` — summary statistics
- `value_counts()` — count of each category
- `.corr()` — correlation between numeric columns

Plotting with **matplotlib** and **seaborn** appears in later lessons; for now, printed tables are enough to inspect your data.

---

### Scikit-learn (`sklearn`)

The gold-standard library for Machine Learning in Python. It contains pre-built algorithms for:

- **Classification** and **Regression** (supervised learning)
- **Clustering** (unsupervised learning)
- **Data preprocessing** (scaling, encoding, train/test split)

You don't have to write the complex math from scratch — Scikit-learn gives you ready-to-use implementations.

---

### Library Overview

| **Library**    | **Purpose**                                              |
| -------------- | -------------------------------------------------------- |
| `numpy`        | Numerical computing, arrays, math operations             |
| `pandas`       | Data manipulation and analysis (DataFrames)              |
| `scikit-learn` | Machine Learning models, preprocessing, and evaluation     |

---

## Your First Notebook

Let's get comfortable running code in Jupyter.

### Create a new notebook

In the Jupyter browser tab, click **New → Python 3 (ipykernel)**. This opens a blank notebook made up of **cells**.

---

### Run a cell

Type some code into the first cell, then press **Shift + Enter** to run it and move to the next cell:

```python
print("Hello, Jupyter!")

x = 5
y = 10
print(x + y)
```

The output appears directly below the cell. You can edit any cell and re-run it as many times as you like.

---

### Import the core libraries

Each library only needs to be imported once per notebook. Run this in a new cell:

```python
import numpy as np
import pandas as pd

data = {
    "name": ["Ali", "Sara", "Omar"],
    "age": [25, 30, 22],
}

df = pd.DataFrame(data)

print(df.head())
print(df.describe())
print(df["age"].mean())
```

Here you build a small table with Pandas, preview it with `head()`, get summary statistics with `describe()`, and compute a column average — the same tools you'll use on real datasets.

---

> **Tip:** Cells run in the order you execute them, not top to bottom. If results look strange, use **Kernel → Restart & Run All** to run every cell fresh from the top.

---

## Troubleshooting

- **Import errors** — Close Jupyter and re-launch it from Anaconda Navigator so it picks up the correct Python environment.
- **File not found** — When loading a file, make sure the path is relative to where you launched Jupyter, or use the full path.
- **Jupyter won't open in the browser** — Check that the terminal window from Anaconda Navigator is still open.

> **Alternative:** You can also use **VS Code** with the Jupyter extension instead of the browser interface. Anaconda remains the recommended way to install Python and the libraries for this course.

---

## Summary

- **Python** + **Anaconda** + **Jupyter Notebook** form the core environment for this bootcamp.
- Anaconda bundles **NumPy**, **Pandas**, and **Scikit-learn** — no manual library installs needed.
- Jupyter cells let you run code step by step (**Shift + Enter**) and see results immediately.
- Load and explore data with Pandas using `head()`, `describe()`, and `value_counts()`.
- After setup, continue **Lesson 3 (Night 2)** with [`code/data-processing.py`](../code/data-processing.py), then move on to **Lesson 4** for your first regression model.

---

*Setup guide — complete before Lesson 3 coding session*

---
