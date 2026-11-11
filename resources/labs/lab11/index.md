---
layout: page
title: "Lab 11: Gram-Schmidt and QR Factorization"
description: "Lab 11: Gram-Schmidt and QR Factorization activities."
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

# Lab 11: Gram-Schmidt and QR Factorization

**due** by the end of class on Wednesday, November 11, 2026

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab11/lab11.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab11/lab11-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
Each lab worksheet will contain several activities, most of which will involve writing math on paper, and some of which will involve running code in a Jupyter Notebook. Lab activities are meant to last an hour, and the second hour of lab is dedicated to starting the homework assignment. To receive credit for a lab, you must show your lab TA your work on both the lab worksheet and homework assignment.

While you must get checked off by your lab TA **individually**, we encourage you to form groups with 1-2 other students to complete the activities together.
</div>

---

## Activities

- [Activity 1: A $2\times2$ QR factorization](#activity-1-a-2times2-qr-factorization)
- [Activity 2: A $3\times3$ QR factorization](#activity-2-a-3times3-qr-factorization)

---

## Activity 1: A <span class="math-inline">\\(2\times2\\)</span> QR factorization

Consider the matrix

<div class="math-display">
$$
A=\begin{bmatrix}5&-7\\12&17\end{bmatrix}.
$$
</div>

 Call its columns <span class="math-inline">\\(\vec v&#95;1,\vec v&#95;2\\)</span>, in that order. Our goal is to find a QR factorization of <span class="math-inline">\\(A\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
First, use the Gram-Schmidt process to find an orthonormal basis <span class="math-inline">\\(\vec u&#95;1,\vec u&#95;2\\)</span> of <span class="math-inline">\\(\operatorname{colsp}(A)\\)</span>.

<details markdown="1"><summary>Solution</summary>

The first column has length <span class="math-inline">\\(\|\vec v&#95;1\|=\sqrt{5^2+12^2}=13\\)</span>, so

<div class="math-display">
$$
\vec u_1=\frac1{13}\begin{bmatrix}5\\12\end{bmatrix},\qquad
\vec v_2\cdot\vec u_1=\frac{-35+204}{13}=13.
$$
</div>

Then

<div class="math-display">
$$
\vec w_2=\vec v_2-13\vec u_1
=\begin{bmatrix}-7\\17\end{bmatrix}-\begin{bmatrix}5\\12\end{bmatrix}
=\begin{bmatrix}-12\\5\end{bmatrix}.
$$
</div>

Its length is also <span class="math-inline">\\(13\\)</span>, giving <span class="math-inline">\\(\vec u&#95;2=\frac1{13}\begin{bmatrix}-12\\\\5\end{bmatrix}\\)</span>.

The Gram-Schmidt process preserves the span: <span class="math-inline">\\(\vec u&#95;1,\vec u&#95;2\\)</span> are combinations of the original columns, and the equations in part (b) recover those columns. Thus they form an orthonormal basis of <span class="math-inline">\\(\operatorname{colsp}(A)\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Write the relationships between the original vectors (<span class="math-inline">\\(\vec v&#95;1\\)</span> and <span class="math-inline">\\(\vec v&#95;2\\)</span>) and the orthonormal basis vectors (<span class="math-inline">\\(\vec u&#95;1\\)</span> and <span class="math-inline">\\(\vec u&#95;2\\)</span>). Use these equations to find <span class="math-inline">\\(Q\\)</span> and <span class="math-inline">\\(R\\)</span> such that <span class="math-inline">\\(A=QR\\)</span>.

<details markdown="1"><summary>Solution</summary>

Undoing the normalization and projection steps gives the relationships <span class="math-inline">\\(\vec v&#95;1=13\vec u&#95;1\\)</span> and <span class="math-inline">\\(\vec v&#95;2=13\vec u&#95;1+13\vec u&#95;2\\)</span>. Thus

<div class="math-display">
$$
Q=\frac1{13}\begin{bmatrix}5&-12\\12&5\end{bmatrix},\qquad
R=\begin{bmatrix}13&13\\0&13\end{bmatrix}.
$$
</div>

Each column of <span class="math-inline">\\(R\\)</span> records the coefficients of one original vector in the orthonormal basis; the columns of <span class="math-inline">\\(Q\\)</span> are <span class="math-inline">\\(\vec u&#95;1\\)</span> and <span class="math-inline">\\(\vec u&#95;2\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Verify that <span class="math-inline">\\(QR=A\\)</span> and that the columns of <span class="math-inline">\\(Q\\)</span> are orthonormal.

<details markdown="1"><summary>Solution</summary>

Both columns have squared length <span class="math-inline">\\((25+144)/169=1\\)</span>, and their dot product is <span class="math-inline">\\((-60+60)/169=0\\)</span>. Also,

<div class="math-display">
$$
QR=\frac1{13}\begin{bmatrix}65&65-156\\156&156+65\end{bmatrix}
=\begin{bmatrix}5&-7\\12&17\end{bmatrix}=A.
$$
</div>

</details>

</div>
</div>
</div>

---

**Gram-Schmidt with three vectors**

We'll now consider the case of three vectors. Suppose that <span class="math-inline">\\(A\\)</span> is a matrix whose columns <span class="math-inline">\\(\vec v&#95;1,\vec v&#95;2,\vec v&#95;3\\)</span> are linearly independent. We want to use the Gram-Schmidt method to construct an orthonormal basis <span class="math-inline">\\(\vec u&#95;1,\vec u&#95;2,\vec u&#95;3\\)</span> of their span and find the QR factorization of <span class="math-inline">\\(A\\)</span>. The first two steps are just what we've already done.

-   **First vector: normalize.** Divide by its length:

<div class="math-display">
$$
\vec u_1=\frac{\vec v_1}{\|\vec v_1\|}.
$$
</div>

-   **Second vector: subtract one projection, then normalize.** Let <span class="math-inline">\\(\ell&#95;1=\operatorname{span}(\vec u&#95;1)\\)</span>. Remove the part of <span class="math-inline">\\(\vec v&#95;2\\)</span> along this line:

<div class="math-display">
$$
\vec w_2=\vec v_2-\operatorname{proj}_{\ell_1}(\vec v_2)
    =\vec v_2-(\vec v_2\cdot\vec u_1)\vec u_1,
    \qquad \vec u_2=\frac{\vec w_2}{\|\vec w_2\|}.
$$
</div>

-   **Third vector: subtract two projections, then normalize.** Here's the new step. We want a vector perpendicular to both <span class="math-inline">\\(\vec u&#95;1\\)</span> and <span class="math-inline">\\(\vec u&#95;2\\)</span>. Let <span class="math-inline">\\(\ell&#95;2=\operatorname{span}(\vec u&#95;2)\\)</span>. Subtract the parts along both lines:



<div class="math-display">
$$
\begin{align*}
    \vec w_3&=\vec v_3-\operatorname{proj}_{\ell_1}(\vec v_3)-\operatorname{proj}_{\ell_2}(\vec v_3)\\
    &=\vec v_3-(\vec v_3\cdot\vec u_1)\vec u_1-(\vec v_3\cdot\vec u_2)\vec u_2,
    \qquad \vec u_3=\frac{\vec w_3}{\|\vec w_3\|}.
    \end{align*}
$$
</div>

Because <span class="math-inline">\\(\vec u&#95;1\\)</span> and <span class="math-inline">\\(\vec u&#95;2\\)</span> are perpendicular, removing the component along one doesn't change the component along the other. What's left is perpendicular to both. The remaining vectors <span class="math-inline">\\(\vec w&#95;2,\vec w&#95;3\\)</span> cannot be zero, because the original columns are independent.

**How does this give <span class="math-inline">\\(A=QR\\)</span>?** First record how the old vectors relate to the new ones. Put back the components we subtracted:

<div class="math-display">
$$
\begin{align*}
\vec v_1&=\boxed{\|\vec v_1\|}\vec u_1,\\
\vec v_2&=\boxed{(\vec v_2\cdot\vec u_1)}\vec u_1+\boxed{\|\vec w_2\|}\vec u_2,\\
\vec v_3&=\boxed{(\vec v_3\cdot\vec u_1)}\vec u_1+\boxed{(\vec v_3\cdot\vec u_2)}\vec u_2+\boxed{\|\vec w_3\|}\vec u_3.
\end{align*}
$$
</div>

These equations can be written together as

<div class="math-display">
$$
\underbrace{\begin{bmatrix}|&|&|\\\vec v_1&\vec v_2&\vec v_3\\|&|&|\end{bmatrix}}_{A}
=\underbrace{\begin{bmatrix}|&|&|\\\vec u_1&\vec u_2&\vec u_3\\|&|&|\end{bmatrix}}_{Q}
\underbrace{\begin{bmatrix}
\|\vec v_1\|&\vec v_2\cdot\vec u_1&\vec v_3\cdot\vec u_1\\
0&\|\vec w_2\|&\vec v_3\cdot\vec u_2\\
0&0&\|\vec w_3\|
\end{bmatrix}}_{R}.
$$
</div>

 So <span class="math-inline">\\(Q\\)</span> contains the orthonormal vectors, and each column of <span class="math-inline">\\(R\\)</span> contains the coefficients for one original vector. The diagonal entries are the lengths we divided by; the entries above them are the dot products we used for the projections. Keep these numbers as you work!

---

## Activity 2: A <span class="math-inline">\\(3\times3\\)</span> QR factorization

Now consider the matrix

<div class="math-display">
$$
A=\begin{bmatrix}2&5&-2\\-2&-2&5\\1&4&5\end{bmatrix}.
$$
</div>

 Our goal is to find a QR factorization of <span class="math-inline">\\(A\\)</span>. To start, we'll apply the Gram-Schmidt process to <span class="math-inline">\\(A\\)</span>. Call <span class="math-inline">\\(A\\)</span>'s columns <span class="math-inline">\\(\vec v&#95;1\\)</span>, <span class="math-inline">\\(\vec v&#95;2\\)</span>, and <span class="math-inline">\\(\vec v&#95;3\\)</span>, in that order.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find <span class="math-inline">\\(\vec u&#95;1\\)</span>, then subtract the component of <span class="math-inline">\\(\vec v&#95;2\\)</span> along <span class="math-inline">\\(\vec u&#95;1\\)</span> and normalize to find <span class="math-inline">\\(\vec u&#95;2\\)</span>.

<details markdown="1"><summary>Solution</summary>

The first column has length <span class="math-inline">\\(\sqrt{2^2+(-2)^2+1^2}=3\\)</span>, so

<div class="math-display">
$$
\vec u_1=\frac13\begin{bmatrix}2\\-2\\1\end{bmatrix},\qquad
\vec v_2\cdot\vec u_1=\frac{10+4+4}{3}=6.
$$
</div>

Then

<div class="math-display">
$$
\vec w_2=\begin{bmatrix}5\\-2\\4\end{bmatrix}
-2\begin{bmatrix}2\\-2\\1\end{bmatrix}
=\begin{bmatrix}1\\2\\2\end{bmatrix}.
$$
</div>

Its length is <span class="math-inline">\\(3\\)</span>, so <span class="math-inline">\\(\vec u&#95;2=\frac13\begin{bmatrix}1\\\\2\\\\2\end{bmatrix}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Subtract the components of <span class="math-inline">\\(\vec v&#95;3\\)</span> along both <span class="math-inline">\\(\vec u&#95;1\\)</span> and <span class="math-inline">\\(\vec u&#95;2\\)</span>, then normalize to find <span class="math-inline">\\(\vec u&#95;3\\)</span>.

<details markdown="1"><summary>Solution</summary>

The projection coefficients are

<div class="math-display">
$$
\vec v_3\cdot\vec u_1=\frac{-4-10+5}{3}=-3,\qquad
\vec v_3\cdot\vec u_2=\frac{-2+10+10}{3}=6.
$$
</div>

Subtracting both components gives

<div class="math-display">
$$
\vec w_3=\vec v_3-(-3)\vec u_1-6\vec u_2
=\begin{bmatrix}-2\\5\\5\end{bmatrix}
+\begin{bmatrix}2\\-2\\1\end{bmatrix}
-2\begin{bmatrix}1\\2\\2\end{bmatrix}
=\begin{bmatrix}-2\\-1\\2\end{bmatrix}.
$$
</div>

Its length is <span class="math-inline">\\(3\\)</span>, so <span class="math-inline">\\(\vec u&#95;3=\frac13\begin{bmatrix}-2\\\\-1\\\\2\end{bmatrix}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Write the relationships between the original vectors (<span class="math-inline">\\(\vec v&#95;1\\)</span>, <span class="math-inline">\\(\vec v&#95;2\\)</span>, and <span class="math-inline">\\(\vec v&#95;3\\)</span>) and the orthonormal basis vectors (<span class="math-inline">\\(\vec u&#95;1\\)</span>, <span class="math-inline">\\(\vec u&#95;2\\)</span>, and <span class="math-inline">\\(\vec u&#95;3\\)</span>). Use these equations to find <span class="math-inline">\\(Q\\)</span> and <span class="math-inline">\\(R\\)</span> such that <span class="math-inline">\\(A=QR\\)</span>. Verify that <span class="math-inline">\\(QR=A\\)</span> and that the columns of <span class="math-inline">\\(Q\\)</span> are orthonormal.

<details markdown="1"><summary>Solution</summary>

Putting back the components we subtracted and undoing normalization gives

<div class="math-display">
$$
\vec v_1=3\vec u_1,\qquad
\vec v_2=6\vec u_1+3\vec u_2,\qquad
\vec v_3=-3\vec u_1+6\vec u_2+3\vec u_3.
$$
</div>

Thus

<div class="math-display">
$$
Q=\frac13\begin{bmatrix}2&1&-2\\-2&2&-1\\1&2&2\end{bmatrix},\qquad
R=\begin{bmatrix}3&6&-3\\0&3&6\\0&0&3\end{bmatrix}.
$$
</div>

Each column of <span class="math-inline">\\(Q\\)</span> has squared length <span class="math-inline">\\(9/9=1\\)</span>. The distinct-column dot products are <span class="math-inline">\\((2-4+2)/9=0\\)</span>, <span class="math-inline">\\((-4+2+2)/9=0\\)</span>, and <span class="math-inline">\\((-2-2+4)/9=0\\)</span>. Finally,

<div class="math-display">
$$
QR=\frac13\begin{bmatrix}6&15&-6\\-6&-6&15\\3&12&15\end{bmatrix}
=\begin{bmatrix}2&5&-2\\-2&-2&5\\1&4&5\end{bmatrix}=A.
$$
</div>

</details>
</div>
</div>

</div>

{% endraw %}
