---
layout: page
title: "Lab 3: Lines, Vectors and Orthogonality in $\\mathbb{R}^2$"
description: "Lab 3: Lines, Vectors and Orthogonality in $\\mathbb{R}^2$ activities."
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

# Lab 3: Lines, Vectors and Orthogonality in $\mathbb{R}^2$

**due** by the end of class on Wednesday, September 16, 2026

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab03/lab03.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab03/lab03-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
Each lab worksheet will contain several activities, most of which will involve writing math on paper, and some of which will involve running code in a Jupyter Notebook. Lab activities are meant to last an hour, and the second hour of lab is dedicated to starting the homework assignment. To receive credit for a lab, you must show your lab TA your work on both the lab worksheet and homework assignment.

While you must get checked off by your lab TA **individually**, we encourage you to form groups with 1-2 other students to complete the activities together.
</div>

---

## Activities

- [Activity 1: Homogeneous and Inhomogeneous Equations](#activity-1-homogeneous-and-inhomogeneous-equations)
- [Activity 2: The Span of One Vector](#activity-2-the-span-of-one-vector)
- [Activity 3: Translating a Line](#activity-3-translating-a-line)
- [Activity 4: A Line and Its Perpendicular Line](#activity-4-a-line-and-its-perpendicular-line)
- [Activity 5: An Affine Line in Equation Form](#activity-5-an-affine-line-in-equation-form)
- [Activity 6: Orthonormal Bases](#activity-6-orthonormal-bases)
- [Activity 7: Coordinates in an Orthonormal Basis](#activity-7-coordinates-in-an-orthonormal-basis)

---

## Activity 1: Homogeneous and Inhomogeneous Equations

Classify each linear equation as *homogeneous* or *inhomogeneous*.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(3x-4y=0\\)</span>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Homogeneous</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Inhomogeneous</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> Homogeneous</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Inhomogeneous</span></div>

A linear equation in two variables is homogeneous if it can be written in the form

<div class="math-display">
$$
ax+by=0.
$$
</div>

 Otherwise, it is inhomogeneous.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(x+2y=5\\)</span>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Homogeneous</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Inhomogeneous</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Homogeneous</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> Inhomogeneous</span></div>
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(2x-y=0\\)</span>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Homogeneous</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Inhomogeneous</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> Homogeneous</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Inhomogeneous</span></div>
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(x-4y+7=0\\)</span>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Homogeneous</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Inhomogeneous</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Homogeneous</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> Inhomogeneous</span></div>
</details>

</div>
</div>

</div>

---

## Activity 2: The Span of One Vector

Let

<div class="math-display">
$$
\vec{v}
=
\begin{bmatrix}
2\\
-3
\end{bmatrix}
.
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Write <span class="math-inline">\\(\operatorname{span}(\vec{v})\\)</span> explicitly in set-builder notation.

<div class="math-display">
$$
\operatorname{span}(\vec{v})
=
\Big\{
\hspace{11cm}
\Big\}.
$$
</div>

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\operatorname{span}(\vec{v})
=
\left\{
t
\begin{bmatrix}
2\\
-3
\end{bmatrix}
:
t\in\mathbb{R}
\right\}.
$$
</div>

Equivalently,

<div class="math-display">
$$
\operatorname{span}(\vec{v})
=
\left\{
\begin{bmatrix}
2t\\
-3t
\end{bmatrix}
:
t\in\mathbb{R}
\right\}.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Draw <span class="math-inline">\\(\operatorname{span}(\vec{v})\\)</span> on the coordinate plane below. Label the line <span class="math-inline">\\(\ell\\)</span>, and mark the vector <span class="math-inline">\\(\vec{v}\\)</span>.

<div style="text-align: center;">
<img src="imgs/lab03-plot-01.png" alt="Blank coordinate axes" class="assignment-vector-plot">
</div>

<details markdown="1"><summary>Solution</summary>

The graph is the line through the origin with direction vector

<div class="math-display">
$$
\begin{bmatrix}
2\\
-3
\end{bmatrix}.
$$
</div>

Its equation is

<div class="math-display">
$$
3x+2y=0.
$$
</div>

<div style="text-align: center;">
<img src="imgs/lab03-plot-02.png" alt="Vector diagram" class="assignment-vector-plot">
</div>
</details>

</div>
</div>

</div>

---

## Activity 3: Translating a Line

Let

<div class="math-display">
$$
\vec{v}_0
=
\begin{bmatrix}
-2\\
1
\end{bmatrix}
\qquad\text{and}\qquad
\vec{v}
=
\begin{bmatrix}
2\\
-3
\end{bmatrix}.
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Write

<div class="math-display">
$$
\vec{v}_0+\operatorname{span}(\vec{v})
$$
</div>

 explicitly in set-builder notation.

<div class="math-display">
$$
\vec{v}_0+\operatorname{span}(\vec{v})
=
\Big\{
\hspace{11cm}
\Big\}.
$$
</div>

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\vec{v}_0+\operatorname{span}(\vec{v})
=
\left\{
\begin{bmatrix}
-2\\
1
\end{bmatrix}
+
t
\begin{bmatrix}
2\\
-3
\end{bmatrix}
:
t\in\mathbb{R}
\right\}.
$$
</div>

Equivalently,

<div class="math-display">
$$
\vec{v}_0+\operatorname{span}(\vec{v})
=
\left\{
\begin{bmatrix}
-2+2t\\
1-3t
\end{bmatrix}
:
t\in\mathbb{R}
\right\}.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Draw this set on the coordinate plane below. Label the affine line <span class="math-inline">\\(\ell'\\)</span> and mark the points represented by <span class="math-inline">\\(\vec{v}&#95;0\\)</span>, <span class="math-inline">\\(\vec{v}&#95;0+\vec{v}\\)</span>, <span class="math-inline">\\(\vec{v}&#95;0 - \vec{v}\\)</span>.

<div style="text-align: center;">
<img src="imgs/lab03-plot-03.png" alt="Blank coordinate axes" class="assignment-vector-plot">
</div>

<details markdown="1"><summary>Solution</summary>

The three requested points are

<div class="math-display">
$$
\vec{v}_0
=
\begin{bmatrix}
-2\\
1
\end{bmatrix},
$$
</div>

<div class="math-display">
$$
\vec{v}_0+\vec{v}
=
\begin{bmatrix}
-2\\
1
\end{bmatrix}
+
\begin{bmatrix}
2\\
-3
\end{bmatrix}
=
\begin{bmatrix}
0\\
-2
\end{bmatrix},
$$
</div>

and

<div class="math-display">
$$
\vec{v}_0-\vec{v}
=
\begin{bmatrix}
-2\\
1
\end{bmatrix}
-
\begin{bmatrix}
2\\
-3
\end{bmatrix}
=
\begin{bmatrix}
-4\\
4
\end{bmatrix}.
$$
</div>

The affine line passes through these three points and is parallel to the line drawn in Activity 2. Its equation is

<div class="math-display">
$$
3x+2y=-4.
$$
</div>

<div style="text-align: center;">
<img src="imgs/lab03-plot-04.png" alt="Vector diagram" class="assignment-vector-plot">
</div>
</details>

</div>
</div>

</div>

---

## Activity 4: A Line and Its Perpendicular Line

Let <span class="math-inline">\\(\ell\\)</span> be the line drawn in Activity 2:

<div class="math-display">
$$
\ell
=
\operatorname{span}
\left(
\begin{bmatrix}
2\\
-3
\end{bmatrix}
\right).
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<ol class="assignment-enumeration" markdown="1">

<li markdown="1">
<div class="assignment-enumeration-label">i.</div>
<div class="assignment-enumeration-content" markdown="1">

Recall that <span class="math-inline">\\(\ell^\perp\\)</span> is the line through the origin that is perpendicular to <span class="math-inline">\\(\ell\\)</span>. Draw <span class="math-inline">\\(\ell^\perp\\)</span> on the coordinate plane from Activity 2.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">ii.</div>
<div class="assignment-enumeration-content" markdown="1">

Find a nonzero vector <span class="math-inline">\\(\vec{w}\\)</span> on <span class="math-inline">\\(\ell^\perp\\)</span>.

<div class="math-display">
$$
\vec{w}
=
\begin{bmatrix}
\phantom{-00}\\
\phantom{-00}
\end{bmatrix}.
$$
</div>

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">iii.</div>
<div class="assignment-enumeration-content" markdown="1">

Check that <span class="math-inline">\\(\vec{w}\\)</span> is perpendicular to <span class="math-inline">\\(\vec{v}\\)</span>:

<div class="math-display">
$$
\vec{w}\cdot\vec{v}
=
\begin{bmatrix}
\phantom{-00}\\
\phantom{-00}
\end{bmatrix}
\cdot
\begin{bmatrix}
2\\
-3
\end{bmatrix} =
$$
</div>

</div></li>
</ol>

<details markdown="1"><summary>Solution</summary>

For (i), drawing <span class="math-inline">\\(\ell^{\perp}\\)</span> on top of the graph from Activity 2 gives us:

<div style="text-align: center;">
<img src="imgs/lab03-plot-05.png" alt="Vector diagram" class="assignment-vector-plot">
</div>

For (ii), one possible choice is

<div class="math-display">
$$
\vec{w}
=
\begin{bmatrix}
3\\
2
\end{bmatrix}.
$$
</div>

Indeed, we check at (iii) that

<div class="math-display">
$$
\vec{w}\cdot\vec{v}
=
\begin{bmatrix}
3\\
2
\end{bmatrix}
\cdot
\begin{bmatrix}
2\\
-3
\end{bmatrix}
=
6-6
=
0.
$$
</div>

Therefore,

<div class="math-display">
$$
\ell^\perp
=
\operatorname{span}
\left(
\begin{bmatrix}
3\\
2
\end{bmatrix}
\right).
$$
</div>

Thus, <span class="math-inline">\\(\ell^\perp\\)</span> is the line through the origin in the direction

<div class="math-display">
$$
\begin{bmatrix}
3\\
2
\end{bmatrix}.
$$
</div>

Any nonzero scalar multiple of

<div class="math-display">
$$
\begin{bmatrix}
3\\
2
\end{bmatrix}
$$
</div>

 is also a valid choice for <span class="math-inline">\\(\vec{w}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Use <span class="math-inline">\\(\vec{w}\\)</span> and the dot product to write an equation for <span class="math-inline">\\(\ell\\)</span>.

<ol class="assignment-enumeration" markdown="1">

<li markdown="1">
<div class="assignment-enumeration-label">i.</div>
<div class="assignment-enumeration-content" markdown="1">

Equation in dot-product form:

<div class="math-display">
$$
\vec{w}\cdot\begin{bmatrix}
x\\
y
\end{bmatrix}
=
\underline{\hspace{1cm}}.
$$
</div>

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">ii.</div>
<div class="assignment-enumeration-content" markdown="1">

Equation written explicitly in <span class="math-inline">\\(x,y\\)</span> coordinates:

</div></li>
</ol>

<details markdown="1"><summary>Solution</summary>

<ol class="assignment-enumeration" markdown="1">

<li markdown="1">
<div class="assignment-enumeration-label">i.</div>
<div class="assignment-enumeration-content" markdown="1">

Using

<div class="math-display">
$$
\vec{w}
=
\begin{bmatrix}
3\\
2
\end{bmatrix},
$$
</div>

 the equation in dot-product form is

<div class="math-display">
$$
\vec{w}\cdot
\begin{bmatrix}
x\\
y
\end{bmatrix}
=0.
$$
</div>

Equivalently,

<div class="math-display">
$$
\begin{bmatrix}
3\\
2
\end{bmatrix}
\cdot
\begin{bmatrix}
x\\
y
\end{bmatrix}
=0.
$$
</div>

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">ii.</div>
<div class="assignment-enumeration-content" markdown="1">

Written explicitly in coordinates, this is

<div class="math-display">
$$
3x+2y=0.
$$
</div>

</div></li>
</ol>
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Use <span class="math-inline">\\(\vec{v}\\)</span> and the dot product to write an equation for <span class="math-inline">\\(\ell^\perp\\)</span>.

<ol class="assignment-enumeration" markdown="1">

<li markdown="1">
<div class="assignment-enumeration-label">i.</div>
<div class="assignment-enumeration-content" markdown="1">

Equation in dot-product form:

<div class="math-display">
$$
\vec{v}\cdot\begin{bmatrix}
x\\
y
\end{bmatrix}
=
\underline{\hspace{1cm}}.
$$
</div>

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">ii.</div>
<div class="assignment-enumeration-content" markdown="1">

Equation written explicitly in <span class="math-inline">\\(x,y\\)</span> coordinates:

</div></li>
</ol>

<details markdown="1"><summary>Solution</summary>

<ol class="assignment-enumeration" markdown="1">

<li markdown="1">
<div class="assignment-enumeration-label">i.</div>
<div class="assignment-enumeration-content" markdown="1">

Since <span class="math-inline">\\(\ell^\perp\\)</span> consists of the vectors perpendicular to <span class="math-inline">\\(\vec{v}\\)</span>, its equation in dot-product form is

<div class="math-display">
$$
\vec{v}\cdot
\begin{bmatrix}
x\\
y
\end{bmatrix}
=0.
$$
</div>

Equivalently,

<div class="math-display">
$$
\begin{bmatrix}
2\\
-3
\end{bmatrix}
\cdot
\begin{bmatrix}
x\\
y
\end{bmatrix}
=0.
$$
</div>

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">ii.</div>
<div class="assignment-enumeration-content" markdown="1">

Written explicitly in coordinates, this is

<div class="math-display">
$$
2x-3y=0.
$$
</div>

</div></li>
</ol>
</details>

</div>
</div>

</div>

---

## Activity 5: An Affine Line in Equation Form

Let <span class="math-inline">\\(\ell'\\)</span> be the affine line drawn in Activity 3:

<div class="math-display">
$$
\ell'
=
\vec{v}_0+\operatorname{span}(\vec{v}),
$$
</div>

where

<div class="math-display">
$$
\vec{v}_0
=
\begin{bmatrix}
-2\\
1
\end{bmatrix},
\qquad
\vec{v}
=
\begin{bmatrix}
2\\
-3
\end{bmatrix}.
$$
</div>

Use <span class="math-inline">\\(\vec{v}&#95;0\\)</span>, the vector <span class="math-inline">\\(\vec{w}\\)</span> from Activity 4, and the dot product to write an equation for <span class="math-inline">\\(\ell'\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
First compute the constant on the right-hand side:

<div class="math-display">
$$
\vec{w}\cdot\vec{v}_0
=
\begin{bmatrix}
\phantom{-00}\\
\phantom{-00}
\end{bmatrix}
\cdot
\begin{bmatrix}
-2\\
1
\end{bmatrix}
=
\underline{\hspace{3cm}}.
$$
</div>

<details markdown="1"><summary>Solution</summary>

Using

<div class="math-display">
$$
\vec{w}
=
\begin{bmatrix}
3\\
2
\end{bmatrix}
\qquad\text{and}\qquad
\vec{v}_0
=
\begin{bmatrix}
-2\\
1
\end{bmatrix},
$$
</div>

we obtain

<div class="math-display">
$$
\begin{aligned}
\vec{w}\cdot\vec{v}_0
&=
\begin{bmatrix}
3\\
2
\end{bmatrix}
\cdot
\begin{bmatrix}
-2\\
1
\end{bmatrix}\\
&=
3(-2)+2(1)\\
&=
-6+2\\
&=
-4.
\end{aligned}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<ol class="assignment-enumeration" markdown="1">

<li markdown="1">
<div class="assignment-enumeration-label">i.</div>
<div class="assignment-enumeration-content" markdown="1">

Find the equation in dot-product form:

<div class="math-display">
$$
\vec{w}\cdot\begin{bmatrix}
x\\
y
\end{bmatrix}
=
\vec{w}\cdot\vec{v}_0
=
\underline{\hspace{3cm}}.
$$
</div>

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">ii.</div>
<div class="assignment-enumeration-content" markdown="1">

Equation written explicitly in <span class="math-inline">\\(x,y\\)</span> coordinates:

</div></li>
</ol>

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(i\\)</span> From the previous subactivity,

<div class="math-display">
$$
\vec{w}\cdot\vec{v}_0=-4.
$$
</div>

Therefore, the equation in dot-product form is

<div class="math-display">
$$
\vec{w}\cdot
\begin{bmatrix}
x\\
y
\end{bmatrix}
=
-4.
$$
</div>

<span class="math-inline">\\(ii\\)</span> Using

<div class="math-display">
$$
\vec{w}
=
\begin{bmatrix}
3\\
2
\end{bmatrix},
$$
</div>

this becomes

<div class="math-display">
$$
\begin{bmatrix}
3\\
2
\end{bmatrix}
\cdot
\begin{bmatrix}
x\\
y
\end{bmatrix}
=
-4.
$$
</div>

Written explicitly in coordinates, the equation is

<div class="math-display">
$$
3x+2y=-4.
$$
</div>

</details>

</div>
</div>

</div>

---

## Activity 6: Orthonormal Bases

Which of the following pairs of vectors are orthonormal bases of <span class="math-inline">\\(\mathbb{R}^2\\)</span>?

For each pair, compute the length of each vector and the dot product of the two vectors. Explain your answer.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<div class="math-display">
$$
\vec{u}
=
\begin{bmatrix}
\frac{1}{\sqrt{5}}\\[2pt]
\frac{2}{\sqrt{5}}
\end{bmatrix},
\qquad
\vec{v}
=
\begin{bmatrix}
-\frac{2}{\sqrt{5}}\\[2pt]
\frac{1}{\sqrt{5}}
\end{bmatrix}.
$$
</div>

<div class="math-display">
$$
\lVert\vec{u}\rVert=\underline{\hspace{1.5cm}},
\qquad
\lVert\vec{v}\rVert=\underline{\hspace{1.5cm}},
\qquad
\vec{u}\cdot\vec{v}=\underline{\hspace{1.5cm}}.
$$
</div>

Is <span class="math-inline">\\((\vec{u},\vec{v})\\)</span> an orthonormal basis?
<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Yes</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> No</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> Yes</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> No</span></div>

For <span class="math-inline">\\(\vec{u}\\)</span> and <span class="math-inline">\\(\vec{v}\\)</span> to form an orthonormal basis of <span class="math-inline">\\(\mathbb{R}^2\\)</span>, both vectors must have length 1 and be perpendicular to each other (their dot product must be 0).

<div class="math-display">
$$
\lVert\vec{u}\rVert
    =
    \sqrt{\frac15+\frac45}
    =
    1,
    \qquad
    \lVert\vec{v}\rVert
    =
    \sqrt{\frac45+\frac15}
    =
    1,
$$
</div>

 and

<div class="math-display">
$$
\vec{u}\cdot\vec{v}
    =
    -\frac25+\frac25
    =
    0.
$$
</div>

 Therefore this pair is an orthonormal basis.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<div class="math-display">
$$
\vec{u}
=
\begin{bmatrix}
\frac35\\[2pt]
\frac45
\end{bmatrix},
\qquad
\vec{v}
=
\begin{bmatrix}
\frac45\\[2pt]
\frac35
\end{bmatrix}.
$$
</div>

<div class="math-display">
$$
\lVert\vec{u}\rVert=\underline{\hspace{1.5cm}},
\qquad
\lVert\vec{v}\rVert=\underline{\hspace{1.5cm}},
\qquad
\vec{u}\cdot\vec{v}=\underline{\hspace{1.5cm}}.
$$
</div>

Is <span class="math-inline">\\((\vec{u},\vec{v})\\)</span> an orthonormal basis?
<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Yes</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> No</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Yes</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> No</span></div>

<div class="math-display">
$$
\lVert\vec{u}\rVert=1,
    \qquad
    \lVert\vec{v}\rVert=1,
$$
</div>

 but

<div class="math-display">
$$
\vec{u}\cdot\vec{v}
    =
    \frac{12}{25}+\frac{12}{25}
    =
    \frac{24}{25}\neq 0.
$$
</div>

 Both vectors are unit vectors, but they are not orthogonal. Therefore, this pair is not an orthonormal basis.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<div class="math-display">
$$
\vec{u}
=
\begin{bmatrix}
2\\
-1
\end{bmatrix},
\qquad
\vec{v}
=
\begin{bmatrix}
1\\
2
\end{bmatrix}.
$$
</div>

<div class="math-display">
$$
\lVert\vec{u}\rVert=\underline{\hspace{1.5cm}},
\qquad
\lVert\vec{v}\rVert=\underline{\hspace{1.5cm}},
\qquad
\vec{u}\cdot\vec{v}=\underline{\hspace{1.5cm}}.
$$
</div>

Is <span class="math-inline">\\((\vec{u},\vec{v})\\)</span> an orthonormal basis?
<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Yes</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> No</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Yes</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> No</span></div>

<div class="math-display">
$$
\lVert\vec{u}\rVert=\sqrt{5},
    \qquad
    \lVert\vec{v}\rVert=\sqrt{5},
$$
</div>

 and

<div class="math-display">
$$
\vec{u}\cdot\vec{v}
    =
    2-2
    =
    0.
$$
</div>

 The vectors are orthogonal, but they are not unit vectors. Therefore, this pair is not an orthonormal basis.
</details>

</div>
</div>

</div>

---

## Activity 7: Coordinates in an Orthonormal Basis

Recall, only one of the three pairs <span class="math-inline">\\((\vec{u},\vec{v})\\)</span> from Activity 6 are an orthonormal basis of <span class="math-inline">\\(\mathbb{R}^2\\)</span>. Write those two vectors here again for your convenience.

<div class="math-display">
$$
\vec{u}=\begin{bmatrix}
\phantom{\dfrac{-00}{\sqrt{5}}}\\[6pt]
\phantom{\dfrac{-00}{\sqrt{5}}}
\end{bmatrix},
\quad
\vec{v}=\begin{bmatrix}
\phantom{\dfrac{-00}{\sqrt{5}}}\\[6pt]
\phantom{\dfrac{-00}{\sqrt{5}}}
\end{bmatrix}.
$$
</div>

Now let

<div class="math-display">
$$
\vec{x}
=
\begin{bmatrix}
4\\
-1
\end{bmatrix}.
$$
</div>

Our goal in this activity is to write <span class="math-inline">\\(\vec{x}\\)</span> as a **linear combination** of <span class="math-inline">\\(\vec{u}\\)</span> and <span class="math-inline">\\(\vec{v}\\)</span>. That is, find scalars <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> such that

<div class="math-display">
$$
\vec{x}=a\vec{u}+b\vec{v}.
$$
</div>

 Because <span class="math-inline">\\((\vec{u},\vec{v})\\)</span> is an orthonormal basis, the coefficients can be found using dot products:

<div class="math-display">
$$
a=\vec{x}\cdot\vec{u},
\qquad
b=\vec{x}\cdot\vec{v}.
$$
</div>

Fill in the blanks below.

Compute <span class="math-inline">\\(a\\)</span>:

<div class="math-display">
$$
\begin{aligned}
a
&=
\vec{x}\cdot\vec{u}\\
&=
\underline{\hspace{5cm}}.
\end{aligned}
$$
</div>

Compute <span class="math-inline">\\(b\\)</span>:

<div class="math-display">
$$
\begin{aligned}
b
&=
\vec{x}\cdot\vec{v}\\
\\
&=
\underline{\hspace{5cm}}.
\end{aligned}
$$
</div>

Therefore,

<div class="math-display">
$$
\vec{x}
=
\underline{\hspace{3cm}}\,\vec{u}
+
\underline{\hspace{3cm}}\,\vec{v}.
$$
</div>

<details markdown="1"><summary>Solution</summary>

The orthonormal basis from the previous activity is

<div class="math-display">
$$
\vec{u}
=
\begin{bmatrix}
\frac{1}{\sqrt{5}}\\[2pt]
\frac{2}{\sqrt{5}}
\end{bmatrix},
\qquad
\vec{v}
=
\begin{bmatrix}
-\frac{2}{\sqrt{5}}\\[2pt]
\frac{1}{\sqrt{5}}
\end{bmatrix}.
$$
</div>

Since the basis is orthonormal, the coefficients are given by the dot products of <span class="math-inline">\\(\vec{x}\\)</span> with the basis vectors.

First,

<div class="math-display">
$$
\begin{aligned}
a
&=
\vec{x}\cdot\vec{u}\\
&=
\begin{bmatrix}
4\\
-1
\end{bmatrix}
\cdot
\begin{bmatrix}
\frac{1}{\sqrt{5}}\\[2pt]
\frac{2}{\sqrt{5}}
\end{bmatrix}\\
&=
\frac{4}{\sqrt{5}}-\frac{2}{\sqrt{5}}\\
&=
\frac{2}{\sqrt{5}}.
\end{aligned}
$$
</div>

Next,

<div class="math-display">
$$
\begin{aligned}
b
&=
\vec{x}\cdot\vec{v}\\
&=
\begin{bmatrix}
4\\
-1
\end{bmatrix}
\cdot
\begin{bmatrix}
-\frac{2}{\sqrt{5}}\\[2pt]
\frac{1}{\sqrt{5}}
\end{bmatrix}\\
&=
-\frac{8}{\sqrt{5}}-\frac{1}{\sqrt{5}}\\
&=
-\frac{9}{\sqrt{5}}.
\end{aligned}
$$
</div>

Therefore,

<div class="math-display">
$$
\boxed{
\vec{x}
=
\frac{2}{\sqrt{5}}\,\vec{u}
-
\frac{9}{\sqrt{5}}\,\vec{v}.
}
$$
</div>

We can check the answer:

<div class="math-display">
$$
\begin{aligned}
\frac{2}{\sqrt{5}}\vec{u}
-
\frac{9}{\sqrt{5}}\vec{v}
&=
\frac{2}{\sqrt{5}}
\begin{bmatrix}
\frac{1}{\sqrt{5}}\\[2pt]
\frac{2}{\sqrt{5}}
\end{bmatrix}
-
\frac{9}{\sqrt{5}}
\begin{bmatrix}
-\frac{2}{\sqrt{5}}\\[2pt]
\frac{1}{\sqrt{5}}
\end{bmatrix}\\
&=
\begin{bmatrix}
\frac25\\[2pt]
\frac45
\end{bmatrix}
+
\begin{bmatrix}
\frac{18}{5}\\[2pt]
-\frac95
\end{bmatrix}\\
&=
\begin{bmatrix}
4\\
-1
\end{bmatrix}\\
&=
\vec{x}.
\end{aligned}
$$
</div>

</details>

{% endraw %}
