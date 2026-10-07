---
layout: page
title: "Lab 6: Matrix-Vector Multiplication"
description: "Lab 6: Matrix-Vector Multiplication activities."
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

# Lab 6: Matrix-Vector Multiplication

**due** by the end of class on Wednesday, October 7, 2026

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab06/lab06.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab06/lab06-solutions.pdf" target="_blank">Solutions PDF ✅</a>
<a class="btn btn-info assignment-pdf-button colab-btn" href="https://colab.research.google.com/github/math-124/fa26-code/blob/main/labs/lab06/lab06.ipynb" target="_blank"><img src="/assets/site-images/google-colab.png" alt="" aria-hidden="true"> Google Colab</a>
</div>

{: .yellow }
<div markdown="1">
Each lab worksheet will contain several activities, most of which will involve writing math on paper, and some of which will involve running code in a Jupyter Notebook. Lab activities are meant to last an hour, and the second hour of lab is dedicated to starting the homework assignment. To receive credit for a lab, you must show your lab TA your work on both the lab worksheet and homework assignment.

While you must get checked off by your lab TA **individually**, we encourage you to form groups with 1-2 other students to complete the activities together.
</div>

---

## Activities

- [Activity 1: Is the expression valid?](#activity-1-is-the-expression-valid)
- [Activity 2: Fundamentals](#activity-2-fundamentals)
- [Activity 3: Shuffle and stretch](#activity-3-shuffle-and-stretch)
- [Activity 4: Mystery matrices](#activity-4-mystery-matrices)
- [Activity 5: Drawing projections](#activity-5-drawing-projections)
- [Activity 6: Programming: Matrix-Vector Multiplication](#activity-6-programming-matrix-vector-multiplication)

---

This content is covered in [Chapter 3.1](https://notes.math124.org/ch03/03-01/) and [Chapter 3.2](https://notes.math124.org/ch03/03-02/) of the course notes, which are now posted. Have these open while working on the worksheet. Homework 5 will be released on Friday.

---

## Activity 1: Is the expression valid?

Suppose:

-   <span class="math-inline">\\(A\in\mathbb R^{5\times3}\\)</span>.

-   <span class="math-inline">\\(B\in\mathbb R^{3\times4}\\)</span>.

-   <span class="math-inline">\\(\vec u\in\mathbb R^4\\)</span>.

-   <span class="math-inline">\\(\vec v\in\mathbb R^3\\)</span>.

Draw a circle around each valid expression and ~~cross out~~ each invalid expression. An expression is valid if the shapes allow the operation shown. **Since you don't actually know <span class="math-inline">\\(A\\)</span>, <span class="math-inline">\\(B\\)</span>, <span class="math-inline">\\(\vec u\\)</span>, and <span class="math-inline">\\(\vec v\\)</span>, you can't actually do the calculation.**

<table>
<tbody>
<tr>
<td style="text-align: left;"><span class="math-inline">\(A\vec v\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\vec v A\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(B\vec u\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(B\vec v\)</span></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math-inline">\(B\vec u+\vec v\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(A\vec v+\vec u\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\vec u\cdot\vec v\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\vec v\cdot\vec v\)</span></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math-inline">\((B\vec u)\cdot\vec v\)</span></td>
<td style="text-align: left;"><span class="math-inline">\((A\vec v)\cdot(B\vec u)\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\|A\vec v\|^2\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\|\vec u+\vec v\|\)</span></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math-inline">\(A(B\vec u)\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(B\vec u-3\vec v\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\vec u+2\vec u\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\|B\vec u\|^2+\|\vec v\|^2\)</span></td>
</tr>
</tbody>
</table>

Compare with your group. Explain any disagreements using the shapes.

<details markdown="1"><summary>Solution</summary>

Here <span class="math-inline">\\(A\\)</span> has shape <span class="math-inline">\\(5\times3\\)</span>, <span class="math-inline">\\(B\\)</span> has shape <span class="math-inline">\\(3\times4\\)</span>, <span class="math-inline">\\(\vec u\\)</span> has shape <span class="math-inline">\\(4\times1\\)</span> (it is a vector in <span class="math-inline">\\(\mathbb R^4\\)</span>), and <span class="math-inline">\\(\vec v\\)</span> has shape <span class="math-inline">\\(3\times1\\)</span> (it is a vector in <span class="math-inline">\\(\mathbb R^3\\)</span>). Thus <span class="math-inline">\\(A\vec v\\)</span> has shape <span class="math-inline">\\(5\times1\\)</span> (it is a vector in <span class="math-inline">\\(\mathbb R^5\\)</span>) and <span class="math-inline">\\(B\vec u\\)</span> has shape <span class="math-inline">\\(3\times1\\)</span> (it is a vector in <span class="math-inline">\\(\mathbb R^3\\)</span>).

<table>
<thead>
<tr>
<th style="text-align: left;">Expression</th>
<th style="text-align: left;">Valid?</th>
<th style="text-align: left;">Reason or shape of the result</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><span class="math-inline">\(A\vec v\)</span></td>
<td style="text-align: left;">Valid</td>
<td style="text-align: left;"><span class="math-inline">\(A\)</span> has 3 columns and <span class="math-inline">\(\vec v\)</span> has 3 entries; result <span class="math-inline">\(5\times1\)</span> (it is a vector in <span class="math-inline">\(\mathbb R^5\)</span>).</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math-inline">\(\vec v A\)</span></td>
<td style="text-align: left;">Invalid</td>
<td style="text-align: left;"><span class="math-inline">\(\vec v\)</span> has shape <span class="math-inline">\(3\times1\)</span> (it is a vector in <span class="math-inline">\(\mathbb R^3\)</span>). The inner numbers in <span class="math-inline">\((3\times1)(5\times3)\)</span> do not match: <span class="math-inline">\(1\ne5\)</span>.</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math-inline">\(B\vec u\)</span></td>
<td style="text-align: left;">Valid</td>
<td style="text-align: left;"><span class="math-inline">\(B\)</span> has 4 columns and <span class="math-inline">\(\vec u\)</span> has 4 entries; result <span class="math-inline">\(3\times1\)</span> (it is a vector in <span class="math-inline">\(\mathbb R^3\)</span>).</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math-inline">\(B\vec v\)</span></td>
<td style="text-align: left;">Invalid</td>
<td style="text-align: left;"><span class="math-inline">\(B\)</span> needs 4 entries, but <span class="math-inline">\(\vec v\)</span> has 3.</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math-inline">\(B\vec u+\vec v\)</span></td>
<td style="text-align: left;">Valid</td>
<td style="text-align: left;">Each vector has shape <span class="math-inline">\(3\times1\)</span> (it is a vector in <span class="math-inline">\(\mathbb R^3\)</span>).</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math-inline">\(A\vec v+\vec u\)</span></td>
<td style="text-align: left;">Invalid</td>
<td style="text-align: left;">The shapes <span class="math-inline">\(5\times1\)</span> (it is a vector in <span class="math-inline">\(\mathbb R^5\)</span>) and <span class="math-inline">\(4\times1\)</span> (it is a vector in <span class="math-inline">\(\mathbb R^4\)</span>) differ.</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math-inline">\(\vec u\cdot\vec v\)</span></td>
<td style="text-align: left;">Invalid</td>
<td style="text-align: left;">A dot product needs the same number of entries: <span class="math-inline">\(4\ne3\)</span>.</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math-inline">\(\vec v\cdot\vec v\)</span></td>
<td style="text-align: left;">Valid</td>
<td style="text-align: left;">Both have 3 entries; the result is a scalar.</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math-inline">\((B\vec u)\cdot\vec v\)</span></td>
<td style="text-align: left;">Valid</td>
<td style="text-align: left;">Both have 3 entries; the result is a scalar.</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math-inline">\((A\vec v)\cdot(B\vec u)\)</span></td>
<td style="text-align: left;">Invalid</td>
<td style="text-align: left;">The vectors have 5 and 3 entries.</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math-inline">\(\|A\vec v\|^2\)</span></td>
<td style="text-align: left;">Valid</td>
<td style="text-align: left;"><span class="math-inline">\(A\vec v\)</span> exists; its squared length is a scalar.</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math-inline">\(\|\vec u+\vec v\|\)</span></td>
<td style="text-align: left;">Invalid</td>
<td style="text-align: left;">The sum inside is not defined.</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math-inline">\(A(B\vec u)\)</span></td>
<td style="text-align: left;">Valid</td>
<td style="text-align: left;"><span class="math-inline">\(B\vec u\)</span> has 3 entries, as <span class="math-inline">\(A\)</span> needs; result <span class="math-inline">\(5\times1\)</span> (it is a vector in <span class="math-inline">\(\mathbb R^5\)</span>).</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math-inline">\(B\vec u-3\vec v\)</span></td>
<td style="text-align: left;">Valid</td>
<td style="text-align: left;">Each vector has shape <span class="math-inline">\(3\times1\)</span> (it is a vector in <span class="math-inline">\(\mathbb R^3\)</span>).</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math-inline">\(\vec u+2\vec u\)</span></td>
<td style="text-align: left;">Valid</td>
<td style="text-align: left;">Each vector has shape <span class="math-inline">\(4\times1\)</span> (it is a vector in <span class="math-inline">\(\mathbb R^4\)</span>).</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math-inline">\(\|B\vec u\|^2+\|\vec v\|^2\)</span></td>
<td style="text-align: left;">Valid</td>
<td style="text-align: left;">Both squared lengths are scalars, so they can be added.</td>
</tr>
</tbody>
</table>
</details>

---

## Activity 2: Fundamentals

Let

<div class="math-display">
$$
A=\begin{bmatrix}4&-3&6\\-2&5&1\end{bmatrix},\qquad
\vec v=\begin{bmatrix}-2\\3\\4\end{bmatrix},\qquad
B=\begin{bmatrix}2&-1\\-3&4\\5&2\end{bmatrix}.
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Compute <span class="math-inline">\\(A\vec v\\)</span>. What are the shapes of <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(A\vec v\\)</span>?

<details markdown="1"><summary>Solution</summary>

Using a dot product with each row,

<div class="math-display">
$$
A\vec v
=\begin{bmatrix}4(-2)+(-3)(3)+6(4)\\(-2)(-2)+5(3)+1(4)\end{bmatrix}
=\boxed{\begin{bmatrix}7\\23\end{bmatrix}}.
$$
</div>

 The shape of <span class="math-inline">\\(\vec v\\)</span> is <span class="math-inline">\\(3\times1\\)</span> (it is a vector in <span class="math-inline">\\(\mathbb R^3\\)</span>); the shape of <span class="math-inline">\\(A\vec v\\)</span> is <span class="math-inline">\\(2\times1\\)</span> (it is a vector in <span class="math-inline">\\(\mathbb R^2\\)</span>).
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Compute <span class="math-inline">\\(B(A\vec v)\\)</span>. What is its shape?

<details markdown="1"><summary>Solution</summary>

Multiply <span class="math-inline">\\(B\\)</span> by the result from part (a):

<div class="math-display">
$$
B(A\vec v)
=\begin{bmatrix}2&-1\\-3&4\\5&2\end{bmatrix}
\begin{bmatrix}7\\23\end{bmatrix}
=\begin{bmatrix}14-23\\-21+92\\35+46\end{bmatrix}
=\boxed{\begin{bmatrix}-9\\71\\81\end{bmatrix}}.
$$
</div>

 Its shape is <span class="math-inline">\\(3\times1\\)</span> (it is a vector in <span class="math-inline">\\(\mathbb R^3\\)</span>).
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Is <span class="math-inline">\\(B\vec v\\)</span> defined? Explain. Explain why <span class="math-inline">\\(B(A\vec v)\\)</span> can be defined even when <span class="math-inline">\\(B\vec v\\)</span> is not.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(B\vec v\\)</span> is not defined: <span class="math-inline">\\(B\\)</span> has 2 columns, but <span class="math-inline">\\(\vec v\\)</span> has 3 entries. However, <span class="math-inline">\\(A\vec v\\)</span> has 2 entries. Therefore it has the shape needed to multiply by <span class="math-inline">\\(B\\)</span>. We compute <span class="math-inline">\\(A\vec v\\)</span> first and then apply <span class="math-inline">\\(B\\)</span>.
</details>

</div>
</div>

</div>

---

## Activity 3: Shuffle and stretch

Let

<div class="math-display">
$$
S=\begin{bmatrix}0&1&0\\0&0&1\\1&0&0\end{bmatrix},\qquad
D=\begin{bmatrix}5&0&0\\0&-2&0\\0&0&1/3\end{bmatrix},\qquad
\vec x=\begin{bmatrix}-4\\7\\9\end{bmatrix}.
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Compute <span class="math-inline">\\(S\vec x\\)</span> and <span class="math-inline">\\(D\vec x\\)</span>. Describe in words what each matrix does to the entries of an input vector.

<details markdown="1"><summary>Solution</summary>

The rows of <span class="math-inline">\\(S\\)</span> pick out the second, third, and first entries, in that order:

<div class="math-display">
$$
S\vec x=\boxed{\begin{bmatrix}7\\9\\-4\end{bmatrix}},
\qquad
D\vec x=\begin{bmatrix}5(-4)\\(-2)(7)\\(1/3)(9)\end{bmatrix}
=\boxed{\begin{bmatrix}-20\\-14\\3\end{bmatrix}}.
$$
</div>

 <span class="math-inline">\\(S\\)</span> moves the first entry to the bottom and moves the other two up one position. <span class="math-inline">\\(D\\)</span> multiplies the first entry by <span class="math-inline">\\(5\\)</span>, the second by <span class="math-inline">\\(-2\\)</span>, and the third by <span class="math-inline">\\(1/3\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Compute <span class="math-inline">\\(S(D\vec x)\\)</span> and <span class="math-inline">\\(D(S\vec x)\\)</span>.

<details markdown="1"><summary>Solution</summary>

Apply the matrices one at a time:

<div class="math-display">
$$
S(D\vec x)=S\begin{bmatrix}-20\\-14\\3\end{bmatrix}
=\boxed{\begin{bmatrix}-14\\3\\-20\end{bmatrix}},
\qquad
D(S\vec x)=D\begin{bmatrix}7\\9\\-4\end{bmatrix}
=\boxed{\begin{bmatrix}35\\-18\\-4/3\end{bmatrix}}.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Why are <span class="math-inline">\\(S(D\vec x)\\)</span> and <span class="math-inline">\\(D(S\vec x)\\)</span> different? Explain using what <span class="math-inline">\\(S\\)</span> and <span class="math-inline">\\(D\\)</span> do to the entries of a vector.

<details markdown="1"><summary>Solution</summary>

The scaling factor depends on an entry's position. In <span class="math-inline">\\(S(D\vec x)\\)</span>, the original second entry, <span class="math-inline">\\(7\\)</span>, is first multiplied by <span class="math-inline">\\(-2\\)</span> and then moved to the first position, giving <span class="math-inline">\\(-14\\)</span>. In <span class="math-inline">\\(D(S\vec x)\\)</span>, it is first moved to the first position and then multiplied by <span class="math-inline">\\(5\\)</span>, giving <span class="math-inline">\\(35\\)</span>. The same change of position changes which factor is applied to the other entries, too.
</details>

</div>
</div>

</div>

---

## Activity 4: Mystery matrices

There is a matrix <span class="math-inline">\\(A\\)</span>, but we have not been given its entries.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Suppose

<div class="math-display">
$$
A\begin{bmatrix}1\\0\end{bmatrix}=\begin{bmatrix}5\\-2\\12\end{bmatrix}.
$$
</div>

 What does this tell you about <span class="math-inline">\\(A\\)</span>?

<details markdown="1"><summary>Solution</summary>

Multiplication by <span class="math-inline">\\(\begin{bmatrix}1\\\\0\end{bmatrix}\\)</span> takes one copy of the first column and zero copies of the second column. Therefore the first column of <span class="math-inline">\\(A\\)</span> is <span class="math-inline">\\(\begin{bmatrix}5\\\\-2\\\\12\end{bmatrix}\\)</span>. The given input and output also show that <span class="math-inline">\\(A\\)</span> has shape <span class="math-inline">\\(3\times2\\)</span>. Its second column is not yet determined.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
We also know that

<div class="math-display">
$$
A\begin{bmatrix}0\\1\end{bmatrix}=\begin{bmatrix}10\\0\\1\end{bmatrix}.
$$
</div>

 What does this tell you about <span class="math-inline">\\(A\\)</span>? Use both pieces of information to write <span class="math-inline">\\(A\\)</span>.

<details markdown="1"><summary>Solution</summary>

Multiplication by <span class="math-inline">\\(\begin{bmatrix}0\\\\1\end{bmatrix}\\)</span> selects the second column. Therefore

<div class="math-display">
$$
\boxed{A=\begin{bmatrix}5&10\\-2&0\\12&1\end{bmatrix}}.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
There is another matrix <span class="math-inline">\\(B\\)</span>. We know only that

<div class="math-display">
$$
B\begin{bmatrix}1\\0\\0\end{bmatrix}=\begin{bmatrix}15\\3\\4\\2\end{bmatrix},\qquad
B\begin{bmatrix}0\\1\\0\end{bmatrix}=\begin{bmatrix}-6\\11\\0\\-5\end{bmatrix},\qquad
B\begin{bmatrix}0\\0\\1\end{bmatrix}=\begin{bmatrix}2\\-7\\9\\6\end{bmatrix}.
$$
</div>

 Using just this information, find <span class="math-inline">\\(B\begin{bmatrix}-2\\\\1\\\\3\end{bmatrix}\\)</span>. Explain how you used the three given outputs.

<details markdown="1"><summary>Solution</summary>

The three given outputs are the three columns of <span class="math-inline">\\(B\\)</span>:

<div class="math-display">
$$
B=\begin{bmatrix}15&-6&2\\3&11&-7\\4&0&9\\2&-5&6\end{bmatrix}.
$$
</div>

 By the column-combination interpretation of matrix-vector multiplication,

<div class="math-display">
$$
\begin{aligned}
B\begin{bmatrix}-2\\1\\3\end{bmatrix}
&=-2\begin{bmatrix}15\\3\\4\\2\end{bmatrix}
+\begin{bmatrix}-6\\11\\0\\-5\end{bmatrix}
+3\begin{bmatrix}2\\-7\\9\\6\end{bmatrix}\\[0.6em]
&=\begin{bmatrix}-30-6+6\\-6+11-21\\-8+0+27\\-4-5+18\end{bmatrix}
=\boxed{\begin{bmatrix}-30\\-16\\19\\9\end{bmatrix}}.
\end{aligned}
$$
</div>

 The coefficients <span class="math-inline">\\(-2\\)</span>, <span class="math-inline">\\(1\\)</span>, and <span class="math-inline">\\(3\\)</span> are the entries of the input vector. Thus the three known outputs give exactly the column vectors needed for this calculation.
</details>

</div>
</div>

</div>

---

## Activity 5: Drawing projections

Let <span class="math-inline">\\(\ell=\operatorname{span}(\vec w)\\)</span>, where

<div class="math-display">
$$
\vec w=\begin{bmatrix}3/5\\4/5\end{bmatrix},\qquad \vec v=\begin{bmatrix}7\\1\end{bmatrix}.
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
First, let's refresh: find <span class="math-inline">\\(\operatorname{proj}&#95;{\ell}(\vec v)\\)</span> the usual way.

<details markdown="1"><summary>Solution</summary>

Here <span class="math-inline">\\(\vec w=\begin{bmatrix}3/5\\\\4/5\end{bmatrix}\\)</span> has length <span class="math-inline">\\(1\\)</span>, since <span class="math-inline">\\((3/5)^2+(4/5)^2=1\\)</span>. The usual unit-vector projection formula gives

<div class="math-display">
$$
\vec v\cdot\vec w=7\left(\frac35\right)+1\left(\frac45\right)=5.
$$
</div>



<div class="math-display">
$$
\operatorname{proj}_{\ell}(\vec v)
=(\vec v\cdot\vec w)\vec w
=5\begin{bmatrix}3/5\\4/5\end{bmatrix}
=\boxed{\begin{bmatrix}3\\4\end{bmatrix}}.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
We can also project onto <span class="math-inline">\\(\ell\\)</span> by multiplying by a matrix. A **projection matrix** <span class="math-inline">\\(P\\)</span> satisfies <span class="math-inline">\\(P\vec v=\operatorname{proj}&#95;{\ell}(\vec v)\\)</span> for every input <span class="math-inline">\\(\vec v\\)</span>. If a unit vector <span class="math-inline">\\(\vec w=\begin{bmatrix}w&#95;1\\\\w&#95;2\end{bmatrix}\\)</span> spans <span class="math-inline">\\(\ell\\)</span>, then

<div class="math-display">
$$
P=\begin{bmatrix}w_1^2&w_1w_2\\w_1w_2&w_2^2\end{bmatrix}.
$$
</div>

 Find <span class="math-inline">\\(P\\)</span> for this line, then find <span class="math-inline">\\(P\vec v\\)</span>. Compare with your answer in part (a). What do you notice about the columns of <span class="math-inline">\\(P\\)</span>?

<details markdown="1"><summary>Solution</summary>

Substitute <span class="math-inline">\\(w&#95;1=3/5\\)</span> and <span class="math-inline">\\(w&#95;2=4/5\\)</span> into the supplied formula:

<div class="math-display">
$$
\boxed{P=\begin{bmatrix}9/25&12/25\\12/25&16/25\end{bmatrix}}.
$$
</div>



<div class="math-display">
$$
P\vec v
=\begin{bmatrix}(9/25)7+(12/25)1\\(12/25)7+(16/25)1\end{bmatrix}
=\begin{bmatrix}75/25\\100/25\end{bmatrix}
=\boxed{\begin{bmatrix}3\\4\end{bmatrix}}.
$$
</div>

 This agrees with part (a). Both columns of <span class="math-inline">\\(P\\)</span> lie on <span class="math-inline">\\(\ell\\)</span>:

<div class="math-display">
$$
\begin{bmatrix}9/25\\12/25\end{bmatrix}=\frac35\vec w,
\qquad
\begin{bmatrix}12/25\\16/25\end{bmatrix}=\frac45\vec w.
$$
</div>

 Every product <span class="math-inline">\\(P\vec z\\)</span> is a combination of these columns, so it is also a multiple of <span class="math-inline">\\(\vec w\\)</span> and lies on <span class="math-inline">\\(\ell\\)</span>.
</details>

**Activity 5: Drawing projections (continued)**

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Use <span class="math-inline">\\(P\\)</span> to find the projection onto <span class="math-inline">\\(\ell\\)</span> of <span class="math-inline">\\(\vec u=\begin{bmatrix}-4\\\\5\end{bmatrix}\\)</span>. On the coordinate axes below, draw <span class="math-inline">\\(\ell\\)</span> and the four vectors <span class="math-inline">\\(\vec u\\)</span>, <span class="math-inline">\\(\vec v\\)</span>, <span class="math-inline">\\(P\vec u\\)</span>, and <span class="math-inline">\\(P\vec v\\)</span>, all starting at the origin. What do you notice?

<img src="imgs/lab06-plot-01.png" alt="Coordinate diagram" class="assignment-vector-plot">

<details markdown="1"><summary>Solution</summary>

For <span class="math-inline">\\(\vec u=\begin{bmatrix}-4\\\\5\end{bmatrix}\\)</span>,

<div class="math-display">
$$
P\vec u=\begin{bmatrix}(9/25)(-4)+(12/25)5\\(12/25)(-4)+(16/25)5\end{bmatrix}
=\boxed{\begin{bmatrix}24/25\\32/25\end{bmatrix}}.
$$
</div>

 In the sketch, both <span class="math-inline">\\(P\vec u\\)</span> and <span class="math-inline">\\(P\vec v\\)</span> lie on <span class="math-inline">\\(\ell\\)</span>. The dashed segments from each original tip to its projected tip are perpendicular to <span class="math-inline">\\(\ell\\)</span>.

<div style="text-align: center;">
<img src="imgs/lab06-plot-02.png" alt="Coordinate diagram" class="assignment-vector-plot">
</div>
</details>

</div>
</div>

</div>

---

## Activity 6: Programming: Matrix-Vector Multiplication

This lab has a programming notebook to help you visualize various matrix-vector operations, and to show you how matrix-vector multiplication works in Python.

To open the notebook for Lab 6, click the Google Colab link under "Code" on the course website for Lab 6. Instructions on how to use Google Colab are at [math124.org/running-code](https://math124.org/running-code). If you are viewing the lab worksheet after it has been posted, [this direct link](https://colab.research.google.com/github/math-124/fa26-code/blob/main/labs/lab06/lab06.ipynb) will work, too. To receive credit for the programming component of the lab, work through the entire notebook and show your lab TA your work.

{% endraw %}
