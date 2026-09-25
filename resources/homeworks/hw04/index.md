---
layout: page
title: "Homework 4: Lines and Planes in $\\mathbb{R}^3$"
description: "Homework 4: Lines and Planes in $\\mathbb{R}^3$ problems."
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

# Homework 4: Lines and Planes in $\mathbb{R}^3$

**due** Friday, October 2nd at 11:59PM

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw04/hw04.pdf" target="_blank">View as PDF ✏️</a>
</div>

{: .yellow }
<div markdown="1">
Write your solutions to the following problems either by writing them on a piece of paper or on a tablet and scanning your answers as a PDF. Note that you are not allowed to use LaTeX, Google Docs, or any other digital document creation software to type your answers. Homeworks are due to Pensive by 11:59PM on the due date. See the [syllabus](https://math124.org/syllabus/#homework) for details on the slip day policy.

Homework will be evaluated not only on the correctness of your answers, but on your ability to present your ideas clearly and logically. You should always explain and justify your conclusions, using sound reasoning. Your goal should be to convince the reader of your assertions. If a question does not require explanation, it will be explicitly stated.

Before proceeding, make sure you're familiar with the [collaboration policy](https://math124.org/syllabus/#collaboration-and-generative-ai-policy).
</div>

---

## Problems

- [Problem 1: Homework 3 Solutions Review](#problem-1-homework-3-solutions-review-6-pts)
- [Problem 2: A Line as an Intersection](#problem-2-a-line-as-an-intersection-12-pts)
- [Problem 3: Perfectly Normal](#problem-3-perfectly-normal-7-pts)
- [Problem 4: Common Ground](#problem-4-common-ground-12-pts)
- [Problem 5: Three Points, One Plane](#problem-5-three-points-one-plane-13-pts)
- [Problem 6: Three Points, Take Two](#problem-6-three-points-take-two-11-pts)
- [Problem 7: Changing the Spanning Vectors](#problem-7-changing-the-spanning-vectors-7-pts)
- [Problem 8: Breaking It Down](#problem-8-breaking-it-down-15-pts)
- [Problem 9: A Change of Reflection](#problem-9-a-change-of-reflection-10-pts)
- [Problem 10: Programming Activity](#problem-10-programming-activity-7-pts)

---

Total Points: <span class="math-inline">\\(6 + 12 + 7 + 12 + 13 + 11 + 7 + 15 + 10 + 7 = 100\\)</span>

---

**Have the notes open while working on the homework!** [Chapter 2.4](https://notes.math124.org/ch02/02-04), [Chapter 2.5](https://notes.math124.org/ch02/02-05), [Chapter 2.6](https://notes.math124.org/ch02/02-06), and Chapter 2.7 (coming soon) are all very relevant. We've added the relevant lab and lecture worksheet content to them, so they are comprehensive.

---

## Problem 1: Homework 3 Solutions Review (6 pts)

Review [the solutions to Homework 3](https://math124.org/resources/homeworks/hw03/). Pick **two problem parts** (for example, Problem 3a and Problem 5b) from Homework 3 in which your solutions have the most room for improvement, i.e., where they have unsound reasoning, could be significantly more efficient or clearer, etc. **Include a screenshot of your solution to each problem part**, and in a few sentences, explain what was deficient and how it could be fixed.

Alternatively, if you think one of your solutions is significantly better than the posted one, copy it here and explain why you think it is better. If you didn't do Homework 3, choose two problem parts from it that look challenging to you, and in a few sentences, explain the key ideas behind their solutions in your own words.

---

## Problem 2: A Line as an Intersection (12 pts)

First, consider the line through the origin

<div class="math-display">
$$
\ell_0=\operatorname{span}\left(\begin{bmatrix}6\\-4\\9\end{bmatrix}\right).
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Write <span class="math-inline">\\(\ell&#95;0\\)</span> in parametric form. In other words, write three separate equations: <span class="math-inline">\\(x=\cdots\\)</span>, <span class="math-inline">\\(y=\cdots\\)</span>, and <span class="math-inline">\\(z=\cdots\\)</span>, each of which involves the same parameter, e.g., <span class="math-inline">\\(t\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Write a system of two linear equations in <span class="math-inline">\\(x\\)</span>, <span class="math-inline">\\(y\\)</span>, and <span class="math-inline">\\(z\\)</span> whose common solutions are exactly the points on <span class="math-inline">\\(\ell&#95;0\\)</span>. Your equations should not contain a parameter.

Then, verify that every point on <span class="math-inline">\\(\ell&#95;0\\)</span> satisfies your system by plugging in your parametric formulas from part (a).

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Now, consider the affine line

<div class="math-display">
$$
\ell=\begin{bmatrix}-5\\7\\4\end{bmatrix}+\operatorname{span}\left(\begin{bmatrix}6\\-4\\9\end{bmatrix}\right).
$$
</div>

 Write <span class="math-inline">\\(\ell\\)</span> in parametric form, then find a system of two linear equations whose common solutions are exactly the points on <span class="math-inline">\\(\ell\\)</span>. Verify your equations by substituting your parametric formulas. How do the equations change from part (b)?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Give a geometric interpretation of your systems in parts (b) and (c): in each case, what type of object does each equation describe in <span class="math-inline">\\(\mathbb{R}^3\\)</span>, and what is the connection between those two objects and the corresponding line (<span class="math-inline">\\(\ell&#95;0\\)</span> or <span class="math-inline">\\(\ell\\)</span>)?

</div>
</div>

</div>

---

## Problem 3: Perfectly Normal (7 pts)

The point <span class="math-inline">\\(A=(8,11,9)\\)</span> lies on the plane <span class="math-inline">\\(P\\)</span> with equation

<div class="math-display">
$$
4x-7y+5z=0.
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Find a nonzero vector normal to <span class="math-inline">\\(P\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find a parametric form for the line through <span class="math-inline">\\(A\\)</span> that is perpendicular to <span class="math-inline">\\(P\\)</span>. Explain why your line passes through <span class="math-inline">\\(A\\)</span> and is perpendicular to <span class="math-inline">\\(P\\)</span>.

</div>
</div>

</div>

---

## Problem 4: Common Ground (12 pts)

You might find [desmos.com/3d](https://desmos.com/3d) useful for visualizing the planes in this question.

Consider the vectors

<div class="math-display">
$$
\vec{v}_1=\begin{bmatrix}5\\4\\2\end{bmatrix},\qquad
\vec{v}_2=\begin{bmatrix}-4\\1\\11\end{bmatrix},\qquad
\vec{v}_3=\begin{bmatrix}4\\-7\\-5\end{bmatrix},\qquad
\vec{v}_4=\begin{bmatrix}8\\3\\7\end{bmatrix},
$$
</div>

 and the planes

<div class="math-display">
$$
P=\operatorname{span}(\vec{v}_1,\vec{v}_2),\qquad
Q=\operatorname{span}(\vec{v}_3,\vec{v}_4).
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find equations for <span class="math-inline">\\(P\\)</span> and <span class="math-inline">\\(Q\\)</span> in the form <span class="math-inline">\\(ax+by+cz=d\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) The planes <span class="math-inline">\\(P\\)</span> and <span class="math-inline">\\(Q\\)</span> intersect in a line <span class="math-inline">\\(\ell\\)</span>. Give a parametric description of <span class="math-inline">\\(\ell\\)</span>, and write it as the span of a single vector.

<em>Hint: Points on <span class="math-inline">\\(\ell\\)</span> satisfy both equations from part (a). Solve this system of two equations in three variables by eliminating variables.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Now, let <span class="math-inline">\\(R=\operatorname{span}(\vec{v}&#95;2,\vec{v}&#95;3)\\)</span>. Find an equation for <span class="math-inline">\\(R\\)</span>, and use it to find all points that belong to all three planes. What type of geometric object is their intersection?

</div>
</div>

</div>

---

## Problem 5: Three Points, One Plane (13 pts)

Let <span class="math-inline">\\(A=(4,-7,5)\\)</span>, <span class="math-inline">\\(B=(10,-3,7)\\)</span>, and <span class="math-inline">\\(C=(-2,-1,13)\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find vectors <span class="math-inline">\\(\vec{u}\\)</span> and <span class="math-inline">\\(\vec{v}\\)</span> pointing from <span class="math-inline">\\(A\\)</span> to <span class="math-inline">\\(B\\)</span> and from <span class="math-inline">\\(A\\)</span> to <span class="math-inline">\\(C\\)</span>, respectively. Then, explain how you know these three points do not lie on one line.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Find a nonzero normal vector to the plane through <span class="math-inline">\\(A\\)</span>, <span class="math-inline">\\(B\\)</span>, and <span class="math-inline">\\(C\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find an equation for this plane in the form <span class="math-inline">\\(ax+by+cz=d\\)</span>. Verify that all three points satisfy your equation.

</div>
</div>

</div>

---

## Problem 6: Three Points, Take Two (11 pts)

Let <span class="math-inline">\\(A=(-5,8,6)\\)</span>, <span class="math-inline">\\(B=(-1,15,1)\\)</span>, and <span class="math-inline">\\(C=(-13,-6,16)\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Is there a unique plane through <span class="math-inline">\\(A\\)</span>, <span class="math-inline">\\(B\\)</span>, and <span class="math-inline">\\(C\\)</span>? Justify your answer using vectors pointing from <span class="math-inline">\\(A\\)</span> to the other two points.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(7 pts) Find equations for two distinct planes that contain all three points. Verify that both planes contain all three points, and explain how you know the planes are different.

</div>
</div>

</div>

---

## Problem 7: Changing the Spanning Vectors (7 pts)

Let <span class="math-inline">\\(\vec{u}\\)</span> and <span class="math-inline">\\(\vec{v}\\)</span> be nonzero vectors in <span class="math-inline">\\(\mathbb{R}^3\\)</span> that are not scalar multiples of one another, and let

<div class="math-display">
$$
P=\operatorname{span}(\vec{u},\vec{v}).
$$
</div>

For each pair below, determine whether it also spans <span class="math-inline">\\(P\\)</span>.

-   If the pair does span <span class="math-inline">\\(P\\)</span>, show how to write an arbitrary vector <span class="math-inline">\\(a\vec{u}+b\vec{v}\\)</span> as a linear combination of the new pair.

-   If the pair does not span <span class="math-inline">\\(P\\)</span>, describe its span and give a vector that is in <span class="math-inline">\\(P\\)</span> but not in the span of the new pair.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts)
<span class="math-inline">\\(\vec{u}\\)</span> and <span class="math-inline">\\(\vec{u}+\vec{v}\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts)
<span class="math-inline">\\(\vec{u}+\vec{v}\\)</span> and <span class="math-inline">\\(2(\vec{u}+\vec{v})\\)</span>.

</div>
</div>

</div>

---

## Problem 8: Breaking It Down (15 pts)

**Note:** This problem involves content from Tuesday, September 29th's lecture, and the soon-to-be-released Chapter 2.7.

Let <span class="math-inline">\\(\vec{v}=\begin{bmatrix}19\\\\2\\\\9\end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Find the orthogonal projection of <span class="math-inline">\\(\vec{v}\\)</span> onto the line

<div class="math-display">
$$
\ell=\operatorname{span}\left(\begin{bmatrix}2\\3\\6\end{bmatrix}\right).
$$
</div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find the orthogonal projection of <span class="math-inline">\\(\vec{v}\\)</span> onto the plane <span class="math-inline">\\(P\\)</span> with equation <span class="math-inline">\\(2x+3y+6z=0\\)</span>.

<em>Hint: The line in part (a) is perpendicular to <span class="math-inline">\\(P\\)</span>. What happens if you subtract the projection onto that line from <span class="math-inline">\\(\vec{v}\\)</span>?</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find the orthogonal projection of <span class="math-inline">\\(\vec{v}\\)</span> onto the plane

<div class="math-display">
$$
Q=\operatorname{span}\left(\begin{bmatrix}5\\4\\-3\end{bmatrix},\begin{bmatrix}-2\\6\\5\end{bmatrix}\right).
$$
</div>

 <em>Hint: First find a nonzero vector normal to <span class="math-inline">\\(Q\\)</span>.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) The vectors

<div class="math-display">
$$
\vec{u}_1=\frac{1}{7}\begin{bmatrix}2\\3\\6\end{bmatrix},\qquad
\vec{u}_2=\frac{1}{7}\begin{bmatrix}-3\\6\\-2\end{bmatrix},\qquad
\vec{u}_3=\frac{1}{7}\begin{bmatrix}-6\\-2\\3\end{bmatrix}
$$
</div>

 form an orthonormal basis of <span class="math-inline">\\(\mathbb{R}^3\\)</span>. Write <span class="math-inline">\\(\vec{v}\\)</span> as a linear combination of <span class="math-inline">\\(\vec{u}&#95;1\\)</span>, <span class="math-inline">\\(\vec{u}&#95;2\\)</span>, and <span class="math-inline">\\(\vec{u}&#95;3\\)</span>.

</div>
</div>

</div>

---

## Problem 9: A Change of Reflection (10 pts)

In this problem, we will explore the idea of **reflecting** a vector across a line. This problem has applications to computer graphics, where reflecting the position vectors of points creates a mirror image of a two-dimensional shape.

Let <span class="math-inline">\\(\vec w=\begin{bmatrix}1\\\\1\end{bmatrix}\\)</span>. The picture below shows reflection of the vector <span class="math-inline">\\(\vec v=\begin{bmatrix}7\\\\-3\end{bmatrix}\\)</span> across the line <span class="math-inline">\\(\ell=\operatorname{span}(\vec w)=\operatorname{span}\left(\begin{bmatrix}1\\\\1\end{bmatrix}\right)\\)</span>.

<div style="text-align: center;">
<img src="imgs/reflection-example.png" alt="image" style="height: 4.5in; width: auto; max-width: 100%;">
</div>

In the picture above, reflecting <span class="math-inline">\\(\vec{v}=\begin{bmatrix}7\\\\-3\end{bmatrix}\\)</span> across <span class="math-inline">\\(\ell=\operatorname{span}(\vec w)\\)</span> gives us <span class="math-inline">\\(\vec{v}&#95;{\mathrm{ref}}=\begin{bmatrix}-3\\\\7\end{bmatrix}\\)</span>. Notice that <span class="math-inline">\\(\vec{p}=\begin{bmatrix}2\\\\2\end{bmatrix}\\)</span>, the projection of <span class="math-inline">\\(\vec{v}\\)</span> onto <span class="math-inline">\\(\ell=\operatorname{span}(\vec w)\\)</span>, has its tip halfway between the tips of <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec v&#95;{\mathrm{ref}}\\)</span>. To get from <span class="math-inline">\\(\vec{v}\\)</span> to <span class="math-inline">\\(\vec{v}&#95;{\mathrm{ref}}\\)</span>, we move to <span class="math-inline">\\(\vec{p}\\)</span>, then keep going the same distance in the same direction.

We'll use this same idea to reflect vectors across lines in <span class="math-inline">\\(\mathbb{R}^2\\)</span>, <span class="math-inline">\\(\mathbb{R}^3\\)</span>, and eventually <span class="math-inline">\\(\mathbb{R}^n\\)</span>. All of the lines in this problem pass through the origin.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Let <span class="math-inline">\\(\vec v=\begin{bmatrix}4\\\\3\end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec w=\begin{bmatrix}1\\\\2\end{bmatrix}\\)</span>.

<ol class="assignment-enumeration" markdown="1">

<li markdown="1">
<div class="assignment-enumeration-label">(i)</div>
<div class="assignment-enumeration-content" markdown="1">

Find the projection <span class="math-inline">\\(\vec p\\)</span> of <span class="math-inline">\\(\vec v\\)</span> onto <span class="math-inline">\\(\ell=\operatorname{span}(\vec w)\\)</span>.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">(ii)</div>
<div class="assignment-enumeration-content" markdown="1">

Now, find <span class="math-inline">\\(\vec v&#95;{\mathrm{ref}}\\)</span>, the reflection of <span class="math-inline">\\(\vec v\\)</span> across <span class="math-inline">\\(\ell=\operatorname{span}(\vec w)\\)</span>.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">(iii)</div>
<div class="assignment-enumeration-content" markdown="1">

Draw a picture showing <span class="math-inline">\\(\vec w\\)</span>, <span class="math-inline">\\(\ell=\operatorname{span}(\vec w)\\)</span> (dotted, as in our example), <span class="math-inline">\\(\vec p\\)</span>, <span class="math-inline">\\(\vec v\\)</span>, and <span class="math-inline">\\(\vec v&#95;{\mathrm{ref}}\\)</span>.

</div></li>
</ol>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Now, let <span class="math-inline">\\(\vec w=\begin{bmatrix}1\\\\1\\\\2\end{bmatrix}\\)</span> and find the reflection of <span class="math-inline">\\(\vec{v}=\begin{bmatrix}3\\\\-1\\\\2\end{bmatrix}\\)</span> across the line <span class="math-inline">\\(\ell=\operatorname{span}(\vec w)\\)</span> in <span class="math-inline">\\(\mathbb{R}^3\\)</span>. Again, start by finding <span class="math-inline">\\(\vec{p}\\)</span>. You don't need to draw a picture.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Let <span class="math-inline">\\(\vec{v}\in\mathbb{R}^n\\)</span>, and let <span class="math-inline">\\(\ell=\operatorname{span}(\vec{w})\\)</span>, where <span class="math-inline">\\(\vec{w}\\)</span> is nonzero. Find a formula for the reflection <span class="math-inline">\\(\vec{v}&#95;{\mathrm{ref}}\\)</span> of <span class="math-inline">\\(\vec{v}\\)</span> across <span class="math-inline">\\(\ell=\operatorname{span}(\vec w)\\)</span>. First, write your formula in terms of <span class="math-inline">\\(\vec{v}\\)</span> and its projection <span class="math-inline">\\(\vec{p}\\)</span> onto <span class="math-inline">\\(\ell=\operatorname{span}(\vec w)\\)</span>. Then, write it using only <span class="math-inline">\\(\vec{w}\\)</span>, <span class="math-inline">\\(\vec{v}\\)</span>, and their dot products.

</div>
</div>

</div>

---

## Problem 10: Programming Activity (7 pts)

Let's implement your logic from Problem 9 in Python! In Homework 1, you changed the **colors** of pixels in an image. This time, you'll change their **positions** to create a mirror image, while keeping the colors the same.

To open the notebook for Homework 4, click [**this link**](https://colab.research.google.com/github/math-124/fa26-code/blob/main/homeworks/hw04/hw04.ipynb). Instructions on how to use Google Colab are at [math124.org/running-code](https://math124.org/running-code).

You won't need to submit the notebook anywhere. To get credit, complete both tasks in the notebook and include the following in your PDF submission to Homework 4 on Pensive, specifically under **Problem 10**:

<ol class="assignment-enumeration" markdown="1">

<li markdown="1">
<div class="assignment-enumeration-label">1.</div>
<div class="assignment-enumeration-content" markdown="1">

**Task 1 (5 pts):** A screenshot of your completed `reflection(v, w)` function and the successful check output.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">2.</div>
<div class="assignment-enumeration-content" markdown="1">

**Task 2 (2 pts):** One screenshot of your canvas with a tilted line, showing the angle, original image, and reflected image. No written response is required.

</div></li>
</ol>

{% endraw %}
