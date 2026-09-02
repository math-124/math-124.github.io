---
layout: page
title: "Lab 1: Mathematical Foundations"
description: "Lab 1: Mathematical Foundations activities."
nav_exclude: true
hide_footer_hr: true
---

{% raw %}

<script>
window.MathJax = {
  tex: {inlineMath: [['$', '$'], ['\\(', '\\)']]},
  options: {ignoreHtmlClass: 'tex2jax_ignore'}
};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" async></script>

<style>
.main-content p {
  margin-bottom: 1.15em;
}
.assignment-pdf-button {
  font-size: 0.95rem;
  padding: 0.35rem 0.65rem;
}
.assignment-actions {
  align-items: center;
  display: flex;
  flex-wrap: wrap;
  gap: 0.55rem;
  margin: 0 0 1rem;
}
.math-display,
mjx-container[jax="CHTML"][display="true"] {
  max-width: 100%;
  overflow-x: auto;
  overflow-y: hidden;
}
.math-display {
  padding-bottom: 0.2rem;
}
.math-display mjx-container[jax="CHTML"][display="true"] {
  padding-bottom: 0.2rem;
}
.answer-blank {
  border-bottom: 1px solid currentColor;
  display: inline-block;
  min-width: 8rem;
  height: 1em;
  vertical-align: baseline;
}
.assignment-parts {
  margin: 1rem 0;
}
.assignment-part {
  column-gap: 0.55rem;
  display: grid;
  grid-template-columns: 1.4rem minmax(0, 1fr);
  margin-bottom: 1.05rem;
}
.assignment-part-label {
  font-weight: 600;
  text-align: right;
}
.assignment-part-content > :first-child {
  margin-top: 0;
}
.mc-options {
  display: flex;
  flex-wrap: wrap;
  gap: 0.9rem 1.6rem;
  margin: 0.9rem 0 1.1rem;
}
.mc-option {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  white-space: nowrap;
}
.mc-bubble,
.mc-square {
  display: inline-block;
  flex: 0 0 auto;
  height: 0.95em;
  width: 0.95em;
  vertical-align: -0.12em;
}
.mc-bubble {
  border: 1.5px solid currentColor;
  border-radius: 50%;
}
.mc-square {
  border: 1.5px solid currentColor;
}
.mc-correct {
  background: currentColor;
}
.main-content table {
  font-size: 0.9rem;
  width: auto;
  max-width: 100%;
}
.main-content table th,
.main-content table td {
  padding: 0.35rem 0.5rem;
  white-space: nowrap;
}
.crossnumber-grid {
  display: grid;
  grid-template-columns: repeat(3, 2.4rem);
  grid-template-rows: repeat(3, 2.4rem);
  margin: 1rem auto;
  width: max-content;
}
.crossnumber-cell {
  align-items: center;
  border: 1.5px solid currentColor;
  display: flex;
  font-size: 1.1rem;
  justify-content: center;
  position: relative;
}
.crossnumber-label {
  font-size: 0.55rem;
  left: 0.15rem;
  line-height: 1;
  position: absolute;
  top: 0.15rem;
}
.crossnumber-missing {
  border: 0;
}
</style>

# Lab 1: Mathematical Foundations

**due** by the end of your lab section on Wednesday, September 2nd, 2026

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab01/lab01.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab01/lab01-solutions.pdf" target="_blank">Solutions PDF ✅</a>
<a class="btn btn-info assignment-pdf-button colab-btn" href="https://colab.research.google.com/github/math-124/fa26-code/blob/main/labs/lab01/lab01.ipynb" target="_blank"><img src="/assets/site-images/google-colab.png" alt="" aria-hidden="true"> Google Colab</a>
</div>

{: .yellow }
<div markdown="1">
Welcome to the first lab of Math 124!

Each lab worksheet will contain several activities, most of which will involve writing math on paper, and some of which will involve running code in a Jupyter Notebook. Lab activities are meant to last an hour, and the second hour of lab is dedicated to starting the homework assignment. To receive credit for a lab, you must show your lab TA your work on both the lab worksheet and homework assignment.

While you must get checked off by your lab TA **individually**, we encourage you to form groups with 1-2 other students to complete the activities together.
</div>

---

## Activities

