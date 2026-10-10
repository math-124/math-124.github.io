---
layout: page
title: "Midterm 1"
description: "Midterm 1 problems."
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
.main-content h2 a.problem-video-button {
  margin-left: 0.5rem;
  vertical-align: middle;
}
</style>

# Midterm 1

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/exams/fa26-mt1/fa26-mt1.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/exams/fa26-mt1/fa26-mt1-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

*This page is meant to give you quick access to problems and their solutions. Refer to the original exam PDF, linked above, for test-taking instructions and formatting. Note that we’ve kept the problem text identical, which is why you may see things like “write your answer in the box below” despite there not being a box on this page.*

---

## Problems

- [Problem 1](#problem-1-10-pts)
- [Problem 2](#problem-2-14-pts)
- [Problem 3](#problem-3-15-pts)
- [Problem 4](#problem-4-11-pts)
- [Problem 5](#problem-5-12-pts)
- [Problem 6](#problem-6-16-pts)
- [Problem 7](#problem-7-10-pts)
- [Problem 8](#problem-8-12-pts)

---

## Problem 1 (10 pts)

Let

<div class="math-display">
$$
\vec d=\begin{bmatrix}6\\-9\\18\end{bmatrix}
$$
</div>

 You may leave numbers as unsimplified fractions.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find a unit vector pointing in the same direction as <span class="math-inline">\\(\vec d\\)</span>.

<details markdown="1"><summary>Solution</summary>

First factor out <span class="math-inline">\\(3\\)</span>:

<div class="math-display">
$$
\vec d=\begin{bmatrix}6\\-9\\18\end{bmatrix}
=3\begin{bmatrix}2\\-3\\6\end{bmatrix}
$$
</div>

 The length of the vector that remains is <span class="math-inline">\\(\sqrt{2^2+(-3)^2+6^2}=\sqrt{49}=7\\)</span>. So <span class="math-inline">\\(\|\vec d\|=3(7)=21\\)</span>. Dividing by the length gives the unit vector:

<div class="math-display">
$$
\frac{\vec d}{\|\vec d\|}
=\frac3{21}\begin{bmatrix}2\\-3\\6\end{bmatrix}
=\frac17\begin{bmatrix}2\\-3\\6\end{bmatrix}
=\boxed{\begin{bmatrix}2/7\\-3/7\\6/7\end{bmatrix}}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Find a vector of length <span class="math-inline">\\(6\\)</span> pointing in the direction opposite to <span class="math-inline">\\(\vec d\\)</span>.

<details markdown="1"><summary>Solution</summary>

Multiply the unit vector from part (a) by <span class="math-inline">\\(-6\\)</span>. The factor <span class="math-inline">\\(6\\)</span> sets the length, and the negative sign reverses the direction:

<div class="math-display">
$$
-6\frac{\vec d}{\|\vec d\|}
=-\frac6{21}\begin{bmatrix}6\\-9\\18\end{bmatrix}
=\boxed{\begin{bmatrix}-12/7\\18/7\\-36/7\end{bmatrix}}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) A robot starts at <span class="math-inline">\\(P=(5,-6,8)\\)</span> and moves <span class="math-inline">\\(x\\)</span> units in the direction of <span class="math-inline">\\(\vec d\\)</span>, ending at <span class="math-inline">\\((9,-12,20)\\)</span>. What is the value of <span class="math-inline">\\(x\\)</span>?

<details markdown="1"><summary>Solution</summary>

The displacement from the starting point to the ending point is

<div class="math-display">
$$
\begin{bmatrix}9-5\\-12-(-6)\\20-8\end{bmatrix}
=\begin{bmatrix}4\\-6\\12\end{bmatrix}
=\frac23\vec d
$$
</div>

 The positive scalar confirms that the robot moves in the direction of <span class="math-inline">\\(\vec d\\)</span>. The distance traveled is the length of this displacement:

<div class="math-display">
$$
x=\left\|\frac23\vec d\right\|=\frac23(21)=\boxed{14}
$$
</div>

</details>

</div>
</div>

</div>

---

## Problem 2 (14 pts)

Suppose <span class="math-inline">\\(\vec u,\vec v\in\mathbb R^3\\)</span> satisfy

<div class="math-display">
$$
\|\vec u\|=3,\qquad \|\vec v\|=4,\qquad \vec u\cdot\vec v=-10
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) Find the value of <span class="math-inline">\\(c\\)</span> for which <span class="math-inline">\\(\vec u+c\vec v\\)</span> is orthogonal to <span class="math-inline">\\(2\vec u-\vec v\\)</span>.

<details markdown="1"><summary>Solution</summary>

Orthogonal vectors have dot product <span class="math-inline">\\(0\\)</span>. Distribute the dot product and use <span class="math-inline">\\(\vec u\cdot\vec u=\|\vec u\|^2\\)</span>:

<div class="math-display">
$$
\begin{align*}
0&=(\vec u+c\vec v)\cdot(2\vec u-\vec v)\\
&=2\|\vec u\|^2-\vec u\cdot\vec v+2c(\vec u\cdot\vec v)-c\|\vec v\|^2\\
&=2(9)-(-10)+2c(-10)-16c\\
&=28-36c
\end{align*}
$$
</div>

Therefore, <span class="math-inline">\\(c=\dfrac{28}{36}=\boxed{\dfrac79}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Find <span class="math-inline">\\(\|3\vec u+\vec v\|\\)</span>.

<details markdown="1"><summary>Solution</summary>

First find the squared length by taking a dot product:

<div class="math-display">
$$
\begin{align*}
\|3\vec u+\vec v\|^2
&=(3\vec u+\vec v)\cdot(3\vec u+\vec v)\\
&=9\|\vec u\|^2+6(\vec u\cdot\vec v)+\|\vec v\|^2\\
&=9(9)+6(-10)+16=37
\end{align*}
$$
</div>

Taking the nonnegative square root gives <span class="math-inline">\\(\boxed{\|3\vec u+\vec v\|=\sqrt{37}}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Find the angle between <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>. Then select the angle type.

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Acute</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Right</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Obtuse</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Acute</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Right</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> Obtuse</span></div>

Using the formula for cosine similarity (which comes from the geometric definition of the dot product):

<div class="math-display">
$$
\cos\theta=\frac{\vec u\cdot\vec v}{\|\vec u\|\|\vec v\|}
=\frac{-10}{3(4)}=-\frac56
$$
</div>

 Thus <span class="math-inline">\\(\boxed{\theta=\cos^{-1}(-5/6)}\\)</span>. The dot product is negative, so the angle is **obtuse** (greater than <span class="math-inline">\\(90^\circ\\)</span>).
</details>

</div>
</div>

</div>

---

## Problem 3 (15 pts)

Consider the line <span class="math-inline">\\(\ell\\)</span> in <span class="math-inline">\\(\mathbb R^2\\)</span> given by

<div class="math-display">
$$
\begin{bmatrix}x\\y\end{bmatrix}
=\begin{bmatrix}5\\3\end{bmatrix}
+t\begin{bmatrix}6\\5\end{bmatrix},\qquad t\in\mathbb R
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Write an equation for <span class="math-inline">\\(\ell\\)</span> in the form <span class="math-inline">\\(ax+by=c\\)</span>.

<details markdown="1"><summary>Solution</summary>

A normal <span class="math-inline">\\(\begin{bmatrix}a\\\\b\end{bmatrix}\\)</span> must be perpendicular to the direction <span class="math-inline">\\(\begin{bmatrix}6\\\\5\end{bmatrix}\\)</span>, so <span class="math-inline">\\(6a+5b=0\\)</span>. An easy choice is <span class="math-inline">\\(a=5\\)</span> and <span class="math-inline">\\(b=-6\\)</span>; this comes from swapping <span class="math-inline">\\(6\\)</span> and <span class="math-inline">\\(5\\)</span> and negating one of them. Then, to find <span class="math-inline">\\(c\\)</span> in

<div class="math-display">
$$
5x-6y=c
$$
</div>

 just plug in a known point on the line, e.g., <span class="math-inline">\\((5,3)\\)</span>:

<div class="math-display">
$$
5(5)-6(3)=7
$$
</div>

 Therefore, one equation is <span class="math-inline">\\(\boxed{5x-6y=7}\\)</span>. Other equations for this line are nonzero scalar multiples of this equation.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(7 pts) Which of the following are valid scalar-parametric forms of <span class="math-inline">\\(\ell\\)</span>? **Select all that apply.** In each option, <span class="math-inline">\\(t\in\mathbb R\\)</span>.

<div class="mc-options"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\(\begin{cases}x=5+12t\\y=4+10t\end{cases}\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\(\begin{cases}x=11+12t\\y=8+10t\end{cases}\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\(\begin{cases}x=-1-18t\\y=-2-15t\end{cases}\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\(\begin{cases}x=11+5t\\y=8-6t\end{cases}\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\(\begin{cases}x=5+12t\\y=4+10t\end{cases}\)</span></span><span class="mc-option"><span class="mc-square mc-correct" aria-hidden="true"></span> <span class="math-inline">\(\begin{cases}x=11+12t\\y=8+10t\end{cases}\)</span></span><span class="mc-option"><span class="mc-square mc-correct" aria-hidden="true"></span> <span class="math-inline">\(\begin{cases}x=-1-18t\\y=-2-15t\end{cases}\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\(\begin{cases}x=11+5t\\y=8-6t\end{cases}\)</span></span></div>

**Select the second and third options.** A parametrization describes <span class="math-inline">\\(\ell\\)</span> when its starting point lies on <span class="math-inline">\\(5x-6y=7\\)</span> and its nonzero direction is a scalar multiple of the original direction.

<ol class="assignment-enumeration" markdown="1">

<li markdown="1">
<div class="assignment-enumeration-label">1.</div>
<div class="assignment-enumeration-content" markdown="1">

**Invalid:** The direction is correct, but <span class="math-inline">\\((5,4)\\)</span> is not on <span class="math-inline">\\(\ell\\)</span>: <span class="math-inline">\\(5(5)-6(4)=1\ne7\\)</span>.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">2.</div>
<div class="assignment-enumeration-content" markdown="1">

**Valid:** <span class="math-inline">\\(5(11)-6(8)=7\\)</span>, and the direction is twice the original direction.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">3.</div>
<div class="assignment-enumeration-content" markdown="1">

**Valid:** <span class="math-inline">\\(5(-1)-6(-2)=7\\)</span>, and the direction is <span class="math-inline">\\(-3\\)</span> times the original direction.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">4.</div>
<div class="assignment-enumeration-content" markdown="1">

**Invalid:** The starting point is on <span class="math-inline">\\(\ell\\)</span>, but the direction is perpendicular to the original direction, rather than parallel to it.

</div></li>
</ol>
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Let <span class="math-inline">\\(\ell'\\)</span> be the line perpendicular to <span class="math-inline">\\(\ell\\)</span> that passes through <span class="math-inline">\\((7,-6)\\)</span>. Write an equation for <span class="math-inline">\\(\ell'\\)</span> in the form <span class="math-inline">\\(ax+by=c\\)</span>.

<details markdown="1"><summary>Solution</summary>

Because <span class="math-inline">\\(\ell'\\)</span> is perpendicular to <span class="math-inline">\\(\ell\\)</span>, the direction of <span class="math-inline">\\(\ell\\)</span> is a normal to <span class="math-inline">\\(\ell'\\)</span>. Thus <span class="math-inline">\\(\ell'\\)</span> has an equation <span class="math-inline">\\(6x+5y=c\\)</span>. Substituting its point <span class="math-inline">\\((7,-6)\\)</span> gives

<div class="math-display">
$$
c=6(7)+5(-6)=12
$$
</div>

 One equation is <span class="math-inline">\\(\boxed{6x+5y=12}\\)</span>.
</details>

</div>
</div>

</div>

---

## Problem 4 (11 pts)

Let <span class="math-inline">\\(\vec u&#95;1\\)</span> and <span class="math-inline">\\(\vec u&#95;2\\)</span> form an orthonormal basis of <span class="math-inline">\\(\mathbb R^2\\)</span>. Suppose

<div class="math-display">
$$
\vec w=6\vec u_1+2\vec u_2.
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find <span class="math-inline">\\(\|\vec w\|\\)</span>.

<details markdown="1"><summary>Solution</summary>

Orthonormality gives <span class="math-inline">\\(\|\vec u&#95;1\|=\|\vec u&#95;2\|=1\\)</span> and <span class="math-inline">\\(\vec u&#95;1\cdot\vec u&#95;2=0\\)</span>. Therefore,

<div class="math-display">
$$
\|\vec w\|^2=(6\vec u_1+2\vec u_2)\cdot(6\vec u_1+2\vec u_2)
=36+24(0)+4=40
$$
</div>

 So <span class="math-inline">\\(\boxed{\|\vec w\|=\sqrt{40}=2\sqrt{10}}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Find <span class="math-inline">\\(\vec w\cdot\vec u&#95;1\\)</span>.

<details markdown="1"><summary>Solution</summary>

Distribute the dot product and use orthonormality:

<div class="math-display">
$$
\vec w\cdot\vec u_1
=6(\vec u_1\cdot\vec u_1)+2(\vec u_2\cdot\vec u_1)
=6(1)+2(0)=\boxed{6}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Suppose <span class="math-inline">\\(\vec v\\)</span> is another vector in <span class="math-inline">\\(\mathbb R^2\\)</span>. Given that the angle between <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec u&#95;1\\)</span> is <span class="math-inline">\\(35^\circ\\)</span>, which of the following *could be* the angle between <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec u&#95;2\\)</span>? **Select all that apply.**

<div class="mc-options"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\(35^\circ\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\(55^\circ\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\(90^\circ\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\(125^\circ\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\(145^\circ\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\(35^\circ\)</span></span><span class="mc-option"><span class="mc-square mc-correct" aria-hidden="true"></span> <span class="math-inline">\(55^\circ\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\(90^\circ\)</span></span><span class="mc-option"><span class="mc-square mc-correct" aria-hidden="true"></span> <span class="math-inline">\(125^\circ\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\(145^\circ\)</span></span></div>

The basis vectors <span class="math-inline">\\(\vec u&#95;1\\)</span> and <span class="math-inline">\\(\vec u&#95;2\\)</span> are perpendicular. We're given that the angle between <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec u&#95;1\\)</span> is <span class="math-inline">\\(35^\circ\\)</span>---this could mean <span class="math-inline">\\(\vec v\\)</span> is <span class="math-inline">\\(35^\circ\\)</span> "below" <span class="math-inline">\\(\vec u&#95;1\\)</span> or <span class="math-inline">\\(35^\circ\\)</span> "above" <span class="math-inline">\\(\vec u&#95;1\\)</span>.

<div style="text-align: center;">
<img src="imgs/fa26-mt1-plot-01.png" alt="Coordinate diagram" class="assignment-vector-plot">
</div>

The angles with <span class="math-inline">\\(\vec u&#95;2\\)</span> are <span class="math-inline">\\(90^\circ-35^\circ=55^\circ\\)</span> and <span class="math-inline">\\(90^\circ+35^\circ=125^\circ\\)</span>. These two pictures cover all possibilities up to rotation and reflection; the length of <span class="math-inline">\\(\vec v\\)</span> does not affect its angles.
</details>

</div>
</div>

</div>

---

## Problem 5 (12 pts)

Consider the vectors

<div class="math-display">
$$
\vec u_1=\frac1{9}\begin{bmatrix}4\\4\\7\end{bmatrix},\qquad
\vec u_2=\frac1{9}\begin{bmatrix}-8\\1\\4\end{bmatrix},\qquad
\vec w=\begin{bmatrix}4\\2\\3\end{bmatrix}
$$
</div>

 The vector <span class="math-inline">\\(\vec w\\)</span> is in <span class="math-inline">\\(\operatorname{span}(\vec u&#95;1,\vec u&#95;2)\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) Verify that <span class="math-inline">\\(\vec u&#95;1\\)</span> and <span class="math-inline">\\(\vec u&#95;2\\)</span> are orthogonal and each has length <span class="math-inline">\\(1\\)</span>.

<details markdown="1"><summary>Solution</summary>

Compute the dot product and both lengths:

<div class="math-display">
$$
\begin{align*}
\vec u_1\cdot\vec u_2&=\frac{4(-8)+4(1)+7(4)}{81}=\frac{-32+4+28}{81}=0\\
\|\vec u_1\|&=\frac{\sqrt{4^2+4^2+7^2}}9=\frac{\sqrt{81}}9=1\\
\|\vec u_2\|&=\frac{\sqrt{(-8)^2+1^2+4^2}}9=\frac{\sqrt{81}}9=1
\end{align*}
$$
</div>

The zero dot product verifies orthogonality, and the two lengths verify that both vectors are unit vectors.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) Write <span class="math-inline">\\(\vec w\\)</span> as a linear combination of <span class="math-inline">\\(\vec u&#95;1\\)</span> and <span class="math-inline">\\(\vec u&#95;2\\)</span>.

<details markdown="1"><summary>Solution</summary>

Write <span class="math-inline">\\(\vec w=a\vec u&#95;1+b\vec u&#95;2\\)</span>. Taking dot products with the orthonormal vectors isolates the coefficients:

<div class="math-display">
$$
\begin{align*}
a=\vec w\cdot\vec u_1&=\frac{4(4)+2(4)+3(7)}9=\frac{45}9=5\\
b=\vec w\cdot\vec u_2&=\frac{4(-8)+2(1)+3(4)}9=\frac{-18}9=-2
\end{align*}
$$
</div>

Therefore, <span class="math-inline">\\(\boxed{\vec w=5\vec u&#95;1-2\vec u&#95;2}\\)</span>. We can check the result directly:

<div class="math-display">
$$
5\vec u_1-2\vec u_2
=\frac19\begin{bmatrix}20+16\\20-2\\35-8\end{bmatrix}
=\begin{bmatrix}4\\2\\3\end{bmatrix}=\vec w
$$
</div>

</details>

</div>
</div>

</div>

---

## Problem 6 (16 pts)

Let <span class="math-inline">\\(P\\)</span> be the plane through <span class="math-inline">\\((6,-5,8)\\)</span> with direction vectors

<div class="math-display">
$$
\vec u=\begin{bmatrix}2\\5\\3\end{bmatrix},\qquad
\vec v=\begin{bmatrix}4\\5\\1\end{bmatrix}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(8 pts) Write an equation for <span class="math-inline">\\(P\\)</span> in the form <span class="math-inline">\\(ax+by+cz=d\\)</span>.

<details markdown="1"><summary>Solution</summary>

Let <span class="math-inline">\\(\vec n=\begin{bmatrix}a\\\\b\\\\c\end{bmatrix}\\)</span> be a normal. It must be perpendicular to both directions, so

<div class="math-display">
$$
\begin{cases}2a+5b+3c=0\\4a+5b+c=0\end{cases}
$$
</div>

 Subtract the first equation from the second to get <span class="math-inline">\\(2a-2c=0\\)</span>, or <span class="math-inline">\\(c=a\\)</span>. Substitute into the first:

<div class="math-display">
$$
2a+5b+3a=0\quad\Longrightarrow\quad b=-a
$$
</div>

 Choose <span class="math-inline">\\(a=1\\)</span>, giving <span class="math-inline">\\(\vec n=\begin{bmatrix}1\\\\-1\\\\1\end{bmatrix}\\)</span>. The plane therefore has an equation <span class="math-inline">\\(x-y+z=d\\)</span>. Its point <span class="math-inline">\\((6,-5,8)\\)</span> determines the constant:

<div class="math-display">
$$
d=6-(-5)+8=19
$$
</div>

 Thus <span class="math-inline">\\(\boxed{P:\ x-y+z=19}\\)</span>. The two given directions are not scalar multiples, so they span a plane, and our normal is perpendicular to both.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(8 pts) For each vector-parametric equation below, select whether it is a valid description of <span class="math-inline">\\(P\\)</span> and give a brief justification. In every option, <span class="math-inline">\\(s,t\in\mathbb R\\)</span>.

<em>Hint: Use the equation you found in the previous part.</em>

<ol class="assignment-enumeration" markdown="1">

<li markdown="1">
<div class="assignment-enumeration-label">i)</div>
<div class="assignment-enumeration-content" markdown="1">

(2 pts) <span class="math-inline">\\(\displaystyle\begin{bmatrix}x\\\\y\\\\z\end{bmatrix}=\begin{bmatrix}6\\\\-5\\\\8\end{bmatrix}+s(\vec u+\vec v)+t\vec v\\)</span>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Valid</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Invalid</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> Valid</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Invalid</span></div>

**Valid.** The starting point is on <span class="math-inline">\\(P\\)</span>, and <span class="math-inline">\\(\vec u+\vec v\\)</span> and <span class="math-inline">\\(\vec v\\)</span> span the same directions as <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>: recover <span class="math-inline">\\(\vec u=(\vec u+\vec v)-\vec v\\)</span>. Thus they still span the entire plane.
</details>

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">ii)</div>
<div class="assignment-enumeration-content" markdown="1">

(2 pts) <span class="math-inline">\\(\displaystyle\begin{bmatrix}x\\\\y\\\\z\end{bmatrix}=\begin{bmatrix}9\\\\-4\\\\6\end{bmatrix}+s\vec u+t\vec v\\)</span>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Valid</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Invalid</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> Valid</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Invalid</span></div>

**Valid.** The new starting point satisfies <span class="math-inline">\\(9-(-4)+6=19\\)</span>, so it lies on <span class="math-inline">\\(P\\)</span>. The original two directions still span the plane; moving the starting point within <span class="math-inline">\\(P\\)</span> does not change the plane.
</details>

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">iii)</div>
<div class="assignment-enumeration-content" markdown="1">

(2 pts) <span class="math-inline">\\(\displaystyle\begin{bmatrix}x\\\\y\\\\z\end{bmatrix}=\begin{bmatrix}6\\\\-5\\\\9\end{bmatrix}+s\vec u+t\vec v\\)</span>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Valid</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Invalid</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Valid</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> Invalid</span></div>

**Invalid.** The starting point does not satisfy the plane's equation:

<div class="math-display">
$$
6-(-5)+9=20\ne19
$$
</div>

 This parametrization describes a parallel plane, <span class="math-inline">\\(x-y+z=20\\)</span>.
</details>

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">iv)</div>
<div class="assignment-enumeration-content" markdown="1">

(2 pts) <span class="math-inline">\\(\displaystyle\begin{bmatrix}x\\\\y\\\\z\end{bmatrix}=\begin{bmatrix}6\\\\-5\\\\8\end{bmatrix}+s(2\vec u-3\vec v)+t(4\vec u-6\vec v)\\)</span>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Valid</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Invalid</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Valid</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> Invalid</span></div>

**Invalid.** The directions are scalar multiples:

<div class="math-display">
$$
4\vec u-6\vec v=2(2\vec u-3\vec v)
$$
</div>

 They provide only one independent direction, so this describes a line within <span class="math-inline">\\(P\\)</span>, rather than the whole plane.
</details>

</div></li>
</ol>

</div>
</div>

</div>

---

## Problem 7 (10 pts)

The equations

<div class="math-display">
$$
P_1:\ 5x+3y=10,\qquad P_2:\ 2x+6y+4z=20
$$
</div>

 describe two planes in <span class="math-inline">\\(\mathbb R^3\\)</span>. Write the set of common solutions to these two equations in vector-parametric form.

<details markdown="1"><summary>Solution</summary>

First solve for <span class="math-inline">\\(y\\)</span> in terms of <span class="math-inline">\\(x\\)</span> using the first equation:

<div class="math-display">
$$
5x+3y=10\quad\Longrightarrow\quad y=\frac{10-5x}{3}
$$
</div>

 Substitute this into the second equation to solve for <span class="math-inline">\\(z\\)</span>:

<div class="math-display">
$$
\begin{align*}
2x+6\left(\frac{10-5x}{3}\right)+4z&=20\\
2x+20-10x+4z&=20\\
z&=2x
\end{align*}
$$
</div>

Since <span class="math-inline">\\(x\\)</span> can be any real number, the common solutions are

<div class="math-display">
$$
\begin{bmatrix}x\\y\\z\end{bmatrix}
=\begin{bmatrix}0\\10/3\\0\end{bmatrix}
+x\begin{bmatrix}1\\-5/3\\2\end{bmatrix},\qquad x\in\mathbb R
$$
</div>

 This is already a valid answer. To avoid fractions, multiply the direction vector by <span class="math-inline">\\(3\\)</span>, which does not change the line. Choosing the point corresponding to <span class="math-inline">\\(x=2\\)</span> as our starting point gives

<div class="math-display">
$$
\boxed{\begin{bmatrix}x\\y\\z\end{bmatrix}
=\begin{bmatrix}2\\0\\4\end{bmatrix}
+t\begin{bmatrix}3\\-5\\6\end{bmatrix},\qquad t\in\mathbb R}
$$
</div>

 Equivalently, we have reparameterized by setting <span class="math-inline">\\(x=2+3t\\)</span>. As <span class="math-inline">\\(t\\)</span> ranges over all real numbers, <span class="math-inline">\\(x\\)</span> does too, so we still describe the entire intersection line.
</details>

---

## Problem 8 (12 pts)

Let

<div class="math-display">
$$
\vec v=\begin{bmatrix}7\\5\\6\end{bmatrix},\qquad
\ell=\operatorname{span}\left(\begin{bmatrix}4\\-5\\7\end{bmatrix}\right),\qquad
P:\ 4x-5y+7z=0
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) Find the orthogonal projection of <span class="math-inline">\\(\vec v\\)</span> onto <span class="math-inline">\\(\ell\\)</span>.

<details markdown="1"><summary>Solution</summary>

Let <span class="math-inline">\\(\vec w=\begin{bmatrix}4\\\\-5\\\\7\end{bmatrix}\\)</span>, the vector spanning <span class="math-inline">\\(\ell\\)</span>. Use the projection formula:

<div class="math-display">
$$
\begin{align*}
\operatorname{proj}_{\ell}(\vec v)
&=\frac{\vec v\cdot\vec w}{\vec w\cdot\vec w}\vec w\\
&=\frac{7(4)+5(-5)+6(7)}{4^2+(-5)^2+7^2}\begin{bmatrix}4\\-5\\7\end{bmatrix}\\
&=\frac{45}{90}\begin{bmatrix}4\\-5\\7\end{bmatrix}
=\boxed{\begin{bmatrix}2\\-5/2\\7/2\end{bmatrix}}
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) Find the orthogonal projection of <span class="math-inline">\\(\vec v\\)</span> onto <span class="math-inline">\\(P\\)</span>.

<details markdown="1"><summary>Solution</summary>

The coefficients of <span class="math-inline">\\(P\\)</span> tell us that the vector <span class="math-inline">\\(\begin{bmatrix}4\\\\-5\\\\7\end{bmatrix}\\)</span> is perpendicular to <span class="math-inline">\\(P\\)</span>. But <span class="math-inline">\\(\ell\\)</span> is the span of <span class="math-inline">\\(\begin{bmatrix}4\\\\-5\\\\7\end{bmatrix}\\)</span>, so <span class="math-inline">\\(P\\)</span> and <span class="math-inline">\\(\ell\\)</span> are perpendicular, and <span class="math-inline">\\(\vec v\\)</span>'s projections onto <span class="math-inline">\\(\ell\\)</span> and onto <span class="math-inline">\\(P\\)</span> sum to <span class="math-inline">\\(\vec v\\)</span> exactly. Thus,

<div class="math-display">
$$
\begin{align*}
\operatorname{proj}_{P}(\vec v)
&=\vec v-\operatorname{proj}_{\ell}(\vec v)\\
&=\begin{bmatrix}7\\5\\6\end{bmatrix}-\begin{bmatrix}2\\-5/2\\7/2\end{bmatrix}
=\boxed{\begin{bmatrix}5\\15/2\\5/2\end{bmatrix}}
\end{align*}
$$
</div>

As a check, this vector lies in <span class="math-inline">\\(P\\)</span>:

<div class="math-display">
$$
4(5)-5\left(\frac{15}2\right)+7\left(\frac52\right)=0
$$
</div>

</details>
</div>
</div>

</div>

{% endraw %}
