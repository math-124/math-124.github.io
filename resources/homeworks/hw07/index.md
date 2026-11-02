---
layout: page
title: "Homework 7: Linear Systems"
description: "Homework 7: Linear Systems problems."
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
.main-content details table td:last-child {
  white-space: normal;
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

# Homework 7: Linear Systems

**due** Sunday, November 8th at 11:59PM

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw07/hw07.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button colab-btn" href="https://colab.research.google.com/github/math-124/fa26-code/blob/main/homeworks/hw07/hw07.ipynb" target="_blank"><img src="/assets/site-images/google-colab.png" alt="" aria-hidden="true"> Google Colab</a>
</div>

{: .yellow }
<div markdown="1">
Write your solutions to the following problems either by writing them on a piece of paper or on a tablet and scanning your answers as a PDF. Note that you are not allowed to use LaTeX, Google Docs, or any other digital document creation software to type your answers. Homeworks are due to Pensive by 11:59PM on the due date. See the [syllabus](https://math124.org/syllabus/#homework) for details on the slip day policy.

Homework will be evaluated not only on the correctness of your answers, but on your ability to present your ideas clearly and logically. You should always explain and justify your conclusions, using sound reasoning. Your goal should be to convince the reader of your assertions. If a question does not require explanation, it will be explicitly stated.

Before proceeding, make sure you're familiar with the [collaboration policy](https://math124.org/syllabus/#collaboration-and-generative-ai-policy).
</div>

---

## Problems

- [Problem 1: Homework 6 Solutions Review](#problem-1-homework-6-solutions-review-6-pts)
- [Problem 2: When a Pivot Goes Missing](#problem-2-when-a-pivot-goes-missing-15-pts)
- [Problem 3: Factoring a Rectangular Matrix](#problem-3-factoring-a-rectangular-matrix-20-pts)
- [Problem 4: Working Backward](#problem-4-working-backward-15-pts)
- [Problem 5: A Plane of Possibilities](#problem-5-a-plane-of-possibilities-26-pts)
- [Problem 6: The Score Adds Up](#problem-6-the-score-adds-up-18-pts)

---

Total Points: <span class="math-inline">\\(6+15+20+15+26+18=100\\)</span>

---

## Problem 1: Homework 6 Solutions Review (6 pts)

Review [the solutions to Homework 6](https://math124.org/resources/homeworks/hw06/). Pick **two problem parts** (for example, Problem 3a and Problem 5b) from Homework 6 in which your solutions have the most room for improvement, i.e., where they have unsound reasoning, could be significantly more efficient or clearer, etc. **Include a screenshot of your solution to each problem part**, and in a few sentences, explain what was deficient and how it could be fixed.

Alternatively, if you think one of your solutions is significantly better than the posted one, copy it here and explain why you think it is better. If you didn't do Homework 6, choose two problem parts from it that look challenging to you, and in a few sentences, explain the key ideas behind their solutions in your own words.

---

## Problem 2: When a Pivot Goes Missing (15 pts)

Let

<div class="math-display">
$$
A=\begin{bmatrix}1&-2&1\\-2&4&0\\3&-6&1\end{bmatrix}.
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(7 pts) Find a factorization <span class="math-inline">\\(A=LU\\)</span>, where <span class="math-inline">\\(L\\)</span> is lower triangular with ones on its diagonal and <span class="math-inline">\\(U\\)</span> is in row echelon form. Identify the pivot columns of <span class="math-inline">\\(U\\)</span>.

<em>Hint: Don't forget about the requirement that <span class="math-inline">\\(U\\)</span> is in row echelon form!</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(8 pts) Use your factors to find all solutions of each system:

<div class="math-display">
$$
A\vec x=\begin{bmatrix}3\\-2\\5\end{bmatrix},\qquad
A\vec x=\begin{bmatrix}3\\-2\\6\end{bmatrix}.
$$
</div>

 If there are infinitely many solutions, give a vector-parametric description of the solution set. If there is no solution, explain why.

</div>
</div>

</div>

---

## Problem 3: Factoring a Rectangular Matrix (20 pts)

Let

<div class="math-display">
$$
B=\begin{bmatrix}2&-2&1&3\\6&-6&3&9\\-2&2&3&1\end{bmatrix}.
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Attempt to find a factorization <span class="math-inline">\\(B=LU\\)</span> without reordering the rows, where <span class="math-inline">\\(L\\)</span> has ones on its diagonal and <span class="math-inline">\\(U\\)</span> is in row echelon form. Explain why a row exchange is necessary.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(8 pts) Find a permutation matrix <span class="math-inline">\\(P\\)</span> and factors <span class="math-inline">\\(L,U\\)</span> such that <span class="math-inline">\\(PB=LU\\)</span>, with <span class="math-inline">\\(L\\)</span> square and lower triangular with ones on its diagonal and <span class="math-inline">\\(U\\)</span> in row echelon form. Identify the pivot columns of <span class="math-inline">\\(U\\)</span>, and verify your factorization by multiplying <span class="math-inline">\\(LU\\)</span> and showing it is equal to <span class="math-inline">\\(PB\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(7 pts) Use your factors to find all solutions of

<div class="math-display">
$$
B\vec x=\begin{bmatrix}6\\18\\2\end{bmatrix}.
$$
</div>

 Give a vector-parametric description of the solution set.

</div>
</div>

</div>

---

## Problem 4: Working Backward (15 pts)

For each part, give a matrix <span class="math-inline">\\(U\\)</span> in row echelon form and a vector <span class="math-inline">\\(\vec y\\)</span> such that the system <span class="math-inline">\\(U\vec x=\vec y\\)</span> has the stated properties. Write your system as a matrix equation, and give a vector-parametric description of the solution set, or explain why it has no solution. Each part may use a different matrix.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(3 pts)
<span class="math-inline">\\(U\\)</span> is <span class="math-inline">\\(3\times3\\)</span>, and the system has a unique solution.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts)
<span class="math-inline">\\(U\\)</span> is <span class="math-inline">\\(3\times3\\)</span>, and the solution set is a line in <span class="math-inline">\\(\mathbb R^3\\)</span> that does not pass through the origin.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(3 pts)
<span class="math-inline">\\(U\\)</span> is <span class="math-inline">\\(3\times4\\)</span>, and the solution set is a plane through the origin in <span class="math-inline">\\(\mathbb R^4\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(3 pts)
<span class="math-inline">\\(U\\)</span> is <span class="math-inline">\\(4\times3\\)</span>, and the system has no solution.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(3 pts)
<span class="math-inline">\\(U\\)</span> is <span class="math-inline">\\(4\times2\\)</span>, and the system has a unique solution.

</div>
</div>

</div>

---

## Problem 5: A Plane of Possibilities (26 pts)

Suppose <span class="math-inline">\\(\vec v=\begin{bmatrix}1\\\\1\\\\1\end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec w=\begin{bmatrix}1\\\\2\\\\3\end{bmatrix}\\)</span>, and let <span class="math-inline">\\(C\\)</span> be the <span class="math-inline">\\(3\times2\\)</span> matrix whose columns are <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec w\\)</span>:

<div class="math-display">
$$
C=\begin{bmatrix}|&|\\\vec v&\vec w\\|&|\end{bmatrix}
=\begin{bmatrix}1&1\\1&2\\1&3\end{bmatrix}.
$$
</div>

 A possible output of a matrix is any vector that can be produced by multiplying that matrix by a vector. For example, <span class="math-inline">\\(\begin{bmatrix}5\\\\9\\\\13\end{bmatrix}\\)</span> is a possible output of <span class="math-inline">\\(C\\)</span>, since

<div class="math-display">
$$
\begin{bmatrix}5\\9\\13\end{bmatrix}=C\begin{bmatrix}1\\4\end{bmatrix}.
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find a factorization <span class="math-inline">\\(C=LU\\)</span>, where <span class="math-inline">\\(L\\)</span> is square and lower triangular with ones on its diagonal and <span class="math-inline">\\(U\\)</span> is in row echelon form.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) What are all possible outputs of <span class="math-inline">\\(C\\)</span>? Using your factorization <span class="math-inline">\\(C=LU\\)</span>, determine the conditions on <span class="math-inline">\\(x\\)</span>, <span class="math-inline">\\(y\\)</span>, and <span class="math-inline">\\(z\\)</span> such that

<div class="math-display">
$$
C\vec u=\begin{bmatrix}x\\y\\z\end{bmatrix}
$$
</div>

 has a solution <span class="math-inline">\\(\vec u\\)</span>. The condition you find should be a single equation involving <span class="math-inline">\\(x\\)</span>, <span class="math-inline">\\(y\\)</span>, and <span class="math-inline">\\(z\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Under the condition you found in part b), find the solution for the vector <span class="math-inline">\\(\vec u\in\mathbb R^2\\)</span> in terms of <span class="math-inline">\\(x\\)</span>, <span class="math-inline">\\(y\\)</span>, and <span class="math-inline">\\(z\\)</span>. Is the solution unique?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(8 pts) Using your understanding of geometry and span from earlier in the semester, find the equation of the plane spanned by <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec w\\)</span>. Why do you get the same answer as in part b)?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Consider the matrix

<div class="math-display">
$$
F=\begin{bmatrix}|&|&|\\\vec v&\vec w&\vec v+\vec w\\|&|&|\end{bmatrix}
=\begin{bmatrix}1&1&2\\1&2&3\\1&3&4\end{bmatrix}.
$$
</div>

 Does <span class="math-inline">\\(F\\)</span> have the same possible outputs as <span class="math-inline">\\(C\\)</span>? Explain. Then, find two different inputs that <span class="math-inline">\\(F\\)</span> sends to

<div class="math-display">
$$
2\vec v+3\vec w=\begin{bmatrix}5\\8\\11\end{bmatrix}.
$$
</div>

</div>
</div>

</div>

---

## Problem 6: The Score Adds Up (18 pts)

Before proceeding, open the supplemental Jupyter Notebook. To open the notebook for Homework 7, click [**this link**](https://colab.research.google.com/github/math-124/fa26-code/blob/main/homeworks/hw07/hw07.ipynb). Instructions on how to use Google Colab are at [math124.org/running-code](https://math124.org/running-code).

Complete Problem 6 in the notebook. Tasks 1–8 are worth <span class="math-inline">\\(1+1+2+5+1+2+1+5=18\\)</span> points, respectively. Follow its orange instructions for what to include in your PDF submission to Pensive.

{% endraw %}
