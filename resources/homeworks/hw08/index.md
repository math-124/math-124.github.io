---
layout: page
title: "Homework 8: Subspaces, Bases, and Rank"
description: "Homework 8: Subspaces, Bases, and Rank problems."
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

# Homework 8: Subspaces, Bases, and Rank

**due** Friday, November 13th at 11:59PM

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw08/hw08.pdf" target="_blank">View as PDF ✏️</a>
</div>

{: .yellow }
<div markdown="1">
Write your solutions to the following problems either by writing them on a piece of paper or on a tablet and scanning your answers as a PDF. Note that you are not allowed to use LaTeX, Google Docs, or any other digital document creation software to type your answers. Homeworks are due to Pensive by 11:59PM on the due date. See the [syllabus](https://math124.org/syllabus/#homework) for details on the slip day policy.

Homework will be evaluated not only on the correctness of your answers, but on your ability to present your ideas clearly and logically. You should always explain and justify your conclusions, using sound reasoning. Your goal should be to convince the reader of your assertions. If a question does not require explanation, it will be explicitly stated.

Before proceeding, make sure you're familiar with the [collaboration policy](https://math124.org/syllabus/#collaboration-and-generative-ai-policy).
</div>

---

## Problems

- [Problem 1: Homework 7 Solutions Review](#problem-1-homework-7-solutions-review-6-pts)
- [Problem 2: Multiplying a column by a row](#problem-2-multiplying-a-column-by-a-row-8-pts)
- [Problem 3: Column spaces and rank](#problem-3-column-spaces-and-rank-21-pts)
- [Problem 4: Reachable outputs and unique inputs](#problem-4-reachable-outputs-and-unique-inputs-10-pts)
- [Problem 5: Rows and columns](#problem-5-rows-and-columns-7-pts)
- [Problem 6: One subspace, several descriptions](#problem-6-one-subspace-several-descriptions-21-pts)
- [Problem 7: Pivots, free variables, and zero outputs](#problem-7-pivots-free-variables-and-zero-outputs-27-pts)

---

Total Points: <span class="math-inline">\\(6+8+21+10+7+21+27=100\\)</span>.

---

{: .yellow }
> Note: Refer to [**Chapter 5**](https://notes.math124.org/ch05/05-01/) while working on the homework!

---

## Problem 1: Homework 7 Solutions Review (6 pts)

Review [the solutions to Homework 7](https://math124.org/resources/homeworks/hw07/). Pick **two problem parts** (for example, Problem 3a and Problem 5b) from Homework 7 in which your solutions have the most room for improvement, i.e., where they have unsound reasoning, could be significantly more efficient or clearer, etc. **Include a screenshot of your solution to each problem part**, and in a few sentences, explain what was deficient and how it could be fixed.

Alternatively, if you think one of your solutions is significantly better than the posted one, copy it here and explain why you think it is better. If you didn't do Homework 7, choose two problem parts from it that look challenging to you, and in a few sentences, explain the key ideas behind their solutions in your own words.

---

## Problem 2: Multiplying a column by a row (8 pts)

Let <span class="math-inline">\\(A=\begin{bmatrix}5\\\\1\\\\3\\\\-1\end{bmatrix}\\)</span> and <span class="math-inline">\\(B=\begin{bmatrix}4&amp;0&amp;10&amp;-2&amp;1\end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Write <span class="math-inline">\\(AB\\)</span> in matrix form. <em>Hint: The result is a <span class="math-inline">\\(4\times5\\)</span> matrix.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Fill in the blanks: Every column of <span class="math-inline">\\(AB\\)</span> is a scalar multiple of , while every row of <span class="math-inline">\\(AB\\)</span> is a scalar multiple of .

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Find <span class="math-inline">\\(\operatorname{rank}(AB)\\)</span>.

</div>
</div>

</div>

---

## Problem 3: Column spaces and rank (21 pts)

Consider the following matrices.

<div class="math-display">
$$
A=\begin{bmatrix}4&-2\\10&0\\1&1\end{bmatrix},\qquad
B=\begin{bmatrix}3&-4\\4&3\\0&0\end{bmatrix},\qquad
C=\begin{bmatrix}6&2\\10&10\\0&2\end{bmatrix}.
$$
</div>



<div class="math-display">
$$
D=\begin{bmatrix}4&-2&2\\10&0&10\\1&1&2\end{bmatrix},\quad
E=\begin{bmatrix}3&-4&0\\4&3&0\\0&0&6\end{bmatrix},\quad
F=\begin{bmatrix}1&2&-1&3\\5&10&-5&15\\1&2&-1&3\end{bmatrix},\quad
G=\begin{bmatrix}4&-2&6&-4\\10&0&10&0\\1&1&0&2\end{bmatrix}.
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(14 pts) For each matrix, determine whether its column space is exactly the plane<span class="math-inline">\\(5x-3y+10z=0\\)</span> in <span class="math-inline">\\(\mathbb R^3\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(7 pts) Find the rank of each matrix.

</div>
</div>

</div>

---

## Problem 4: Reachable outputs and unique inputs (10 pts)

For parts (a)--(c), suppose <span class="math-inline">\\(A\\)</span> has shape <span class="math-inline">\\(5\times7\\)</span> and rank <span class="math-inline">\\(5\\)</span>. Determine whether each statement is **true or false**, and explain your answer.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts)
<span class="math-inline">\\(\operatorname{colsp}(A)=\mathbb R^5\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) The columns of <span class="math-inline">\\(A\\)</span> are linearly independent.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) There is exactly one input <span class="math-inline">\\(\vec x\\)</span> such that <span class="math-inline">\\(A\vec x=\begin{bmatrix}1\\\\2\\\\3\\\\4\\\\5\end{bmatrix}\\)</span>.

**Now suppose <span class="math-inline">\\(B\\)</span> has shape <span class="math-inline">\\(5\times3\\)</span> and rank <span class="math-inline">\\(3\\)</span>.**

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Is every vector in <span class="math-inline">\\(\mathbb R^5\\)</span> an output of <span class="math-inline">\\(B\\)</span>?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Can two different inputs produce the same output under <span class="math-inline">\\(B\\)</span>?

</div>
</div>

</div>

---

## Problem 5: Rows and columns (7 pts)

The first <span class="math-inline">\\(3\\)</span> columns of <span class="math-inline">\\(A\\)</span> below are linearly independent. Consider

<div class="math-display">
$$
A=\begin{bmatrix}4&6&-8&10&-2\\0&5&10&-5&15\\0&0&7&14&-7\end{bmatrix},\qquad
B=\begin{bmatrix}4&0&0\\6&5&0\\-8&10&7\\10&-5&14\\-2&15&-7\end{bmatrix}.
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find <span class="math-inline">\\(\operatorname{rank}(A)\\)</span> and <span class="math-inline">\\(\operatorname{rank}(B)\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(1 pt) How are the entries of <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span> related?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Make a guess as to how the number of linearly independent rows of a matrix compares with the number of linearly independent columns.

</div>
</div>

</div>

---

## Problem 6: One subspace, several descriptions (21 pts)

Let

<div class="math-display">
$$
W=\left\{\begin{bmatrix}x_1\\x_2\\x_3\\x_4\end{bmatrix}\in\mathbb R^4:
 x_3=4x_1-3x_2,\quad x_4=2x_1+5x_2\right\}.
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Write a general vector <span class="math-inline">\\(\begin{bmatrix}a\\\\b\\\\4a-3b\\\\2a+5b\end{bmatrix}\\)</span> in the subspace <span class="math-inline">\\(W\\)</span> as a linear combination of two linearly independent vectors. Use this to find a basis of <span class="math-inline">\\(W\\)</span> and determine <span class="math-inline">\\(\dim(W)\\)</span>.

For the remainder of this problem, let <span class="math-inline">\\(\vec u,\vec v\\)</span> be your basis vectors from part (a). Furthermore, let

<div class="math-display">
$$
\vec x=5\vec u+9\vec v,\qquad \vec y=\begin{bmatrix}0\\0\\0\\1\end{bmatrix}.
$$
</div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(8 pts) Which of the following collections are bases of <span class="math-inline">\\(W\\)</span>? Explain why or why not for each collection.

<div class="math-display">
$$
\begin{array}{ll}
\text{(i)}\quad\{\vec u+\vec v,\;\vec x\}
&\qquad\text{(ii)}\quad\{\vec x-5\vec u,\;\vec v\}\\[8pt]
\text{(iii)}\quad\{\vec x,\;\vec y\}
&\qquad\text{(iv)}\quad\{4\vec u+7\vec v,\;7\vec u+12\vec v\}.
\end{array}
$$
</div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(8 pts) Find the rank of each matrix below. Explain your answers.

<div class="math-display">
$$
\text{(i)}\ A=\begin{bmatrix}|&|\\\vec u&\vec v\\|&|\end{bmatrix},\quad
\text{(ii)}\ B=\begin{bmatrix}|&|\\\vec u&2\vec u\\|&|\end{bmatrix},\quad
\text{(iii)}\ C=\begin{bmatrix}|&|&|\\\vec u&\vec v&\vec x\\|&|&|\end{bmatrix},\quad
\text{(iv)}\ D=\begin{bmatrix}|&|&|&|\\\vec u&\vec v&\vec x&\vec y\\|&|&|&|\end{bmatrix}.
$$
</div>

</div>
</div>

</div>

---

## Problem 7: Pivots, free variables, and zero outputs (27 pts)

Consider the factorization <span class="math-inline">\\(A=LU\\)</span>:

<div class="math-display">
$$
\underbrace{\begin{bmatrix}4&8&-4&0\\16&32&-11&15\\-12&-24&37&75\end{bmatrix}}_A
=
\underbrace{\begin{bmatrix}1&0&0\\4&1&0\\-3&5&1\end{bmatrix}}_L
\underbrace{\begin{bmatrix}4&8&-4&0\\0&0&5&15\\0&0&0&0\end{bmatrix}}_U.
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Write the three scalar equations in <span class="math-inline">\\(x&#95;1,x&#95;2,x&#95;3,x&#95;4\\)</span> represented by <span class="math-inline">\\(U\vec x=\vec0\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) What is <span class="math-inline">\\(\operatorname{rank}(A)\\)</span>? Explain in two ways:

<ol class="assignment-enumeration" markdown="1">
<li markdown="1">
<div class="assignment-enumeration-label">(i)</div>
<div class="assignment-enumeration-content" markdown="1">

Using the pivots of <span class="math-inline">\\(U\\)</span>.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">(ii)</div>
<div class="assignment-enumeration-content" markdown="1">

Using linear independence and a basis of <span class="math-inline">\\(\operatorname{colsp}(A)\\)</span>.

</div></li>
</ol>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Set <span class="math-inline">\\(x&#95;2=s\\)</span> and <span class="math-inline">\\(x&#95;4=t\\)</span>. Use your equations from part (a) to fill in the blanks below, describing the set of inputs <span class="math-inline">\\(\vec x\\)</span> such that <span class="math-inline">\\(A\vec x=\vec0\\)</span>:

<div class="math-display">
$$
\vec x=s\begin{bmatrix}\underline{\hspace{0.6cm}}\\1\\\underline{\hspace{0.6cm}}\\0\end{bmatrix}
+t\begin{bmatrix}\underline{\hspace{0.6cm}}\\0\\\underline{\hspace{0.6cm}}\\1\end{bmatrix},\qquad s,t\in\mathbb R.
$$
</div>

The set of inputs that <span class="math-inline">\\(A\\)</span> sends to zero is called its **null space**. It is itself a **subspace of <span class="math-inline">\\(\mathbb R^4\\)</span>**:

<div class="math-display">
$$
\operatorname{nullsp}(A)=\{\vec x\in\mathbb R^4:A\vec x=\vec0\}.
$$
</div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) What is <span class="math-inline">\\(\dim(\operatorname{nullsp}(A))\\)</span>? Explain using the <span class="math-inline">\\(2\\)</span> vectors in part (c).

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Show that <span class="math-inline">\\(\operatorname{nullsp}(A)\\)</span> is a subspace: if <span class="math-inline">\\(\vec x,\vec y\in\operatorname{nullsp}(A)\\)</span> and <span class="math-inline">\\(c\in\mathbb R\\)</span>, show that <span class="math-inline">\\(\vec x+\vec y\in\operatorname{nullsp}(A)\\)</span> and <span class="math-inline">\\(c\vec x\in\operatorname{nullsp}(A)\\)</span>.

<em>Hint: You know <span class="math-inline">\\(A\vec x=A\vec y=\vec0\\)</span>. Use this to compute <span class="math-inline">\\(A(\vec x+\vec y)\\)</span> and <span class="math-inline">\\(A(c\vec x)\\)</span>. Also check that <span class="math-inline">\\(\vec0\in\operatorname{nullsp}(A)\\)</span>.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">f)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) Suppose, for this same <span class="math-inline">\\(A\\)</span>, that <span class="math-inline">\\(A\begin{bmatrix}9\\\\1\\\\2\\\\6\end{bmatrix}=\vec y\\)</span>. Find three other inputs whose output is also <span class="math-inline">\\(\vec y\\)</span>. Then, in vector-parametric form, describe the complete set of vectors <span class="math-inline">\\(\vec v\\)</span> such that <span class="math-inline">\\(A\vec v=\vec y\\)</span>.

<em>Hint: If <span class="math-inline">\\(A\vec v=\vec y\\)</span> and <span class="math-inline">\\(\vec n\in\operatorname{nullsp}(A)\\)</span>, then what is <span class="math-inline">\\(A(\vec v+\vec n)\\)</span>?</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">g)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Complete the table below. Once the free variables are chosen, each pivot determines one remaining variable. Each free variable contributes one basis vector to the null space.

<table>
<thead>
<tr>
<th style="text-align: center;">Matrix shape</th>
<th style="text-align: center;">Pivots (rank)</th>
<th style="text-align: center;">Free variables</th>
<th style="text-align: center;">Dimension of null space</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><span class="math-inline">\(3\times4\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(2\)</span></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;"><span class="math-inline">\(5\times7\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(5\)</span></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;"><span class="math-inline">\(n\times d\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(r\)</span></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
</tbody>
</table>
</div>
</div>

</div>

{% endraw %}
