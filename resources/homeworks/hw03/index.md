---
layout: page
title: "Homework 3: Lines, Orthogonality, and Projections in $\\mathbb{R}^2$"
description: "Homework 3: Lines, Orthogonality, and Projections in $\\mathbb{R}^2$ problems."
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
.assignment-vector-plot {
  max-width: 100%;
  height: auto;
  display: block;
  margin: 1rem auto;
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

# Homework 3: Lines, Orthogonality, and Projections in $\mathbb{R}^2$

**due** Monday, September 21st at 11:59PM

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw03/hw03.pdf" target="_blank">View as PDF ✏️</a>
</div>

{: .yellow }
<div markdown="1">
Write your solutions to the following problems either by writing them on a piece of paper or on a tablet and scanning your answers as a PDF. Note that you are not allowed to use LaTeX, Google Docs, or any other digital document creation software to type your answers. Homeworks are due to Pensive by 11:59PM on the due date. See the [syllabus](https://math124.org/syllabus/#homework) for details on the slip day policy.

Homework will be evaluated not only on the correctness of your answers, but on your ability to present your ideas clearly and logically. You should always explain and justify your conclusions, using sound reasoning. Your goal should be to convince the reader of your assertions. If a question does not require explanation, it will be explicitly stated.

Before proceeding, make sure you're familiar with the [collaboration policy](https://math124.org/syllabus/#collaboration-and-generative-ai-policy).
</div>

---

## Problems

- [Problem 1: Feedback](#problem-1-feedback-5-pts)
- [Problem 2: Line Dancing](#problem-2-line-dancing-15-pts)
- [Problem 3: Perfectly Normal](#problem-3-perfectly-normal-12-pts)
- [Problem 4: Covering All the Bases](#problem-4-covering-all-the-bases-24-pts)
- [Problem 5: Projecting Confidence](#problem-5-projecting-confidence-17-pts)
- [Problem 6: May the Force Be with Blue](#problem-6-may-the-force-be-with-blue-12-pts)
- [Problem 7: Programming Activity](#problem-7-programming-activity-15-pts)

---

Total Points: <span class="math-inline">\\(5 + 15 + 12 + 24 + 17 + 12 + 15 = 100\\)</span>

---

## Problem 1: Feedback (5 pts)

We'd like to get your feedback on how the course has been going so far!

You will find a survey [**at this link**](https://forms.gle/XrBKnzrFPDaxsfEB7). It is **not anonymous** --- we need to know your identity to give you homework credit for it, and so that you can give us feedback that we can reply to (if you'd like).

**Please fill out the survey AFTER you've finished the rest of Homework 3.** When submitting to Pensive, it does not matter which page of your submission you assign to Problem 1; we will enter survey completion credit in manually.

Thank you for your feedback --- it's helping shape our brand-new course.

---

## Problem 2: Line Dancing (15 pts)

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) The line <span class="math-inline">\\(\ell\\)</span> shown below passes through the origin. Find a nonzero vector <span class="math-inline">\\(\vec{v}\\)</span> lying on <span class="math-inline">\\(\ell\\)</span>. Use this vector to express <span class="math-inline">\\(\ell\\)</span> in parametric form, as we did in [Chapter 2.1](https://notes.math124.org/ch02/02-01/#affine-lines).

<div style="text-align: center;">
<img src="imgs/hw03-plot-01.png" alt="Coordinate diagram" class="assignment-vector-plot">
</div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(10 pts) The affine line <span class="math-inline">\\(\ell'\\)</span> shown below is parallel to <span class="math-inline">\\(\ell\\)</span>.

<div style="text-align: center;">
<img src="imgs/hw03-plot-02.png" alt="Coordinate diagram" class="assignment-vector-plot">
</div>

<ol class="assignment-enumeration" markdown="1">

<li markdown="1">
<div class="assignment-enumeration-label">i.</div>
<div class="assignment-enumeration-content" markdown="1">

(5 pts) Find a vector <span class="math-inline">\\(\vec{v}&#95;0\\)</span> whose endpoint lies on <span class="math-inline">\\(\ell'\\)</span>. Use <span class="math-inline">\\(\vec{v}&#95;0\\)</span> and your vector <span class="math-inline">\\(\vec{v}\\)</span> from part (a) to express <span class="math-inline">\\(\ell'\\)</span> in parametric form.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">ii.</div>
<div class="assignment-enumeration-content" markdown="1">

(5 pts) Give a different choice of <span class="math-inline">\\(\vec{v}&#95;0\\)</span> and <span class="math-inline">\\(\vec{v}\\)</span> that also works. Use these vectors to express <span class="math-inline">\\(\ell'\\)</span> in parametric form.

</div></li>
</ol>

</div>
</div>

</div>

---

## Problem 3: Perfectly Normal (12 pts)

Let <span class="math-inline">\\(\ell\\)</span> and <span class="math-inline">\\(\ell'\\)</span> be the lines from Problem 2.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) First, let's work with <span class="math-inline">\\(\ell\\)</span>, the line through the origin.

<ol class="assignment-enumeration" markdown="1">

<li markdown="1">
<div class="assignment-enumeration-label">(i)</div>
<div class="assignment-enumeration-content" markdown="1">

Find a nonzero vector <span class="math-inline">\\(\vec{w}\\)</span> that is normal to <span class="math-inline">\\(\ell\\)</span>; that is, <span class="math-inline">\\(\vec{w}\\)</span> lies on <span class="math-inline">\\(\ell^\perp\\)</span> (the line through the origin that is perpendicular to <span class="math-inline">\\(\ell\\)</span>).

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">(ii)</div>
<div class="assignment-enumeration-content" markdown="1">

Use <span class="math-inline">\\(\vec{w}\\)</span> to express <span class="math-inline">\\(\ell\\)</span> as an equation in dot-product form.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">(iii)</div>
<div class="assignment-enumeration-content" markdown="1">

Finally, express <span class="math-inline">\\(\ell\\)</span> as a linear equation in terms of <span class="math-inline">\\(x\\)</span> and <span class="math-inline">\\(y\\)</span> (with no vectors).

</div></li>
</ol>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) Now, let's work with <span class="math-inline">\\(\ell'\\)</span>, the affine line.

<ol class="assignment-enumeration" markdown="1">

<li markdown="1">
<div class="assignment-enumeration-label">(i)</div>
<div class="assignment-enumeration-content" markdown="1">

Use <span class="math-inline">\\(\vec{w}\\)</span> and <span class="math-inline">\\(\vec{v}&#95;0\\)</span> to express <span class="math-inline">\\(\ell'\\)</span> as an equation in dot-product form.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">(ii)</div>
<div class="assignment-enumeration-content" markdown="1">

Express <span class="math-inline">\\(\ell'\\)</span> as a linear equation in terms of <span class="math-inline">\\(x\\)</span> and <span class="math-inline">\\(y\\)</span> (with no vectors).

</div></li>
</ol>

</div>
</div>

</div>

---

## Problem 4: Covering All the Bases (24 pts)

For each pair of vectors <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> below,

<ol class="assignment-enumeration" markdown="1">

<li markdown="1">
<div class="assignment-enumeration-label">(i)</div>
<div class="assignment-enumeration-content" markdown="1">

Determine whether it is an orthonormal basis of <span class="math-inline">\\(\mathbb{R}^2\\)</span>, and explain why or why not.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">(ii)</div>
<div class="assignment-enumeration-content" markdown="1">

If it is an orthonormal basis, write

<div class="math-display">
$$
\vec{w}=\begin{bmatrix}7\\-4\end{bmatrix}
$$
</div>

 as a linear combination of <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>, i.e. find scalars <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> such that

<div class="math-display">
$$
a \vec u + b \vec v = \vec w.
$$
</div>

</div></li>
</ol>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(6 pts)
<span class="math-inline">\\(\displaystyle \quad \vec{u} = \begin{bmatrix} \frac35\\\\[2pt] \frac45 \end{bmatrix}, \quad \vec{v} = \begin{bmatrix} \frac45\\\\[2pt] \frac35 \end{bmatrix}\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(6 pts)
<span class="math-inline">\\(\displaystyle \quad \vec{u} = \begin{bmatrix} 1\\\\ -2 \end{bmatrix}, \quad \vec{v} = \begin{bmatrix} 2\\\\ 1 \end{bmatrix}\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(6 pts)
<span class="math-inline">\\(\displaystyle \quad \vec{u} = \begin{bmatrix} \frac{5}{13}\\\\[2pt] \frac{12}{13} \end{bmatrix}, \quad \vec{v} = \begin{bmatrix} -\frac{12}{13}\\\\[2pt] \frac{5}{13} \end{bmatrix}\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(6 pts)
<span class="math-inline">\\(\displaystyle \quad \vec{u}=\begin{bmatrix}\frac{3}{\sqrt{13}}\\\\[2pt]\frac{2}{\sqrt{13}}\end{bmatrix}, \quad \vec{v}=\begin{bmatrix}-\frac{2}{\sqrt{13}}\\\\[2pt]\frac{3}{\sqrt{13}}\end{bmatrix}\\)</span>

</div>
</div>

</div>

---

## Problem 5: Projecting Confidence (17 pts)

Let

<div class="math-display">
$$
\vec{w}
  =
  \begin{bmatrix}
  5\\
  7
  \end{bmatrix},
$$
</div>

 and let

<div class="math-display">
$$
\ell
  =
  \operatorname{span}
  \left(
  \begin{bmatrix}
  2\\
  -1
  \end{bmatrix}
  \right).
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(7 pts) Find the orthogonal projection of <span class="math-inline">\\(\vec{w}\\)</span> onto <span class="math-inline">\\(\ell\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(10 pts) Let <span class="math-inline">\\(\vec p\\)</span> be your answer to part (a). Let

<div class="math-display">
$$
\vec r = \vec w - \vec p.
$$
</div>

 This means <span class="math-inline">\\(\vec r\\)</span> is the difference between <span class="math-inline">\\(\vec w\\)</span> and its projection onto <span class="math-inline">\\(\ell\\)</span>.

<ol class="assignment-enumeration" markdown="1">

<li markdown="1">
<div class="assignment-enumeration-label">i.</div>
<div class="assignment-enumeration-content" markdown="1">

(5 pts) Draw <span class="math-inline">\\(\vec{w}\\)</span>, <span class="math-inline">\\(\ell\\)</span>, and <span class="math-inline">\\(\vec{r}\\)</span> on axes like the one below. Make sure to label each one.

<div style="text-align: center;">
<img src="imgs/hw03-plot-03.png" alt="Coordinate diagram" class="assignment-vector-plot">
</div>

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">ii.</div>
<div class="assignment-enumeration-content" markdown="1">

(5 pts) Using a dot product, verify that <span class="math-inline">\\(\vec{r}\\)</span> is perpendicular to <span class="math-inline">\\(\ell\\)</span>.

</div></li>
</ol>

</div>
</div>

</div>

---

## Problem 6: May the Force Be with Blue (12 pts)

A heavy equipment cart with a weight of <span class="math-inline">\\(500\\)</span> Newtons (N) rests on a frictionless inclined ramp. For every <span class="math-inline">\\(7\\)</span> meters of horizontal distance, the ramp rises <span class="math-inline">\\(6\\)</span> meters.

Team Maize stands uphill from the cart and pulls it up the ramp with a force of <span class="math-inline">\\(900\\)</span> N. Team Blue stands downhill from the cart and pulls it down the ramp. Both teams pull in directions parallel to the ramp.

<div style="text-align: center;">
<img src="imgs/hw03-plot-04.png" alt="Coordinate diagram" class="assignment-vector-plot">
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(8 pts) Find the component of the cart's weight that acts parallel to the ramp. Give both its magnitude and its direction.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) How hard must Team Blue pull to keep the cart stationary? Give your answer in Newtons.

</div>
</div>

</div>

---

## Problem 7: Programming Activity (15 pts)

Most homeworks and some labs will have a Jupyter Notebook, containing Python code that supplements our understanding of the relevant mathematical ideas of the week.

To open the notebook for Homework 3, click [**this link**](https://colab.research.google.com/github/math-124/fa26-code/blob/main/homeworks/hw03/hw03.ipynb). Instructions on how to use Google Colab are at [math124.org/running-code](https://math124.org/running-code).

You won't need to submit the notebook anywhere. To get credit for the work you did in this notebook, include the following in your PDF submission to Homework 3 on Pensive, specifically under **Problem 7**:

<ol class="assignment-enumeration" markdown="1">

<li markdown="1">
<div class="assignment-enumeration-label">1.</div>
<div class="assignment-enumeration-content" markdown="1">

**Task 1 (3 pts):** A screenshot of the plot showing your two wind vectors.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">2.</div>
<div class="assignment-enumeration-content" markdown="1">

**Task 2 (0 pts; but must complete):** Nothing to submit.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">3.</div>
<div class="assignment-enumeration-content" markdown="1">

**Task 3 (0 pts; but must complete):** Nothing to submit.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">4.</div>
<div class="assignment-enumeration-content" markdown="1">

**Task 4 (4 pts):** A screenshot of your completed reconstruction code, plus a written response stating the sign of <span class="math-inline">\\(a\\)</span>, using it to identify whether `w = np.array([10, 0])` is a headwind or tailwind for Runway 24, and stating the crosswind magnitude <span class="math-inline">\\(|b|\\)</span>.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">5.</div>
<div class="assignment-enumeration-content" markdown="1">

**Task 5 (8 pts):** Your written answers to both questions (4 pts each). No screenshots are required.

</div></li>
</ol>

{% endraw %}
