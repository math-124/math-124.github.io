---
layout: page
title: "Homework 9: Orthogonality and Least Squares"
description: "Homework 9: Orthogonality and Least Squares problems."
nav_exclude: true
hide_footer_hr: true
---

{% raw %}

<script>
window.MathJax = {
  loader: {load: ['[tex]/html']},
  tex: {packages: {'[+]': ['html']}, inlineMath: [['$', '$'], ['\\(', '\\)']]},
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
.main-content ol.assignment-enumeration > li.assignment-task {
  grid-template-columns: 4.3em minmax(0, 1fr);
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

# Homework 9: Orthogonality and Least Squares

**due** Tuesday, November 24th at 11:59PM

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button colab-btn" href="https://colab.research.google.com/github/math-124/fa26-code/blob/main/homeworks/hw09/hw09.ipynb" target="_blank"><img src="/assets/site-images/google-colab.png" alt="" aria-hidden="true"> Google Colab</a>
</div>

{: .yellow }
<div markdown="1">
Write your solutions to the following problems either by writing them on a piece of paper or on a tablet and scanning your answers as a PDF. Note that you are not allowed to use LaTeX, Google Docs, or any other digital document creation software to type your answers. Homeworks are due to Pensive by 11:59PM on the due date. See the [syllabus](https://math124.org/syllabus/#homework) for details on the slip day policy.

Homework will be evaluated not only on the correctness of your answers, but on your ability to present your ideas clearly and logically. You should always explain and justify your conclusions, using sound reasoning. Your goal should be to convince the reader of your assertions. If a question does not require explanation, it will be explicitly stated.

Before proceeding, make sure you're familiar with the [collaboration policy](https://math124.org/syllabus/#collaboration-and-generative-ai-policy).
</div>

---

## Problems

- [Problem 1: Midterm 2 Reflection](#problem-1-midterm-2-reflection-6-pts)
- [Problem 2: Complete the QR factorization](#problem-2-complete-the-qr-factorization-8-pts)
- [Problem 3: Completing an orthogonal matrix](#problem-3-completing-an-orthogonal-matrix-20-pts)
- [Problem 4: The cross product and orientation](#problem-4-the-cross-product-and-orientation-16-pts)
- [Problem 5: Rotations, reflections, and their compositions](#problem-5-rotations-reflections-and-their-compositions-22-pts)
- [Problem 6: Orthonormal columns and least squares](#problem-6-orthonormal-columns-and-least-squares-16-pts)
- [Problem 7: Predicting Billy's tips: use a computer](#problem-7-predicting-billys-tips-use-a-computer-12-pts)

---

Total Points: <span class="math-inline">\\(6+8+20+16+22+16+12=100\\)</span>.

---

{: .yellow }
> Using one slip day extends this homework's deadline to **Monday, November 30th at 11:59PM**. We don't recommend leaving the entire homework to the last minute, because the next homework is due **Friday, December 4th**.
>
> While working on this homework, refer to [Chapter 6](https://notes.math124.org/ch06/06-01/) and Chapter 7 (coming soon).

---

## Problem 1: Midterm 2 Reflection (6 pts)

Write a response to the following prompt and include it in your homework PDF:

> Think of one specific topic you struggled with while studying for Midterm 2. What did you do to make sense of it, and how did it go on the exam? If you were studying for Midterm 2 again, what would you do differently?

**This problem is graded on completion.** Make an honest effort to respond to the prompt, and you will receive full credit. Your explanation does not need to be polished or perfect.

---

## Problem 2: Complete the QR factorization (8 pts)

The following is a partially completed QR factorization <span class="math-inline">\\(A=QR\\)</span>. Fill in every missing entry so that the columns of <span class="math-inline">\\(Q\\)</span> are orthonormal and <span class="math-inline">\\(R\\)</span> is upper triangular with positive diagonal entries.

<div class="math-display">
$$
\underbrace{\begin{bmatrix}
3&3&0\\3&-5&12\\3&-5&-2\\3&3&-2
\end{bmatrix}}_A
=
\underbrace{\begin{bmatrix}
1/2&1/2&1/10\\
\boxed{\phantom{-10}}&-1/2&7/10\\
1/2&\boxed{\phantom{-10}}&-7/10\\
1/2&1/2&\boxed{\phantom{-10}}
\end{bmatrix}}_Q
\underbrace{\begin{bmatrix}
\boxed{\phantom{-10}}&\boxed{\phantom{-10}}&4\\0&8&\boxed{\phantom{-10}}\\0&0&\boxed{\phantom{-10}}
\end{bmatrix}}_R.
$$
</div>

 Explain how you found the missing entries. Check that the completed factors satisfy <span class="math-inline">\\(Q^TQ=I\\)</span> and <span class="math-inline">\\(QR=A\\)</span>.

---

## Problem 3: Completing an orthogonal matrix (20 pts)

Let

<div class="math-display">
$$
Q_1=\begin{bmatrix}
\frac3{13}&\frac{12}{17}\\
\frac4{13}&-\frac{12}{17}\\
\frac{12}{13}&\frac1{17}
\end{bmatrix}
=\begin{bmatrix}|&|\\\vec{u}_1&\vec{u}_2\\|&|\end{bmatrix}.
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Compute <span class="math-inline">\\(Q&#95;1^TQ&#95;1\\)</span> and <span class="math-inline">\\(Q&#95;1Q&#95;1^T\\)</span> to check that <span class="math-inline">\\(Q&#95;1^TQ&#95;1=I\\)</span>, but <span class="math-inline">\\(Q&#95;1Q&#95;1^T\ne I\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Find a third column <span class="math-inline">\\(\vec{u}&#95;3\\)</span> so that the <span class="math-inline">\\(3\times3\\)</span> matrix

<div class="math-display">
$$
Q=\begin{bmatrix}|&|&|\\\vec{u}_1&\vec{u}_2&\vec{u}_3\\|&|&|\end{bmatrix}
$$
</div>

 is orthogonal. Do this by the following method:

Pick a random vector <span class="math-inline">\\(\vec{v}&#95;3\\)</span> that is not in the span of <span class="math-inline">\\(\vec{u}&#95;1\\)</span> and <span class="math-inline">\\(\vec{u}&#95;2\\)</span>. Apply Gram--Schmidt to <span class="math-inline">\\(\vec{u}&#95;1,\vec{u}&#95;2,\vec{v}&#95;3\\)</span> to obtain the third column <span class="math-inline">\\(\vec{u}&#95;3\\)</span>. Write down the resulting orthogonal matrix <span class="math-inline">\\(Q\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Now we'll use a different method. Use the methods we learned previously to find an equation for the plane spanned by <span class="math-inline">\\(\vec{u}&#95;1\\)</span> and <span class="math-inline">\\(\vec{u}&#95;2\\)</span>. Use this equation to find a nonzero vector perpendicular to both columns, and normalize it to length one. Write down the resulting orthogonal matrix <span class="math-inline">\\(Q\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(1 pt) How many choices are there for the third column <span class="math-inline">\\(\vec{u}&#95;3\\)</span>? Explain your answer.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Check that <span class="math-inline">\\(QQ^T=I\\)</span> as well. What does this tell you about the rows of <span class="math-inline">\\(Q\\)</span>? Write down the orthonormal basis of <span class="math-inline">\\(\mathbb{R}^3\\)</span> given by this relation, expressing the vectors as column vectors.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">f)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Let

<div class="math-display">
$$
\vec x=\begin{bmatrix}5\\14\\6\end{bmatrix}.
$$
</div>

 Use your completed matrix <span class="math-inline">\\(Q\\)</span> from part (b) to find scalars <span class="math-inline">\\(c&#95;1,c&#95;2,c&#95;3\\)</span> such that

<div class="math-display">
$$
\vec x=c_1\vec u_1+c_2\vec u_2+c_3\vec u_3.
$$
</div>

 Explain how the fact that <span class="math-inline">\\(Q\\)</span> is orthogonal allows you to find these coordinates.

</div>
</div>

</div>

---

## Problem 4: The cross product and orientation (16 pts)

For vectors <span class="math-inline">\\(\style{color:rgb(176,79,9)}{\boldsymbol{\vec a}},\style{color:rgb(29,78,216)}{\boldsymbol{\vec b}}\\)</span> in <span class="math-inline">\\(\mathbb{R}^3\\)</span>, their *cross product* is the vector

<div class="math-display">
$$
\style{color:rgb(162,28,88)}{\boldsymbol{\vec c}}
=\style{color:rgb(176,79,9)}{\boldsymbol{\vec a}}\times\style{color:rgb(29,78,216)}{\boldsymbol{\vec b}}
=\begin{bmatrix}\style{color:rgb(162,28,88)}{\boldsymbol{c_1}}\\\style{color:rgb(162,28,88)}{\boldsymbol{c_2}}\\\style{color:rgb(162,28,88)}{\boldsymbol{c_3}}\end{bmatrix}
=\begin{bmatrix}
\style{color:rgb(176,79,9)}{\boldsymbol{a_2}}\style{color:rgb(29,78,216)}{\boldsymbol{b_3}}-\style{color:rgb(176,79,9)}{\boldsymbol{a_3}}\style{color:rgb(29,78,216)}{\boldsymbol{b_2}}\\
\style{color:rgb(176,79,9)}{\boldsymbol{a_3}}\style{color:rgb(29,78,216)}{\boldsymbol{b_1}}-\style{color:rgb(176,79,9)}{\boldsymbol{a_1}}\style{color:rgb(29,78,216)}{\boldsymbol{b_3}}\\
\style{color:rgb(176,79,9)}{\boldsymbol{a_1}}\style{color:rgb(29,78,216)}{\boldsymbol{b_2}}-\style{color:rgb(176,79,9)}{\boldsymbol{a_2}}\style{color:rgb(29,78,216)}{\boldsymbol{b_1}}
\end{bmatrix}.
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) In this part only, consider the vectors

<div class="math-display">
$$
\vec u=\begin{bmatrix}7\\-4\\9\end{bmatrix},\qquad
\vec v=\begin{bmatrix}-6\\8\\5\end{bmatrix}.
$$
</div>

 Compute <span class="math-inline">\\(\vec u\times\vec v\\)</span>. Then compute <span class="math-inline">\\(\vec u\cdot(\vec u\times\vec v)\\)</span> and <span class="math-inline">\\(\vec v\cdot(\vec u\times\vec v)\\)</span> to show that the cross product is orthogonal to both <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(1 pt) Compute <span class="math-inline">\\(\vec e&#95;1\times\vec e&#95;2\\)</span> and <span class="math-inline">\\(\vec e&#95;2\times\vec e&#95;1\\)</span>, where <span class="math-inline">\\(\vec e&#95;1,\vec e&#95;2,\vec e&#95;3\\)</span> are the standard basis vectors. What happens when you reverse the order?

For the rest of this problem, let's consider the arbitrary vectors

<div class="math-display">
$$
\style{color:rgb(176,79,9)}{\boldsymbol{\vec a}}=\begin{bmatrix}\style{color:rgb(176,79,9)}{\boldsymbol{a_1}}\\\style{color:rgb(176,79,9)}{\boldsymbol{a_2}}\\\style{color:rgb(176,79,9)}{\boldsymbol{a_3}}\end{bmatrix},\qquad
\style{color:rgb(29,78,216)}{\boldsymbol{\vec b}}=\begin{bmatrix}\style{color:rgb(29,78,216)}{\boldsymbol{b_1}}\\\style{color:rgb(29,78,216)}{\boldsymbol{b_2}}\\\style{color:rgb(29,78,216)}{\boldsymbol{b_3}}\end{bmatrix}.
$$
</div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Verify directly from the formula that

<div class="math-display">
$$
\vec a\cdot(\vec a\times\vec b)=0,\qquad
\vec b\cdot(\vec a\times\vec b)=0.
$$
</div>

 Thus the cross product is perpendicular to both input vectors.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Verify that

<div class="math-display">
$$
\|\vec a\times\vec b\|^2
=\|\vec a\|^2\|\vec b\|^2-(\vec a\cdot\vec b)^2.
$$
</div>

 <em>Hint: Expand both sides and collect terms.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) For nonzero vectors <span class="math-inline">\\(\vec a,\vec b\\)</span>, let <span class="math-inline">\\(\theta\\)</span> be the angle between them. Deduce that

<div class="math-display">
$$
\|\vec a\times\vec b\|=\|\vec a\|\,\|\vec b\|\sin\theta.
$$
</div>

 <em>Hint: Use <span class="math-inline">\\(\vec a\cdot\vec b=\|\vec a\|\|\vec b\|\cos\theta\\)</span> and <span class="math-inline">\\(1-\cos^2\theta=\sin^2\theta\\)</span>.</em>

Explain why this is the area of the parallelogram with sides <span class="math-inline">\\(\vec a,\vec b\\)</span>. In particular, what is the length of their cross product if they are perpendicular unit vectors?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">f)</div>
<div class="assignment-part-content" markdown="1">
(1 pt) Its direction follows the *right-hand rule*: curl the fingers of your right hand from the first vector toward the second through the smaller angle; your thumb points along their cross product. In particular,

<div class="math-display">
$$
\vec u_1,\quad\vec u_2,\quad\vec u_1\times\vec u_2
$$
</div>

 form a *right-handed orthonormal basis* when <span class="math-inline">\\(\vec u&#95;1,\vec u&#95;2\\)</span> are perpendicular unit vectors. Replacing the third vector by its negative gives a *left-handed* basis.

<img src="imgs/hw09-plot-01.png" alt="Coordinate diagram" class="assignment-vector-plot">

The picture is viewed from the tip of the third vector toward the origin; the circled dot means that vector points out of the page. In a right-handed basis the turn from the first vector to the second is counterclockwise in this view.

Using your answers to (b), classify the ordered bases <span class="math-inline">\\((\vec e&#95;1,\vec e&#95;2,\vec e&#95;3)\\)</span> and <span class="math-inline">\\((\vec e&#95;2,\vec e&#95;1,\vec e&#95;3)\\)</span> as right-handed or left-handed.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">g)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Compute <span class="math-inline">\\(\vec u&#95;1\times\vec u&#95;2\\)</span> for the two columns of <span class="math-inline">\\(Q&#95;1\\)</span> in Problem 3. Compare this with your two possible third columns. Which choice makes the columns of the completed matrix <span class="math-inline">\\(Q\\)</span> a right-handed orthonormal basis?

</div>
</div>

</div>

---

## Problem 5: Rotations, reflections, and their compositions (22 pts)

In this problem, we will explore the compositions of rotations and reflections, two types of linear transformations we have already studied earlier in the semester.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Recall that the matrix representing counterclockwise rotation by <span class="math-inline">\\(\theta\\)</span> is

<div class="math-display">
$$
R_\theta=\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}.
$$
</div>

 Let's use the fact that rotating by <span class="math-inline">\\(\alpha\\)</span> and then by <span class="math-inline">\\(\beta\\)</span> is the same as rotating by <span class="math-inline">\\(\alpha+\beta\\)</span> to recover the trigonometric identities you learned about in high school.

Let <span class="math-inline">\\(R&#95;\alpha\\)</span> and <span class="math-inline">\\(R&#95;\beta\\)</span> be matrices that represent counterclockwise rotations by <span class="math-inline">\\(\alpha\\)</span> and <span class="math-inline">\\(\beta\\)</span>, respectively. Find <span class="math-inline">\\(R&#95;\beta R&#95;\alpha\\)</span>, and use it to find formulas for <span class="math-inline">\\(\cos(\alpha+\beta)\\)</span> and <span class="math-inline">\\(\sin(\alpha+\beta)\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Reflecting a vector across a line means reflecting its tip across that line while keeping its tail at the origin. Let <span class="math-inline">\\(H&#95;\alpha\\)</span> represent reflection across the line through the origin making angle <span class="math-inline">\\(\alpha\\)</span> with the positive <span class="math-inline">\\(x\\)</span>-axis.

Use geometry to show that

<div class="math-display">
$$
H_\alpha=\begin{bmatrix}\cos(2\alpha)&\sin(2\alpha)\\\sin(2\alpha)&-\cos(2\alpha)\end{bmatrix}.
$$
</div>

<ol class="assignment-enumeration" markdown="1">
<li markdown="1">
<div class="assignment-enumeration-label">(i)</div>
<div class="assignment-enumeration-content" markdown="1">

Draw the line, the standard basis vectors <span class="math-inline">\\(\vec e&#95;1\\)</span> and <span class="math-inline">\\(\vec e&#95;2\\)</span>, and their reflections. Label the relevant angles.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">(ii)</div>
<div class="assignment-enumeration-content" markdown="1">

Find the coordinates of the two reflected vectors, then use them as the columns of <span class="math-inline">\\(H&#95;\alpha\\)</span>.

</div></li>
</ol>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) The lines <span class="math-inline">\\(\ell&#95;\alpha\\)</span> and <span class="math-inline">\\(\ell&#95;\beta\\)</span> below pass through the origin and make angles <span class="math-inline">\\(\alpha\\)</span> and <span class="math-inline">\\(\beta\\)</span> with the positive <span class="math-inline">\\(x\\)</span>-axis. Consider <span class="math-inline">\\(H&#95;\beta H&#95;\alpha\\)</span>: first reflect across <span class="math-inline">\\(\ell&#95;\alpha\\)</span>, then across <span class="math-inline">\\(\ell&#95;\beta\\)</span>.

Do not use matrix multiplication in this part.

<ol class="assignment-enumeration" markdown="1">
<li markdown="1">
<div class="assignment-enumeration-label">(i)</div>
<div class="assignment-enumeration-content" markdown="1">

Draw <span class="math-inline">\\(\vec v\\)</span>, the vector obtained after the first reflection, and the vector obtained after the second reflection. Label the relevant angles.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">(ii)</div>
<div class="assignment-enumeration-content" markdown="1">

Use your picture to show that the composition is a rotation and find its angle.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">(iii)</div>
<div class="assignment-enumeration-content" markdown="1">

Express your answer as <span class="math-inline">\\(H&#95;\beta H&#95;\alpha=R&#95;{?}\\)</span>.

</div></li>
</ol>

<img src="imgs/hw09-plot-02.png" alt="Coordinate diagram" class="assignment-vector-plot">

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) Now recover your answer to part (c) algebraically. Multiply the matrices in <span class="math-inline">\\(H&#95;\beta H&#95;\alpha\\)</span>, simplify the entries using trigonometric identities, and identify the resulting rotation and its angle.

</div>
</div>

</div>

---

## Problem 6: Orthonormal columns and least squares (16 pts)

Consider the matrix <span class="math-inline">\\(A\\)</span> and vector <span class="math-inline">\\(\vec b\\)</span> below:

<div class="math-display">
$$
A=\begin{bmatrix}1&3\\2&1\\2&6\\4&2\end{bmatrix},\qquad
\vec b=\begin{bmatrix}7\\6\\4\\7\end{bmatrix}.
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find the least-squares solution <span class="math-inline">\\(\vec x^{\ast}\\)</span> to <span class="math-inline">\\(A\vec x=\vec b\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Find the projection <span class="math-inline">\\(\vec p\\)</span> of <span class="math-inline">\\(\vec b\\)</span> onto the column space of <span class="math-inline">\\(A\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Applying Gram--Schmidt to the columns of <span class="math-inline">\\(A\\)</span> gives the following matrix with orthonormal columns:

<div class="math-display">
$$
G=\frac15\begin{bmatrix}1&2\\2&-1\\2&4\\4&-2\end{bmatrix}.
$$
</div>

 Find the least-squares solution <span class="math-inline">\\(\vec x&#95;G^{\ast}\\)</span> to <span class="math-inline">\\(G\vec x=\vec b\\)</span>, and compute <span class="math-inline">\\(\vec p&#95;G=G\vec x&#95;G^{\ast}\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Why was it easier to find the least-squares solution in part (c) than in part (a)? Explain why the projection vectors are the same even though <span class="math-inline">\\(\vec x^{\ast}\\)</span> and <span class="math-inline">\\(\vec x&#95;G^{\ast}\\)</span> are different.

</div>
</div>

</div>

---

## Problem 7: Predicting Billy's tips: use a computer (12 pts)

Before proceeding, open the supplemental Jupyter Notebook. To open the notebook for Homework 9, click [**this link**](https://colab.research.google.com/github/math-124/fa26-code/blob/main/homeworks/hw09/hw09.ipynb). Instructions on how to use Google Colab are at [math124.org/running-code](https://math124.org/running-code).

You will fit a line <span class="math-inline">\\(y=c+mt\\)</span>, where <span class="math-inline">\\(t\\)</span> is the total bill and <span class="math-inline">\\(y\\)</span> is the predicted tip. The notebook provides the data, setup, and most of the code.

Complete Tasks 1-6 in the notebook. Include the requested code, output, and written responses in your homework PDF.

<ol class="assignment-enumeration" markdown="1">
<li class="assignment-task" markdown="1">
<div class="assignment-enumeration-label"><strong>Task 1.</strong></div>
<div class="assignment-enumeration-content" markdown="1">

(3 points) Fit the line by solving the normal equations with `np.linalg.solve`.

</div></li>
<li class="assignment-task" markdown="1">
<div class="assignment-enumeration-label"><strong>Task 2.</strong></div>
<div class="assignment-enumeration-content" markdown="1">

(1 point) Interpret the slope <span class="math-inline">\\(m\\)</span>.

</div></li>
<li class="assignment-task" markdown="1">
<div class="assignment-enumeration-label"><strong>Task 3.</strong></div>
<div class="assignment-enumeration-content" markdown="1">

(2 points) Complete `predict_tip` and predict the tip for a <span class="currency tex2jax_ignore">$38.50</span> bill.

</div></li>
<li class="assignment-task" markdown="1">
<div class="assignment-enumeration-label"><strong>Task 4.</strong></div>
<div class="assignment-enumeration-content" markdown="1">

(2 points) Assess whether the prediction for a <span class="currency tex2jax_ignore">$3,000</span> bill is accurate.

</div></li>
<li class="assignment-task" markdown="1">
<div class="assignment-enumeration-label"><strong>Task 5.</strong></div>
<div class="assignment-enumeration-content" markdown="1">

(2 points) Complete `compute_mse` and find the fitted line's mean squared error.

</div></li>
<li class="assignment-task" markdown="1">
<div class="assignment-enumeration-label"><strong>Task 6.</strong></div>
<div class="assignment-enumeration-content" markdown="1">

(2 points) Use the sliders to compare another line with the least-squares line.

</div></li>
</ol>

{% endraw %}
