---
layout: page
title: "Midterm 2"
description: "Midterm 2 problems."
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
  width: 390px;
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
.mc-options-stacked {
  align-items: flex-start;
  flex-direction: column;
}
.mc-option {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  white-space: normal;
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
</style>

# Midterm 2

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/exams/fa26-mt2/fa26-mt2.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/exams/fa26-mt2/fa26-mt2-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

*This page is meant to give you quick access to problems and their solutions. Refer to the original exam PDF, linked above, for test-taking instructions and formatting. Note that we’ve kept the problem text identical, which is why you may see things like “write your answer in the box below” despite there not being a box on this page.*

---


## Problems

- [Problem 1](#problem-1-8-pts)
- [Problem 2](#problem-2-12-pts)
- [Problem 3](#problem-3-12-pts)
- [Problem 4](#problem-4-12-pts)
- [Problem 5](#problem-5-10-pts)
- [Problem 6](#problem-6-18-pts)
- [Problem 7](#problem-7-11-pts)
- [Problem 8](#problem-8-17-pts)

---

## Problem 1 (8 pts)

<div class="assignment-parts">
<div class="assignment-part"><div class="assignment-part-label">a)</div><div class="assignment-part-content">
<p>(4 pts) Let</p>
<div class="math-display">\[C=\begin{bmatrix}4&amp;-2\\-3&amp;5\\6&amp;1\end{bmatrix},\qquad
D=\begin{bmatrix}2&amp;-4&amp;3\\5&amp;1&amp;-2\\-3&amp;6&amp;4\\7&amp;-2&amp;5\end{bmatrix}.\]</div>
<p>Give the shape of each expression (e.g. <span class="math-inline">\(5\times3\)</span>), or write “undefined.”</p>
<div class="math-display">\[CD\qquad DC\qquad C+C\qquad D(3C).\]</div>
<details><summary>Solution</summary>
<p>The shape of <span class="math-inline">\(C\)</span> is <span class="math-inline">\(3\times2\)</span>, and the shape of <span class="math-inline">\(D\)</span> is <span class="math-inline">\(4\times3\)</span>. For a product, the inner dimensions must agree, and the outer dimensions give its shape. Thus</p>
<div class="math-display">\[\boxed{CD:\ \text{undefined},\qquad DC:\ 4\times2,\qquad C+C:\ 3\times2,\qquad D(3C):\ 4\times2.}\]</div>
<p>The product <span class="math-inline">\(CD\)</span> is undefined because <span class="math-inline">\(2\ne4\)</span>. Adding <span class="math-inline">\(C\)</span> to itself or multiplying it by <span class="math-inline">\(3\)</span> does not change its shape.</p>
</details>
</div></div>
<div class="assignment-part"><div class="assignment-part-label">b)</div><div class="assignment-part-content">
<p>(4 pts) Let <span class="math-inline">\(a\)</span> be a real constant, and let</p>
<div class="math-display">\[A=\begin{bmatrix}a&amp;4\\5&amp;a\\-1&amp;-7\end{bmatrix},\qquad
B=\begin{bmatrix}3&amp;4&amp;2\\-2&amp;5&amp;-1\end{bmatrix}.\]</div>
<p>Suppose the third column of <span class="math-inline">\(AB\)</span> is</p>
<div class="math-display">\[\begin{bmatrix}2\\m\\5\end{bmatrix}.\]</div>
<p><strong>i)</strong> (2 pts) Find the value of <span class="math-inline">\(a\)</span>. Show your work.</p>
<details><summary>Solution</summary>
<p>The third column of <span class="math-inline">\(AB\)</span> is <span class="math-inline">\(A\)</span> times the third column of <span class="math-inline">\(B\)</span>:</p>
<div class="math-display">\[A\begin{bmatrix}2\\-1\end{bmatrix}
=2\begin{bmatrix}a\\5\\-1\end{bmatrix}-\begin{bmatrix}4\\a\\-7\end{bmatrix}
=\begin{bmatrix}2a-4\\10-a\\5\end{bmatrix}.\]</div>
<p>Matching the first entry gives <span class="math-inline">\(2a-4=2\)</span>, so <span class="math-inline">\(\boxed{a=3}\)</span>.</p>
</details>
<p><strong>ii)</strong> (2 pts) Find the value of <span class="math-inline">\(m\)</span>. Show your work.</p>
<details><summary>Solution</summary>
<p>The second entry of the third column is <span class="math-inline">\(10-a\)</span>. Using <span class="math-inline">\(a=3\)</span> from part (i), we get</p>
<div class="math-display">\[\boxed{m=10-3=7.}\]</div>
</details>
</div></div>
</div>

---

## Problem 2 (12 pts)

<div class="assignment-parts">
<div class="assignment-part"><div class="assignment-part-label">a)</div><div class="assignment-part-content">
<p>(8 pts) Suppose a linear transformation <span class="math-inline">\(T:\mathbb R^2\to\mathbb R^3\)</span> satisfies</p>
<div class="math-display">\[T\!\left(\begin{bmatrix}2\\-1\end{bmatrix}\right)=\begin{bmatrix}4\\2\\-3\end{bmatrix},\quad
T\!\left(\begin{bmatrix}-1\\3\end{bmatrix}\right)=\begin{bmatrix}-2\\5\\1\end{bmatrix}.\]</div>
<p><strong>i)</strong> (1 pt) What is the shape of the matrix <span class="math-inline">\(A\)</span> where <span class="math-inline">\(T(\vec x)=A\vec x\)</span>?</p>
<details><summary>Solution</summary>
<p>The matrix takes a vector with <span class="math-inline">\(2\)</span> entries as input and produces a vector with <span class="math-inline">\(3\)</span> entries. It therefore has <span class="math-inline">\(3\)</span> rows and <span class="math-inline">\(2\)</span> columns, so its shape is <span class="math-inline">\(\boxed{3\times2}\)</span>.</p>
</details>
<p><strong>ii)</strong> (7 pts) Find an input vector <span class="math-inline">\(\vec v\in\mathbb R^2\)</span> such that</p>
<div class="math-display">\[T(\vec v)=\begin{bmatrix}10\\-1\\-7\end{bmatrix}.\]</div>
<details><summary>Solution</summary>
<p>We want to write the desired output as a linear combination of the two outputs we know. Suppose</p>
<div class="math-display">\[\alpha\begin{bmatrix}4\\2\\-3\end{bmatrix}
+\beta\begin{bmatrix}-2\\5\\1\end{bmatrix}
=\begin{bmatrix}10\\-1\\-7\end{bmatrix}.\]</div>
<p>The first two entries give <span class="math-inline">\(4\alpha-2\beta=10\)</span> and <span class="math-inline">\(2\alpha+5\beta=-1\)</span>. From the first equation, <span class="math-inline">\(\beta=2\alpha-5\)</span>. Substituting into the second gives <span class="math-inline">\(12\alpha=24\)</span>, so <span class="math-inline">\(\alpha=2\)</span> and <span class="math-inline">\(\beta=-1\)</span>. These values also give the required third entry, since <span class="math-inline">\(2(-3)-1=-7\)</span>.</p>
<p>By linearity, we can use the same coefficients on the inputs:</p>
<div class="math-display">\[T\!\left(2\begin{bmatrix}2\\-1\end{bmatrix}-\begin{bmatrix}-1\\3\end{bmatrix}\right)
=2\begin{bmatrix}4\\2\\-3\end{bmatrix}-\begin{bmatrix}-2\\5\\1\end{bmatrix}
=\begin{bmatrix}10\\-1\\-7\end{bmatrix}.\]</div>
<p>Therefore, <span class="math-inline">\(\boxed{\vec v=\begin{bmatrix}5\\-5\end{bmatrix}}\)</span>.</p>
</details>
</div></div>
<div class="assignment-part"><div class="assignment-part-label">b)</div><div class="assignment-part-content">
<p>(4 pts) Which of the following transformations from <span class="math-inline">\(\mathbb R^2\)</span> to <span class="math-inline">\(\mathbb R^2\)</span> are linear? <strong>Select all that apply.</strong></p>
<div class="mc-options mc-options-stacked">
<span class="mc-option"><span class="mc-square" aria-hidden="true"></span><span>Multiply each vector by its length.</span></span>
<span class="mc-option"><span class="mc-square" aria-hidden="true"></span><span>Swap the horizontal and vertical components.</span></span>
<span class="mc-option"><span class="mc-square" aria-hidden="true"></span><span>Add <span class="math-inline">\(4\)</span> to the horizontal component and subtract <span class="math-inline">\(2\)</span> from the vertical component.</span></span>
<span class="mc-option"><span class="mc-square" aria-hidden="true"></span><span>Send every vector to the zero vector.</span></span>
</div>
<details><summary>Solution</summary>
<p>Select <strong>the second and fourth choices</strong>.</p>
<ul><li>Multiplying each vector by its length is not linear. The vector <span class="math-inline">\(\begin{bmatrix}1\\0\end{bmatrix}\)</span> maps to itself, but twice that vector, <span class="math-inline">\(\begin{bmatrix}2\\0\end{bmatrix}\)</span>, maps to <span class="math-inline">\(\begin{bmatrix}4\\0\end{bmatrix}\)</span>. Doubling the input does not double the output.</li><li>Swapping the components is linear: it is multiplication by <span class="math-inline">\(\begin{bmatrix}0&amp;1\\1&amp;0\end{bmatrix}\)</span>.</li><li>Adding <span class="math-inline">\(4\)</span> to one component and subtracting <span class="math-inline">\(2\)</span> from the other is not linear. It sends <span class="math-inline">\(\vec0\)</span> to <span class="math-inline">\(\begin{bmatrix}4\\-2\end{bmatrix}\)</span>, but a linear transformation must send <span class="math-inline">\(\vec0\)</span> to <span class="math-inline">\(\vec0\)</span>.</li><li>Sending every vector to <span class="math-inline">\(\vec0\)</span> is linear: it is multiplication by the zero matrix.</li></ul>
</details>
</div></div>
</div>

---

## Problem 3 (12 pts)

<div class="assignment-parts">
<div class="assignment-part"><div class="assignment-part-label">a)</div><div class="assignment-part-content">
<p>(4 pts) Let</p>
<div class="math-display">\[A=\frac15\begin{bmatrix}1&amp;2\\2&amp;4\end{bmatrix}.\]</div>
<p>This matrix projects vectors orthogonally onto a line <span class="math-inline">\(\ell\)</span> through the origin. Give a nonzero vector <span class="math-inline">\(\vec u\)</span> such that <span class="math-inline">\(\ell=\operatorname{span}(\vec u)\)</span>.</p>
<details><summary>Solution</summary>
<p>The columns of <span class="math-inline">\(A\)</span> are the projections of the standard basis vectors, so both lie on <span class="math-inline">\(\ell\)</span>. The first column is the nonzero vector <span class="math-inline">\(\frac15\begin{bmatrix}1\\2\end{bmatrix}\)</span>, which gives the direction of the line. One answer is therefore</p>
<div class="math-display">\[\boxed{\vec u=\begin{bmatrix}1\\2\end{bmatrix}.}\]</div>
<p>Any nonzero scalar multiple of this vector also works.</p>
</details>
</div></div>
<div class="assignment-part"><div class="assignment-part-label">b)</div><div class="assignment-part-content">
<p>(8 pts) The diagram shows <span class="math-inline">\(T(\vec e&#95;1)\)</span> and <span class="math-inline">\(T(\vec e&#95;2)\)</span> for a linear transformation <span class="math-inline">\(T:\mathbb R^2\to\mathbb R^2\)</span>, where the standard basis vectors are</p>
<div class="math-display">\[\vec e_1=\begin{bmatrix}1\\0\end{bmatrix},\qquad \vec e_2=\begin{bmatrix}0\\1\end{bmatrix}.\]</div>
<p>The transformation <span class="math-inline">\(S\)</span> first applies <span class="math-inline">\(T\)</span>, <strong>then</strong> rotates the resulting vector <span class="math-inline">\(90^\circ\)</span> <strong>clockwise</strong> about the origin. Find the <span class="math-inline">\(2\times2\)</span> matrix <span class="math-inline">\(B\)</span> corresponding to <span class="math-inline">\(S\)</span> (<strong>not</strong> <span class="math-inline">\(T\)</span>).</p>
<img src="imgs/fa26-mt2-plot-01.png" alt="Coordinate grid with two labeled vector arrows from the origin" class="assignment-vector-plot">
<details><summary>Solution</summary>
<p>From the diagram,</p>
<div class="math-display">\[T(\vec e_1)=\begin{bmatrix}-3\\2\end{bmatrix},\qquad
T(\vec e_2)=\begin{bmatrix}5\\4\end{bmatrix}.\]</div>
<p>A <span class="math-inline">\(90^\circ\)</span> clockwise rotation sends <span class="math-inline">\(\begin{bmatrix}r\\s\end{bmatrix}\)</span> to <span class="math-inline">\(\begin{bmatrix}s\\-r\end{bmatrix}\)</span>. Therefore,</p>
<div class="math-display">\[S(\vec e_1)=\begin{bmatrix}2\\3\end{bmatrix},\qquad
S(\vec e_2)=\begin{bmatrix}4\\-5\end{bmatrix}.\]</div>
<p>These outputs are the first and second columns of the matrix for <span class="math-inline">\(S\)</span>, so</p>
<div class="math-display">\[\boxed{B=\begin{bmatrix}2&amp;4\\3&amp;-5\end{bmatrix}.}\]</div>
</details>
</div></div>
</div>

---

## Problem 4 (12 pts)

<div class="assignment-parts">
<div class="assignment-part"><div class="assignment-part-label">a)</div><div class="assignment-part-content">
<p>(5 pts) Find <span class="math-inline">\(A^{-1}\)</span>, where</p>
<div class="math-display">\[A=\begin{bmatrix}7&amp;-3\\5&amp;-1\end{bmatrix}.\]</div>
<details><summary>Solution</summary>
<p>The <span class="math-inline">\(2\times2\)</span> inverse formula gives</p>
<div class="math-display">\[A^{-1}=\frac{1}{7(-1)-(-3)(5)}\begin{bmatrix}-1&amp;3\\-5&amp;7\end{bmatrix}
=\boxed{\frac18\begin{bmatrix}-1&amp;3\\-5&amp;7\end{bmatrix}.}\]</div>
<p>The denominator is <span class="math-inline">\(-7+15=8\ne0\)</span>, so the inverse exists.</p>
</details>
</div></div>
<div class="assignment-part"><div class="assignment-part-label">b)</div><div class="assignment-part-content">
<p>(7 pts) Two invertible matrices <span class="math-inline">\(C\)</span> and <span class="math-inline">\(D\)</span> have inverses</p>
<div class="math-display">\[C^{-1}=\begin{bmatrix}2&amp;3\\-1&amp;4\end{bmatrix},\qquad
D^{-1}=\begin{bmatrix}1&amp;-2\\0&amp;1\end{bmatrix}.\]</div>
<p>A vector <span class="math-inline">\(\vec x\)</span> is first multiplied by <span class="math-inline">\(C\)</span>, and the result is then multiplied by <span class="math-inline">\(D\)</span>. The final output is</p>
<div class="math-display">\[\begin{bmatrix}5\\2\end{bmatrix}.\]</div>
<p>Find <span class="math-inline">\(\vec x\)</span>.</p>
<details><summary>Solution</summary>
<p>The given output is <span class="math-inline">\(DC\vec x\)</span>. We need to undo <span class="math-inline">\(D\)</span> first, then undo <span class="math-inline">\(C\)</span>. Multiplying the output by <span class="math-inline">\(D^{-1}\)</span> gives</p>
<div class="math-display">\[C\vec x=D^{-1}\begin{bmatrix}5\\2\end{bmatrix}
=\begin{bmatrix}1&amp;-2\\0&amp;1\end{bmatrix}\begin{bmatrix}5\\2\end{bmatrix}
=\begin{bmatrix}1\\2\end{bmatrix}.\]</div>
<p>Now multiply by <span class="math-inline">\(C^{-1}\)</span>:</p>
<div class="math-display">\[\vec x=\begin{bmatrix}2&amp;3\\-1&amp;4\end{bmatrix}\begin{bmatrix}1\\2\end{bmatrix}
=\boxed{\begin{bmatrix}8\\7\end{bmatrix}.}\]</div>
</details>
</div></div>
</div>

