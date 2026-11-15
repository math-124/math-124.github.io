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
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw08/hw08-solutions.pdf" target="_blank">Solutions PDF ✅</a>
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

<details markdown="1"><summary>Solution</summary>

Responses will vary. Identify the specific issue in each selected solution and explain how to improve the reasoning or presentation.
</details>

---

## Problem 2: Multiplying a column by a row (8 pts)

Let <span class="math-inline">\\(A=\begin{bmatrix}5\\\\1\\\\3\\\\-1\end{bmatrix}\\)</span> and <span class="math-inline">\\(B=\begin{bmatrix}4&amp;0&amp;10&amp;-2&amp;1\end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Write <span class="math-inline">\\(AB\\)</span> in matrix form. <em>Hint: The result is a <span class="math-inline">\\(4\times5\\)</span> matrix.</em>

<details markdown="1"><summary>Solution</summary>

Each entry of <span class="math-inline">\\(A\\)</span> multiplies the entire row <span class="math-inline">\\(B\\)</span>:

<div class="math-display">
$$
AB=\begin{bmatrix}
5(4)&5(0)&5(10)&5(-2)&5(1)\\
1(4)&1(0)&1(10)&1(-2)&1(1)\\
3(4)&3(0)&3(10)&3(-2)&3(1)\\
-1(4)&-1(0)&-1(10)&-1(-2)&-1(1)
\end{bmatrix}
=\boxed{\begin{bmatrix}20&0&50&-10&5\\4&0&10&-2&1\\12&0&30&-6&3\\-4&0&-10&2&-1\end{bmatrix}}.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Fill in the blanks: Every column of <span class="math-inline">\\(AB\\)</span> is a scalar multiple of , while every row of <span class="math-inline">\\(AB\\)</span> is a scalar multiple of .

<details markdown="1"><summary>Solution</summary>

The blanks are

<div class="math-display">
$$
\boxed{\begin{bmatrix}5\\1\\3\\-1\end{bmatrix}}
\qquad\text{and}\qquad
\boxed{\begin{bmatrix}4&0&10&-2&1\end{bmatrix}}.
$$
</div>

 The columns are <span class="math-inline">\\(4A,0A,10A,-2A,A\\)</span>. The rows are <span class="math-inline">\\(5B,B,3B,-B\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Find <span class="math-inline">\\(\operatorname{rank}(AB)\\)</span>.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(\boxed{\operatorname{rank}(AB)=1}\\)</span>. Every column is a multiple of <span class="math-inline">\\(A\\)</span>, and <span class="math-inline">\\(A\\)</span> itself is the last column. Thus

<div class="math-display">
$$
\operatorname{colsp}(AB)=\operatorname{span}\left(\begin{bmatrix}5\\1\\3\\-1\end{bmatrix}\right).
$$
</div>

 This nonzero vector is a basis of the column space, so its dimension is <span class="math-inline">\\(1\\)</span>. The zero column does not make the rank <span class="math-inline">\\(0\\)</span>.
</details>

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

<details markdown="1"><summary>Solution</summary>

Call the plane <span class="math-inline">\\(P\\)</span>. To have column space exactly <span class="math-inline">\\(P\\)</span>, all columns must lie on <span class="math-inline">\\(P\\)</span>, and they must span the whole plane. Having all columns on <span class="math-inline">\\(P\\)</span> is not enough if their span is only a line.

Let

<div class="math-display">
$$
\vec u=\begin{bmatrix}4\\10\\1\end{bmatrix},\qquad
\vec v=\begin{bmatrix}-2\\0\\1\end{bmatrix}.
$$
</div>

 Both are on <span class="math-inline">\\(P\\)</span>, since <span class="math-inline">\\(5(4)-3(10)+10(1)=0\\)</span> and <span class="math-inline">\\(5(-2)-3(0)+10(1)=0\\)</span>. They are not scalar multiples, so they span a plane. Since that plane is contained in <span class="math-inline">\\(P\\)</span>, their span is exactly <span class="math-inline">\\(P\\)</span>.

-   **<span class="math-inline">\\(A\\)</span>: Yes.** Its columns are <span class="math-inline">\\(\vec u,\vec v\\)</span>, which span <span class="math-inline">\\(P\\)</span>.

-   **<span class="math-inline">\\(B\\)</span>: No.** Its first column is not on <span class="math-inline">\\(P\\)</span>: <span class="math-inline">\\(5(3)-3(4)+10(0)=3\ne0\\)</span>. This column is itself an output of <span class="math-inline">\\(B\\)</span>, so the column space includes a vector outside <span class="math-inline">\\(P\\)</span>.

-   **<span class="math-inline">\\(C\\)</span>: Yes.** Its columns are <span class="math-inline">\\(\vec u-\vec v\\)</span> and <span class="math-inline">\\(\vec u+\vec v\\)</span>. They lie on <span class="math-inline">\\(P\\)</span>, and adding and subtracting them recovers <span class="math-inline">\\(2\vec u\\)</span> and <span class="math-inline">\\(2\vec v\\)</span>. Thus they span all of <span class="math-inline">\\(P\\)</span>.

-   **<span class="math-inline">\\(D\\)</span>: Yes.** Its columns are <span class="math-inline">\\(\vec u,\vec v,\vec u+\vec v\\)</span>. The third column adds no new outputs, so its column space is still <span class="math-inline">\\(P\\)</span>.

-   **<span class="math-inline">\\(E\\)</span>: No.** As with <span class="math-inline">\\(B\\)</span>, its first column is not on <span class="math-inline">\\(P\\)</span>. Its column space is actually all of <span class="math-inline">\\(\mathbb R^3\\)</span>.

-   **<span class="math-inline">\\(F\\)</span>: No.** Its columns are <span class="math-inline">\\(\vec f,2\vec f,-\vec f,3\vec f\\)</span>, where <span class="math-inline">\\(\vec f=\begin{bmatrix}1\\\\5\\\\1\end{bmatrix}\\)</span> lies on <span class="math-inline">\\(P\\)</span>. They span only the line through <span class="math-inline">\\(\vec f\\)</span>. For example, <span class="math-inline">\\(\vec u\\)</span> lies on <span class="math-inline">\\(P\\)</span> but is not a multiple of <span class="math-inline">\\(\vec f\\)</span>, so it is not an output of <span class="math-inline">\\(F\\)</span>.

-   **<span class="math-inline">\\(G\\)</span>: Yes.** Its columns are <span class="math-inline">\\(\vec u,\vec v,\vec u-\vec v,2\vec v\\)</span>. The last <span class="math-inline">\\(2\\)</span> columns are redundant, so its column space is <span class="math-inline">\\(P\\)</span>.

The matrices with the requested column space are <span class="math-inline">\\(\boxed{A,C,D,G}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(7 pts) Find the rank of each matrix.

<details markdown="1"><summary>Solution</summary>

Rank is the dimension of the column space, or the maximum number of linearly independent columns.

<table>
<thead>
<tr>
<th style="text-align: center;">Matrix</th>
<th style="text-align: center;">Rank</th>
<th style="text-align: left;">Reason</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><span class="math-inline">\(A\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(2\)</span></td>
<td style="text-align: left;">Its <span class="math-inline">\(2\)</span> columns are independent and span <span class="math-inline">\(P\)</span>.</td>
</tr>
<tr>
<td style="text-align: center;"><span class="math-inline">\(B\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(2\)</span></td>
<td style="text-align: left;">Its <span class="math-inline">\(2\)</span> nonzero columns are orthogonal: <span class="math-inline">\(3(-4)+4(3)+0(0)=0\)</span>. They are independent and span the plane <span class="math-inline">\(z=0\)</span>.</td>
</tr>
<tr>
<td style="text-align: center;"><span class="math-inline">\(C\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(2\)</span></td>
<td style="text-align: left;">Its <span class="math-inline">\(2\)</span> columns span <span class="math-inline">\(P\)</span> and are independent.</td>
</tr>
<tr>
<td style="text-align: center;"><span class="math-inline">\(D\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(2\)</span></td>
<td style="text-align: left;">The first <span class="math-inline">\(2\)</span> columns form a basis; the third is their sum.</td>
</tr>
<tr>
<td style="text-align: center;"><span class="math-inline">\(E\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(3\)</span></td>
<td style="text-align: left;">The first <span class="math-inline">\(2\)</span> columns span <span class="math-inline">\(z=0\)</span>; the third, <span class="math-inline">\(\begin{bmatrix}0\\0\\6\end{bmatrix}\)</span>, lies outside that plane. All <span class="math-inline">\(3\)</span> columns are independent.</td>
</tr>
<tr>
<td style="text-align: center;"><span class="math-inline">\(F\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(1\)</span></td>
<td style="text-align: left;">All columns are multiples of the same nonzero vector.</td>
</tr>
<tr>
<td style="text-align: center;"><span class="math-inline">\(G\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(2\)</span></td>
<td style="text-align: left;">The first <span class="math-inline">\(2\)</span> columns form a basis; the remaining columns are redundant.</td>
</tr>
</tbody>
</table>

In particular, <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span> have the same rank but different column spaces. Rank tells us the dimension of the output set, not which plane it is.
</details>

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

<details markdown="1"><summary>Solution</summary>

**True.** <span class="math-inline">\\(A\\)</span> has <span class="math-inline">\\(5\\)</span> rows, so its column space is a subspace of <span class="math-inline">\\(\mathbb R^5\\)</span>. Its rank is <span class="math-inline">\\(5\\)</span>, so that subspace has dimension <span class="math-inline">\\(5\\)</span> and must be all of <span class="math-inline">\\(\mathbb R^5\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) The columns of <span class="math-inline">\\(A\\)</span> are linearly independent.

<details markdown="1"><summary>Solution</summary>

**False.** There are <span class="math-inline">\\(7\\)</span> columns, but the maximum number of independent columns is the rank, <span class="math-inline">\\(5\\)</span>. Therefore the full collection of <span class="math-inline">\\(7\\)</span> columns is dependent.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) There is exactly one input <span class="math-inline">\\(\vec x\\)</span> such that <span class="math-inline">\\(A\vec x=\begin{bmatrix}1\\\\2\\\\3\\\\4\\\\5\end{bmatrix}\\)</span>.

<details markdown="1"><summary>Solution</summary>

**False.** Part (a) guarantees that the specified output is possible. But the columns are dependent, so there are infinitely many inputs that produce it. In terms of a system, there are <span class="math-inline">\\(7\\)</span> unknowns and <span class="math-inline">\\(5\\)</span> pivots, leaving <span class="math-inline">\\(2\\)</span> free variables.
</details>

**Now suppose <span class="math-inline">\\(B\\)</span> has shape <span class="math-inline">\\(5\times3\\)</span> and rank <span class="math-inline">\\(3\\)</span>.**

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Is every vector in <span class="math-inline">\\(\mathbb R^5\\)</span> an output of <span class="math-inline">\\(B\\)</span>?

<details markdown="1"><summary>Solution</summary>

**No.** <span class="math-inline">\\(\dim(\operatorname{colsp}(B))=3\\)</span>, while <span class="math-inline">\\(\dim(\mathbb R^5)=5\\)</span>. Thus <span class="math-inline">\\(\operatorname{colsp}(B)\\)</span> is a proper subspace of <span class="math-inline">\\(\mathbb R^5\\)</span>, and some vectors in <span class="math-inline">\\(\mathbb R^5\\)</span> are not outputs of <span class="math-inline">\\(B\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Can two different inputs produce the same output under <span class="math-inline">\\(B\\)</span>?

<details markdown="1"><summary>Solution</summary>

**No.** <span class="math-inline">\\(B\\)</span> has <span class="math-inline">\\(3\\)</span> columns and rank <span class="math-inline">\\(3\\)</span>, so its columns are independent. Every output in <span class="math-inline">\\(\operatorname{colsp}(B)\\)</span> therefore comes from exactly one input. An output outside <span class="math-inline">\\(\operatorname{colsp}(B)\\)</span> has no input.

The two matrices illustrate the two different comparisons: rank equal to the number of **rows** means every output is possible; rank equal to the number of **columns** means each possible output has a unique input.
</details>

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

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(\boxed{\operatorname{rank}(A)=3}\\)</span> because its first <span class="math-inline">\\(3\\)</span> columns are independent, and a subspace of <span class="math-inline">\\(\mathbb R^3\\)</span> cannot have dimension greater than <span class="math-inline">\\(3\\)</span>.

For <span class="math-inline">\\(B\\)</span>, call its columns <span class="math-inline">\\(\vec b&#95;1,\vec b&#95;2,\vec b&#95;3\\)</span>. If <span class="math-inline">\\(c&#95;1\vec b&#95;1+c&#95;2\vec b&#95;2+c&#95;3\vec b&#95;3=\vec0\\)</span>, the first <span class="math-inline">\\(3\\)</span> entries give

<div class="math-display">
$$
4c_1=0,\qquad 6c_1+5c_2=0,\qquad -8c_1+10c_2+7c_3=0.
$$
</div>

 The first equation forces <span class="math-inline">\\(c&#95;1=0\\)</span>, the second then forces <span class="math-inline">\\(c&#95;2=0\\)</span>, and the third forces <span class="math-inline">\\(c&#95;3=0\\)</span>. Thus no column can be written as a combination of the other columns: the <span class="math-inline">\\(3\\)</span> columns are independent. Therefore <span class="math-inline">\\(\boxed{\operatorname{rank}(B)=3}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(1 pt) How are the entries of <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span> related?

<details markdown="1"><summary>Solution</summary>

The rows of <span class="math-inline">\\(A\\)</span> become the columns of <span class="math-inline">\\(B\\)</span>, in the same order. Equivalently, the entry in row <span class="math-inline">\\(i\\)</span>, column <span class="math-inline">\\(j\\)</span> of <span class="math-inline">\\(A\\)</span> becomes the entry in row <span class="math-inline">\\(j\\)</span>, column <span class="math-inline">\\(i\\)</span> of <span class="math-inline">\\(B\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Make a guess as to how the number of linearly independent rows of a matrix compares with the number of linearly independent columns.

<details markdown="1"><summary>Solution</summary>

The maximum number of linearly independent rows of a matrix appears to equal the maximum number of linearly independent columns. This is true in general. In this example, both numbers for <span class="math-inline">\\(A\\)</span> are <span class="math-inline">\\(3\\)</span>: its rows are exactly the independent columns of <span class="math-inline">\\(B\\)</span>.
</details>

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

<details markdown="1"><summary>Solution</summary>

Separate the contributions from <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span>:

<div class="math-display">
$$
\begin{bmatrix}a\\b\\4a-3b\\2a+5b\end{bmatrix}
=a\underbrace{\begin{bmatrix}1\\0\\4\\2\end{bmatrix}}_{\vec u}
+b\underbrace{\begin{bmatrix}0\\1\\-3\\5\end{bmatrix}}_{\vec v}.
$$
</div>

 Every vector in <span class="math-inline">\\(W\\)</span> is such a combination, and every choice of <span class="math-inline">\\(a,b\\)</span> gives a vector satisfying the equations for <span class="math-inline">\\(W\\)</span>. Therefore <span class="math-inline">\\(W=\operatorname{span}(\vec u,\vec v)\\)</span>.

These vectors are not scalar multiples: their first <span class="math-inline">\\(2\\)</span> entries are <span class="math-inline">\\(\begin{bmatrix}1\\\\0\end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix}0\\\\1\end{bmatrix}\\)</span>. Thus they are independent, and

<div class="math-display">
$$
\boxed{\left\{\begin{bmatrix}1\\0\\4\\2\end{bmatrix},\begin{bmatrix}0\\1\\-3\\5\end{bmatrix}\right\}\text{ is a basis of }W,\qquad \dim(W)=2.}
$$
</div>

</details>

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

<details markdown="1"><summary>Solution</summary>

We use the fact that <span class="math-inline">\\(\vec u,\vec v\\)</span> form a basis of <span class="math-inline">\\(W\\)</span>. These arguments work for any basis chosen in part (a).

<ol class="assignment-enumeration" markdown="1">
<li markdown="1">
<div class="assignment-enumeration-label">(i)</div>
<div class="assignment-enumeration-content" markdown="1">

**Yes.** Let <span class="math-inline">\\(\vec p=\vec u+\vec v\\)</span> and <span class="math-inline">\\(\vec q=\vec x=5\vec u+9\vec v\\)</span>. We can recover the original basis vectors:

<div class="math-display">
$$
\vec v=\frac{\vec q-5\vec p}{4},\qquad
\vec u=\frac{9\vec p-\vec q}{4}.
$$
</div>

 So the new pair spans <span class="math-inline">\\(W\\)</span>. It is independent: if <span class="math-inline">\\(\vec q=c\vec p\\)</span>, independence of <span class="math-inline">\\(\vec u,\vec v\\)</span> would require both <span class="math-inline">\\(c=5\\)</span> and <span class="math-inline">\\(c=9\\)</span>, which is impossible.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">(ii)</div>
<div class="assignment-enumeration-content" markdown="1">

**No.** <span class="math-inline">\\(\vec x-5\vec u=9\vec v\\)</span>, so the pair is <span class="math-inline">\\(\lbrace{}9\vec v,\vec v\rbrace{}\\)</span>. It is dependent and spans only the line through <span class="math-inline">\\(\vec v\\)</span>, not all of <span class="math-inline">\\(W\\)</span>.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">(iii)</div>
<div class="assignment-enumeration-content" markdown="1">

**No.** <span class="math-inline">\\(\vec y=\begin{bmatrix}0\\\\0\\\\0\\\\1\end{bmatrix}\\)</span> is not in <span class="math-inline">\\(W\\)</span>: its fourth entry would have to be <span class="math-inline">\\(2(0)+5(0)=0\\)</span>, but it is <span class="math-inline">\\(1\\)</span>. A basis of <span class="math-inline">\\(W\\)</span> cannot contain a vector outside <span class="math-inline">\\(W\\)</span>.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">(iv)</div>
<div class="assignment-enumeration-content" markdown="1">

**Yes.** Let <span class="math-inline">\\(\vec p=4\vec u+7\vec v\\)</span> and <span class="math-inline">\\(\vec q=7\vec u+12\vec v\\)</span>. Then

<div class="math-display">
$$
\vec u=-12\vec p+7\vec q,\qquad
\vec v=7\vec p-4\vec q.
$$
</div>

 Thus the pair spans <span class="math-inline">\\(W\\)</span>. It is independent: <span class="math-inline">\\(\vec q=c\vec p\\)</span> would require <span class="math-inline">\\(c=7/4\\)</span> and <span class="math-inline">\\(c=12/7\\)</span>, which are different.

</div></li>
</ol>
</details>

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

<details markdown="1"><summary>Solution</summary>

<ol class="assignment-enumeration" markdown="1">
<li markdown="1">
<div class="assignment-enumeration-label">(i)</div>
<div class="assignment-enumeration-content" markdown="1">

<span class="math-inline">\\(\boxed{\operatorname{rank}(A)=2}\\)</span>. Its columns <span class="math-inline">\\(\vec u,\vec v\\)</span> form a basis of <span class="math-inline">\\(W\\)</span>.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">(ii)</div>
<div class="assignment-enumeration-content" markdown="1">

<span class="math-inline">\\(\boxed{\operatorname{rank}(B)=1}\\)</span>. <span class="math-inline">\\(\vec u\\)</span> is nonzero, and <span class="math-inline">\\(2\vec u\\)</span> adds no new direction. The column space is the line through <span class="math-inline">\\(\vec u\\)</span>.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">(iii)</div>
<div class="assignment-enumeration-content" markdown="1">

<span class="math-inline">\\(\boxed{\operatorname{rank}(C)=2}\\)</span>. <span class="math-inline">\\(\vec x=5\vec u+9\vec v\\)</span> is redundant, so the column space is still <span class="math-inline">\\(W\\)</span>.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">(iv)</div>
<div class="assignment-enumeration-content" markdown="1">

<span class="math-inline">\\(\boxed{\operatorname{rank}(D)=3}\\)</span>. <span class="math-inline">\\(\vec x\\)</span> is redundant, but <span class="math-inline">\\(\vec y\notin W\\)</span>. Since <span class="math-inline">\\(\vec u,\vec v\\)</span> span <span class="math-inline">\\(W\\)</span>, <span class="math-inline">\\(\vec y\\)</span> cannot be made using them. Thus <span class="math-inline">\\(\vec u,\vec v,\vec y\\)</span> form a basis of <span class="math-inline">\\(\operatorname{colsp}(D)\\)</span>.

</div></li>
</ol>
</details>

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

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\boxed{
$$
</div>

\begin{aligned}
4x_1+8x_2-4x_3&=0,

5x_3+15x_4&=0,

0&=0.
\end{aligned}

<div class="math-display">
$$
}
$$
</div>

 The last equation imposes no restriction. The pivot variables are <span class="math-inline">\\(x&#95;1,x&#95;3\\)</span>; the free variables are <span class="math-inline">\\(x&#95;2,x&#95;4\\)</span>.
</details>

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

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(\boxed{\operatorname{rank}(A)=2}\\)</span>.

<ol class="assignment-enumeration" markdown="1">
<li markdown="1">
<div class="assignment-enumeration-label">(i)</div>
<div class="assignment-enumeration-content" markdown="1">

<span class="math-inline">\\(U\\)</span> has <span class="math-inline">\\(2\\)</span> pivots, in columns <span class="math-inline">\\(1\\)</span> and <span class="math-inline">\\(3\\)</span>. The number of pivots is the rank.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">(ii)</div>
<div class="assignment-enumeration-content" markdown="1">

Call the columns of <span class="math-inline">\\(A\\)</span> <span class="math-inline">\\(\vec a&#95;1,\vec a&#95;2,\vec a&#95;3,\vec a&#95;4\\)</span>. They satisfy

<div class="math-display">
$$
\vec a_2=2\vec a_1,\qquad \vec a_4=3\vec a_1+3\vec a_3.
$$
</div>

 So <span class="math-inline">\\(\vec a&#95;1,\vec a&#95;3\\)</span> span the column space. They are independent: their first entries would require <span class="math-inline">\\(\vec a&#95;3=-\vec a&#95;1\\)</span> if they were multiples, but their second entries are <span class="math-inline">\\(-11\\)</span> and <span class="math-inline">\\(16\\)</span>, and <span class="math-inline">\\(-11\ne-16\\)</span>. Thus

<div class="math-display">
$$
\left\{\begin{bmatrix}4\\16\\-12\end{bmatrix},\begin{bmatrix}-4\\-11\\37\end{bmatrix}\right\}
$$
</div>

 is a basis of <span class="math-inline">\\(\operatorname{colsp}(A)\\)</span>. This basis has <span class="math-inline">\\(2\\)</span> vectors, so <span class="math-inline">\\(\dim(\operatorname{colsp}(A))=2\\)</span>.

</div></li>
</ol>
</details>

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

<details markdown="1"><summary>Solution</summary>

Since <span class="math-inline">\\(L\\)</span> is invertible, <span class="math-inline">\\(A\vec x=LU\vec x=\vec0\\)</span> holds exactly when <span class="math-inline">\\(U\vec x=\vec0\\)</span>. We can therefore use the equations from part (a).

Set <span class="math-inline">\\(x&#95;2=s\\)</span> and <span class="math-inline">\\(x&#95;4=t\\)</span>. The second equation gives <span class="math-inline">\\(5x&#95;3+15t=0\\)</span>, so <span class="math-inline">\\(x&#95;3=-3t\\)</span>. The first then gives

<div class="math-display">
$$
4x_1+8s-4(-3t)=0\quad\Longrightarrow\quad x_1=-2s-3t.
$$
</div>

 Thus the complete set of inputs sent to zero is

<div class="math-display">
$$
\boxed{\vec x=s\begin{bmatrix}-2\\1\\0\\0\end{bmatrix}
+t\begin{bmatrix}-3\\0\\-3\\1\end{bmatrix},\qquad s,t\in\mathbb R.}
$$
</div>

 Every choice of <span class="math-inline">\\(s,t\\)</span> satisfies all <span class="math-inline">\\(3\\)</span> equations, and every solution has this form.
</details>

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

<details markdown="1"><summary>Solution</summary>

Let

<div class="math-display">
$$
\vec n_1=\begin{bmatrix}-2\\1\\0\\0\end{bmatrix},\qquad
\vec n_2=\begin{bmatrix}-3\\0\\-3\\1\end{bmatrix}.
$$
</div>

 Part (c) shows that they span <span class="math-inline">\\(\operatorname{nullsp}(A)\\)</span>. They are independent: they are not scalar multiples, as we can see from their second and fourth entries. They therefore form a basis, so <span class="math-inline">\\(\boxed{\dim(\operatorname{nullsp}(A))=2}\\)</span>.

The null space consists of inputs in <span class="math-inline">\\(\mathbb R^4\\)</span>; the column space consists of outputs in <span class="math-inline">\\(\mathbb R^3\\)</span>. Both happen to have dimension <span class="math-inline">\\(2\\)</span> for this matrix, but they are different subspaces.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Show that <span class="math-inline">\\(\operatorname{nullsp}(A)\\)</span> is a subspace: if <span class="math-inline">\\(\vec x,\vec y\in\operatorname{nullsp}(A)\\)</span> and <span class="math-inline">\\(c\in\mathbb R\\)</span>, show that <span class="math-inline">\\(\vec x+\vec y\in\operatorname{nullsp}(A)\\)</span> and <span class="math-inline">\\(c\vec x\in\operatorname{nullsp}(A)\\)</span>.

<em>Hint: You know <span class="math-inline">\\(A\vec x=A\vec y=\vec0\\)</span>. Use this to compute <span class="math-inline">\\(A(\vec x+\vec y)\\)</span> and <span class="math-inline">\\(A(c\vec x)\\)</span>. Also check that <span class="math-inline">\\(\vec0\in\operatorname{nullsp}(A)\\)</span>.</em>

<details markdown="1"><summary>Solution</summary>

We check all <span class="math-inline">\\(3\\)</span> conditions for a subspace of <span class="math-inline">\\(\mathbb R^4\\)</span>.

<ol class="assignment-enumeration" markdown="1">
<li markdown="1">
<div class="assignment-enumeration-label">1.</div>
<div class="assignment-enumeration-content" markdown="1">

**Contains zero.** <span class="math-inline">\\(A\vec0=\vec0\\)</span>, so <span class="math-inline">\\(\vec0\in\operatorname{nullsp}(A)\\)</span>.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">2.</div>
<div class="assignment-enumeration-content" markdown="1">

**Closed under addition.** If <span class="math-inline">\\(\vec x,\vec y\in\operatorname{nullsp}(A)\\)</span>, then <span class="math-inline">\\(A\vec x=\vec0\\)</span> and <span class="math-inline">\\(A\vec y=\vec0\\)</span>. By distributivity,

<div class="math-display">
$$
A(\vec x+\vec y)=A\vec x+A\vec y=\vec0+\vec0=\vec0.
$$
</div>

 Thus <span class="math-inline">\\(\vec x+\vec y\in\operatorname{nullsp}(A)\\)</span>.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">3.</div>
<div class="assignment-enumeration-content" markdown="1">

**Closed under scalar multiplication.** For any <span class="math-inline">\\(c\in\mathbb R\\)</span> and <span class="math-inline">\\(\vec x\in\operatorname{nullsp}(A)\\)</span>,

<div class="math-display">
$$
A(c\vec x)=c(A\vec x)=c\vec0=\vec0.
$$
</div>

 Thus <span class="math-inline">\\(c\vec x\in\operatorname{nullsp}(A)\\)</span>.

</div></li>
</ol>

All <span class="math-inline">\\(3\\)</span> conditions hold, so <span class="math-inline">\\(\operatorname{nullsp}(A)\\)</span> is a subspace of <span class="math-inline">\\(\mathbb R^4\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">f)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) Suppose, for this same <span class="math-inline">\\(A\\)</span>, that <span class="math-inline">\\(A\begin{bmatrix}9\\\\1\\\\2\\\\6\end{bmatrix}=\vec y\\)</span>. Find three other inputs whose output is also <span class="math-inline">\\(\vec y\\)</span>. Then, in vector-parametric form, describe the complete set of vectors <span class="math-inline">\\(\vec v\\)</span> such that <span class="math-inline">\\(A\vec v=\vec y\\)</span>.

<em>Hint: If <span class="math-inline">\\(A\vec v=\vec y\\)</span> and <span class="math-inline">\\(\vec n\in\operatorname{nullsp}(A)\\)</span>, then what is <span class="math-inline">\\(A(\vec v+\vec n)\\)</span>?</em>

<details markdown="1"><summary>Solution</summary>

Let <span class="math-inline">\\(\vec v&#95;0\\)</span> be the given input, so <span class="math-inline">\\(A\vec v&#95;0=\vec y\\)</span>. If <span class="math-inline">\\(\vec n\in\operatorname{nullsp}(A)\\)</span>, then

<div class="math-display">
$$
A(\vec v_0+\vec n)=A\vec v_0+A\vec n=\vec y+\vec0=\vec y.
$$
</div>

 Using the null-space basis from part (d), we obtain <span class="math-inline">\\(3\\)</span> other inputs:

<div class="math-display">
$$
\vec v_0+\vec n_1=\boxed{\begin{bmatrix}7\\2\\2\\6\end{bmatrix}},\qquad
\vec v_0+\vec n_2=\boxed{\begin{bmatrix}6\\1\\-1\\7\end{bmatrix}},\qquad
\vec v_0+\vec n_1+\vec n_2=\boxed{\begin{bmatrix}4\\2\\-1\\7\end{bmatrix}}.
$$
</div>

 The complete set is

<div class="math-display">
$$
\boxed{\vec v=\begin{bmatrix}9\\1\\2\\6\end{bmatrix}
+s\begin{bmatrix}-2\\1\\0\\0\end{bmatrix}
+t\begin{bmatrix}-3\\0\\-3\\1\end{bmatrix},\qquad s,t\in\mathbb R.}
$$
</div>

 Why does this give *every* input with output <span class="math-inline">\\(\vec y\\)</span>? If <span class="math-inline">\\(A\vec v=\vec y\\)</span>, then

<div class="math-display">
$$
A(\vec v-\vec v_0)=A\vec v-A\vec v_0=\vec y-\vec y=\vec0.
$$
</div>

 Thus <span class="math-inline">\\(\vec v-\vec v&#95;0\in\operatorname{nullsp}(A)\\)</span>, so it equals <span class="math-inline">\\(s\vec n&#95;1+t\vec n&#95;2\\)</span> for some <span class="math-inline">\\(s,t\\)</span>. No new system needs to be solved.
</details>

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

<details markdown="1"><summary>Solution</summary>

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
<td style="text-align: center;"><span class="math-inline">\(2\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(2\)</span></td>
</tr>
<tr>
<td style="text-align: center;"><span class="math-inline">\(5\times7\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(5\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(2\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(2\)</span></td>
</tr>
<tr>
<td style="text-align: center;"><span class="math-inline">\(n\times d\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(r\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(d-r\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(d-r\)</span></td>
</tr>
</tbody>
</table>

There are <span class="math-inline">\\(d\\)</span> input variables. Of these, <span class="math-inline">\\(r\\)</span> are pivot variables, so the remaining <span class="math-inline">\\(d-r\\)</span> are free. In a vector-parametric description of the zero-output inputs, each free variable supplies a basis vector. Hence

<div class="math-display">
$$
\boxed{\operatorname{rank}(A)+\dim(\operatorname{nullsp}(A))=d.}
$$
</div>

 The total is the number of *columns*, because that is the number of entries in each input.
</details>
</div>
</div>

</div>

{% endraw %}
