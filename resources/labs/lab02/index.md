---
layout: page
title: "Lab 2: Vector Arithmetic, Lengths, and the Dot Product"
description: "Lab 2: Vector Arithmetic, Lengths, and the Dot Product activities."
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

# Lab 2: Vector Arithmetic, Lengths, and the Dot Product

**due** by the end of class on Wednesday, September 9, 2026

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab02/lab02.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab02/lab02-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
Each lab worksheet will contain several activities, most of which will involve writing math on paper, and some of which will involve running code in a Jupyter Notebook. Lab activities are meant to last an hour, and the second hour of lab is dedicated to starting the homework assignment. To receive credit for a lab, you must show your lab TA your work on both the lab worksheet and homework assignment.

While you must get checked off by your lab TA **individually**, we encourage you to form groups with 1-2 other students to complete the activities together.
</div>

---

## Activities

- [Activity 1: Linear Combinations and Lengths](#activity-1-linear-combinations-and-lengths)
- [Activity 2: The Dot Product](#activity-2-the-dot-product)
- [Activity 3: Angles and Orthogonality](#activity-3-angles-and-orthogonality)
- [Activity 4: Comparing Vectors](#activity-4-comparing-vectors)

---

**Review**

-   <span class="math-inline">\\(\vec v\in\mathbb R^n\\)</span>, pronounced "v in R n", means that <span class="math-inline">\\(\vec v\\)</span> is a vector with <span class="math-inline">\\(n\\)</span> components. Usually, <span class="math-inline">\\(v&#95;1,v&#95;2,\ldots,v&#95;n\\)</span> are placeholders for <span class="math-inline">\\(\vec v\\)</span>'s components.

-   A vector that results from scaling and adding one or more vectors is called a **linear combination** of the original vectors. For example, if <span class="math-inline">\\(\vec u=\begin{bmatrix}5\\\\1\end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec v=\begin{bmatrix}1\\\\7\end{bmatrix}\\)</span>, then <span class="math-inline">\\(2\vec u-3\vec v\\)</span> is a linear combination of <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>. It is the new vector

<div class="math-display">
$$
2\vec u-3\vec v
    =2\begin{bmatrix}5\\1\end{bmatrix}-3\begin{bmatrix}1\\7\end{bmatrix}
    =\begin{bmatrix}10-3\\2-21\end{bmatrix}
    =\begin{bmatrix}7\\-19\end{bmatrix}.
$$
</div>

-   For a vector <span class="math-inline">\\(\vec v\in\mathbb R^n\\)</span>, its **length**, **norm**, or **magnitude**, is

<div class="math-display">
$$
\lVert\vec v\rVert=\sqrt{v_1^2+v_2^2+\cdots+v_n^2}.
$$
</div>

 For the vectors above,

<div class="math-display">
$$
\lVert\vec u\rVert=\sqrt{5^2+1^2}=\sqrt{26},
    \qquad
    \lVert\vec v\rVert=\sqrt{1^2+7^2}=\sqrt{50}.
$$
</div>

-   The **dot product** of two nonzero vectors <span class="math-inline">\\(\vec u,\vec v\in\mathbb R^n\\)</span> can be computed in two ways:

-   Algebraic definition: <span class="math-inline">\\(\vec u\cdot\vec v=u&#95;1v&#95;1+u&#95;2v&#95;2+\cdots+u&#95;nv&#95;n\\)</span>.

-   Geometric definition: <span class="math-inline">\\(\vec u\cdot\vec v=\lVert\vec u\rVert\lVert\vec v\rVert\cos\theta\\)</span>, where <span class="math-inline">\\(\theta\\)</span> is the angle between the vectors.

   For the vectors above,

<div class="math-display">
$$
\vec u\cdot\vec v=\begin{bmatrix}5\\1\end{bmatrix}\cdot\begin{bmatrix}1\\7\end{bmatrix}=5(1)+1(7)=12.
$$
</div>

---

## Activity 1: Linear Combinations and Lengths

Let <span class="math-inline">\\(\vec u=\begin{bmatrix}3\\\\4\end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec v=\begin{bmatrix}-1\\\\-4\end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Let <span class="math-inline">\\(\vec w=-\vec u-\vec v\\)</span> and let <span class="math-inline">\\(\vec x=2\vec u+\vec v\\)</span>. Draw <span class="math-inline">\\(\vec u\\)</span>, <span class="math-inline">\\(\vec v\\)</span>, <span class="math-inline">\\(\vec w\\)</span>, and <span class="math-inline">\\(\vec x\\)</span> on the axes below, with each vector starting at the origin. Label each vector.

<details markdown="1"><summary>Solution</summary>

To find <span class="math-inline">\\(\vec w\\)</span> and <span class="math-inline">\\(\vec x\\)</span>, we'll scale the vectors and add their corresponding components:

<div class="math-display">
$$
\begin{align*}
\vec w &= -\vec u-\vec v
= -\begin{bmatrix}3\\4\end{bmatrix}-\begin{bmatrix}-1\\-4\end{bmatrix}
= \boxed{\begin{bmatrix}-2\\0\end{bmatrix}} \\
\vec x &= 2\vec u+\vec v
= 2\begin{bmatrix}3\\4\end{bmatrix}+\begin{bmatrix}-1\\-4\end{bmatrix}
= \boxed{\begin{bmatrix}5\\4\end{bmatrix}}
\end{align*}
$$
</div>

Each vector starts at the origin, so its components tell us where its tip goes. For instance, <span class="math-inline">\\(\vec w\\)</span> ends at <span class="math-inline">\\((-2,0)\\)</span>, which is 2 units to the left of the origin.

<div style="text-align: center;">
<img src="imgs/lab02-plot-01.png" alt="Vector diagram" class="assignment-vector-plot">
</div>
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Which of the following vectors is equal to <span class="math-inline">\\(5\vec e&#95;1-4\vec e&#95;2\\)</span>? Select one option. Recall that <span class="math-inline">\\(\vec e&#95;1=\begin{bmatrix}1\\\\0\end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec e&#95;2=\begin{bmatrix}0\\\\1\end{bmatrix}\\)</span> are the **standard basis vectors** in <span class="math-inline">\\(\mathbb R^2\\)</span>.

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(3\vec u-4\vec v\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(4\vec u+3\vec v\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(3\vec u+4\vec v\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(-3\vec u+4\vec v\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(4\vec u-3\vec v\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

**The third option, <span class="math-inline">\\(3\vec u+4\vec v\\)</span>.**

Since <span class="math-inline">\\(\vec e&#95;1\\)</span> moves us one unit horizontally and <span class="math-inline">\\(\vec e&#95;2\\)</span> moves us one unit vertically, the vector we're looking for is:

<div class="math-display">
$$
5\vec e_1-4\vec e_2=\begin{bmatrix}5\\-4\end{bmatrix}
$$
</div>

 The third option gives us exactly this vector:

<div class="math-display">
$$
3\vec u+4\vec v
=3\begin{bmatrix}3\\4\end{bmatrix}+4\begin{bmatrix}-1\\-4\end{bmatrix}
=\begin{bmatrix}9-4\\12-16\end{bmatrix}
=\boxed{\begin{bmatrix}5\\-4\end{bmatrix}}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Find the lengths of <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>.

<details markdown="1"><summary>Solution</summary>

To find a vector's length, we square its components, add them, and take the square root:

<div class="math-display">
$$
\begin{align*}
\lVert\vec u\rVert &= \sqrt{3^2+4^2}=\boxed{5} \\
\lVert\vec v\rVert &= \sqrt{(-1)^2+(-4)^2}=\boxed{\sqrt{17}}
\end{align*}
$$
</div>

Notice that the negative components of <span class="math-inline">\\(\vec v\\)</span> become positive when we square them. They tell us which way <span class="math-inline">\\(\vec v\\)</span> points, but its length is still positive.
</details>

</div>
</div>

</div>

---

## Activity 2: The Dot Product

For each pair of vectors below, draw them on the axes, compute their dot product, and select whether the angle between them is acute, right, or obtuse. Draw each vector from the origin.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\begin{bmatrix}8\\\\6\end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix}1\\\\0\end{bmatrix}\\)</span>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Acute</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Right</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Obtuse</span></div>

<details markdown="1"><summary>Solution</summary>

**Acute.** The dot product is:

<div class="math-display">
$$
8(1)+6(0)=\boxed{8}
$$
</div>

 Since it's positive, the angle is acute.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\begin{bmatrix}8\\\\6\end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix}-5\\\\0\end{bmatrix}\\)</span>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Acute</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Right</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Obtuse</span></div>

<details markdown="1"><summary>Solution</summary>

**Obtuse.** The dot product is:

<div class="math-display">
$$
8(-5)+6(0)=\boxed{-40}
$$
</div>

 Since it's negative, the angle is obtuse.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\begin{bmatrix}8\\\\6\end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix}6\\\\8\end{bmatrix}\\)</span>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Acute</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Right</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Obtuse</span></div>

<details markdown="1"><summary>Solution</summary>

**Acute.** The dot product is:

<div class="math-display">
$$
8(6)+6(8)=\boxed{96}
$$
</div>

 Since it's positive, the angle is acute.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\begin{bmatrix}8\\\\6\end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix}4\\\\7\end{bmatrix}\\)</span>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Acute</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Right</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Obtuse</span></div>

<details markdown="1"><summary>Solution</summary>

**Acute.** The dot product is:

<div class="math-display">
$$
8(4)+6(7)=\boxed{74}
$$
</div>

 Since it's positive, the angle is acute.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\begin{bmatrix}8\\\\6\end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix}-3\\\\4\end{bmatrix}\\)</span>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Acute</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Right</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Obtuse</span></div>

<details markdown="1"><summary>Solution</summary>

**Right.** The dot product is:

<div class="math-display">
$$
8(-3)+6(4)=\boxed{0}
$$
</div>

 Since it's zero, the vectors are orthogonal.
</details>

<details markdown="1"><summary>Solution</summary>

Each pair contains <span class="math-inline">\\(\begin{bmatrix}8\\\\6\end{bmatrix}\\)</span>, so we only need to draw that vector once. The labels below give the coordinates of each vector's tip.

<div style="text-align: center;">
<img src="imgs/lab02-plot-02.png" alt="Vector diagram" class="assignment-vector-plot">
</div>

Why does the sign of the dot product tell us about the angle? Recall that:

<div class="math-display">
$$
\vec u\cdot\vec v=\lVert\vec u\rVert\lVert\vec v\rVert\cos\theta
$$
</div>

 Both lengths are positive here, so the dot product has the same sign as <span class="math-inline">\\(\cos\theta\\)</span>. A positive dot product means the angle is acute, a negative dot product means it's obtuse, and a zero dot product means it's a right angle.
</details>

</div>
</div>

</div>

---

## Activity 3: Angles and Orthogonality

Suppose <span class="math-inline">\\(\vec u=\begin{bmatrix}5\\\\0\\\\-4\\\\1\end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec v=\begin{bmatrix}9\\\\1\\\\2\\\\3\end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find <span class="math-inline">\\(\vec u\cdot\vec v\\)</span>, <span class="math-inline">\\(\lVert\vec u\rVert\\)</span>, and <span class="math-inline">\\(\lVert\vec v\rVert\\)</span>.

<details markdown="1"><summary>Solution</summary>

For the dot product, we multiply corresponding components and add the results:

<div class="math-display">
$$
\vec u\cdot\vec v=5(9)+0(1)+(-4)(2)+1(3)=45-8+3=\boxed{40}
$$
</div>

 For each length, we square the components of that vector, add them, and take the square root:

<div class="math-display">
$$
\begin{align*}
\lVert\vec u\rVert &= \sqrt{5^2+0^2+(-4)^2+1^2}=\boxed{\sqrt{42}} \\
\lVert\vec v\rVert &= \sqrt{9^2+1^2+2^2+3^2}=\boxed{\sqrt{95}}
\end{align*}
$$
</div>

The calculations work just as they did in <span class="math-inline">\\(\mathbb R^2\\)</span>; we now have four components to work with.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Using the results of part **a)**, find the angle between <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>. Leave your answer in the form <span class="math-inline">\\(\cos^{-1}(\cdot)\\)</span>.

<details markdown="1"><summary>Solution</summary>

We know the dot product and both lengths from part **a)**. To find the angle, we'll substitute them into the geometric definition of the dot product and solve for <span class="math-inline">\\(\theta\\)</span>:

<div class="math-display">
$$
\begin{align*}
\vec u\cdot\vec v &= \lVert\vec u\rVert\lVert\vec v\rVert\cos\theta \\
40 &= \sqrt{42}\sqrt{95}\cos\theta \\
\cos\theta &= \frac{40}{\sqrt{42}\sqrt{95}} \\
\theta &= \boxed{\cos^{-1}\!\left(\frac{40}{\sqrt{42}\sqrt{95}}\right)}
\end{align*}
$$
</div>

Since the dot product is positive, this angle is acute, which agrees with what we saw in Activity 2.
</details>

Even though we cannot directly visualize these vectors in <span class="math-inline">\\(\mathbb R^4\\)</span>, the formula

<div class="math-display">
$$
\theta=\cos^{-1}\!\left(\frac{\vec u\cdot\vec v}{\lVert\vec u\rVert\lVert\vec v\rVert}\right)
$$
</div>

 **defines** the angle between them. Another term for the cosine of the angle between two nonzero vectors is their **cosine similarity**.

</div>
</div>

</div>

---

## Activity 4: Comparing Vectors

As we saw in the previous activity, the cosine similarity of two nonzero vectors is the cosine of the angle between them. It is one of the many ways we can measure how "different" two vectors are, by comparing their directions.

Suppose

<div class="math-display">
$$
\vec u=\begin{bmatrix}2\\1\\2\end{bmatrix}
\qquad\text{and}\qquad
\vec v=\begin{bmatrix}-2\\4\\4\end{bmatrix}.
$$
</div>

 Explore and rotate the vectors at [`desmos.com/3d/4wygwwruil`](https://www.desmos.com/3d/4wygwwruil).

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find the cosine similarity of <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>.

<details markdown="1"><summary>Solution</summary>

The cosine similarity is <span class="math-inline">\\(\boxed{\frac49}\\)</span>.

To find it, we'll divide the dot product by the product of the two lengths. We have:

<div class="math-display">
$$
\begin{align*}
\vec u\cdot\vec v &= 2(-2)+1(4)+2(4)=8 \\
\lVert\vec u\rVert &= \sqrt{2^2+1^2+2^2}=3 \\
\lVert\vec v\rVert &= \sqrt{(-2)^2+4^2+4^2}=6
\end{align*}
$$
</div>

So, their cosine similarity is:

<div class="math-display">
$$
\frac{\vec u\cdot\vec v}{\lVert\vec u\rVert\lVert\vec v\rVert}
=\frac{8}{3\cdot6}=\boxed{\frac49}
$$
</div>

 This is the cosine of the angle between the vectors. Since it's positive, the angle is acute.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Another way to measure how "different" two vectors are is to measure the distance between their tips when both vectors start at the origin. Find this distance for <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>, that is, <span class="math-inline">\\(\lVert\vec u-\vec v\rVert\\)</span>.

<details markdown="1"><summary>Solution</summary>

The distance is <span class="math-inline">\\(\boxed{\sqrt{29}}\\)</span>.

The vector <span class="math-inline">\\(\vec u-\vec v\\)</span> tells us how to get from the tip of <span class="math-inline">\\(\vec v\\)</span> to the tip of <span class="math-inline">\\(\vec u\\)</span>:

<div class="math-display">
$$
\vec u-\vec v
=\begin{bmatrix}2-(-2)\\1-4\\2-4\end{bmatrix}
=\begin{bmatrix}4\\-3\\-2\end{bmatrix}
$$
</div>

 Its length is the distance we're looking for:

<div class="math-display">
$$
\lVert\vec u-\vec v\rVert
=\sqrt{4^2+(-3)^2+(-2)^2}
=\boxed{\sqrt{29}}
$$
</div>

 We could also use <span class="math-inline">\\(\vec v-\vec u\\)</span>. That vector points in the opposite direction, but it has the same length.
</details>
</div>
</div>

</div>

{% endraw %}
