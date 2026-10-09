---
layout: page
title: "Homework 5: Matrices and Linear Transformations"
description: "Homework 5: Matrices and Linear Transformations problems."
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

# Homework 5: Matrices and Linear Transformations

**due** Friday, October 16th at 11:59PM

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw05/hw05.pdf" target="_blank">View as PDF ✏️</a>
</div>

{: .yellow }
<div markdown="1">
Write your solutions to the following problems either by writing them on a piece of paper or on a tablet and scanning your answers as a PDF. Note that you are not allowed to use LaTeX, Google Docs, or any other digital document creation software to type your answers. Homeworks are due to Pensive by 11:59PM on the due date. See the [syllabus](https://math124.org/syllabus/#homework) for details on the slip day policy.

Homework will be evaluated not only on the correctness of your answers, but on your ability to present your ideas clearly and logically. You should always explain and justify your conclusions, using sound reasoning. Your goal should be to convince the reader of your assertions. If a question does not require explanation, it will be explicitly stated.

Before proceeding, make sure you're familiar with the [collaboration policy](https://math124.org/syllabus/#collaboration-and-generative-ai-policy).
</div>

---

## Problems

- [Problem 1: Midterm 1 Solutions Reflection](#problem-1-midterm-1-solutions-reflection-6-pts)
- [Problem 2: Matrix--Vector Practice](#problem-2-matrix--vector-practice-8-pts)
- [Problem 3: Is It Linear?](#problem-3-is-it-linear-9-pts)
- [Problem 4: What Linearity Tells Us](#problem-4-what-linearity-tells-us-8-pts)
- [Problem 5: Finding a Transformation's Matrix](#problem-5-finding-a-transformations-matrix-8-pts)
- [Problem 6: Can We Work Backward?](#problem-6-can-we-work-backward-6-pts)
- [Problem 7: Matrix Products](#problem-7-matrix-products-12-pts)
- [Problem 8: Do the Usual Rules Still Work?](#problem-8-do-the-usual-rules-still-work-6-pts)
- [Problem 9: Transforming a Triangle](#problem-9-transforming-a-triangle-8-pts)
- [Problem 10: From Projection to Reflection](#problem-10-from-projection-to-reflection-9-pts)
- [Problem 11: Programming Activity](#problem-11-programming-activity-20-pts)

---

Total Points: <span class="math-inline">\\(6 + 8 + 9 + 8 + 8 + 6 + 12 + 6 + 8 + 9 + 20 = 100\\)</span>

---

## Problem 1: Midterm 1 Solutions Reflection (6 pts)

Review the solutions to Midterm 1. Pick **two problem parts** in which your solutions have the most room for improvement: for example, where your reasoning was unsound or your presentation could have been clearer or more efficient. Include a screenshot of your solution to each part. For each, explain what was deficient and how to fix it.

Alternatively, if one of your solutions is significantly better than the posted one, include it and explain why. If you did not take Midterm 1, choose two challenging parts and explain the key ideas behind their solutions in your own words.

---

## Problem 2: Matrix--Vector Practice (8 pts)

Compute each product, or explain why it is undefined. For each defined product, state the shape of the output. Show your arithmetic.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts)
<span class="math-inline">\\(\displaystyle \begin{bmatrix}4&amp;-2&amp;0&amp;3\\\\-3&amp;5&amp;2&amp;-1\\\\4&amp;1&amp;-5&amp;2\end{bmatrix} \begin{bmatrix}-2\\\\3\\\\1\\\\-2\end{bmatrix}\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts)
<span class="math-inline">\\(\displaystyle \begin{bmatrix}-8&amp;0&amp;0&amp;0&amp;0\\\\0&amp;\frac32&amp;0&amp;0&amp;0\\\\0&amp;0&amp;11&amp;0&amp;0\\\\0&amp;0&amp;0&amp;-5&amp;0\\\\0&amp;0&amp;0&amp;0&amp;7\end{bmatrix} \begin{bmatrix}3\\\\-4\\\\2\\\\6\\\\-3\end{bmatrix}\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(2 pts)
<span class="math-inline">\\(\displaystyle \begin{bmatrix}12&amp;-7&amp;\frac12&amp;9\end{bmatrix}\begin{bmatrix}3\\\\-2\\\\8\\\\-4\end{bmatrix}\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(2 pts)
<span class="math-inline">\\(\displaystyle \begin{bmatrix}-5&amp;8&amp;3&amp;12\\\\7&amp;-2&amp;6&amp;-9\end{bmatrix}\begin{bmatrix}4\\\\-1\\\\5\end{bmatrix}\\)</span>

</div>
</div>

</div>

---

## Problem 3: Is It Linear? (9 pts)

For each transformation, decide whether it is linear. A linear transformation must satisfy both properties below for all vectors <span class="math-inline">\\(\vec u,\vec v\\)</span> in its domain and all scalars <span class="math-inline">\\(c\\)</span>:

-   **Additivity:** <span class="math-inline">\\(T(\vec u+\vec v)=T(\vec u)+T(\vec v)\\)</span>.

-   **Compatibility with scaling:** <span class="math-inline">\\(T(c\vec v)=cT(\vec v)\\)</span>.

For a linear transformation, verify both properties for arbitrary inputs. For a nonlinear transformation, give a specific counterexample to at least one property. State your inputs and show that the two sides are different.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(3 pts)
<span class="math-inline">\\(T:\mathbb R^2\to\mathbb R^2\\)</span>, defined by <span class="math-inline">\\(T\left(\begin{bmatrix}x\\\\y\end{bmatrix}\right) =\begin{bmatrix}(3x+2y)^2-9x^2-4y^2\\\\7x-5y\end{bmatrix}\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts)
<span class="math-inline">\\(T:\mathbb R^3\to\mathbb R^2\\)</span>, defined by <span class="math-inline">\\(T\left(\begin{bmatrix}x\\\\y\\\\z\end{bmatrix}\right) =\begin{bmatrix}4(x-2y)+3(2y-z)\\\\5(x+z)-2(3x-y)\end{bmatrix}\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(3 pts)
<span class="math-inline">\\(T:\mathbb R^2\to\mathbb R^3\\)</span>, defined by <span class="math-inline">\\(T\left(\begin{bmatrix}x\\\\y\end{bmatrix}\right) =\begin{bmatrix}6x-5y+8\\\\4(x+y)-7\\\\9x+2y-8\end{bmatrix}\\)</span>.

</div>
</div>

</div>

---

## Problem 4: What Linearity Tells Us (8 pts)

Let <span class="math-inline">\\(T:\mathbb R^3\to\mathbb R^2\\)</span> be a linear transformation, and let

<div class="math-display">
$$
\vec u=\begin{bmatrix}2\\-1\\3\end{bmatrix},\qquad
\vec v=\begin{bmatrix}-1\\2\\1\end{bmatrix}.
$$
</div>

 Suppose we know that

<div class="math-display">
$$
T(3\vec u+\vec v)=\begin{bmatrix}8\\-1\end{bmatrix},\qquad
T(2\vec u-3\vec v)=\begin{bmatrix}9\\-8\end{bmatrix}.
$$
</div>

 Use linearity directly; you do not need to find the matrix of <span class="math-inline">\\(T\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Find <span class="math-inline">\\(T(\vec u)\\)</span> and <span class="math-inline">\\(T(\vec v)\\)</span>. Show how you use the two given outputs.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Find <span class="math-inline">\\(T\left(\begin{bmatrix}8\\\\-7\\\\7\end{bmatrix}\right)\\)</span>. Explain how you express this input using <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) A student claims that <span class="math-inline">\\(T\left(\begin{bmatrix}3\\\\0\\\\7\end{bmatrix}\right)=\begin{bmatrix}5\\\\1\end{bmatrix}\\)</span>. Is this consistent? Explain.

</div>
</div>

</div>

---

## Problem 5: Finding a Transformation's Matrix (8 pts)

Let <span class="math-inline">\\(S:\mathbb R^2\to\mathbb R^2\\)</span> be a linear transformation satisfying

<div class="math-display">
$$
S\!\left(\begin{bmatrix}2\\0\end{bmatrix}\right)=\begin{bmatrix}8\\6\end{bmatrix},\qquad
S\!\left(\begin{bmatrix}0\\3\end{bmatrix}\right)=\begin{bmatrix}-9\\12\end{bmatrix}.
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Find <span class="math-inline">\\(S\left(\begin{bmatrix}1\\\\0\end{bmatrix}\right)\\)</span> and <span class="math-inline">\\(S\left(\begin{bmatrix}0\\\\1\end{bmatrix}\right)\\)</span>, then construct the matrix of <span class="math-inline">\\(S\\)</span>. Explain how you chose its columns.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Use your matrix to find <span class="math-inline">\\(S\left(\begin{bmatrix}3\\\\-2\end{bmatrix}\right)\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Describe the geometric effect of <span class="math-inline">\\(S\\)</span> in words, using the types of linear transformations we saw in [Chapter 3.2](https://notes.math124.org/ch03/03-02/) and [Chapter 3.4](https://notes.math124.org/ch03/03-04/). Specify any scale factor and, if there is a rotation, its direction and angle. You may specify an angle by giving its sine and cosine.

</div>
</div>

</div>

---

## Problem 6: Can We Work Backward? (6 pts)

Let <span class="math-inline">\\(\displaystyle A=\begin{bmatrix}4&amp;-6\\\\-2&amp;3\end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Find two different inputs <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> such that <span class="math-inline">\\(A\vec u=A\vec v=\begin{bmatrix}12\\\\-6\end{bmatrix}\\)</span>. Write the system of equations you are solving.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Is there an input with output <span class="math-inline">\\(\begin{bmatrix}12\\\\-5\end{bmatrix}\\)</span>? Explain using the columns of <span class="math-inline">\\(A\\)</span> and their span.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Using your inputs from part (a), find a nonzero input with output <span class="math-inline">\\(\vec0\\)</span>. Explain why your construction works using linearity.

**Note: Problems 7--11 require material from Tuesday's lecture.**

</div>
</div>

</div>

---

## Problem 7: Matrix Products (12 pts)

Compute the requested products and state their shapes. Show your arithmetic.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Let

<div class="math-display">
$$
A=\begin{bmatrix}3&-2\\-1&4\\4&1\\2&-3\end{bmatrix},\qquad
B=\begin{bmatrix}2&-3&1&2\\-2&1&4&-1\end{bmatrix}.
$$
</div>

 Compute both <span class="math-inline">\\(AB\\)</span> and <span class="math-inline">\\(BA\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Let

<div class="math-display">
$$
C=\begin{bmatrix}3&-2&4\\0&5&2\\0&0&-2\end{bmatrix},\qquad
D=\begin{bmatrix}2&4&-3\\5&-2&1\\-4&3&2\end{bmatrix}.
$$
</div>

 Compute both <span class="math-inline">\\(CD\\)</span> and <span class="math-inline">\\(DC\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) A mechanical engineer wants to measure how a beam bends when forces are applied at different locations. A **test rig** is a laboratory setup built to test a component under controlled conditions. This rig has three **actuators**, motor-driven devices that push or pull on the beam, and five **sensors**, devices that measure the beam's vertical movement at five locations.

<div style="text-align: center;">
<img src="imgs/hw05-plot-01.png" alt="Coordinate diagram" class="assignment-vector-plot">
</div>

In a simplified linear model, <span class="math-inline">\\(H\vec u\\)</span> gives the five sensor readings, in millimeters, when <span class="math-inline">\\(\vec u\\)</span> lists the forces applied by the three actuators, in **newtons (N)**. For example, <span class="math-inline">\\(\vec u=\begin{bmatrix}2\\\\-3\\\\4\end{bmatrix}\\)</span> corresponds to the first actuator pushing upward with a force of <span class="math-inline">\\(2\\)</span> N, the second pulling downward with a force of <span class="math-inline">\\(3\\)</span> N, and the third pushing upward with a force of <span class="math-inline">\\(4\\)</span> N. Sensor readings are displacements from the beam's unloaded position; positive readings mean upward movement.

The columns of <span class="math-inline">\\(U\\)</span> give the actuator forces for two separate trials:

<div class="math-display">
$$
H=\begin{bmatrix}
3&-2&4\\-2&4&3\\5&1&-3\\3&-4&2\\-4&3&2
\end{bmatrix},\qquad
U=\begin{bmatrix}2&-3\\-3&4\\4&2\end{bmatrix}.
$$
</div>

 Compute <span class="math-inline">\\(HU\\)</span>. What does the entry in row 4, column 2 of your answer represent? Why is <span class="math-inline">\\(UH\\)</span> undefined? Write a sentence involving the actuators, sensors, and two trials; simply saying that the matrix shapes do not match is not enough.

</div>
</div>

</div>

---

## Problem 8: Do the Usual Rules Still Work? (6 pts)

All matrices in this problem are <span class="math-inline">\\(2\times2\\)</span> and all vectors are in <span class="math-inline">\\(\mathbb R^2\\)</span>. Justify each answer. A counterexample must include specific matrices or vectors and the relevant products.

<em>Hint: It may help to complete Problem 6(c) first, where you find a nonzero vector whose product with a matrix is zero.</em>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) If <span class="math-inline">\\(B\vec v=\vec0\\)</span>, must <span class="math-inline">\\(AB\vec v=\vec0\\)</span>? If <span class="math-inline">\\(AB\vec v=\vec0\\)</span>, must <span class="math-inline">\\(B\vec v=\vec0\\)</span>? Address both directions.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Can <span class="math-inline">\\(AB=0&#95;{2\times2}\\)</span> even when neither <span class="math-inline">\\(A\\)</span> nor <span class="math-inline">\\(B\\)</span> is the zero matrix? Give an example or explain why it is impossible.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Expand <span class="math-inline">\\((A+B)^2\\)</span> using distributivity, keeping the factors in their original order. Is it always equal to <span class="math-inline">\\(A^2+2AB+B^2\\)</span>? If not, give a counterexample.

</div>
</div>

</div>

---

## Problem 9: Transforming a Triangle (8 pts)

Consider the triangle with vertices <span class="math-inline">\\(\begin{bmatrix}0\\\\0\end{bmatrix}\\)</span>, <span class="math-inline">\\(\begin{bmatrix}4\\\\0\end{bmatrix}\\)</span>, and <span class="math-inline">\\(\begin{bmatrix}0\\\\2\end{bmatrix}\\)</span>. To transform it, transform its three vertices and connect their images.

<div style="text-align: center;">
<img src="imgs/hw05-plot-02.png" alt="Coordinate diagram" class="assignment-vector-plot">
</div>

Let <span class="math-inline">\\(D\\)</span> stretch horizontally by a factor of <span class="math-inline">\\(2\\)</span>, leaving vertical coordinates unchanged. Let <span class="math-inline">\\(Q\\)</span> rotate counterclockwise by <span class="math-inline">\\(45^\circ\\)</span> about the origin. Recall that the rotation matrix is

<div class="math-display">
$$
\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}.
$$
</div>

 Give exact matrix entries and vertex coordinates. You may use decimal approximations when drawing.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Write the matrices <span class="math-inline">\\(Q\\)</span> and <span class="math-inline">\\(D\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Find the matrix for stretching first and then rotating. Draw the resulting triangle on a coordinate plane, labeling the coordinates of all three vertices.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Reverse the order, find the new combined matrix, and draw the resulting triangle on a second coordinate plane with the same scale. Label the coordinates of all three vertices. Describe how the two transformed triangles differ.

</div>
</div>

</div>

---

## Problem 10: From Projection to Reflection (9 pts)

In [Homework 4, Problem 9](https://math124.org/resources/homeworks/hw04/), you found that the reflection of a vector <span class="math-inline">\\(\vec v\\)</span> across a line can be written as

<div class="math-display">
$$
\vec v_{\mathrm{ref}}=2\vec p-\vec v,
$$
</div>

 where <span class="math-inline">\\(\vec p\\)</span> is the projection of <span class="math-inline">\\(\vec v\\)</span> onto the line. Here's the same picture again: the tip of <span class="math-inline">\\(\vec p\\)</span> is halfway between the tips of <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec v&#95;{\mathrm{ref}}\\)</span>.

<div style="text-align: center;">
<img src="imgs/reflection-example.png" alt="image" style="height: 3.15in; width: auto; max-width: 100%;">
</div>

In Lab 6, you used the matrix

<div class="math-display">
$$
P=\begin{bmatrix}w_1^2&w_1w_2\\w_1w_2&w_2^2\end{bmatrix}
$$
</div>

 to project onto a line spanned by a **unit vector** <span class="math-inline">\\(\vec w=\begin{bmatrix}w&#95;1\\\\w&#95;2\end{bmatrix}\\)</span>. Thus <span class="math-inline">\\(\vec p=P\vec v\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Derive a matrix <span class="math-inline">\\(R\\)</span>, expressed in terms of <span class="math-inline">\\(P\\)</span> and the identity matrix <span class="math-inline">\\(I\\)</span>, such that <span class="math-inline">\\(R\vec v=\vec v&#95;{\mathrm{ref}}\\)</span> for every <span class="math-inline">\\(\vec v\\)</span>. Then write all four entries of <span class="math-inline">\\(R\\)</span> in terms of <span class="math-inline">\\(w&#95;1,w&#95;2\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Now use the line spanned by <span class="math-inline">\\(\vec w=\begin{bmatrix}3/5\\\\4/5\end{bmatrix}\\)</span>. Find <span class="math-inline">\\(P\\)</span>, <span class="math-inline">\\(R\\)</span>, and the reflection of <span class="math-inline">\\(\vec v=\begin{bmatrix}7\\\\1\end{bmatrix}\\)</span> across this line.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) What does <span class="math-inline">\\(R\\)</span> do to a vector parallel to the line? To a vector perpendicular to it? Explain using projections.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Explain geometrically why <span class="math-inline">\\(P^2=P\\)</span> and <span class="math-inline">\\(R^2=I\\)</span>. Then use <span class="math-inline">\\(P^2=P\\)</span> and your expression for <span class="math-inline">\\(R\\)</span> to verify <span class="math-inline">\\(R^2=I\\)</span> algebraically.

</div>
</div>

</div>

---

## Problem 11: Programming Activity (20 pts)

The programming activity will be posted separately. It will be worth 20 points.

{% endraw %}
