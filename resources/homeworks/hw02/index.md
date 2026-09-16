---
layout: page
title: "Homework 2: Vector Arithmetic, Lengths, and the Dot Product"
description: "Homework 2: Vector Arithmetic, Lengths, and the Dot Product problems."
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

# Homework 2: Vector Arithmetic, Lengths, and the Dot Product

**due** Monday, September 14th at 11:59PM

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw02/hw02.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw02/hw02-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
Write your solutions to the following problems either by writing them on a piece of paper or on a tablet and scanning your answers as a PDF. Note that you are not allowed to use LaTeX, Google Docs, or any other digital document creation software to type your answers. Homeworks are due to Pensive by 11:59PM on the due date. See the [syllabus](https://math124.org/syllabus/#homework) for details on the slip day policy.

Homework will be evaluated not only on the correctness of your answers, but on your ability to present your ideas clearly and logically. You should always explain and justify your conclusions, using sound reasoning. Your goal should be to convince the reader of your assertions. If a question does not require explanation, it will be explicitly stated.

Before proceeding, make sure you're familiar with the [collaboration policy](https://math124.org/syllabus/#collaboration-and-generative-ai-policy).
</div>

---

## Problems

- [Problem 1: Homework 1 Solutions Review](#problem-1-homework-1-solutions-review-8-pts)
- [Problem 2: Setting Ourselves Up](#problem-2-setting-ourselves-up-10-pts)
- [Problem 3: Add All Ingredients to the Bowl and Combine](#problem-3-add-all-ingredients-to-the-bowl-and-combine-8-pts)
- [Problem 4: *Norm*alize Doing Math 124!](#problem-4-normalize-doing-math-124-6-pts)
- [Problem 5: Displacement and Distance](#problem-5-displacement-and-distance-10-pts)
- [Problem 6: Dot Products, Angles, and Orthogonality](#problem-6-dot-products-angles-and-orthogonality-20-pts)
- [Problem 7: Distributing the Dots](#problem-7-distributing-the-dots-17-pts)
- [Problem 8: Triangle Inequality](#problem-8-triangle-inequality-6-pts)
- [Problem 9: Programming Activity](#problem-9-programming-activity-15-pts)

---

Total Points: 8 + 10 + 8 + 6 + 10 + 20 + 17 + 6 + 15 = 100

---

Note: While working on the homework, have Chapters [1.4](https://notes.math124.org/ch01/01-04/), [1.5](https://notes.math124.org/ch01/01-05/), and [1.6](https://notes.math124.org/ch01/01-06/) of the course notes open! They contain lots of relevant examples and explanations.

---

## Problem 1: Homework 1 Solutions Review (8 pts)

Review [the solutions to Homework 1](https://math124.org/resources/homeworks/hw01/). Pick **two problem parts** (for example, Problem 3a and Problem 5b) from Homework 1 in which your solutions have the most room for improvement, i.e., where they have unsound reasoning, could be significantly more efficient or clearer, etc. **Include a screenshot of your solution to each problem part**, and in a few sentences, explain what was deficient and how it could be fixed.

Alternatively, if you think one of your solutions is significantly better than the posted one, copy it here and explain why you think it is better. If you didn't do Homework 1, choose two problem parts from it that look challenging to you, and in a few sentences, explain the key ideas behind their solutions in your own words.

<details markdown="1"><summary>Solution</summary>

Responses will vary. Look for specific comparisons with the posted solutions and clear explanations of how to improve the selected work.
</details>

---

## Problem 2: Setting Ourselves Up (10 pts)

Given the following sets, translate the set notation into plain English and sketch a picture of what each set looks like in <span class="math-inline">\\(\mathbb{R}^2\\)</span> or <span class="math-inline">\\(\mathbb{R}^3\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(3 pts)
<span class="math-inline">\\(\lbrace{}\begin{bmatrix} x\\\\y \end{bmatrix} \in \mathbb{R}^2 : x &gt; 0, y &lt; 0\rbrace{}\\)</span>

<details markdown="1"><summary>Solution</summary>

This is the set of all vectors in <span class="math-inline">\\(\mathbb{R}^2\\)</span> with a positive first coordinate and negative second coordinate. Shade the fourth quadrant, excluding both axes; draw the boundary rays dashed.

<div style="text-align: center;">
<img src="imgs/hw02-plot-01.png" alt="Coordinate diagram" class="assignment-vector-plot">
</div>
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts)
<span class="math-inline">\\(\lbrace{}\begin{bmatrix} x\\\\y \end{bmatrix} \in \mathbb{R}^2 : x &lt; 0, y \geq 3\rbrace{}\\)</span>

<details markdown="1"><summary>Solution</summary>

This is the set of vectors in <span class="math-inline">\\(\mathbb{R}^2\\)</span> with a negative first coordinate and a second coordinate at least <span class="math-inline">\\(3\\)</span>. Shade the region to the left of the <span class="math-inline">\\(y\\)</span>-axis and on or above the line <span class="math-inline">\\(y=3\\)</span>. Include the boundary <span class="math-inline">\\(y=3\\)</span> for <span class="math-inline">\\(x&lt;0\\)</span> and exclude the boundary <span class="math-inline">\\(x=0\\)</span>, including <span class="math-inline">\\((0,3)\\)</span>; draw the horizontal boundary solid and the vertical boundary dashed.

<div style="text-align: center;">
<img src="imgs/hw02-plot-02.png" alt="Coordinate diagram" class="assignment-vector-plot">
</div>
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts)
<span class="math-inline">\\(\lbrace{}\begin{bmatrix} x\\\\y\\\\z \end{bmatrix} \in \mathbb{R}^3 : x, z \in \mathbb{R}, y = -5\rbrace{}\\)</span>

<details markdown="1"><summary>Solution</summary>

This is the plane <span class="math-inline">\\(y=-5\\)</span> in <span class="math-inline">\\(\mathbb{R}^3\\)</span>: the first and third coordinates can be any real numbers, and the second coordinate is always <span class="math-inline">\\(-5\\)</span>. Sketch a plane parallel to the <span class="math-inline">\\(xz\\)</span>-plane passing through the point <span class="math-inline">\\((0,-5,0)\\)</span>.

<div style="text-align: center;">
<img src="imgs/hw02-plot-03.png" alt="Coordinate diagram" class="assignment-vector-plot">
</div>
</details>

</div>
</div>

</div>

---

## Problem 3: Add All Ingredients to the Bowl and Combine (8 pts)

A cake recipe uses three ingredients: sugar, flour, and milk. We represent the ingredients in one batch by a vector in <span class="math-inline">\\(\mathbb{R}^3\\)</span>, using the order

<div class="math-display">
$$
\begin{bmatrix}
\text{sugar in tbsp}\\
\text{flour in cups}\\
\text{milk in tbsp}
\end{bmatrix}.
$$
</div>

 Consider the following four recipe batches:

-   Recipe 1 uses <span class="math-inline">\\(2\\)</span> tbsp of sugar, <span class="math-inline">\\(1\\)</span> cup of flour, and <span class="math-inline">\\(3\\)</span> tbsp of milk.

-   Recipe 2 uses <span class="math-inline">\\(3\\)</span> tbsp of sugar, <span class="math-inline">\\(2\\)</span> cups of flour, and <span class="math-inline">\\(4\\)</span> tbsp of milk.

-   Recipe 3 uses <span class="math-inline">\\(4\\)</span> tbsp of sugar, <span class="math-inline">\\(2\\)</span> cups of flour, and <span class="math-inline">\\(6\\)</span> tbsp of milk.

-   Recipe 4 uses <span class="math-inline">\\(1\\)</span> tbsp of sugar, <span class="math-inline">\\(1\\)</span> cup of flour, and <span class="math-inline">\\(2\\)</span> tbsp of milk.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Write vectors <span class="math-inline">\\(\vec{v}&#95;1,\vec{v}&#95;2,\vec{v}&#95;3,\vec{v}&#95;4\\)</span> representing the four recipes. Identify a relationship between two of the vectors and explain what that relationship means in the context of the recipes.

<details markdown="1"><summary>Solution</summary>

The recipe vectors are

<div class="math-display">
$$
\vec{v}_1=\begin{bmatrix}2\\1\\3\end{bmatrix},\quad
\vec{v}_2=\begin{bmatrix}3\\2\\4\end{bmatrix},\quad
\vec{v}_3=\begin{bmatrix}4\\2\\6\end{bmatrix},\quad
\vec{v}_4=\begin{bmatrix}1\\1\\2\end{bmatrix}.
$$
</div>

 Since <span class="math-inline">\\(\vec{v}&#95;3=2\vec{v}&#95;1\\)</span>, Recipe 3 is a double batch of Recipe 1, with the same ingredient proportions.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Suppose you make two batches of Recipe 1, no batches of Recipe 2, three batches of Recipe 3, and two batches of Recipe 4. Write a linear combination representing the total ingredients used. Then determine the total amount of sugar, flour, and milk used.

<details markdown="1"><summary>Solution</summary>

The appropriate linear combination is

<div class="math-display">
$$
2\vec{v}_1+0\vec{v}_2+3\vec{v}_3+2\vec{v}_4
=2\begin{bmatrix}2\\1\\3\end{bmatrix}
+3\begin{bmatrix}4\\2\\6\end{bmatrix}
+2\begin{bmatrix}1\\1\\2\end{bmatrix}
=\begin{bmatrix}18\\10\\28\end{bmatrix}.
$$
</div>

 Thus, the total is <span class="math-inline">\\(18\\)</span> tbsp of sugar, <span class="math-inline">\\(10\\)</span> cups of flour, and <span class="math-inline">\\(28\\)</span> tbsp of milk.
</details>

</div>
</div>

</div>

---

## Problem 4: *Norm*alize Doing Math 124! (6 pts)

The length, or norm, of a vector is denoted by <span class="math-inline">\\(\lVert \vec{v} \rVert\\)</span>. Consider the vector

<div class="math-display">
$$
\vec{v}=\begin{bmatrix}-5\\12\end{bmatrix}\in\mathbb{R}^2.
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Sketch <span class="math-inline">\\(\vec{v}\\)</span> in the coordinate plane.

<details markdown="1"><summary>Solution</summary>

Draw an arrow from <span class="math-inline">\\((0,0)\\)</span> to <span class="math-inline">\\((-5,12)\\)</span>, with the axes and endpoint labeled.

<div style="text-align: center;">
<img src="imgs/hw02-plot-04.png" alt="Coordinate diagram" class="assignment-vector-plot">
</div>
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Compute <span class="math-inline">\\(\lVert \vec{v} \rVert\\)</span>.

<details markdown="1"><summary>Solution</summary>

By the Pythagorean theorem,

<div class="math-display">
$$
\lVert \vec{v} \rVert=\sqrt{(-5)^2+12^2}=\sqrt{169}=13.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Find a unit vector (i.e. a vector of length one) pointing in the same direction as <span class="math-inline">\\(\vec{v}\\)</span>.

<details markdown="1"><summary>Solution</summary>

Dividing by the length gives

<div class="math-display">
$$
\frac{\vec{v}}{\lVert \vec{v} \rVert}=\frac1{13}\begin{bmatrix}-5\\12\end{bmatrix}
=\begin{bmatrix}-\frac5{13}\\[2pt]\frac{12}{13}\end{bmatrix}.
$$
</div>

 Its length is <span class="math-inline">\\(1\\)</span>, and the positive scale factor preserves direction.
</details>

</div>
</div>

</div>

---

## Problem 5: Displacement and Distance (10 pts)

A drone begins at the point

<div class="math-display">
$$
P=(2,-1,4)
$$
</div>

 and flies in a straight line to the point

<div class="math-display">
$$
Q=(6,7,-4).
$$
</div>

 The coordinates here are in meters.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Let <span class="math-inline">\\(\vec{d}\\)</span> be the vector that describes the displacement from <span class="math-inline">\\(P\\)</span> to <span class="math-inline">\\(Q\\)</span>. Find <span class="math-inline">\\(\vec{d}\\)</span>.

<details markdown="1"><summary>Solution</summary>

Let <span class="math-inline">\\(\vec p, \vec q\\)</span> be the position vectors of <span class="math-inline">\\(P\\)</span>, <span class="math-inline">\\(Q\\)</span> respectively. We obtain <span class="math-inline">\\(\vec d\\)</span> by subtracting the two vectors:

<div class="math-display">
$$
\vec{d}=\vec q - \vec p = \begin{bmatrix}6-2\\7-(-1)\\-4-4\end{bmatrix}
=\begin{bmatrix}4\\8\\-8\end{bmatrix}.
$$
</div>

<div style="text-align: center;">
<img src="imgs/hw02-plot-05.png" alt="Coordinate diagram" class="assignment-vector-plot">
</div>
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Find the exact distance traveled by the drone.

<details markdown="1"><summary>Solution</summary>

The distance is the length of the displacement:

<div class="math-display">
$$
\lVert \vec{d} \rVert=\sqrt{4^2+8^2+(-8)^2}=\sqrt{144}=12\text{ meters}.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) Suppose the drone continues to travel another 10 meters in the same direction. What are its coordinates?

<details markdown="1"><summary>Solution</summary>

We divide the displacement by its length <span class="math-inline">\\(12\\)</span> to obtain the unit vector in the direction of <span class="math-inline">\\(\vec d\\)</span>. Scale this unit vector by <span class="math-inline">\\(10\\)</span> and add the additional displacement to <span class="math-inline">\\(Q\\)</span>, where the drone starts this part of its flight:

<div class="math-display">
$$
\vec q + \frac{10}{12}\vec{d} = \begin{bmatrix}6\\7\\-4\end{bmatrix}
+\frac{10}{12}\begin{bmatrix}4\\8\\-8\end{bmatrix}
=\begin{bmatrix}\frac{28}{3}\\[2pt]\frac{41}{3}\\[2pt]-\frac{32}{3}\end{bmatrix}.
$$
</div>

 The new coordinates are <span class="math-inline">\\(\left(\frac{28}{3},\frac{41}{3},-\frac{32}{3}\right)\\)</span>. In the figure below, the drone's new position is <span class="math-inline">\\(R\\)</span>.

<div style="text-align: center;">
<img src="imgs/hw02-plot-06.png" alt="Coordinate diagram" class="assignment-vector-plot">
</div>
</details>

</div>
</div>

</div>

---

## Problem 6: Dot Products, Angles, and Orthogonality (20 pts)

As discussed in [Chapter 1.6](https://notes.math124.org/ch01/01-06/), for nonzero vectors <span class="math-inline">\\(\vec{u},\vec{v}\in\mathbb{R}^n\\)</span>, the angle <span class="math-inline">\\(\theta\\)</span> between them satisfies

<div class="math-display">
$$
\cos\theta=\frac{\vec{u}\cdot\vec{v}}{\lVert \vec{u} \rVert\lVert \vec{v} \rVert}.
$$
</div>

 This ratio is called their **cosine similarity**: the dot product divided by the product of their lengths. To find the angle itself, take the inverse cosine of this ratio.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(9 pts) For each pair below, draw the vectors, compute their dot product, and find their cosine similarity (i.e. the cosine of the angle between them). In which case are the vectors orthogonal?

<ol class="assignment-enumeration" markdown="1">

<li markdown="1">
<div class="assignment-enumeration-label">(i)</div>
<div class="assignment-enumeration-content" markdown="1">

(3 pts) <span class="math-inline">\\(\vec{u}=\begin{bmatrix}-6\\\\3\end{bmatrix},\quad \vec{v}=\begin{bmatrix}1\\\\2\end{bmatrix}\\)</span>.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">(ii)</div>
<div class="assignment-enumeration-content" markdown="1">

(3 pts) <span class="math-inline">\\(\vec{u}=\begin{bmatrix}4\\\\1\end{bmatrix},\quad \vec{v}=\begin{bmatrix}4\\\\-1\end{bmatrix}\\)</span>.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">(iii)</div>
<div class="assignment-enumeration-content" markdown="1">

(3 pts) <span class="math-inline">\\(\vec{u}=\begin{bmatrix}3\\\\3\end{bmatrix},\quad \vec{v}=\begin{bmatrix}2\\\\2\end{bmatrix}\\)</span>.

</div></li>
</ol>

<details markdown="1"><summary>Solution</summary>

Draw each vector as an arrow from the origin to its coordinates.

<div style="text-align: center;">
<img src="imgs/hw02-plot-07.png" alt="Coordinate diagram" class="assignment-vector-plot">
</div>

The dot products are <span class="math-inline">\\(0\\)</span>, <span class="math-inline">\\(15\\)</span>, and <span class="math-inline">\\(12\\)</span>, respectively. The corresponding cosine similarities are <span class="math-inline">\\(0\\)</span>, <span class="math-inline">\\(15/17\\)</span>, and <span class="math-inline">\\(1\\)</span>. Only the first pair is orthogonal.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) For each pair below, find all values of <span class="math-inline">\\(k\\)</span> that make <span class="math-inline">\\(\vec{u}\\)</span> and <span class="math-inline">\\(\vec{v}\\)</span> orthogonal.

<ol class="assignment-enumeration" markdown="1">

<li markdown="1">
<div class="assignment-enumeration-label">(i)</div>
<div class="assignment-enumeration-content" markdown="1">

(3 pts) <span class="math-inline">\\(\vec{u}=\begin{bmatrix}k\\\\3\\\\-\frac12\end{bmatrix},\quad \vec{v}=\begin{bmatrix}-5\\\\-k\\\\\frac12\end{bmatrix}\\)</span>.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">(ii)</div>
<div class="assignment-enumeration-content" markdown="1">

(3 pts) <span class="math-inline">\\(\vec{u}=\begin{bmatrix}2k\\\\-4\\\\1\end{bmatrix},\quad \vec{v}=\begin{bmatrix}2k\\\\-2k\\\\0\end{bmatrix}\\)</span>.

</div></li>
</ol>

<details markdown="1"><summary>Solution</summary>

In (i), orthogonality requires

<div class="math-display">
$$
\vec u\cdot \vec v = -5k-3k-\frac14=0,
$$
</div>

 giving <span class="math-inline">\\(k=-\frac1{32}\\)</span>. In (ii), it requires

<div class="math-display">
$$
\vec u\cdot \vec v = 4k^2+8k=4k(k+2)=0,
$$
</div>

 giving <span class="math-inline">\\(k=0\\)</span> or <span class="math-inline">\\(k=-2\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Use the cosine formula to explain why, for nonzero vectors <span class="math-inline">\\(\vec{u},\vec{v}\in\mathbb{R}^n\\)</span>,

<div class="math-display">
$$
|\vec{u}\cdot\vec{v}|\leq\lVert \vec{u} \rVert\lVert \vec{v} \rVert.
$$
</div>

 Explain why equality holds exactly when the vectors point in the same or opposite directions. Finally, explain why the inequality also holds if either vector is zero. This inequality is called the Cauchy--Schwarz inequality.

<details markdown="1"><summary>Solution</summary>

Let <span class="math-inline">\\(\theta\\)</span> denote the angle between the vectors <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>. Then since <span class="math-inline">\\(|\cos\theta|\leq1\\)</span>,

<div class="math-display">
$$
|\vec{u}\cdot\vec{v}|=\lVert \vec{u} \rVert\lVert \vec{v} \rVert\,|\cos\theta|
\leq\lVert \vec{u} \rVert\lVert \vec{v} \rVert.
$$
</div>

 For nonzero vectors, equality holds exactly when <span class="math-inline">\\(|\cos\theta|=1\\)</span>, so <span class="math-inline">\\(\theta=0^\circ\\)</span> or <span class="math-inline">\\(180^\circ\\)</span>: the vectors point in the same or opposite directions. If either vector is zero, both sides of the inequality are zero.
</details>

</div>
</div>

</div>

---

## Problem 7: Distributing the Dots (17 pts)

Let <span class="math-inline">\\(\vec{u},\vec{v}\in\mathbb{R}^n\\)</span> satisfy

<div class="math-display">
$$
\lVert \vec{u} \rVert=3,\qquad \lVert \vec{v} \rVert=2,\qquad
(3\vec{u}-4\vec{v})\cdot(\vec{u}+9\vec{v})=-71.
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find <span class="math-inline">\\(\vec{u}\cdot\vec{v}\\)</span>.

<details markdown="1"><summary>Solution</summary>

Distributing the dot product gives

<div class="math-display">
$$
\begin{aligned}
-71 = (3\vec{u}-4\vec{v})\cdot(\vec{u}+9\vec{v})
&=3\lVert \vec{u} \rVert^2+27\vec{u}\cdot\vec{v}
-4\vec{v}\cdot\vec{u}-36\lVert \vec{v} \rVert^2\\
&=27+23\vec{u}\cdot\vec{v}-144.
\end{aligned}
$$
</div>

 Thus <span class="math-inline">\\(23\vec{u}\cdot\vec{v}=46\\)</span> and <span class="math-inline">\\(\boxed{\vec{u}\cdot\vec{v}=2}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Find <span class="math-inline">\\(\lVert -2\vec{u} \rVert\\)</span> and <span class="math-inline">\\(\lVert 3\vec{v} \rVert\\)</span>. Explain why neither length is negative.

<details markdown="1"><summary>Solution</summary>

The scaling property gives

<div class="math-display">
$$
\lVert -2\vec{u} \rVert=|-2|\lVert \vec{u} \rVert=2(3)=6,
\qquad
\lVert 3\vec{v} \rVert=|3|\lVert \vec{v} \rVert=3(2)=6.
$$
</div>

 Lengths are nonnegative. A negative scalar reverses direction, but scales length by its absolute value.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find the cosine similarity of <span class="math-inline">\\(\vec{u}\\)</span> and <span class="math-inline">\\(\vec{v}\\)</span>. Then find the cosine similarity of <span class="math-inline">\\(-2\vec{u}\\)</span> and <span class="math-inline">\\(3\vec{v}\\)</span>. If the two cosine similarities are different, why are they different?

<details markdown="1"><summary>Solution</summary>

The original cosine similarity is

<div class="math-display">
$$
\frac{\vec{u}\cdot\vec{v}}{\lVert \vec{u} \rVert\lVert \vec{v} \rVert}
=\frac{2}{3(2)}=\frac13.
$$
</div>

 For the scaled vectors, it is

<div class="math-display">
$$
\frac{(-2\vec{u})\cdot(3\vec{v})}{\lVert -2\vec{u} \rVert\lVert 3\vec{v} \rVert}
=\frac{-6(\vec{u}\cdot\vec{v})}{6(6)}
=\frac{-12}{36}=-\frac13.
$$
</div>

 The cosine similarities differ because multiplying <span class="math-inline">\\(\vec{u}\\)</span> by <span class="math-inline">\\(-2\\)</span> reverses its direction, while multiplying <span class="math-inline">\\(\vec{v}\\)</span> by <span class="math-inline">\\(3\\)</span> preserves its direction. Reversing exactly one vector changes the sign of the cosine similarity; the positive scaling factors cancel between the numerator and denominator.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Find <span class="math-inline">\\(\vec{u}\cdot\vec{u}\\)</span> and <span class="math-inline">\\(\vec{v}\cdot\vec{v}\\)</span>.

<details markdown="1"><summary>Solution</summary>

A vector's dot product with itself is its squared length, so

<div class="math-display">
$$
\vec{u}\cdot\vec{u}=\lVert \vec{u} \rVert^2=3^2=9,
\qquad
\vec{v}\cdot\vec{v}=\lVert \vec{v} \rVert^2=2^2=4.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Find <span class="math-inline">\\(\lVert \vec{u}+\vec{v} \rVert\\)</span>. Is it equal to <span class="math-inline">\\(\sqrt{\lVert \vec{u} \rVert^2+\lVert \vec{v} \rVert^2}\\)</span>? Explain what condition would make these quantities equal.

<em>Hint: Start by writing <span class="math-inline">\\(\lVert\vec{u}+\vec{v}\rVert^2\\)</span> as <span class="math-inline">\\((\vec{u}+\vec{v})\cdot(\vec{u}+\vec{v})\\)</span>. Then, expand this as we did in <a href="https://notes.math124.org/ch01/01-06/#orthogonality-and-the-pythagorean-theorem">Chapter 1.6</a>.</em>

<details markdown="1"><summary>Solution</summary>

Expanding gives

<div class="math-display">
$$
\lVert \vec{u}+\vec{v} \rVert^2
=\lVert \vec{u} \rVert^2+2\vec{u}\cdot\vec{v}+\lVert \vec{v} \rVert^2
=9+4+4=17.
$$
</div>

 Thus <span class="math-inline">\\(\lVert \vec{u}+\vec{v} \rVert=\sqrt{17}\\)</span>, whereas <span class="math-inline">\\(\sqrt{\lVert \vec{u} \rVert^2+\lVert \vec{v} \rVert^2}=\sqrt{13}\\)</span>. The quantities are equal exactly when <span class="math-inline">\\(\vec{u}\cdot\vec{v}=0\\)</span>, meaning the vectors are orthogonal.
</details>

</div>
</div>

</div>

---

## Problem 8: Triangle Inequality (6 pts)

In [Chapter 1.5](https://notes.math124.org/ch01/01-05/#the-triangle-inequality), we stated the triangle inequality without proof. Intuitively, the triangle inequality says that for any triangle (even in <span class="math-inline">\\(\mathbb{R}^n\\)</span>), the length of any side of the triangle is less than or equal to the sum of the lengths of the other two sides. Here, we'll prove the triangle inequality using the Cauchy--Schwarz inequality, established in Problem 6c.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Let <span class="math-inline">\\(\vec{u},\vec{v}\\)</span> be any two vectors in <span class="math-inline">\\(\mathbb{R}^n\\)</span>. Show that

<div class="math-display">
$$
\lVert\vec{u}+\vec{v}\rVert^2\leq(\lVert\vec{u}\rVert+\lVert\vec{v}\rVert)^2.
$$
</div>

 <em>Hint: Start by following the same hint as in Problem 7e, then use the Cauchy--Schwarz inequality.</em>

<details markdown="1"><summary>Solution</summary>

Using distributivity, symmetry, and Cauchy--Schwarz,

<div class="math-display">
$$
\begin{aligned}
\lVert \vec{u}+\vec{v} \rVert^2
&=\lVert \vec{u} \rVert^2+2\vec{u}\cdot\vec{v}+\lVert \vec{v} \rVert^2\\
&\leq\lVert \vec{u} \rVert^2+2|\vec{u}\cdot\vec{v}|+\lVert \vec{v} \rVert^2\\
&\leq\lVert \vec{u} \rVert^2+2\lVert \vec{u} \rVert\lVert \vec{v} \rVert+\lVert \vec{v} \rVert^2\\
&=(\lVert \vec{u} \rVert+\lVert \vec{v} \rVert)^2.
\end{aligned}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Why does the above imply that

<div class="math-display">
$$
\lVert\vec{u}+\vec{v}\rVert\leq\lVert\vec{u}\rVert+\lVert\vec{v}\rVert
$$
</div>

<details markdown="1"><summary>Solution</summary>

Both <span class="math-inline">\\(\lVert \vec{u}+\vec{v} \rVert\\)</span> and <span class="math-inline">\\(\lVert \vec{u} \rVert+\lVert \vec{v} \rVert\\)</span> are nonnegative. Taking square roots preserves the inequality from part (a), giving <span class="math-inline">\\(\lVert \vec{u}+\vec{v} \rVert\leq\lVert \vec{u} \rVert+\lVert \vec{v} \rVert\\)</span>.
</details>

</div>
</div>

</div>

---

## Problem 9: Programming Activity (15 pts)

Most homeworks and some labs will have a Jupyter Notebook, containing Python code that supplements our understanding of the relevant mathematical ideas of the week.

To open the notebook for Homework 2, click [**this link**](https://colab.research.google.com/github/math-124/fa26-code/blob/main/homeworks/hw02/hw02.ipynb). Instructions on how to use Google Colab are at [math124.org/running-code](https://math124.org/running-code).

You won't need to submit the notebook anywhere. To get credit for the work you did in this notebook, include the following in your PDF submission to Homework 2 on Pensive, specifically under **Problem 9**:

<ol class="assignment-enumeration" markdown="1">

<li markdown="1">
<div class="assignment-enumeration-label">1.</div>
<div class="assignment-enumeration-content" markdown="1">

**Task 1:** A screenshot of your three word-count arrays and their output.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">2.</div>
<div class="assignment-enumeration-content" markdown="1">

**Task 2:** A screenshot of your completed cosine similarity function and the outputs of the three example calls.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">3.</div>
<div class="assignment-enumeration-content" markdown="1">

**Task 3:** A screenshot of the three document comparisons and your written answer identifying the most similar pair.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">4.</div>
<div class="assignment-enumeration-content" markdown="1">

**Task 4:** Your written responses to all three prompts.

</div></li>
</ol>

{% endraw %}