- [Activity 1: Hello World!](#activity-1-hello-world)
- [Activity 2: Sets and subsets](#activity-2-sets-and-subsets)
- [Activity 3: Mathematical Hygiene](#activity-3-mathematical-hygiene)
- [Activity 4: (Set)ting the Stage](#activity-4-setting-the-stage)
- [Activity 5: Parallel and Perpendicular Lines](#activity-5-parallel-and-perpendicular-lines)
- [Activity 6: Programming Activity](#activity-6-programming-activity)

---

## Activity 1: Hello World!

In this class and in labs, collaboration is key because together groups can accomplish much more than individuals can on their own.

First, introduce yourself to two people in the class and exchange contact information. Write down their names and contact information below.

Next, pair up with one or two other students and solve the following cross-number crossword puzzle, adapted from the [Berkeley Math Tournament 2023](https://berkeley.mt/resources/archives/bmmt-2023/puzzle-problems.pdf). Each spot in the grid should be filled with a digit from 0 to 9 using the clues below. Digits may be repeated.

<div class="crossnumber-grid" role="img" aria-label="Blank cross-number grid"> <div class="crossnumber-cell"><span class="crossnumber-label">A</span></div> <div class="crossnumber-cell"><span class="crossnumber-label">B</span></div> <div class="crossnumber-cell"><span class="crossnumber-label">C</span></div> <div class="crossnumber-cell"><span class="crossnumber-label">D</span></div> <div class="crossnumber-cell"></div> <div class="crossnumber-cell"></div> <div class="crossnumber-cell"><span class="crossnumber-label">E</span></div> <div class="crossnumber-cell"></div> <div class="crossnumber-cell crossnumber-missing"></div> </div>

<table>
<tbody>
<tr>
<td style="text-align: left;">A Across:</td>
<td style="text-align: left;">A number with only even digits, in strictly descending order (3)</td>
</tr>
<tr>
<td style="text-align: left;">D Across:</td>
<td style="text-align: left;">A number not divisible by 9 (3)</td>
</tr>
<tr>
<td style="text-align: left;">E Across:</td>
<td style="text-align: left;">A number divisible by 11 (2)</td>
</tr>
<tr>
<td style="text-align: left;">A Down:</td>
<td style="text-align: left;">A number with consecutive digits, in ascending order (3)</td>
</tr>
<tr>
<td style="text-align: left;">B Down:</td>
<td style="text-align: left;">A number where the product of the lesser-valued two digits</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">is equal to the largest digit (3)</td>
</tr>
<tr>
<td style="text-align: left;">C Down:</td>
<td style="text-align: left;">A prime number greater than 10 (2)</td>
</tr>
</tbody>
</table>

After you solve the puzzle, compare your thinking with the rest of your group. Write one insight that someone else in your group had that you did not think of.

<details markdown="1"><summary>Solution</summary>

The completed grid is

<div class="crossnumber-grid" role="img" aria-label="Completed cross-number grid"> <div class="crossnumber-cell"><span class="crossnumber-label">A</span>6</div> <div class="crossnumber-cell"><span class="crossnumber-label">B</span>4</div> <div class="crossnumber-cell"><span class="crossnumber-label">C</span>2</div> <div class="crossnumber-cell"><span class="crossnumber-label">D</span>7</div> <div class="crossnumber-cell">2</div> <div class="crossnumber-cell">3</div> <div class="crossnumber-cell"><span class="crossnumber-label">E</span>8</div> <div class="crossnumber-cell">8</div> <div class="crossnumber-cell crossnumber-missing"></div> </div>

The written insight will vary. See a walkthrough of the puzzle solution on [page 75 of this PDF](https://berkeley.mt/resources/archives/bmmt-2023/puzzle-solutions.pdf#page=75).
</details>

**Overview: Sets and set-builder notation**

<em>The material here is a summary of <a href="https://notes.math124.org/ch01/01-02/">Chapter 1.2</a> of the course notes.</em>

A **set** is a well-defined collection of distinct objects. For example,

<div class="math-display">
$$
A=\{2,4,6,8\}
$$
</div>

 is the set of even numbers between <span class="math-inline">\\(2\\)</span> and <span class="math-inline">\\(8\\)</span>. The numbers <span class="math-inline">\\(2\\)</span>, <span class="math-inline">\\(4\\)</span>, <span class="math-inline">\\(6\\)</span>, and <span class="math-inline">\\(8\\)</span> are the **elements** of <span class="math-inline">\\(A\\)</span>. We write <span class="math-inline">\\(2\in A\\)</span> and <span class="math-inline">\\(3\notin A\\)</span>. Sets do not contain duplicates, so <span class="math-inline">\\(\lbrace{}2, 2, 4, 6, 6\rbrace{}\\)</span> is not a valid set. Sets do not keep track of order, so

<div class="math-display">
$$
\{2,4,6\}=\{6,4,2\}.
$$
</div>

**Set-builder notation** describes a set by stating a rule that all of its elements follow. Its general form is

<div class="math-display">
$$
\{\text{what goes in the set}:\text{condition}\}.
$$
</div>

 For example, if <span class="math-inline">\\(A=\lbrace{}2,4,6,8\rbrace{}\\)</span>, then the set <span class="math-inline">\\(C = \lbrace{}6, 12, 18, 24\rbrace{}\\)</span> can be described as

<div class="math-display">
$$
C = \{3x:x\in A\}.
$$
</div>

More examples:

<ol class="assignment-enumeration" markdown="1">

<li markdown="1">

<span class="math-inline">\\(\lbrace{}x: x \in C, x &gt; 10\rbrace{}\\)</span> is the set of elements of <span class="math-inline">\\(C\\)</span> that are greater than <span class="math-inline">\\(10\\)</span>.

</li>
<li markdown="1">

<span class="math-inline">\\(\lbrace{}10, 20, 30, ..., 100\rbrace{}\\)</span> can be expressed in set-builder notation as

<div class="math-display">
$$
\{10x: x \in \mathbb{Z}, 1 \leq x \leq 10 \}.
$$
</div>

 <span class="math-inline">\\(\mathbb{Z}\\)</span> is the set of all **integers**.

</li>
<li markdown="1">

<span class="math-inline">\\(\lbrace{}x: x \in \mathbb{Z}, x \geq 0\rbrace{}\\)</span> is the set of all non-negative integers.

</li>
<li markdown="1">

<span class="math-inline">\\(\lbrace{}(x, y): x^2 + y^2 = 16, x \in \mathbb{R}, y \in \mathbb{R} \rbrace{}\\)</span> is the set of all points on the circle with radius <span class="math-inline">\\(4\\)</span> centered at <span class="math-inline">\\((0, 0)\\)</span>. <span class="math-inline">\\(\mathbb{R}\\)</span> refers to the set of **real numbers**.

</li>
</ol>

In many of these examples, the item before the colon <span class="math-inline">\\(:\\)</span> was simply <span class="math-inline">\\(x\\)</span>, and following the colon were multiple conditions on <span class="math-inline">\\(x\\)</span>, one of which was the set we were selecting elements from to create our new set (e.g. <span class="math-inline">\\(C\\)</span>, <span class="math-inline">\\(\mathbb{Z}\\)</span>, or <span class="math-inline">\\(\mathbb{R}\\)</span>). There is a shorter notation that is often used for sets like these:

-   <span class="math-inline">\\(\lbrace{}x : x \in C,\ x &gt; 10\rbrace{}\\)</span> can be shortened to <span class="math-inline">\\(\lbrace{}x \in C : x &gt; 10\rbrace{}\\)</span>.

-   <span class="math-inline">\\(\lbrace{}x : x \in \mathbb{Z},\ x \geq 0\rbrace{}\\)</span> can be shortened to <span class="math-inline">\\(\lbrace{}x \in \mathbb{Z} : x \geq 0\rbrace{}\\)</span>.

In general, the two forms you'll see are:

<div class="math-display">
$$
\{f(x): \text{conditions on } x \}
$$
</div>



<div class="math-display">
$$
\{x \in S: \text{conditions on } x\}
$$
</div>

---

## Activity 2: Sets and subsets

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Write the set <span class="math-inline">\\(\lbrace{}k\in\mathbb{Z}:|k+1|&lt;5\rbrace{}\\)</span> using enumerative notation.

<details markdown="1"><summary>Solution</summary>

The set <span class="math-inline">\\(\lbrace{}k\in\mathbb{Z}:|k+1|&lt;5\rbrace{}\\)</span> in enumerative notation is

<div class="math-display">
$$
\{-5,-4,-3,\ldots,3\}.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Write the set <span class="math-inline">\\(\lbrace{}2,5,10,17,26,37,\ldots\rbrace{}\\)</span> using set-builder notation. Try doing so in at least two different ways, each using a different formula before the colon.

<details markdown="1"><summary>Solution</summary>

One way to write the set is

<div class="math-display">
$$
\{x^2+1:x\in\mathbb{Z},x\geq 1\}.
$$
</div>

 Two other forms are

<div class="math-display">
$$
\{(x-1)^2+1:x\in\mathbb{Z},x\geq 2\}
\quad\text{and}\quad
\{(x+1)^2+1:x\in\mathbb{Z},x\geq 0\}.
$$
</div>

</details>

A set <span class="math-inline">\\(B\\)</span> is a **subset** of a set <span class="math-inline">\\(A\\)</span> if every element of <span class="math-inline">\\(B\\)</span> is also an element of <span class="math-inline">\\(A\\)</span>, written <span class="math-inline">\\(B\subseteq A\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Let <span class="math-inline">\\(A=\lbrace{}x\in\mathbb{Z}:x&gt;2\rbrace{}\\)</span> and <span class="math-inline">\\(B=\lbrace{}x\in\mathbb{Z}:x&gt;6\rbrace{}\\)</span>. Is <span class="math-inline">\\(A\subseteq B\\)</span>? Is <span class="math-inline">\\(B\subseteq A\\)</span>? Both? Neither?

<details markdown="1"><summary>Solution</summary>

In enumerative notation,

<div class="math-display">
$$
A=\{3,4,5,6,7,8,9,10,\ldots\},
\qquad
B=\{7,8,9,10,\ldots\}.
$$
</div>

 Every element in <span class="math-inline">\\(B\\)</span> is also in <span class="math-inline">\\(A\\)</span>, so <span class="math-inline">\\(B\subseteq A\\)</span>. The opposite is not true: <span class="math-inline">\\(3\in A\\)</span> but <span class="math-inline">\\(3\notin B\\)</span>, so <span class="math-inline">\\(A\\)</span> is not a subset of <span class="math-inline">\\(B\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
Let <span class="math-inline">\\(C=\lbrace{}x\in\mathbb{R}:x^2&gt;4\rbrace{}\\)</span> and <span class="math-inline">\\(D=\lbrace{}x\in\mathbb{R}:x&gt;2\rbrace{}\\)</span>. Explain why it is **not true** that <span class="math-inline">\\(C\subseteq D\\)</span> by finding one element in <span class="math-inline">\\(C\\)</span> that is not in <span class="math-inline">\\(D\\)</span>.

<details markdown="1"><summary>Solution</summary>

The set <span class="math-inline">\\(C\\)</span> includes negative numbers such as <span class="math-inline">\\(-3\\)</span>, since <span class="math-inline">\\((-3)^2&gt;4\\)</span>. But <span class="math-inline">\\(-3\notin D\\)</span>, so <span class="math-inline">\\(C\\)</span> cannot be a subset of <span class="math-inline">\\(D\\)</span>.
</details>

</div>
</div>

</div>

---

## Activity 3: Mathematical Hygiene

One of the main learning objectives in this course is to develop proper mathematical **hygiene** --- that is, writing clear solutions using proper mathematical grammar and correctly stating assumptions.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
The "proof" below shows that <span class="math-inline">\\(0 = 1\\)</span>.

<table>
<tbody>
<tr>
<td style="text-align: right;"><span style="color: gray">1</span></td>
<td style="text-align: left;">Suppose <span class="math-inline">\(a=b\)</span>. Then,</td>
</tr>
<tr>
<td style="text-align: right;"><span style="color: gray">2</span></td>
<td style="text-align: left;"><span class="math-inline">\(a^2=ab\)</span></td>
</tr>
<tr>
<td style="text-align: right;"><span style="color: gray">3</span></td>
<td style="text-align: left;"><span class="math-inline">\(a^2-b^2=ab-b^2\)</span></td>
</tr>
<tr>
<td style="text-align: right;"><span style="color: gray">4</span></td>
<td style="text-align: left;"><span class="math-inline">\((a-b)(a+b)=b(a-b)\)</span></td>
</tr>
<tr>
<td style="text-align: right;"><span style="color: gray">5</span></td>
<td style="text-align: left;"><span class="math-inline">\(a+b=b\)</span></td>
</tr>
<tr>
<td style="text-align: right;"><span style="color: gray">6</span></td>
<td style="text-align: left;"><span class="math-inline">\(2b=b\)</span></td>
</tr>
<tr>
<td style="text-align: right;"><span style="color: gray">7</span></td>
<td style="text-align: left;"><span class="math-inline">\(2=1\)</span></td>
</tr>
<tr>
<td style="text-align: right;"><span style="color: gray">8</span></td>
<td style="text-align: left;"><span class="math-inline">\(1=0\)</span></td>
</tr>
</tbody>
</table>

Identify the line on which a mistake is first made and explain what the mistake is.

<details markdown="1"><summary>Solution</summary>

The error is in going from line 4 to line 5: we cannot divide by <span class="math-inline">\\(a-b\\)</span>, because it is <span class="math-inline">\\(0\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Express the set of solutions <span class="math-inline">\\(x\\)</span> to the inequality below in set-builder notation.

<div class="math-display">
$$
\frac{-3x+2}{7}\le 5
$$
</div>

<details markdown="1"><summary>Solution</summary>

Solving the inequality step by step,

<div class="math-display">
$$
\begin{align*}
\frac{-3x+2}{7} &\le 5 \\\\
-3x+2 &\le 35 && \text{(multiply both sides by 7)} \\\\
-3x &\le 33 && \text{(subtract 2 from both sides)} \\\\
x &\ge -11 && \text{(divide by -3 and reverse the inequality).}
\end{align*}
$$
</div>

Therefore, in set-builder notation, the solution set is

<div class="math-display">
$$
\{x\in\mathbb{R}: x\ge -11\}.
$$
</div>

</details>

</div>
</div>

</div>

---

## Activity 4: (Set)ting the Stage

Find the equation of the line below. Then, describe the set of all points <span class="math-inline">\\((x, y)\\)</span> that satisfy the equation in set-builder notation.

<div style="text-align: center;">
<img src="imgs/activity4-line.png" alt="image" style="width: 65%; max-width: 100%;">
</div>

<details markdown="1"><summary>Solution</summary>

The line has slope <span class="math-inline">\\(-\frac12\\)</span> and passes through the origin, so its equation is <span class="math-inline">\\(y=-\frac12x\\)</span>. In set-builder notation, the solution set is <span class="math-inline">\\(\lbrace{}(x,y)\in\mathbb{R}^2: y=-\frac12x\rbrace{}\\)</span>.
</details>

---

## Activity 5: Parallel and Perpendicular Lines

Consider the line

<div class="math-display">
$$
5x-4y=12.
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Plot the line on the axes below.

<div style="text-align: center;">
<img src="imgs/activity5-blank-axes.png" alt="image" style="height: 14.17rem; width: auto; max-width: 100%;">
</div>

<details markdown="1"><summary>Solution</summary>

<div style="text-align: center;">
<img src="imgs/activity5-solution.png" alt="image" style="height: 14.17rem; width: auto; max-width: 100%;">
</div>

The line has slope <span class="math-inline">\\(\frac54\\)</span> and <span class="math-inline">\\(y\\)</span>-intercept <span class="math-inline">\\(-3\\)</span>. It passes through <span class="math-inline">\\((0,-3)\\)</span> and <span class="math-inline">\\((4,2)\\)</span>, for example.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Find an equation for a line that is parallel to this line.

<details markdown="1"><summary>Solution</summary>

Parallel lines have the same slope. Any line of the form <span class="math-inline">\\(5x-4y=c\\)</span> with <span class="math-inline">\\(c\neq 12\\)</span> works. For example,

<div class="math-display">
$$
5x-4y=20.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Find an equation for a line that is perpendicular to this line.

<details markdown="1"><summary>Solution</summary>

Perpendicular lines have slopes that are the negative reciprocals of each other. Thus, any line of the form <span class="math-inline">\\(4x+5y=c\\)</span> is perpendicular. For example,

<div class="math-display">
$$
4x+5y=10.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
Find the point where this line intersects with the line

<div class="math-display">
$$
y=x-2.
$$
</div>

<details markdown="1"><summary>Solution</summary>

Rewrite the first line as <span class="math-inline">\\(y=\frac54x-3\\)</span> and set the two expressions for <span class="math-inline">\\(y\\)</span> equal to each other. Solving gives <span class="math-inline">\\(x=4\\)</span> and <span class="math-inline">\\(y=2\\)</span>, so the intersection point is

<div class="math-display">
$$
(4,2).
$$
</div>

</details>

</div>
</div>

</div>

---

## Activity 6: Programming Activity

Most homeworks and some labs will have a Jupyter Notebook, containing Python code that supplements our understanding of the relevant mathematical ideas of the week.

To open the notebook for Lab 1, click the Google Colab link under "Code" on the course website for Lab 1. Instructions on how to use Google Colab are at [math124.org/running-code](https://math124.org/running-code). If you are viewing the lab worksheet after it has been posted, [this](https://colab.research.google.com/github/math-124/fa26-code/blob/main/labs/lab01/lab01.ipynb) direct link will work, too.

To receive credit for the programming component of the lab, work through the entire notebook and show your lab TA the graph you create at the very bottom, with your name in it.

{% endraw %}
