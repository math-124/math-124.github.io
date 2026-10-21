---
layout: page
title: "Lab 8: Inverses"
description: "Lab 8: Inverses activities."
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

# Lab 8: Inverses

**due** by the end of class on Wednesday, October 21, 2026

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab08/lab08.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab08/lab08-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
Each lab worksheet will contain several activities, most of which will involve writing math on paper, and some of which will involve running code in a Jupyter Notebook. To receive credit for today's lab, you must show your lab TA your work on this worksheet.

While you must get checked off by your lab TA **individually**, we encourage you to form groups with 1-2 other students to complete the activities together.
</div>

---

## Activities

- [Activity 1: A quick check](#activity-1-a-quick-check)
- [Activity 2: Undo the motion](#activity-2-undo-the-motion)
- [Activity 3: A formula for $2\times2$ inverses](#activity-3-a-formula-for-2times2-inverses)
- [Activity 4: Recover the input](#activity-4-recover-the-input)
- [Activity 5: Undo a sequence](#activity-5-undo-a-sequence)
- [Activity 6: Solving matrix equations](#activity-6-solving-matrix-equations)

---

**Review: Inverses.** For a square matrix <span class="math-inline">\\(A\\)</span>, an **inverse** is a matrix <span class="math-inline">\\(A^{-1}\\)</span> satisfying

<div class="math-display">
$$
A^{-1}A=AA^{-1}=I.
$$
</div>

 Thus <span class="math-inline">\\(A^{-1}(A\vec x)=\vec x\\)</span> for every input <span class="math-inline">\\(\vec x\\)</span>. A square matrix with an inverse is **invertible**; one without an inverse is **singular**.

---

## Activity 1: A quick check

Let <span class="math-inline">\\(D=\begin{bmatrix}-2&amp;0\\\\0&amp;3\end{bmatrix}\\)</span> and <span class="math-inline">\\(E=\begin{bmatrix}-1/2&amp;0\\\\0&amp;1/3\end{bmatrix}\\)</span>. Verify that <span class="math-inline">\\(E=D^{-1}\\)</span> by computing both products in the definition above. Explain geometrically how <span class="math-inline">\\(E\\)</span> undoes <span class="math-inline">\\(D\\)</span>.

<details markdown="1"><summary>Solution</summary>

Both products are the identity:

<div class="math-display">
$$
DE=\begin{bmatrix}(-2)(-1/2)&0\\0&3(1/3)\end{bmatrix}=I,
\qquad
ED=\begin{bmatrix}(-1/2)(-2)&0\\0&(1/3)3\end{bmatrix}=I.
$$
</div>

 So <span class="math-inline">\\(\boxed{E=D^{-1}}\\)</span>. The matrix <span class="math-inline">\\(D\\)</span> flips the sign of the horizontal coordinate and stretches it by a factor of <span class="math-inline">\\(2\\)</span>, and stretches the vertical coordinate by a factor of <span class="math-inline">\\(3\\)</span>. The matrix <span class="math-inline">\\(E\\)</span> flips the horizontal sign back and scales the coordinates by <span class="math-inline">\\(1/2\\)</span> and <span class="math-inline">\\(1/3\\)</span>, undoing both stretches.
</details>

---

## Activity 2: Undo the motion

Find the inverse of each matrix below **without** using the formula given in Activity 3. Instead, use geometry and/or your understanding of the given transformation. Verify your answers by multiplying.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
The matrix <span class="math-inline">\\(Q=\begin{bmatrix}0&amp;-1\\\\1&amp;0\end{bmatrix}\\)</span> rotates counterclockwise by <span class="math-inline">\\(90^\circ\\)</span>. Describe the inverse transformation and write <span class="math-inline">\\(Q^{-1}\\)</span>.

<details markdown="1"><summary>Solution</summary>

To undo a counterclockwise rotation by <span class="math-inline">\\(90^\circ\\)</span>, rotate clockwise by <span class="math-inline">\\(90^\circ\\)</span>. This sends <span class="math-inline">\\(\begin{bmatrix}x\\\\y\end{bmatrix}\\)</span> to <span class="math-inline">\\(\begin{bmatrix}y\\\\-x\end{bmatrix}\\)</span>, so

<div class="math-display">
$$
\boxed{Q^{-1}=\begin{bmatrix}0&1\\-1&0\end{bmatrix}}.
$$
</div>

 Checking both orders,

<div class="math-display">
$$
QQ^{-1}=\begin{bmatrix}0&-1\\1&0\end{bmatrix}\begin{bmatrix}0&1\\-1&0\end{bmatrix}=I,
\qquad
Q^{-1}Q=\begin{bmatrix}0&1\\-1&0\end{bmatrix}\begin{bmatrix}0&-1\\1&0\end{bmatrix}=I.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
The shear <span class="math-inline">\\(S=\begin{bmatrix}1&amp;2\\\\0&amp;1\end{bmatrix}\\)</span> sends <span class="math-inline">\\(\begin{bmatrix}x\\\\y\end{bmatrix}\\)</span> to <span class="math-inline">\\(\begin{bmatrix}x+2y\\\\y\end{bmatrix}\\)</span>. Explain how to recover the original coordinates from the output, and use this to find <span class="math-inline">\\(S^{-1}\\)</span>.

<details markdown="1"><summary>Solution</summary>

The second coordinate doesn't change. To recover the first coordinate, subtract twice the second coordinate from the first. In other words, the inverse sends <span class="math-inline">\\(\begin{bmatrix}u\\\\v\end{bmatrix}\\)</span> to <span class="math-inline">\\(\begin{bmatrix}u-2v\\\\v\end{bmatrix}\\)</span>, so

<div class="math-display">
$$
\boxed{S^{-1}=\begin{bmatrix}1&-2\\0&1\end{bmatrix}}.
$$
</div>

 Indeed,

<div class="math-display">
$$
SS^{-1}=\begin{bmatrix}1&2\\0&1\end{bmatrix}\begin{bmatrix}1&-2\\0&1\end{bmatrix}
=\begin{bmatrix}1&-2+2\\0&1\end{bmatrix}=I,
$$
</div>



<div class="math-display">
$$
S^{-1}S=\begin{bmatrix}1&-2\\0&1\end{bmatrix}\begin{bmatrix}1&2\\0&1\end{bmatrix}
=\begin{bmatrix}1&2-2\\0&1\end{bmatrix}=I.
$$
</div>

</details>

</div>
</div>

</div>

---

## Activity 3: A formula for <span class="math-inline">\\(2\times2\\)</span> inverses

For a <span class="math-inline">\\(2\times2\\)</span> matrix,

<div class="math-display">
$$
A=\begin{bmatrix}a&b\\c&d\end{bmatrix},\qquad
A^{-1}=\frac{1}{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}
\quad\text{given }ad-bc\ne0.
$$
</div>

 The number <span class="math-inline">\\(ad-bc\\)</span> is called the **determinant** of <span class="math-inline">\\(A\\)</span>. If <span class="math-inline">\\(ad-bc=0\\)</span>, then <span class="math-inline">\\(A\\)</span> has no inverse.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find the inverse of <span class="math-inline">\\(A=\begin{bmatrix}4&amp;-2\\\\3&amp;2\end{bmatrix}\\)</span>. Verify your result.

<details markdown="1"><summary>Solution</summary>

Here <span class="math-inline">\\(ad-bc=4(2)-(-2)(3)=14\\)</span>, so

<div class="math-display">
$$
\boxed{A^{-1}=\frac1{14}\begin{bmatrix}2&2\\-3&4\end{bmatrix}}.
$$
</div>

 Checking both products,

<div class="math-display">
$$
AA^{-1}=\frac1{14}\begin{bmatrix}8+6&8-8\\6-6&6+8\end{bmatrix}=I,
\qquad
A^{-1}A=\frac1{14}\begin{bmatrix}8+6&-4+4\\-12+12&6+8\end{bmatrix}=I.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
For which values of <span class="math-inline">\\(t\\)</span> is <span class="math-inline">\\(M=\begin{bmatrix}4&amp;-2\\\\3&amp;t\end{bmatrix}\\)</span> invertible? For the value of <span class="math-inline">\\(t\\)</span> that makes <span class="math-inline">\\(M\\)</span> singular, describe the span of its columns and explain why some output vectors cannot be reached.

<details markdown="1"><summary>Solution</summary>

The determinant is <span class="math-inline">\\(4t-(-2)(3)=4t+6\\)</span>. Thus, <span class="math-inline">\\(M\\)</span> is invertible exactly when

<div class="math-display">
$$
\boxed{t\ne-\frac32}.
$$
</div>

 When <span class="math-inline">\\(t=-3/2\\)</span>, the second column is <span class="math-inline">\\(-1/2\\)</span> times the first. Their span is therefore the line

<div class="math-display">
$$
\operatorname{span}\!\left(\begin{bmatrix}4\\3\end{bmatrix}\right).
$$
</div>

 Every output <span class="math-inline">\\(M\vec x\\)</span> is a linear combination of these columns, so it lies on this line. A vector outside the line, such as <span class="math-inline">\\(\begin{bmatrix}1\\\\0\end{bmatrix}\\)</span>, cannot be an output. There is no way to undo <span class="math-inline">\\(M\\)</span> on all of <span class="math-inline">\\(\mathbb R^2\\)</span>.
</details>

</div>
</div>

</div>

---

## Activity 4: Recover the input

Consider the equation

<div class="math-display">
$$
A\vec x=\vec b,
$$
</div>

 where

<div class="math-display">
$$
A=\begin{bmatrix}4&-2\\3&2\end{bmatrix},\qquad
\vec x=\begin{bmatrix}x_1\\x_2\end{bmatrix},\qquad
\vec b=\begin{bmatrix}6\\8\end{bmatrix}.
$$
</div>

 You found the inverse of <span class="math-inline">\\(A\\)</span> in Activity 3.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Write <span class="math-inline">\\(A\vec x=\vec b\\)</span> as a system of two equations in the two unknowns <span class="math-inline">\\(x&#95;1\\)</span> and <span class="math-inline">\\(x&#95;2\\)</span>. Then solve the system using <span class="math-inline">\\(A^{-1}\\)</span> and verify your solution.

<details markdown="1"><summary>Solution</summary>

Multiplying out <span class="math-inline">\\(A\vec x\\)</span> gives the system

<div class="math-display">
$$
\begin{aligned}
4x_1-2x_2&=6,\\
3x_1+2x_2&=8.
\end{aligned}
$$
</div>

 Multiplying both sides of <span class="math-inline">\\(A\vec x=\vec b\\)</span> on the left by <span class="math-inline">\\(A^{-1}\\)</span> gives <span class="math-inline">\\(\vec x=A^{-1}\vec b\\)</span>. Using our inverse from Activity 3,

<div class="math-display">
$$
\vec x=\frac1{14}\begin{bmatrix}2&2\\-3&4\end{bmatrix}\begin{bmatrix}6\\8\end{bmatrix}
=\frac1{14}\begin{bmatrix}12+16\\-18+32\end{bmatrix}
=\boxed{\begin{bmatrix}2\\1\end{bmatrix}}.
$$
</div>

 Checking in the original equations, <span class="math-inline">\\(4(2)-2(1)=6\\)</span> and <span class="math-inline">\\(3(2)+2(1)=8\\)</span>, as needed.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Suppose the first entry of <span class="math-inline">\\(\vec b\\)</span> increases by <span class="math-inline">\\(1\\)</span> while the second stays fixed. How do <span class="math-inline">\\(x&#95;1\\)</span> and <span class="math-inline">\\(x&#95;2\\)</span> change? Explain how your answer is encoded in a column of <span class="math-inline">\\(A^{-1}\\)</span> and why the change does not depend on the original entries of <span class="math-inline">\\(\vec b\\)</span>.

<details markdown="1"><summary>Solution</summary>

Increasing the first entry of <span class="math-inline">\\(\vec b\\)</span> by <span class="math-inline">\\(1\\)</span> adds <span class="math-inline">\\(\begin{bmatrix}1\\\\0\end{bmatrix}\\)</span> to <span class="math-inline">\\(\vec b\\)</span>. The new solution is

<div class="math-display">
$$
A^{-1}\!\left(\vec b+\begin{bmatrix}1\\0\end{bmatrix}\right)
=A^{-1}\vec b+A^{-1}\begin{bmatrix}1\\0\end{bmatrix}
=\vec x+\frac1{14}\begin{bmatrix}2\\-3\end{bmatrix}.
$$
</div>

 So <span class="math-inline">\\(\boxed{x&#95;1\text{ increases by }1/7}\\)</span> and <span class="math-inline">\\(\boxed{x&#95;2\text{ decreases by }3/14}\\)</span>. Multiplying by <span class="math-inline">\\(\begin{bmatrix}1\\\\0\end{bmatrix}\\)</span> picks out the first column of <span class="math-inline">\\(A^{-1}\\)</span>. The change depends only on this column and the change in <span class="math-inline">\\(\vec b\\)</span>, not on the original entries of <span class="math-inline">\\(\vec b\\)</span>.
</details>

</div>
</div>

</div>

---

## Activity 5: Undo a sequence

An image editor first stretches horizontally by a factor of <span class="math-inline">\\(2\\)</span>, then applies a horizontal shear:

<div class="math-display">
$$
D=\begin{bmatrix}2&0\\0&1\end{bmatrix},\qquad
S=\begin{bmatrix}1&1\\0&1\end{bmatrix}.
$$
</div>

 Find the combined matrix <span class="math-inline">\\(C\\)</span> and its inverse. Express <span class="math-inline">\\(C^{-1}\\)</span> as a product involving <span class="math-inline">\\(D^{-1}\\)</span> and <span class="math-inline">\\(S^{-1}\\)</span>, and explain the order in terms of undoing the two edits.

<details markdown="1"><summary>Solution</summary>

Stretching first and then shearing gives <span class="math-inline">\\(S(D\vec x)\\)</span>, so

<div class="math-display">
$$
C=SD=\begin{bmatrix}1&1\\0&1\end{bmatrix}\begin{bmatrix}2&0\\0&1\end{bmatrix}
=\boxed{\begin{bmatrix}2&1\\0&1\end{bmatrix}}.
$$
</div>

 To undo the edits, first undo the shear, then undo the stretch. Since the matrix on the right acts first,

<div class="math-display">
$$
C^{-1}=D^{-1}S^{-1}
=\begin{bmatrix}1/2&0\\0&1\end{bmatrix}\begin{bmatrix}1&-1\\0&1\end{bmatrix}
=\boxed{\begin{bmatrix}1/2&-1/2\\0&1\end{bmatrix}}.
$$
</div>

 This order also works algebraically:

<div class="math-display">
$$
(D^{-1}S^{-1})(SD)=D^{-1}(S^{-1}S)D=I,
$$
</div>



<div class="math-display">
$$
(SD)(D^{-1}S^{-1})=S(DD^{-1})S^{-1}=I.
$$
</div>

</details>

---

## Activity 6: Solving matrix equations

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Suppose <span class="math-inline">\\(A\\)</span> is a square matrix satisfying

<div class="math-display">
$$
A^4-3A^3+A^2+3A+5I=0,
$$
</div>

 where <span class="math-inline">\\(I\\)</span> and <span class="math-inline">\\(0\\)</span> are the identity and zero matrices of the same shape as <span class="math-inline">\\(A\\)</span>. Find an expression for <span class="math-inline">\\(A^{-1}\\)</span> in terms of powers of <span class="math-inline">\\(A\\)</span>, and justify why it is an inverse.

<details markdown="1"><summary>Solution</summary>

Move the constant term to the other side and factor out <span class="math-inline">\\(A\\)</span>:

<div class="math-display">
$$
A^4-3A^3+A^2+3A=-5I,
\qquad
A(A^3-3A^2+A+3I)=-5I.
$$
</div>

 Dividing by <span class="math-inline">\\(-5\\)</span> gives

<div class="math-display">
$$
A\left[-\frac15(A^3-3A^2+A+3I)\right]=I.
$$
</div>

 We can also factor <span class="math-inline">\\(A\\)</span> on the right, because multiplying powers of <span class="math-inline">\\(A\\)</span> in either order gives the same result. Thus the proposed inverse multiplies with <span class="math-inline">\\(A\\)</span> to give <span class="math-inline">\\(I\\)</span> in both orders, and

<div class="math-display">
$$
\boxed{A^{-1}=-\frac15A^3+\frac35A^2-\frac15A-\frac35I}.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Suppose <span class="math-inline">\\(A=BC\\)</span>, where

<div class="math-display">
$$
A=\begin{bmatrix}5&-3\\10&1\end{bmatrix},\qquad
B=\begin{bmatrix}2&1\\1&3\end{bmatrix}.
$$
</div>

 Find <span class="math-inline">\\(C\\)</span>.

<details markdown="1"><summary>Solution</summary>

Multiply both sides of <span class="math-inline">\\(A=BC\\)</span> on the left by <span class="math-inline">\\(B^{-1}\\)</span>:

<div class="math-display">
$$
B^{-1}A=B^{-1}BC=C.
$$
</div>

 Since <span class="math-inline">\\(2(3)-1(1)=5\\)</span>,

<div class="math-display">
$$
B^{-1}=\frac15\begin{bmatrix}3&-1\\-1&2\end{bmatrix}.
$$
</div>

 Therefore,

<div class="math-display">
$$
C=\frac15\begin{bmatrix}3&-1\\-1&2\end{bmatrix}\begin{bmatrix}5&-3\\10&1\end{bmatrix}
=\frac15\begin{bmatrix}5&-10\\15&5\end{bmatrix}
=\boxed{\begin{bmatrix}1&-2\\3&1\end{bmatrix}}.
$$
</div>

 As a check,

<div class="math-display">
$$
BC=\begin{bmatrix}2&1\\1&3\end{bmatrix}\begin{bmatrix}1&-2\\3&1\end{bmatrix}
=\begin{bmatrix}5&-3\\10&1\end{bmatrix}=A.
$$
</div>

</details>
</div>
</div>

</div>

{% endraw %}