---

## Problem 5 (10 pts)

<p>Find matrices <span class="math-inline">\(L\)</span> and <span class="math-inline">\(U\)</span> such that <span class="math-inline">\(A=LU\)</span>, where</p>
<div class="math-display">\[A=\begin{bmatrix}5&amp;2&amp;-4\\15&amp;3&amp;-5\\-10&amp;-1&amp;7\end{bmatrix}.\]</div>
<p>Here, <span class="math-inline">\(L\)</span> must be lower triangular with ones on its diagonal, and <span class="math-inline">\(U\)</span> must be upper triangular. No row swaps are necessary.</p>
<details><summary>Solution</summary>
<p>Write the factors in the required forms:</p>
<div class="math-display">\[L=\begin{bmatrix}1&amp;0&amp;0\\\ell_{21}&amp;1&amp;0\\\ell_{31}&amp;\ell_{32}&amp;1\end{bmatrix},\qquad
U=\begin{bmatrix}u_{11}&amp;u_{12}&amp;u_{13}\\0&amp;u_{22}&amp;u_{23}\\0&amp;0&amp;u_{33}\end{bmatrix}.\]</div>
<p>The first row of <span class="math-inline">\(LU\)</span> is the first row of <span class="math-inline">\(U\)</span>, so <span class="math-inline">\(u&#95;{11}=5\)</span>, <span class="math-inline">\(u&#95;{12}=2\)</span>, and <span class="math-inline">\(u&#95;{13}=-4\)</span>. Matching the first column gives</p>
<div class="math-display">\[5\ell_{21}=15,\qquad5\ell_{31}=-10,
\qquad\text{so}\qquad\ell_{21}=3,\quad\ell_{31}=-2.\]</div>
<p>Matching the remaining entries in row 2 gives</p>
<div class="math-display">\[3(2)+u_{22}=3,\qquad3(-4)+u_{23}=-5,\]</div>
<p>so <span class="math-inline">\(u&#95;{22}=-3\)</span> and <span class="math-inline">\(u&#95;{23}=7\)</span>. Entry <span class="math-inline">\((3,2)\)</span> then gives</p>
<div class="math-display">\[(-2)(2)+\ell_{32}(-3)=-1,
\qquad\text{so}\qquad\ell_{32}=-1.\]</div>
<p>Finally, entry <span class="math-inline">\((3,3)\)</span> gives <span class="math-inline">\((-2)(-4)+(-1)(7)+u&#95;{33}=7\)</span>, so <span class="math-inline">\(u&#95;{33}=6\)</span>. Thus</p>
<div class="math-display">\[\boxed{L=\begin{bmatrix}1&amp;0&amp;0\\3&amp;1&amp;0\\-2&amp;-1&amp;1\end{bmatrix},\qquad
U=\begin{bmatrix}5&amp;2&amp;-4\\0&amp;-3&amp;7\\0&amp;0&amp;6\end{bmatrix}.}\]</div>
<p>Multiplying these factors gives <span class="math-inline">\(A\)</span>, as required.</p>
</details>

---

## Problem 6 (18 pts)

<div class="assignment-parts">
<div class="assignment-part"><div class="assignment-part-label">a)</div><div class="assignment-part-content">
<p>(10 pts) Suppose a <span class="math-inline">\(3\times5\)</span> matrix <span class="math-inline">\(A\)</span> has the factorization <span class="math-inline">\(PA=LU\)</span>, where</p>
<div class="math-display">\[P=\begin{bmatrix}0&amp;1&amp;0\\0&amp;0&amp;1\\1&amp;0&amp;0\end{bmatrix},\quad
L=\begin{bmatrix}1&amp;0&amp;0\\-2&amp;1&amp;0\\3&amp;-1&amp;1\end{bmatrix},\quad
U=\begin{bmatrix}4&amp;-8&amp;3&amp;2&amp;-5\\0&amp;0&amp;5&amp;-10&amp;5\\0&amp;0&amp;0&amp;0&amp;0\end{bmatrix}.\]</div>
<p>Use the given factorization to find all real values of <span class="math-inline">\(c\)</span> for which the following system has no solutions:</p>
<div class="math-display">\[A\vec x=\begin{bmatrix}c\\4\\7\end{bmatrix}.\]</div>
<details><summary>Solution</summary>
<p>Let <span class="math-inline">\(\vec b=\begin{bmatrix}c\\4\\7\end{bmatrix}\)</span>. Since <span class="math-inline">\(PA=LU\)</span>, we can solve <span class="math-inline">\(L\vec y=P\vec b\)</span> first, then consider <span class="math-inline">\(U\vec x=\vec y\)</span>. The permutation changes the order of the entries:</p>
<div class="math-display">\[P\vec b=\begin{bmatrix}4\\7\\c\end{bmatrix}.\]</div>
<p>Forward substitution in <span class="math-inline">\(L\vec y=P\vec b\)</span> gives</p>
<div class="math-display">\[\begin{aligned}
y_1&amp;=4,\\
-2y_1+y_2&amp;=7 &amp;&amp;\Longrightarrow\quad y_2=15,\\
3y_1-y_2+y_3&amp;=c &amp;&amp;\Longrightarrow\quad y_3=c+3.
\end{aligned}\]</div>
<p>The last row of <span class="math-inline">\(U\vec x=\vec y\)</span> is therefore <span class="math-inline">\(0=c+3\)</span>. If <span class="math-inline">\(c\ne-3\)</span>, this is impossible, so there are no solutions.</p>
<p>If <span class="math-inline">\(c=-3\)</span>, the last equation is <span class="math-inline">\(0=0\)</span>. The second equation determines <span class="math-inline">\(x&#95;3\)</span> after choosing <span class="math-inline">\(x&#95;4,x&#95;5\)</span>, and the first determines <span class="math-inline">\(x&#95;1\)</span> after choosing <span class="math-inline">\(x&#95;2\)</span>. Thus the system is consistent when <span class="math-inline">\(c=-3\)</span>, and the requested values are exactly</p>
<div class="math-display">\[\boxed{c\ne-3.}\]</div>
</details>
</div></div>
<div class="assignment-part"><div class="assignment-part-label">b)</div><div class="assignment-part-content">
<p>(8 pts) Find all solutions of the following system. Give your answer in vector-parametric form.</p>
<div class="math-display">\[\begin{bmatrix}5&amp;-4&amp;3\\0&amp;6&amp;-12\\0&amp;0&amp;0\\0&amp;0&amp;0\\0&amp;0&amp;0\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=\begin{bmatrix}7\\-18\\0\\0\\0\end{bmatrix}.\]</div>
<details><summary>Solution</summary>
<p>The only nonzero equations are</p>
<div class="math-display">\[5x_1-4x_2+3x_3=7,\qquad6x_2-12x_3=-18.\]</div>
<p>The last three rows give <span class="math-inline">\(0=0\)</span>, so they add no restrictions. Let the free variable be <span class="math-inline">\(x&#95;3=t\)</span>. The second equation gives</p>
<div class="math-display">\[x_2=-3+2t.\]</div>
<p>Substituting into the first gives <span class="math-inline">\(5x&#95;1-4(-3+2t)+3t=7\)</span>, so <span class="math-inline">\(5x&#95;1=-5+5t\)</span> and <span class="math-inline">\(x&#95;1=-1+t\)</span>. Therefore all solutions are</p>
<div class="math-display">\[\boxed{\vec x=\begin{bmatrix}-1\\-3\\0\end{bmatrix}
+t\begin{bmatrix}1\\2\\1\end{bmatrix},\qquad t\in\mathbb R.}\]</div>
</details>
</div></div>
</div>

---

## Problem 7 (11 pts)

<div class="assignment-parts">
<div class="assignment-part"><div class="assignment-part-label">a)</div><div class="assignment-part-content">
<p>(8 pts) Let <span class="math-inline">\(S\)</span> be the plane <span class="math-inline">\(3x+2y-z=0\)</span> in <span class="math-inline">\(\mathbb R^3\)</span>. Which of the following matrices <span class="math-inline">\(A\)</span> satisfy <span class="math-inline">\(\operatorname{colsp}(A)=S\)</span>? <strong>Select all that apply.</strong></p>
<div class="mc-options mc-options-stacked">
<span class="mc-option"><span class="mc-square" aria-hidden="true"></span><span class="math-inline">\(A=\begin{bmatrix}2&amp;-1\\-1&amp;3\\4&amp;3\end{bmatrix}\)</span></span>
<span class="mc-option"><span class="mc-square" aria-hidden="true"></span><span class="math-inline">\(A=\begin{bmatrix}2&amp;-1&amp;1\\-1&amp;3&amp;2\\4&amp;3&amp;7\end{bmatrix}\)</span></span>
<span class="mc-option"><span class="mc-square" aria-hidden="true"></span><span class="math-inline">\(A=\begin{bmatrix}2&amp;6\\-1&amp;-3\\4&amp;12\end{bmatrix}\)</span></span>
<span class="mc-option"><span class="mc-square" aria-hidden="true"></span><span class="math-inline">\(A=\begin{bmatrix}2&amp;-1\\-1&amp;3\\4&amp;5\end{bmatrix}\)</span></span>
</div>
<details><summary>Solution</summary>
<p><strong>Select the first and second matrices.</strong> Let</p>
<div class="math-display">\[\vec u=\begin{bmatrix}2\\-1\\4\end{bmatrix},\qquad
\vec v=\begin{bmatrix}-1\\3\\3\end{bmatrix}.\]</div>
<p>Both vectors belong to <span class="math-inline">\(S\)</span>, since</p>
<div class="math-display">\[3(2)+2(-1)-4=0,\qquad 3(-1)+2(3)-3=0.\]</div>
<p>They are also linearly independent. If <span class="math-inline">\(\vec v=k\vec u\)</span>, the first entries would require <span class="math-inline">\(k=-\frac12\)</span>, but then the second entry of <span class="math-inline">\(k\vec u\)</span> would be <span class="math-inline">\(\frac12\)</span>, not <span class="math-inline">\(3\)</span>. Thus they are not scalar multiples of one another.</p>
<p>Since <span class="math-inline">\(S\)</span> is a plane through the origin, it has dimension 2. Two linearly independent vectors in <span class="math-inline">\(S\)</span> form a basis for <span class="math-inline">\(S\)</span>, so the first matrix has column space <span class="math-inline">\(S\)</span>.</p>
<p>The second matrix has the same first two columns, and its third column is their sum:</p>
<div class="math-display">\[\begin{bmatrix}1\\2\\7\end{bmatrix}=\vec u+\vec v.\]</div>
<p>This extra column does not change the column space, so the second matrix also works.</p>
<p>The third matrix does not work: its second column is <span class="math-inline">\(3\vec u\)</span>, so its column space is only the line spanned by <span class="math-inline">\(\vec u\)</span>.</p>
<p>The fourth matrix does not work either. Its second column is not even in <span class="math-inline">\(S\)</span>, since</p>
<div class="math-display">\[3(-1)+2(3)-5=-2\ne0.\]</div>
<p>Therefore the correct choices are <span class="math-inline">\(\boxed{\text{the first and second matrices}}\)</span>.</p>
</details>
</div></div>
<div class="assignment-part"><div class="assignment-part-label">b)</div><div class="assignment-part-content">
<p>(3 pts) Recall that a subspace contains the zero vector and is closed under addition and scalar multiplication. Consider the set</p>
<div class="math-display">\[W=\left\{\begin{bmatrix}x\\y\end{bmatrix}\in\mathbb R^2:xy=0\right\}.\]</div>
<p>This set is <strong>not</strong> a subspace of <span class="math-inline">\(\mathbb R^2\)</span>, but it still satisfies some of these properties. For each property below, select <strong>yes or no</strong>.</p>
<p><strong>i)</strong> (1 pt) Does <span class="math-inline">\(W\)</span> contain the zero vector?</p>
<div class="mc-options">
<span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span>Yes</span>
<span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span>No</span>
</div>
<p><strong>ii)</strong> (1 pt) Is <span class="math-inline">\(W\)</span> closed under addition?</p>
<div class="mc-options">
<span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span>Yes</span>
<span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span>No</span>
</div>
<p><strong>iii)</strong> (1 pt) Is <span class="math-inline">\(W\)</span> closed under scalar multiplication by any real number?</p>
<div class="mc-options">
<span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span>Yes</span>
<span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span>No</span>
</div>
<details><summary>Solution</summary>
<p><strong>i)</strong> <span class="math-inline">\(\boxed{\text{Yes.}}\)</span> The zero vector belongs to <span class="math-inline">\(W\)</span>, since <span class="math-inline">\(0\cdot0=0\)</span>.</p>
<p><strong>ii)</strong> <span class="math-inline">\(\boxed{\text{No.}}\)</span> For example, both <span class="math-inline">\(\begin{bmatrix}1\\0\end{bmatrix}\)</span> and <span class="math-inline">\(\begin{bmatrix}0\\1\end{bmatrix}\)</span> belong to <span class="math-inline">\(W\)</span>, but their sum does not:</p>
<div class="math-display">\[\begin{bmatrix}1\\0\end{bmatrix}+\begin{bmatrix}0\\1\end{bmatrix}=\begin{bmatrix}1\\1\end{bmatrix},\qquad 1\cdot1\ne0.\]</div>
<p><strong>iii)</strong> <span class="math-inline">\(\boxed{\text{Yes.}}\)</span> If <span class="math-inline">\(\begin{bmatrix}x\\y\end{bmatrix}\in W\)</span>, then <span class="math-inline">\(xy=0\)</span>. For any real scalar <span class="math-inline">\(a\)</span>, the product of the entries of <span class="math-inline">\(a\begin{bmatrix}x\\y\end{bmatrix}\)</span> is</p>
<div class="math-display">\[(ax)(ay)=a^2xy=0.\]</div>
<p>Thus the scalar multiple also belongs to <span class="math-inline">\(W\)</span>.</p>
</details>
</div></div>
</div>

