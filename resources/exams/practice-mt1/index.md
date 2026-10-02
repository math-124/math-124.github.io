---
layout: page
title: "Practice Midterm 1"
description: "Practice Midterm 1 problems."
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

# Practice Midterm 1

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/exams/practice-mt1/practice-mt1.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/exams/practice-mt1/practice-mt1-solutions.pdf" target="_blank">Solutions PDF ✅</a>
<a class="btn btn-info assignment-pdf-button" href="https://www.youtube.com/playlist?list=PLYUNPCpJ6xgs" target="_blank" rel="noopener">Video Walkthroughs 🎥</a>
</div>

*This page is meant to give you quick access to problems and their solutions. Refer to the original exam PDF, linked above, for test-taking instructions and formatting. Note that we’ve kept the problem text identical, which is why you may see things like “write your answer in the box below” despite there not being a box on this page.*

---

## Problems

- [Problem 1](#problem-1-9-pts)
- [Problem 2](#problem-2-16-pts)
- [Problem 3](#problem-3-14-pts)
- [Problem 4](#problem-4-14-pts)
- [Problem 5](#problem-5-19-pts)
- [Problem 6](#problem-6-18-pts)
- [Problem 7](#problem-7-10-pts)

---

<h2 id="problem-1-9-pts" markdown="span">Problem 1 (9 pts) <a class="btn btn-info assignment-pdf-button problem-video-button" href="https://youtu.be/HVlCDE2MwNY" target="_blank" rel="noopener" aria-label="Walkthrough video for Problem 1">🎥 Walkthrough</a></h2>

Consider the points

<div class="math-display">
$$
P=(-7,8,-6),\qquad Q=(8,-12,19)
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Let <span class="math-inline">\\(\vec d\\)</span> be the vector pointing from <span class="math-inline">\\(P\\)</span> to <span class="math-inline">\\(Q\\)</span>. Find <span class="math-inline">\\(\vec d\\)</span>. Give your answer as a vector.

<details markdown="1"><summary>Solution</summary>

Subtract the coordinates of the starting point from those of the ending point.

<div class="math-display">
$$
\vec d=\begin{bmatrix}8-(-7)\\-12-8\\19-(-6)\end{bmatrix}
=\boxed{\begin{bmatrix}15\\-20\\25\end{bmatrix}}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Find the distance between <span class="math-inline">\\(P\\)</span> and <span class="math-inline">\\(Q\\)</span>.

<details markdown="1"><summary>Solution</summary>

The distance is the length of the vector from <span class="math-inline">\\(P\\)</span> to <span class="math-inline">\\(Q\\)</span>. Notice that

<div class="math-display">
$$
\vec d=5\begin{bmatrix}3\\-4\\5\end{bmatrix}
$$
</div>

 The length of a scalar multiple is the absolute value of the scalar times the original length. So,

<div class="math-display">
$$
\Vert \vec d\Vert =5\left\Vert \begin{bmatrix}3\\-4\\5\end{bmatrix}\right\Vert
=5\sqrt{3^2+(-4)^2+5^2}=5\sqrt{50}=\boxed{25\sqrt2}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find the coordinates of the point <span class="math-inline">\\(R\\)</span> that is <span class="math-inline">\\(\frac35\\)</span> of the way from <span class="math-inline">\\(P\\)</span> to <span class="math-inline">\\(Q\\)</span>.

<details markdown="1"><summary>Solution</summary>

Start at <span class="math-inline">\\(P\\)</span> and add <span class="math-inline">\\(\frac35\\)</span> of the vector pointing from <span class="math-inline">\\(P\\)</span> to <span class="math-inline">\\(Q\\)</span>.

<div class="math-display">
$$
\begin{bmatrix}-7\\8\\-6\end{bmatrix}
+\frac35\begin{bmatrix}15\\-20\\25\end{bmatrix}
=\begin{bmatrix}-7\\8\\-6\end{bmatrix}
+\begin{bmatrix}9\\-12\\15\end{bmatrix}
=\begin{bmatrix}2\\-4\\9\end{bmatrix}
$$
</div>

 So, <span class="math-inline">\\(\boxed{R=(2,-4,9)}\\)</span>.
</details>

</div>
</div>

</div>

---

<h2 id="problem-2-16-pts" markdown="span">Problem 2 (16 pts) <a class="btn btn-info assignment-pdf-button problem-video-button" href="https://youtu.be/2EzvyV4OoeY" target="_blank" rel="noopener" aria-label="Walkthrough video for Problem 2">🎥 Walkthrough</a></h2>

Suppose <span class="math-inline">\\(\vec u,\vec v\in\mathbb R^3\\)</span> satisfy

<div class="math-display">
$$
\Vert \vec u\Vert =5,\qquad \Vert \vec v\Vert =4,\qquad \vec u\cdot\vec v=-6
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(7 pts)

<ol class="assignment-enumeration" markdown="1">

<li markdown="1">
<div class="assignment-enumeration-label">I)</div>
<div class="assignment-enumeration-content" markdown="1">

(5 pts) Find <span class="math-inline">\\((5\vec u-6\vec v)\cdot(8\vec u+10\vec v)\\)</span>. Show your work.

<details markdown="1"><summary>Solution</summary>

Distribute the dot product, using <span class="math-inline">\\(\vec u\cdot\vec u=\Vert \vec u\Vert ^2\\)</span> and <span class="math-inline">\\(\vec v\cdot\vec v=\Vert \vec v\Vert ^2\\)</span>.

<div class="math-display">
$$
\begin{align*}
(5\vec u-6\vec v)\cdot(8\vec u+10\vec v)
&=40\Vert \vec u\Vert ^2+(50-48)(\vec u\cdot\vec v)-60\Vert \vec v\Vert ^2\\
&=20\bigl(2\Vert \vec u\Vert ^2-3\Vert \vec v\Vert ^2\bigr)+2(\vec u\cdot\vec v)\\
&=20(50-48)+2(-6)=40-12=\boxed{28}
\end{align*}
$$
</div>

</details>

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">II)</div>
<div class="assignment-enumeration-content" markdown="1">

(2 pts) What type of angle is formed by <span class="math-inline">\\(5\vec u-6\vec v\\)</span> and <span class="math-inline">\\(8\vec u+10\vec v\\)</span>? Select one.

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Acute</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Right</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Obtuse</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> Acute</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Right</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Obtuse</span></div>

The dot product is positive, so the angle is <span class="math-inline">\\(\boxed{\text{acute}}\\)</span>. Recall that <span class="math-inline">\\(\vec a\cdot\vec b=\Vert \vec a\Vert \Vert \vec b\Vert \cos\theta\\)</span>; a positive dot product means <span class="math-inline">\\(\cos\theta&gt;0\\)</span>.
</details>

</div></li>
</ol>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Find <span class="math-inline">\\(\Vert \vec u-\vec v\Vert\\)</span>.

<details markdown="1"><summary>Solution</summary>

First find the squared length by taking the dot product of the vector with itself.

<div class="math-display">
$$
\begin{align*}
\Vert \vec u-\vec v\Vert ^2
&=(\vec u-\vec v)\cdot(\vec u-\vec v)\\
&=\Vert \vec u\Vert ^2-2(\vec u\cdot\vec v)+\Vert \vec v\Vert ^2\\
&=25-2(-6)+16=53
\end{align*}
$$
</div>

Therefore, <span class="math-inline">\\(\boxed{\Vert \vec u-\vec v\Vert =\sqrt{53}}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Could a unit vector <span class="math-inline">\\(\vec w\in\mathbb R^3\\)</span> satisfy <span class="math-inline">\\(\vec u\cdot\vec w=9\\)</span>? Explain why or why not.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(\boxed{\text{No}}\\)</span>. By the Cauchy--Schwarz inequality, a unit vector <span class="math-inline">\\(\vec w\\)</span> must satisfy

<div class="math-display">
$$
|\vec u\cdot\vec w|\leq\Vert \vec u\Vert \Vert \vec w\Vert =5(1)=5
$$
</div>

 Since <span class="math-inline">\\(9&gt;5\\)</span>, the proposed dot product is impossible.
</details>

</div>
</div>

</div>

---

<h2 id="problem-3-14-pts" markdown="span">Problem 3 (14 pts) <a class="btn btn-info assignment-pdf-button problem-video-button" href="https://youtu.be/a0ucVLmbJDk" target="_blank" rel="noopener" aria-label="Walkthrough video for Problem 3">🎥 Walkthrough</a></h2>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Let <span class="math-inline">\\(\ell\\)</span> be the line in <span class="math-inline">\\(\mathbb R^2\\)</span> defined by <span class="math-inline">\\(5x+7y=35\\)</span>. Find nonzero vectors <span class="math-inline">\\(\vec n\\)</span> and <span class="math-inline">\\(\vec d\\)</span> such that <span class="math-inline">\\(\vec n\\)</span> is perpendicular to <span class="math-inline">\\(\ell\\)</span> and <span class="math-inline">\\(\vec d\\)</span> is parallel to <span class="math-inline">\\(\ell\\)</span>.

<span class="math-inline">\\(\vec n=\\)</span>

<span class="answer-blank"></span>

<span class="math-inline">\\(\vec d=\\)</span>

<span class="answer-blank"></span>

<details markdown="1"><summary>Solution</summary>

The coefficients of <span class="math-inline">\\(x\\)</span> and <span class="math-inline">\\(y\\)</span> give a normal vector. A direction vector must be orthogonal to it, so one choice is

<div class="math-display">
$$
\boxed{\vec n=\begin{bmatrix}5\\7\end{bmatrix}},\qquad
\boxed{\vec d=\begin{bmatrix}7\\-5\end{bmatrix}}
$$
</div>

 These work because <span class="math-inline">\\(\vec n\cdot\vec d=5(7)+7(-5)=0\\)</span>. Any nonzero scalar multiples also work.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Write the line <span class="math-inline">\\(\ell\\)</span>, defined by <span class="math-inline">\\(5x+7y=35\\)</span>, in vector-parametric form.

<details markdown="1"><summary>Solution</summary>

The point <span class="math-inline">\\((7,0)\\)</span> is on <span class="math-inline">\\(\ell\\)</span>, and part (a) gives a direction vector. So, one vector-parametric form is

<div class="math-display">
$$
\boxed{\begin{bmatrix}x\\y\end{bmatrix}
=\begin{bmatrix}7\\0\end{bmatrix}
+t\begin{bmatrix}7\\-5\end{bmatrix},\qquad t\in\mathbb R}
$$
</div>

 Substituting gives <span class="math-inline">\\(5(7+7t)+7(-5t)=35\\)</span> for every <span class="math-inline">\\(t\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(7 pts) Consider another line <span class="math-inline">\\(\ell'\\)</span>, defined by <span class="math-inline">\\(7x-5y=13\\)</span>. Which of the following are valid scalar-parametric forms of <span class="math-inline">\\(\ell'\\)</span>? **Select all that apply.** In each option, <span class="math-inline">\\(t\in\mathbb R\\)</span>.

<div class="mc-options"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\(\begin{cases}x=9+5t\\y=10+7t\end{cases}\)</span></span></div>

<div class="mc-options"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\(\begin{cases}x=9+7t\\y=10-5t\end{cases}\)</span></span></div>

<div class="mc-options"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\(\begin{cases}x=-6-10t\\y=-11-14t\end{cases}\)</span></span></div>

<div class="mc-options"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\(\begin{cases}x=14+15t\\y=17+21t\end{cases}\)</span></span></div>

<div class="mc-options"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\(\begin{cases}x=8+5t\\y=9+7t\end{cases}\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

Select <span class="math-inline">\\(\boxed{\text{the first, third, and fourth options}}\\)</span>. Substitute each option into <span class="math-inline">\\(7x-5y=13\\)</span>:

-   **Option 1:** <span class="math-inline">\\(x=9+5t,\ y=10+7t\\)</span>. Substituting gives <span class="math-inline">\\(7(9+5t)-5(10+7t)=63+35t-50-35t=13\\)</span>. The equation is satisfied for every <span class="math-inline">\\(t\\)</span>, so this option is valid.

-   **Option 2:** <span class="math-inline">\\(x=9+7t,\ y=10-5t\\)</span>. Substituting gives <span class="math-inline">\\(7(9+7t)-5(10-5t)=63+49t-50+25t=13+74t\\)</span>. The equation is satisfied only when <span class="math-inline">\\(t=0\\)</span>, so this option is invalid.

-   **Option 3:** <span class="math-inline">\\(x=-6-10t,\ y=-11-14t\\)</span>. Substituting gives <span class="math-inline">\\(7(-6-10t)-5(-11-14t)=-42-70t+55+70t=13\\)</span>. The equation is satisfied for every <span class="math-inline">\\(t\\)</span>, so this option is valid.

-   **Option 4:** <span class="math-inline">\\(x=14+15t,\ y=17+21t\\)</span>. Substituting gives <span class="math-inline">\\(7(14+15t)-5(17+21t)=98+105t-85-105t=13\\)</span>. The equation is satisfied for every <span class="math-inline">\\(t\\)</span>, so this option is valid.

-   **Option 5:** <span class="math-inline">\\(x=8+5t,\ y=9+7t\\)</span>. Substituting gives <span class="math-inline">\\(7(8+5t)-5(9+7t)=56+35t-45-35t=11\ne13\\)</span>. The equation is never satisfied, so this option is invalid.
</details>

</div>
</div>

</div>

---

<h2 id="problem-4-14-pts" markdown="span">Problem 4 (14 pts) <a class="btn btn-info assignment-pdf-button problem-video-button" href="https://youtu.be/4nDllJnq--8" target="_blank" rel="noopener" aria-label="Walkthrough video for Problem 4">🎥 Walkthrough</a></h2>

The vectors

<div class="math-display">
$$
\vec u_1=\frac1{19}\begin{bmatrix}-15\\10\\6\end{bmatrix},\qquad
\vec u_2=\frac1{19}\begin{bmatrix}-6\\-15\\10\end{bmatrix},\qquad
\vec u_3=\frac1{19}\begin{bmatrix}10\\6\\15\end{bmatrix}
$$
</div>

 form an orthonormal basis of <span class="math-inline">\\(\mathbb R^3\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Given that these vectors form an orthonormal basis of <span class="math-inline">\\(\mathbb R^3\\)</span>, find the following quantities.

<span class="math-inline">\\(\vec u&#95;1\cdot\vec u&#95;3=\\)</span>

<span class="answer-blank"></span>

<span class="math-inline">\\(\Vert \vec u&#95;1\Vert =\\)</span>

<span class="answer-blank"></span>

<details markdown="1"><summary>Solution</summary>

Orthonormal means that distinct basis vectors are orthogonal and each basis vector has length 1. Therefore,

<div class="math-display">
$$
\boxed{\vec u_1\cdot\vec u_3=0},\qquad \boxed{\Vert \vec u_1\Vert =1}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find <span class="math-inline">\\(\Vert 5\vec u&#95;1-7\vec u&#95;2\Vert\\)</span>.

<details markdown="1"><summary>Solution</summary>

Since <span class="math-inline">\\(\vec u&#95;1\\)</span> and <span class="math-inline">\\(\vec u&#95;2\\)</span> are orthogonal unit vectors,

<div class="math-display">
$$
\begin{align*}
\Vert 5\vec u_1-7\vec u_2\Vert ^2
&=25\Vert \vec u_1\Vert ^2-70(\vec u_1\cdot\vec u_2)+49\Vert \vec u_2\Vert ^2\\
&=25+49=74
\end{align*}
$$
</div>

So, <span class="math-inline">\\(\boxed{\Vert 5\vec u&#95;1-7\vec u&#95;2\Vert =\sqrt{74}}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(8 pts) Let <span class="math-inline">\\(\vec w=\begin{bmatrix}-4\\\\3\\\\4\end{bmatrix}\\)</span>. Write <span class="math-inline">\\(\vec w\\)</span> as a linear combination of <span class="math-inline">\\(\vec u&#95;1\\)</span>, <span class="math-inline">\\(\vec u&#95;2\\)</span>, and <span class="math-inline">\\(\vec u&#95;3\\)</span>.

<details markdown="1"><summary>Solution</summary>

For an orthonormal basis, the coefficient of <span class="math-inline">\\(\vec u&#95;i\\)</span> is <span class="math-inline">\\(\vec w\cdot\vec u&#95;i\\)</span>. Taking dot products gives

<div class="math-display">
$$
\begin{align*}
\vec w\cdot\vec u_1&=\frac{(-4)(-15)+3(10)+4(6)}{19}=\frac{114}{19}=6\\
\vec w\cdot\vec u_2&=\frac{(-4)(-6)+3(-15)+4(10)}{19}=\frac{19}{19}=1\\
\vec w\cdot\vec u_3&=\frac{(-4)(10)+3(6)+4(15)}{19}=\frac{38}{19}=2
\end{align*}
$$
</div>

Therefore,

<div class="math-display">
$$
\boxed{\vec w=6\vec u_1+\vec u_2+2\vec u_3}
$$
</div>

</details>

</div>
</div>

</div>

---

<h2 id="problem-5-19-pts" markdown="span">Problem 5 (19 pts) <a class="btn btn-info assignment-pdf-button problem-video-button" href="https://youtu.be/qbKAUGUNbg8" target="_blank" rel="noopener" aria-label="Walkthrough video for Problem 5">🎥 Walkthrough</a></h2>

Let <span class="math-inline">\\(P\\)</span> be the plane through the points

<div class="math-display">
$$
A=(8,-15,6),\qquad B=(13,-5,11),\qquad C=(15,-8,7)
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Express <span class="math-inline">\\(P\\)</span> in vector-parametric form.

<details markdown="1"><summary>Solution</summary>

Use <span class="math-inline">\\(A\\)</span> as a starting point. The directions <span class="math-inline">\\(\vec d&#95;1\\)</span> from <span class="math-inline">\\(A\\)</span> to <span class="math-inline">\\(B\\)</span> and <span class="math-inline">\\(\vec d&#95;2\\)</span> from <span class="math-inline">\\(A\\)</span> to <span class="math-inline">\\(C\\)</span> are not scalar multiples, so they span the plane.

<div class="math-display">
$$
\boxed{\begin{bmatrix}x\\y\\z\end{bmatrix}
=\begin{bmatrix}8\\-15\\6\end{bmatrix}
+s\underbrace{\begin{bmatrix}5\\10\\5\end{bmatrix}}_{\vec d_1}
+t\underbrace{\begin{bmatrix}7\\7\\1\end{bmatrix}}_{\vec d_2},\quad s,t\in\mathbb R}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(8 pts) Write an equation for <span class="math-inline">\\(P\\)</span> in the form <span class="math-inline">\\(ax+by+cz=d\\)</span>.

<details markdown="1"><summary>Solution</summary>

The coefficients <span class="math-inline">\\(a,b,c\\)</span> of a nonzero normal vector must satisfy

<div class="math-display">
$$
\begin{cases}
5a+10b+5c=0\\
7a+7b+c=0
\end{cases}
$$
</div>

 The second equation gives <span class="math-inline">\\(c=-7a-7b\\)</span>. Substituting into the first gives <span class="math-inline">\\(-30a-25b=0\\)</span>, or <span class="math-inline">\\(6a+5b=0\\)</span>.

Choose <span class="math-inline">\\(a=5\\)</span>. Then <span class="math-inline">\\(b=-6\\)</span> and <span class="math-inline">\\(c=-7(5)-7(-6)=7\\)</span>. Since <span class="math-inline">\\(A\\)</span> lies on the plane <span class="math-inline">\\(5x-6y+7z=d\\)</span>,

<div class="math-display">
$$
d=5(8)-6(-15)+7(6)=172
$$
</div>

 So, the equation is <span class="math-inline">\\(\boxed{5x-6y+7z=172}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) Suppose <span class="math-inline">\\(C\\)</span> is replaced by <span class="math-inline">\\(C'=(23,15,21)\\)</span>, while <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span> stay the same. Do the three points <span class="math-inline">\\(A\\)</span>, <span class="math-inline">\\(B\\)</span>, <span class="math-inline">\\(C'\\)</span> determine a unique plane? Explain what changes geometrically.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(\boxed{\text{No}}\\)</span>. The new direction vector is

<div class="math-display">
$$
\vec d_3=\begin{bmatrix}23-8\\15-(-15)\\21-6\end{bmatrix}
=\begin{bmatrix}15\\30\\15\end{bmatrix}
=3\vec d_1
$$
</div>

 Unlike <span class="math-inline">\\(\vec d&#95;1\\)</span> and <span class="math-inline">\\(\vec d&#95;2\\)</span>, the vectors <span class="math-inline">\\(\vec d&#95;1\\)</span> and <span class="math-inline">\\(\vec d&#95;3\\)</span> are linearly dependent. The three points are now collinear, so infinitely many planes contain their line.
</details>

</div>
</div>

</div>

---

<h2 id="problem-6-18-pts" markdown="span">Problem 6 (18 pts) <a class="btn btn-info assignment-pdf-button problem-video-button" href="https://youtu.be/Ggli3iB3DEw" target="_blank" rel="noopener" aria-label="Walkthrough video for Problem 6">🎥 Walkthrough</a></h2>

Consider the line <span class="math-inline">\\(\ell\\)</span> in <span class="math-inline">\\(\mathbb R^3\\)</span> given by

<div class="math-display">
$$
\begin{bmatrix}x\\y\\z\end{bmatrix}
=\begin{bmatrix}7\\-8\\11\end{bmatrix}
+t\begin{bmatrix}5\\-6\\7\end{bmatrix},\qquad t\in\mathbb R
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(10 pts) Find equations for two distinct planes whose intersection is exactly <span class="math-inline">\\(\ell\\)</span>. Your equations should both be of the form <span class="math-inline">\\(ax+by+cz=d\\)</span>.

<details markdown="1"><summary>Solution</summary>

Each plane must contain <span class="math-inline">\\((7,-8,11)\\)</span>, and its normal must be orthogonal to the line's direction <span class="math-inline">\\(\begin{bmatrix}5\\\\-6\\\\7\end{bmatrix}\\)</span>. Two nonparallel choices are

<div class="math-display">
$$
\vec n_1=\begin{bmatrix}6\\5\\0\end{bmatrix},\qquad
\vec n_2=\begin{bmatrix}7\\0\\-5\end{bmatrix}
$$
</div>

 Their dot products with the direction vector are <span class="math-inline">\\(30-30=0\\)</span> and <span class="math-inline">\\(35-35=0\\)</span>. Substituting the point into each plane gives

<div class="math-display">
$$
6(7)+5(-8)=2,\qquad 7(7)-5(11)=-6
$$
</div>

 So, one answer is

<div class="math-display">
$$
\boxed{6x+5y+0z=2},\qquad \boxed{7x+0y-5z=-6}
$$
</div>
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(8 pts) A student proposes the equations <span class="math-inline">\\(11x+15y+5z=12\\)</span> and <span class="math-inline">\\(55x+75y+25z=60\\)</span>. Every point on <span class="math-inline">\\(\ell\\)</span> satisfies both. Explain why these equations, unlike those in part (a), do not intersect exactly at the line <span class="math-inline">\\(\ell\\)</span>. Describe their intersection and give one point in it that is not on <span class="math-inline">\\(\ell\\)</span>.

<details markdown="1"><summary>Solution</summary>

The second equation is five times the first, so they describe the same plane. Their intersection is that entire plane, which contains points outside <span class="math-inline">\\(\ell\\)</span>.

One such point is <span class="math-inline">\\(\boxed{(2,1,-5)}\\)</span>, since

<div class="math-display">
$$
11(2)+15(1)+5(-5)=12,\qquad
55(2)+75(1)+25(-5)=60
$$
</div>

 It is not on <span class="math-inline">\\(\ell\\)</span>: its <span class="math-inline">\\(x\\)</span>-coordinate would require <span class="math-inline">\\(7+5t=2\\)</span>, or <span class="math-inline">\\(t=-1\\)</span>, but then the line's <span class="math-inline">\\(y\\)</span>-coordinate would be <span class="math-inline">\\(-8-6(-1)=-2\\)</span>, rather than 1.
</details>

</div>
</div>

</div>

---

<h2 id="problem-7-10-pts" markdown="span">Problem 7 (10 pts) <a class="btn btn-info assignment-pdf-button problem-video-button" href="https://youtu.be/LIOhnTC4ti4" target="_blank" rel="noopener" aria-label="Walkthrough video for Problem 7">🎥 Walkthrough</a></h2>

Let

<div class="math-display">
$$
\vec v=\begin{bmatrix}6\\8\\-8\end{bmatrix},\qquad
\ell=\operatorname{span}\left(\begin{bmatrix}5\\-5\\7\end{bmatrix}\right),\qquad
P:\ 5x-5y+7z=0
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) Find the orthogonal projection of <span class="math-inline">\\(\vec v\\)</span> onto <span class="math-inline">\\(\ell\\)</span>.

<details markdown="1"><summary>Solution</summary>

Let <span class="math-inline">\\(\vec w=\begin{bmatrix}5\\\\-5\\\\7\end{bmatrix}\\)</span>. The projection onto its span is

<div class="math-display">
$$
\operatorname{proj}_{\ell}(\vec v)=\frac{\vec v\cdot\vec w}{\vec w\cdot\vec w}\vec w
$$
</div>

 Here,

<div class="math-display">
$$
\vec v\cdot\vec w=6(5)+8(-5)+(-8)(7)=-66,\qquad
\vec w\cdot\vec w=25+25+49=99
$$
</div>

 Therefore,

<div class="math-display">
$$
\operatorname{proj}_{\ell}(\vec v)
=-\frac23\begin{bmatrix}5\\-5\\7\end{bmatrix}
=\boxed{\begin{bmatrix}-10/3\\10/3\\-14/3\end{bmatrix}}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find the orthogonal projection of <span class="math-inline">\\(\vec v\\)</span> onto <span class="math-inline">\\(P\\)</span>.

<details markdown="1"><summary>Solution</summary>

The plane passes through the origin and has normal <span class="math-inline">\\(\vec w\\)</span>, so it is perpendicular to <span class="math-inline">\\(\ell\\)</span>. To project onto the plane, subtract the component along the normal.

<div class="math-display">
$$
\operatorname{proj}_{P}(\vec v)
=\vec v-\operatorname{proj}_{\ell}(\vec v)
=\begin{bmatrix}6\\8\\-8\end{bmatrix}
-\begin{bmatrix}-10/3\\10/3\\-14/3\end{bmatrix}
=\boxed{\begin{bmatrix}28/3\\14/3\\-10/3\end{bmatrix}}
$$
</div>

 This vector lies in <span class="math-inline">\\(P\\)</span>, since <span class="math-inline">\\(5(28/3)-5(14/3)+7(-10/3)=0\\)</span>, and the subtracted component is perpendicular to <span class="math-inline">\\(P\\)</span>.
</details>
</div>
</div>

</div>

{% endraw %}
