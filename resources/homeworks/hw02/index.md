---
layout: page
title: "Homework 2: Vector Arithmetic, Lengths, and the Dot Product"
description: "Homework 2: Vector Arithmetic, Lengths, and the Dot Product problems."
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
  align-items: baseline;
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
.main-content ol.assignment-enumeration {
  padding-left: 0;
  list-style: none;
}
.main-content ol.assignment-enumeration > li {
  display: grid;
  grid-template-columns: 2.5em minmax(0, 1fr);
  align-items: baseline;
  column-gap: 0.5em;
  padding-left: 0;
  margin: 0.8em 0;
}
.main-content ol.assignment-enumeration > li::before {
  content: none;
}
.assignment-enumeration-label {
  text-align: right;
}
.assignment-enumeration-content > :first-child {
  margin-top: 0;
}
.assignment-enumeration-content > :last-child {
  margin-bottom: 0;
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

# Homework 2: Vector Arithmetic, Lengths, and the Dot Product

**due** Monday, September 14th at 11:59PM

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw02/hw02.pdf" target="_blank">View as PDF ✏️</a>
</div>

{: .yellow }
<div markdown="1">
Write your solutions to the following problems either by writing them on a piece of paper or on a tablet and scanning your answers as a PDF. Note that you are not allowed to use LaTeX, Google Docs, or any other digital document creation software to type your answers. Homeworks are due to Pensive by 11:59PM on the due date. See the [syllabus](https://math124.org/syllabus/#homework) for details on the slip day policy.

Homework will be evaluated not only on the correctness of your answers, but on your ability to present your ideas clearly and logically. You should always explain and justify your conclusions, using sound reasoning. Your goal should be to convince the reader of your assertions. If a question does not require explanation, it will be explicitly stated.

Before proceeding, make sure you're familiar with the [collaboration policy](https://math124.org/syllabus/#collaboration-and-generative-ai-policy).
</div>

---

## Problems

- [Problem 1: Homework 1 Solutions Review](#problem-1-homework-1-solutions-review-8-pts)
- [Problem 2: Setting Ourselves Up](#problem-2-setting-ourselves-up-10-pts)
- [Problem 3: Add All Ingredients to the Bowl and Combine](#problem-3-add-all-ingredients-to-the-bowl-and-combine-8-pts)
- [Problem 4: *Norm*alize Doing Math 124!](#problem-4-normalize-doing-math-124-6-pts)
- [Problem 5: Displacement and Distance](#problem-5-displacement-and-distance-10-pts)
- [Problem 6: Dot Products, Angles, and Orthogonality](#problem-6-dot-products-angles-and-orthogonality-20-pts)
- [Problem 7: Distributing the Dots](#problem-7-distributing-the-dots-17-pts)
- [Problem 8: Triangle Inequality](#problem-8-triangle-inequality-6-pts)
- [Problem 9: Programming Activity](#problem-9-programming-activity-15-pts)

---

Total Points: 8 + 10 + 8 + 6 + 10 + 20 + 17 + 6 + 15 = 100

---

Note: While working on the homework, have Chapters [1.4](https://notes.math124.org/ch01/01-04/), [1.5](https://notes.math124.org/ch01/01-05/), and [1.6](https://notes.math124.org/ch01/01-06/) of the course notes open! They contain lots of relevant examples and explanations.

---

## Problem 1: Homework 1 Solutions Review (8 pts)

Review the solutions to Homework 1 (once they're posted). Pick **two problem parts** (for example, Problem 3a and Problem 5b) from Homework 1 in which your solutions have the most room for improvement, i.e., where they have unsound reasoning, could be significantly more efficient or clearer, etc. **Include a screenshot of your solution to each problem part**, and in a few sentences, explain what was deficient and how it could be fixed.

Alternatively, if you think one of your solutions is significantly better than the posted one, copy it here and explain why you think it is better. If you didn't do Homework 1, choose two problem parts from it that look challenging to you, and in a few sentences, explain the key ideas behind their solutions in your own words.

---

## Problem 2: Setting Ourselves Up (10 pts)

Given the following sets, translate the set notation into plain English and sketch a picture of what each set looks like in <span class="math-inline">\\(\mathbb{R}^2\\)</span> or <span class="math-inline">\\(\mathbb{R}^3\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(3 pts)
<span class="math-inline">\\(\lbrace{}\begin{bmatrix} x\\\\y \end{bmatrix} \in \mathbb{R}^2 : x &gt; 0, y &lt; 0\rbrace{}\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts)
<span class="math-inline">\\(\lbrace{}\begin{bmatrix} x\\\\y \end{bmatrix} \in \mathbb{R}^2 : x &lt; 0, y \geq 3\rbrace{}\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts)
<span class="math-inline">\\(\lbrace{}\begin{bmatrix} x\\\\y\\\\z \end{bmatrix} \in \mathbb{R}^3 : x, z \in \mathbb{R}, y = -5\rbrace{}\\)</span>

</div>
</div>

</div>

---

## Problem 3: Add All Ingredients to the Bowl and Combine (8 pts)

A cake recipe uses three ingredients: sugar, flour, and milk. We represent the ingredients in one batch by a vector in <span class="math-inline">\\(\mathbb{R}^3\\)</span>, using the order

<div class="math-display">
$$
\begin{bmatrix}
\text{sugar in tbsp}\\\\
\text{flour in cups}\\\\
\text{milk in tbsp}
\end{bmatrix}.
$$
</div>

 Consider the following four recipe batches:

-   Recipe 1 uses <span class="math-inline">\\(2\\)</span> tbsp of sugar, <span class="math-inline">\\(1\\)</span> cup of flour, and <span class="math-inline">\\(3\\)</span> tbsp of milk.

-   Recipe 2 uses <span class="math-inline">\\(3\\)</span> tbsp of sugar, <span class="math-inline">\\(2\\)</span> cups of flour, and <span class="math-inline">\\(4\\)</span> tbsp of milk.

-   Recipe 3 uses <span class="math-inline">\\(4\\)</span> tbsp of sugar, <span class="math-inline">\\(2\\)</span> cups of flour, and <span class="math-inline">\\(6\\)</span> tbsp of milk.

-   Recipe 4 uses <span class="math-inline">\\(1\\)</span> tbsp of sugar, <span class="math-inline">\\(1\\)</span> cup of flour, and <span class="math-inline">\\(2\\)</span> tbsp of milk.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Write vectors <span class="math-inline">\\(\vec{v}&#95;1,\vec{v}&#95;2,\vec{v}&#95;3,\vec{v}&#95;4\\)</span> representing the four recipes. Identify a relationship between two of the vectors and explain what that relationship means in the context of the recipes.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Suppose you make two batches of Recipe 1, no batches of Recipe 2, three batches of Recipe 3, and two batches of Recipe 4. Write a linear combination representing the total ingredients used. Then determine the total amount of sugar, flour, and milk used.

</div>
</div>

</div>

---

## Problem 4: *Norm*alize Doing Math 124! (6 pts)

The length, or norm, of a vector is denoted by <span class="math-inline">\\(\lVert \vec{v} \rVert\\)</span>. Consider the vector

<div class="math-display">
$$
\vec{v}=\begin{bmatrix}-5\\\\12\end{bmatrix}\in\mathbb{R}^2.
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Sketch <span class="math-inline">\\(\vec{v}\\)</span> in the coordinate plane.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Compute <span class="math-inline">\\(\lVert \vec{v} \rVert\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Find a unit vector (i.e. a vector of length one) pointing in the same direction as <span class="math-inline">\\(\vec{v}\\)</span>.

</div>
</div>

</div>

---

## Problem 5: Displacement and Distance (10 pts)

A drone begins at the point

<div class="math-display">
$$
P=(2,-1,4)
$$
</div>

 and flies in a straight line to the point

<div class="math-display">
$$
Q=(6,7,-4).
$$
</div>

 The coordinates here are in meters.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Let <span class="math-inline">\\(\vec{d}\\)</span> be the vector that describes the displacement from <span class="math-inline">\\(P\\)</span> to <span class="math-inline">\\(Q\\)</span>. Find <span class="math-inline">\\(\vec{d}\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Find the exact distance traveled by the drone.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) Suppose the drone continues to travel another 10 meters in the same direction. What are its coordinates?

</div>
</div>

</div>

---

## Problem 6: Dot Products, Angles, and Orthogonality (20 pts)

As discussed in [Chapter 1.6](https://notes.math124.org/ch01/01-06/), for nonzero vectors <span class="math-inline">\\(\vec{u},\vec{v}\in\mathbb{R}^n\\)</span>, the angle <span class="math-inline">\\(\theta\\)</span> between them satisfies

<div class="math-display">
$$
\cos\theta=\frac{\vec{u}\cdot\vec{v}}{\lVert \vec{u} \rVert\lVert \vec{v} \rVert}.
$$
</div>

 This ratio is called their **cosine similarity**: the dot product divided by the product of their lengths. To find the angle itself, take the inverse cosine of this ratio.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(9 pts) For each pair below, draw the vectors, compute their dot product, and find their cosine similarity (i.e. the cosine of the angle between them). In which case are the vectors orthogonal?

<ol class="assignment-enumeration" markdown="1">

<li markdown="1">
<div class="assignment-enumeration-label">(i)</div>
<div class="assignment-enumeration-content" markdown="1">

(3 pts) <span class="math-inline">\\(\vec{u}=\begin{bmatrix}-6\\\\3\end{bmatrix},\quad \vec{v}=\begin{bmatrix}1\\\\2\end{bmatrix}\\)</span>.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">(ii)</div>
<div class="assignment-enumeration-content" markdown="1">

(3 pts) <span class="math-inline">\\(\vec{u}=\begin{bmatrix}4\\\\1\end{bmatrix},\quad \vec{v}=\begin{bmatrix}4\\\\-1\end{bmatrix}\\)</span>.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">(iii)</div>
<div class="assignment-enumeration-content" markdown="1">

(3 pts) <span class="math-inline">\\(\vec{u}=\begin{bmatrix}3\\\\3\end{bmatrix},\quad \vec{v}=\begin{bmatrix}2\\\\2\end{bmatrix}\\)</span>.

</div></li>
</ol>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) For each pair below, find all values of <span class="math-inline">\\(k\\)</span> that make <span class="math-inline">\\(\vec{u}\\)</span> and <span class="math-inline">\\(\vec{v}\\)</span> orthogonal.

<ol class="assignment-enumeration" markdown="1">

<li markdown="1">
<div class="assignment-enumeration-label">(i)</div>
<div class="assignment-enumeration-content" markdown="1">

(3 pts) <span class="math-inline">\\(\vec{u}=\begin{bmatrix}k\\\\3\\\\-\frac12\end{bmatrix},\quad \vec{v}=\begin{bmatrix}-5\\\\-k\\\\\frac12\end{bmatrix}\\)</span>.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">(ii)</div>
<div class="assignment-enumeration-content" markdown="1">

(3 pts) <span class="math-inline">\\(\vec{u}=\begin{bmatrix}2k\\\\-4\\\\1\end{bmatrix},\quad \vec{v}=\begin{bmatrix}2k\\\\-2k\\\\0\end{bmatrix}\\)</span>.

</div></li>
</ol>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Use the cosine formula to explain why, for nonzero vectors <span class="math-inline">\\(\vec{u},\vec{v}\in\mathbb{R}^n\\)</span>,

<div class="math-display">
$$
|\vec{u}\cdot\vec{v}|\leq\lVert \vec{u} \rVert\lVert \vec{v} \rVert.
$$
</div>

 Explain why equality holds exactly when the vectors point in the same or opposite directions. Finally, explain why the inequality also holds if either vector is zero. This inequality is called the Cauchy--Schwarz inequality.

</div>
</div>

</div>

---

## Problem 7: Distributing the Dots (17 pts)

Let <span class="math-inline">\\(\vec{u},\vec{v}\in\mathbb{R}^n\\)</span> satisfy

<div class="math-display">
$$
\lVert \vec{u} \rVert=3,\qquad \lVert \vec{v} \rVert=2,\qquad
(3\vec{u}-4\vec{v})\cdot(\vec{u}+9\vec{v})=-71.
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find <span class="math-inline">\\(\vec{u}\cdot\vec{v}\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Find <span class="math-inline">\\(\lVert -2\vec{u} \rVert\\)</span> and <span class="math-inline">\\(\lVert 3\vec{v} \rVert\\)</span>. Explain why neither length is negative.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find the cosine similarity of <span class="math-inline">\\(\vec{u}\\)</span> and <span class="math-inline">\\(\vec{v}\\)</span>. Then find the cosine similarity of <span class="math-inline">\\(-2\vec{u}\\)</span> and <span class="math-inline">\\(3\vec{v}\\)</span>. If the two cosine similarities are different, why are they different?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Find <span class="math-inline">\\(\vec{u}\cdot\vec{u}\\)</span> and <span class="math-inline">\\(\vec{v}\cdot\vec{v}\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Find <span class="math-inline">\\(\lVert \vec{u}+\vec{v} \rVert\\)</span>. Is it equal to <span class="math-inline">\\(\sqrt{\lVert \vec{u} \rVert^2+\lVert \vec{v} \rVert^2}\\)</span>? Explain what condition would make these quantities equal.

<em>Hint: Start by writing <span class="math-inline">\\(\lVert\vec{u}+\vec{v}\rVert^2\\)</span> as <span class="math-inline">\\((\vec{u}+\vec{v})\cdot(\vec{u}+\vec{v})\\)</span>. Then, expand this as we did in <a href="https://notes.math124.org/ch01/01-06/#orthogonality-and-the-pythagorean-theorem">Chapter 1.6</a>.</em>

</div>
</div>

</div>

---

## Problem 8: Triangle Inequality (6 pts)

In [Chapter 1.5](https://notes.math124.org/ch01/01-05/#the-triangle-inequality), we stated the triangle inequality without proof. Intuitively, the triangle inequality says that for any triangle (even in <span class="math-inline">\\(\mathbb{R}^n\\)</span>), the length of any side of the triangle is less than or equal to the sum of the lengths of the other two sides. Here, we'll prove the triangle inequality using the Cauchy--Schwarz inequality, established in Problem 6c.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Let <span class="math-inline">\\(\vec{u},\vec{v}\\)</span> be any two vectors in <span class="math-inline">\\(\mathbb{R}^n\\)</span>. Show that

<div class="math-display">
$$
\lVert\vec{u}+\vec{v}\rVert^2\leq(\lVert\vec{u}\rVert+\lVert\vec{v}\rVert)^2.
$$
</div>

 <em>Hint: Start by following the same hint as in Problem 7e, then use the Cauchy--Schwarz inequality.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Why does the above imply that

<div class="math-display">
$$
\lVert\vec{u}+\vec{v}\rVert\leq\lVert\vec{u}\rVert+\lVert\vec{v}\rVert
$$
</div>

</div>
</div>

</div>

---

## Problem 9: Programming Activity (15 pts)

Most homeworks and some labs will have a Jupyter Notebook, containing Python code that supplements our understanding of the relevant mathematical ideas of the week.

To open the notebook for Homework 2, click [**this link**](https://colab.research.google.com/github/math-124/fa26-code/blob/main/homeworks/hw02/hw02.ipynb). Instructions on how to use Google Colab are at [math124.org/running-code](https://math124.org/running-code).

You won't need to submit the notebook anywhere. To get credit for the work you did in this notebook, include the following in your PDF submission to Homework 2 on Pensive, specifically under **Problem 9**:

<ol class="assignment-enumeration" markdown="1">

<li markdown="1">
<div class="assignment-enumeration-label">1.</div>
<div class="assignment-enumeration-content" markdown="1">

**Task 1:** A screenshot of your three word-count arrays and their output.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">2.</div>
<div class="assignment-enumeration-content" markdown="1">

**Task 2:** A screenshot of your completed cosine similarity function and the outputs of the three example calls.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">3.</div>
<div class="assignment-enumeration-content" markdown="1">

**Task 3:** A screenshot of the three document comparisons and your written answer identifying the most similar pair.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">4.</div>
<div class="assignment-enumeration-content" markdown="1">

**Task 4:** Your written responses to all three prompts.

</div></li>
</ol>

{% endraw %}