---

## Problem 8 (17 pts)

<div class="assignment-parts">
<div class="assignment-part"><div class="assignment-part-label">a)</div><div class="assignment-part-content">
<p>(6 pts) Let <span class="math-inline">\(\vec x,\vec y,\vec z\in\mathbb R^5\)</span> be linearly independent, and let <span class="math-inline">\(t\in\mathbb R\)</span>. Define</p>
<div class="math-display">\[A=\begin{bmatrix}|&amp;|\\2\vec x-\vec y&amp;6\vec x+t\vec y\\|&amp;|\end{bmatrix},\qquad
B=\begin{bmatrix}|&amp;|&amp;|\\\vec x+\vec y&amp;\vec y-4\vec z&amp;\vec x+t\vec z\\|&amp;|&amp;|\end{bmatrix}.\]</div>
<p>For each part below, select the <strong>one value of <span class="math-inline">\(t\)</span></strong> that satisfies the given condition.</p>
<p><strong>i)</strong> (3 pts) <span class="math-inline">\(\operatorname{rank}(A)=1\)</span></p>
<div class="mc-options">
<span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span><span class="math-inline">\(t=-4\)</span></span>
<span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span><span class="math-inline">\(t=-3\)</span></span>
<span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span><span class="math-inline">\(t=0\)</span></span>
<span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span><span class="math-inline">\(t=1\)</span></span>
<span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span><span class="math-inline">\(t=3\)</span></span>
<span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span><span class="math-inline">\(t=4\)</span></span>
</div>
<details><summary>Solution</summary>
<p>The first column, <span class="math-inline">\(2\vec x-\vec y\)</span>, is nonzero: otherwise <span class="math-inline">\(\vec y=2\vec x\)</span>, contradicting linear independence. Therefore <span class="math-inline">\(A\)</span> has rank 1 exactly when its second column is a scalar multiple of its first. Write</p>
<div class="math-display">\[6\vec x+t\vec y=k(2\vec x-\vec y)=2k\vec x-k\vec y.\]</div>
<p>Because <span class="math-inline">\(\vec x\)</span> and <span class="math-inline">\(\vec y\)</span> are linearly independent, their coefficients on the two sides must match. This gives <span class="math-inline">\(6=2k\)</span> and <span class="math-inline">\(t=-k\)</span>, so</p>
<div class="math-display">\[\boxed{t=-3}.\]</div>
<p>For this value, the second column is three times the first, as required.</p>
</details>
<p><strong>ii)</strong> (3 pts) <span class="math-inline">\(\operatorname{rank}(B)=2\)</span></p>
<div class="mc-options">
<span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span><span class="math-inline">\(t=-4\)</span></span>
<span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span><span class="math-inline">\(t=-3\)</span></span>
<span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span><span class="math-inline">\(t=0\)</span></span>
<span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span><span class="math-inline">\(t=1\)</span></span>
<span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span><span class="math-inline">\(t=3\)</span></span>
<span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span><span class="math-inline">\(t=4\)</span></span>
</div>
<details><summary>Solution</summary>
<p>Try to write the first column as a scalar multiple of the second:</p>
<div class="math-display">\[\vec x+\vec y=k(\vec y-4\vec z)
\quad\Longrightarrow\quad
\vec x=(k-1)\vec y-4k\vec z.\]</div>
<p>This is impossible: it writes <span class="math-inline">\(\vec x\)</span> as a linear combination of <span class="math-inline">\(\vec y\)</span> and <span class="math-inline">\(\vec z\)</span>. The second column is also nonzero, since otherwise <span class="math-inline">\(\vec y=4\vec z\)</span>. Thus the first two columns are linearly independent.</p>
<p>Thus <span class="math-inline">\(B\)</span> has rank 2 exactly when its third column is a linear combination of the first two. Suppose</p>
<div class="math-display">\[\vec x+t\vec z=a(\vec x+\vec y)+b(\vec y-4\vec z)=a\vec x+(a+b)\vec y-4b\vec z.\]</div>
<p>Matching the coefficients of <span class="math-inline">\(\vec x,\vec y,\vec z\)</span> gives</p>
<div class="math-display">\[a=1,\qquad a+b=0,\qquad t=-4b.\]</div>
<p>So <span class="math-inline">\(b=-1\)</span> and <span class="math-inline">\(\boxed{t=4}\)</span>. For this value, the third column is the first minus the second:</p>
<div class="math-display">\[\vec x+4\vec z=(\vec x+\vec y)-(\vec y-4\vec z).\]</div>
</details>
</div></div>
<div class="assignment-part"><div class="assignment-part-label">b)</div><div class="assignment-part-content">
<p>(2 pts) A matrix <span class="math-inline">\(D\)</span> has rank <span class="math-inline">\(8\)</span>. The solutions of <span class="math-inline">\(D\vec x=\vec0\)</span> have <span class="math-inline">\(5\)</span> free variables. How many columns does <span class="math-inline">\(D\)</span> have?</p>
<details><summary>Solution</summary>
<p>Rank 8 means there are 8 pivot columns. Each of the 5 free variables corresponds to a non-pivot column. Thus the total number of columns is</p>
<div class="math-display">\[\boxed{8+5=13}.\]</div>
</details>
</div></div>
<div class="assignment-part"><div class="assignment-part-label">c)</div><div class="assignment-part-content">
<p>(6 pts) Suppose <span class="math-inline">\(E\)</span> is a <span class="math-inline">\(3\times3\)</span> matrix such that</p>
<div class="math-display">\[E\begin{bmatrix}8\\-5\\11\end{bmatrix}=\begin{bmatrix}6\\-8\\13\end{bmatrix},\qquad
E\begin{bmatrix}-3\\7\\4\end{bmatrix}=\begin{bmatrix}0\\0\\0\end{bmatrix}.\]</div>
<p><strong>i)</strong> (2 pts) True or false: <span class="math-inline">\(E\)</span> is invertible.</p>
<div class="mc-options">
<span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span>True</span>
<span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span>False</span>
</div>
<details><summary>Solution</summary>
<p><span class="math-inline">\(\boxed{\text{False.}}\)</span> The nonzero vector <span class="math-inline">\(\begin{bmatrix}-3\\7\\4\end{bmatrix}\)</span> is mapped to the zero vector. If <span class="math-inline">\(E\)</span> were invertible, multiplying both sides of the given equality by <span class="math-inline">\(E^{-1}\)</span> would give</p>
<div class="math-display">\[\begin{bmatrix}-3\\7\\4\end{bmatrix}=E^{-1}\begin{bmatrix}0\\0\\0\end{bmatrix}=\begin{bmatrix}0\\0\\0\end{bmatrix}.\]</div>
<p>This is impossible. Thus <span class="math-inline">\(E\)</span> is not invertible.</p>
</details>
<p><strong>ii)</strong> (4 pts) Give a solution of the following system <strong>other than</strong> <span class="math-inline">\(\begin{bmatrix}8\\-5\\11\end{bmatrix}\)</span>:</p>
<div class="math-display">\[E\vec x=\begin{bmatrix}6\\-8\\13\end{bmatrix}.\]</div>
<details><summary>Solution</summary>
<p>We can add a vector that <span class="math-inline">\(E\)</span> sends to zero to the given solution without changing the output. In particular,</p>
<div class="math-display">\[E\!\left(\begin{bmatrix}8\\-5\\11\end{bmatrix}+\begin{bmatrix}-3\\7\\4\end{bmatrix}\right)
=E\begin{bmatrix}8\\-5\\11\end{bmatrix}+E\begin{bmatrix}-3\\7\\4\end{bmatrix}
=\begin{bmatrix}6\\-8\\13\end{bmatrix}+\begin{bmatrix}0\\0\\0\end{bmatrix}.\]</div>
<p>Therefore one valid answer is</p>
<div class="math-display">\[\boxed{\vec x=\begin{bmatrix}5\\2\\15\end{bmatrix}}.\]</div>
</details>
</div></div>
<div class="assignment-part"><div class="assignment-part-label">d)</div><div class="assignment-part-content">
<p>(3 pts) A <span class="math-inline">\(6\times4\)</span> matrix <span class="math-inline">\(G\)</span> has rank <span class="math-inline">\(4\)</span>. Is <span class="math-inline">\(G\vec x=\vec b\)</span> guaranteed to have a solution for every <span class="math-inline">\(\vec b\in\mathbb R^6\)</span>? Briefly explain.</p>
<details><summary>Solution</summary>
<p><span class="math-inline">\(\boxed{\text{No.}}\)</span> The column space of <span class="math-inline">\(G\)</span> has dimension 4, while <span class="math-inline">\(\mathbb R^6\)</span> has dimension 6. Thus the columns of <span class="math-inline">\(G\)</span> cannot span all of <span class="math-inline">\(\mathbb R^6\)</span>. If <span class="math-inline">\(\vec b\)</span> lies outside the column space, <span class="math-inline">\(G\vec x=\vec b\)</span> has no solution.</p>
</details>
</div></div>
</div>

{% endraw %}
