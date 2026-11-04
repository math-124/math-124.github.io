---
layout: page
title: "Lab 10: Column Space"
description: "Lab 10: Column Space activities."
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
.sketch-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1rem;margin:1.5rem 0}.sketch-card{text-align:center}.sketch-card p{min-height:6rem}.preview-controls{display:flex;gap:.6rem;flex-wrap:wrap;margin:1rem 0}@media(max-width:600px){.sketch-grid{grid-template-columns:1fr}}

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

# Lab 10: Column Space

**due** by the end of class on Wednesday, November 4, 2026

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab10/lab10.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab10/lab10-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
Each lab worksheet will contain several activities, most of which will involve writing math on paper, and some of which will involve running code in a Jupyter Notebook. Lab activities are meant to last an hour, and the second hour of lab is dedicated to starting the homework assignment. To receive credit for a lab, you must show your lab TA your work on both the lab worksheet and homework assignment.

While you must get checked off by your lab TA **individually**, we encourage you to form groups with 1-2 other students to complete the activities together.
</div>

---


## Activities

- [Activity 1: Column space basics](#activity-1-column-space-basics)
- [Activity 2: Two independent directions](#activity-2-two-independent-directions)
- [Activity 3: Columns and invertibility](#activity-3-columns-and-invertibility)
- [Activity 4: Subspaces](#activity-4-subspaces)

---

## Activity 1: Column space basics

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Fill in the blank: The **column space** of a matrix <span class="math-inline">\\(A\\)</span>, written <span class="math-inline">\\(\operatorname{colsp}(A)\\)</span>, is the set of all <span class="answer-blank" style="min-width:6rem"></span> <span class="answer-blank" style="min-width:9rem"></span>s of <span class="math-inline">\\(A\\)</span>'s <span class="answer-blank" style="min-width:7rem"></span>.

<details markdown="1"><summary>Solution</summary>

The column space of <span class="math-inline">\\(A\\)</span> is the set of all **linear combinations** of <span class="math-inline">\\(A\\)</span>'s **columns**. The three blanks are **linear**, **combination**, and **columns**.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Let <span class="math-inline">\\(P\\)</span> be the plane

<div class="math-display">
$$
5x-y+3z=0.
$$
</div>

 Which of the following matrices have a column space equal to <span class="math-inline">\\(P\\)</span>? <span class="math-inline">\\(\boxed{\text{Circle}}\\)</span> all that apply.

<div class="math-display">
$$
A=\begin{bmatrix}1&5&0\\0&3&1\end{bmatrix},\quad
B=\begin{bmatrix}1&0\\5&3\\0&1\end{bmatrix},\quad
C=\begin{bmatrix}1&0&1\\5&3&8\\0&1&1\end{bmatrix},\quad
D=\begin{bmatrix}1&2&-1\\5&10&-5\\0&0&0\end{bmatrix},\quad
E=\begin{bmatrix}1&0\\5&1\\0&0\end{bmatrix}.
$$
</div>

<details markdown="1"><summary>Solution</summary>

**Circle <span class="math-inline">\\(B\\)</span> and <span class="math-inline">\\(C\\)</span>.**

-   **<span class="math-inline">\\(A\\)</span>: No.** Its columns have two entries, so its column space is a subset of <span class="math-inline">\\(\mathbb{R}^2\\)</span>. It cannot be the plane <span class="math-inline">\\(P\\)</span> in <span class="math-inline">\\(\mathbb{R}^3\\)</span>.

-   **<span class="math-inline">\\(B\\)</span>: Yes.** Multiplying by an arbitrary input gives

<div class="math-display">
$$
B\begin{bmatrix}a\\b\end{bmatrix}
    =\begin{bmatrix}a\\5a+3b\\b\end{bmatrix}.
$$
</div>

 These outputs satisfy <span class="math-inline">\\(5x-y+3z=0\\)</span>. Conversely, any vector on the plane has <span class="math-inline">\\(y=5x+3z\\)</span>, so we can produce it using the input <span class="math-inline">\\(\begin{bmatrix}x\\\\z\end{bmatrix}\\)</span>. Thus the set of possible outputs is exactly <span class="math-inline">\\(P\\)</span>.

-   **<span class="math-inline">\\(C\\)</span>: Yes.** The new column is on <span class="math-inline">\\(P\\)</span>, so its inclusion does not expand <span class="math-inline">\\(\operatorname{colsp}(B)\\)</span> beyond the vectors that were already in <span class="math-inline">\\(\operatorname{colsp}(B)\\)</span>. Thus <span class="math-inline">\\(\operatorname{colsp}(C)=\operatorname{colsp}(B)=P\\)</span>.

-   **<span class="math-inline">\\(D\\)</span>: No.** Every column is a multiple of <span class="math-inline">\\(\begin{bmatrix}1\\\\5\\\\0\end{bmatrix}\\)</span>, so its column space is only a line. For instance, <span class="math-inline">\\(\begin{bmatrix}0\\\\3\\\\1\end{bmatrix}\\)</span> is on <span class="math-inline">\\(P\\)</span> but cannot be produced by <span class="math-inline">\\(D\\)</span>, since every output of <span class="math-inline">\\(D\\)</span> has third entry zero.

-   **<span class="math-inline">\\(E\\)</span>: No.** Its second column, <span class="math-inline">\\(\begin{bmatrix}0\\\\1\\\\0\end{bmatrix}\\)</span>, is a possible output of <span class="math-inline">\\(E\\)</span>, but it is not on <span class="math-inline">\\(P\\)</span>: <span class="math-inline">\\(5(0)-1+3(0)=-1\ne0\\)</span>. Having one column on the plane is not enough.
</details>

</div>
</div>

</div>

---

## Activity 2: Two independent directions

Consider the matrix

<div class="math-display">
$$
A=\begin{bmatrix}1&2&0&-1\\0&0&1&3\\0&0&0&0\\0&0&0&0\end{bmatrix}.
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Fill in the blank: <span class="math-inline">\\(\operatorname{colsp}(A)\\)</span> is a <span class="answer-blank"></span> in <span class="math-inline">\\(\mathbb{R}^{\boxed{\phantom{4}}}\\)</span>.

<details markdown="1"><summary>Solution</summary>

**A plane in <span class="math-inline">\\(\mathbb{R}^4\\)</span>.** For an arbitrary input,

<div class="math-display">
$$
A\begin{bmatrix}a\\b\\c\\d\end{bmatrix}
=\begin{bmatrix}a+2b-d\\c+3d\\0\\0\end{bmatrix}
=(a+2b-d)\begin{bmatrix}1\\0\\0\\0\end{bmatrix}
+(c+3d)\begin{bmatrix}0\\1\\0\\0\end{bmatrix}.
$$
</div>

 Every output has last two entries zero. Setting <span class="math-inline">\\(b=d=0\\)</span> lets us choose the first two entries freely through <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(c\\)</span>. Thus the possible outputs form a plane in <span class="math-inline">\\(\mathbb{R}^4\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Find two vectors <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> such that

<ol class="assignment-enumeration" markdown="1">
<li markdown="1">
<div class="assignment-enumeration-label">1.</div>
<div class="assignment-enumeration-content" markdown="1">

<span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> are linearly independent.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">2.</div>
<div class="assignment-enumeration-content" markdown="1">

<span class="math-inline">\\(\operatorname{span}(\vec u,\vec v)=\operatorname{colsp}(A)\\)</span>.

</div></li>
</ol>

As we will see tomorrow, your <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> are a **basis** for <span class="math-inline">\\(\operatorname{colsp}(A)\\)</span>.

<details markdown="1"><summary>Solution</summary>

Choose the first and third columns:

<div class="math-display">
$$
\boxed{\vec u=\begin{bmatrix}1\\0\\0\\0\end{bmatrix},\qquad
\vec v=\begin{bmatrix}0\\1\\0\\0\end{bmatrix}.}
$$
</div>

 Neither vector is a scalar multiple of the other, so they are linearly independent.

Column 2 is <span class="math-inline">\\(2\vec u\\)</span>, and column 4 is <span class="math-inline">\\(-\vec u+3\vec v\\)</span>. These are redundant columns, so removing them does not change the column space. Thus <span class="math-inline">\\(\operatorname{span}(\vec u,\vec v)=\operatorname{colsp}(A)\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Find two **different** <span class="math-inline">\\(4\times2\\)</span> matrices whose column space is equal to <span class="math-inline">\\(\operatorname{colsp}(A)\\)</span>.

<details markdown="1"><summary>Solution</summary>

One possible pair is

<div class="math-display">
$$
\boxed{A_1=\begin{bmatrix}1&0\\0&1\\0&0\\0&0\end{bmatrix},\qquad
A_2=\begin{bmatrix}1&1\\0&1\\0&0\\0&0\end{bmatrix}.}
$$
</div>

 The columns of <span class="math-inline">\\(A&#95;1\\)</span> are <span class="math-inline">\\(\vec u,\vec v\\)</span> from part (b), and those of <span class="math-inline">\\(A&#95;2\\)</span> are <span class="math-inline">\\(\vec u,\vec u+\vec v\\)</span>. Both pairs span the same plane, since <span class="math-inline">\\(\vec v=(\vec u+\vec v)-\vec u\\)</span>.
</details>

</div>
</div>

</div>

---

## Activity 3: Columns and invertibility

**Definition: Linearly independent.** The collection of vectors <span class="math-inline">\\(\vec v&#95;1,\vec v&#95;2,\ldots,\vec v&#95;d\\)</span> is **linearly independent** when none of the vectors in the collection can be written as a linear combination of the other vectors in the collection.

**Fact**: A square matrix is invertible if and only if its columns are linearly independent.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
For each matrix, determine whether or not it is invertible.

<div class="math-display">
$$
A=\begin{bmatrix}1&0&1\\0&1&1\\1&1&2\end{bmatrix},\qquad
B=\begin{bmatrix}1&2&0\\0&1&3\\0&0&2\end{bmatrix},\qquad
C=\begin{bmatrix}1&0&0\\2&0&1\\0&0&1\end{bmatrix}.
$$
</div>

<details markdown="1"><summary>Solution</summary>

-   **<span class="math-inline">\\(A\\)</span> is not invertible.** Its third column is the sum of its first two columns. This redundancy means that different inputs can give the same output. For instance,

<div class="math-display">
$$
A\begin{bmatrix}1\\1\\0\end{bmatrix}
    =\begin{bmatrix}1\\1\\2\end{bmatrix}
    =A\begin{bmatrix}0\\0\\1\end{bmatrix}.
$$
</div>

 We cannot uniquely recover the input from the output.

-   **<span class="math-inline">\\(B\\)</span> is invertible.** It is already upper triangular, with nonzero diagonal entries. For any proposed output <span class="math-inline">\\(\begin{bmatrix}b&#95;1\\\\b&#95;2\\\\b&#95;3\end{bmatrix}\\)</span>, the input must satisfy

<div class="math-display">
$$
2x_3=b_3,\qquad x_2+3x_3=b_2,\qquad x_1+2x_2=b_1.
$$
</div>

 Solve from the bottom row upward: first <span class="math-inline">\\(x&#95;3\\)</span> is determined, then <span class="math-inline">\\(x&#95;2\\)</span>, then <span class="math-inline">\\(x&#95;1\\)</span>. Every output has exactly one input, so <span class="math-inline">\\(B\\)</span> is invertible.

-   **<span class="math-inline">\\(C\\)</span> is not invertible.** Its second column is <span class="math-inline">\\(\vec0\\)</span>, which is a linear combination of the other columns with both coefficients zero. Changing the second entry of an input does not change the output, so the input cannot be recovered uniquely.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
For which real values of <span class="math-inline">\\(t\\)</span> is <span class="math-inline">\\(D\\)</span> invertible?

<div class="math-display">
$$
D=\begin{bmatrix}2&0&0&0\\0&-1&0&0\\0&0&3&0\\0&0&0&t\end{bmatrix}.
$$
</div>

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(\boxed{t\ne0}\\)</span>. When <span class="math-inline">\\(t\ne0\\)</span>, the matrix multiplies each input coordinate by a nonzero number. We can undo this by dividing the four output coordinates by <span class="math-inline">\\(2,-1,3,t\\)</span>, respectively.

When <span class="math-inline">\\(t=0\\)</span>, the fourth column is <span class="math-inline">\\(\vec0\\)</span>. Changing the fourth input coordinate does not change the output, so the matrix is not invertible.
</details>

</div>
</div>

</div>

---

## Activity 4: Subspaces

A **subspace** generalizes a line or plane through the origin: it is a set of vectors that contains <span class="math-inline">\\(\vec0\\)</span> and is "flat" in some sense. Formally, a subset <span class="math-inline">\\(S\\)</span> of <span class="math-inline">\\(\mathbb{R}^n\\)</span> is a subspace of <span class="math-inline">\\(\mathbb{R}^n\\)</span> if:

<ol class="assignment-enumeration" markdown="1">
<li markdown="1">
<div class="assignment-enumeration-label">1.</div>
<div class="assignment-enumeration-content" markdown="1">

<span class="math-inline">\\(\vec0\in S\\)</span>.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">2.</div>
<div class="assignment-enumeration-content" markdown="1">

If <span class="math-inline">\\(\vec u,\vec v\in S\\)</span>, then <span class="math-inline">\\(\vec u+\vec v\in S\\)</span>. We say <span class="math-inline">\\(S\\)</span> is **closed** under addition.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">3.</div>
<div class="assignment-enumeration-content" markdown="1">

If <span class="math-inline">\\(\vec u\in S\\)</span> and <span class="math-inline">\\(c\in\mathbb{R}\\)</span>, then <span class="math-inline">\\(c\vec u\in S\\)</span>. We say <span class="math-inline">\\(S\\)</span> is **closed** under scalar multiplication.

</div></li>
</ol>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Sketch each set below. Each is a subset of <span class="math-inline">\\(\mathbb{R}^2\\)</span>, but only some are sub<strong>spaces</strong> of <span class="math-inline">\\(\mathbb{R}^2\\)</span>. Which and why?

<div class="sketch-grid"><div class="sketch-card"><p><strong>(i)</strong> Top right quadrant<br>including its boundary<br>\(x\ge0,\ y\ge0\)</p><svg viewBox="0 0 280 280" role="img" aria-label="Coordinate plane" style="width:100%;max-width:260px"><path d="M 20 20 V 260 M 20 20 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 40 20 V 260 M 20 40 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 60 20 V 260 M 20 60 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 80 20 V 260 M 20 80 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 100 20 V 260 M 20 100 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 120 20 V 260 M 20 120 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 140 20 V 260 M 20 140 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 160 20 V 260 M 20 160 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 180 20 V 260 M 20 180 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 200 20 V 260 M 20 200 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 220 20 V 260 M 20 220 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 240 20 V 260 M 20 240 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 260 20 V 260 M 20 260 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 20 140 H 260 M 140 20 V 260" stroke="currentColor" stroke-width="1.2"/><g fill="currentColor" font-size="12" font-family="sans-serif"><text x="264" y="145">x</text><text x="137" y="14">y</text><text x="34" y="156">−5</text><text x="237" y="156">5</text><text x="122" y="44">5</text><text x="117" y="245">−5</text></g></svg></div><div class="sketch-card"><p><strong>(ii)</strong> The line<br>\(y=2x\)</p><svg viewBox="0 0 280 280" role="img" aria-label="Coordinate plane" style="width:100%;max-width:260px"><path d="M 20 20 V 260 M 20 20 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 40 20 V 260 M 20 40 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 60 20 V 260 M 20 60 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 80 20 V 260 M 20 80 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 100 20 V 260 M 20 100 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 120 20 V 260 M 20 120 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 140 20 V 260 M 20 140 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 160 20 V 260 M 20 160 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 180 20 V 260 M 20 180 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 200 20 V 260 M 20 200 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 220 20 V 260 M 20 220 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 240 20 V 260 M 20 240 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 260 20 V 260 M 20 260 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 20 140 H 260 M 140 20 V 260" stroke="currentColor" stroke-width="1.2"/><g fill="currentColor" font-size="12" font-family="sans-serif"><text x="264" y="145">x</text><text x="137" y="14">y</text><text x="34" y="156">−5</text><text x="237" y="156">5</text><text x="122" y="44">5</text><text x="117" y="245">−5</text></g></svg></div><div class="sketch-card"><p><strong>(iii)</strong> The line<br>\(y=3x-4\)</p><svg viewBox="0 0 280 280" role="img" aria-label="Coordinate plane" style="width:100%;max-width:260px"><path d="M 20 20 V 260 M 20 20 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 40 20 V 260 M 20 40 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 60 20 V 260 M 20 60 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 80 20 V 260 M 20 80 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 100 20 V 260 M 20 100 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 120 20 V 260 M 20 120 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 140 20 V 260 M 20 140 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 160 20 V 260 M 20 160 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 180 20 V 260 M 20 180 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 200 20 V 260 M 20 200 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 220 20 V 260 M 20 220 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 240 20 V 260 M 20 240 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 260 20 V 260 M 20 260 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 20 140 H 260 M 140 20 V 260" stroke="currentColor" stroke-width="1.2"/><g fill="currentColor" font-size="12" font-family="sans-serif"><text x="264" y="145">x</text><text x="137" y="14">y</text><text x="34" y="156">−5</text><text x="237" y="156">5</text><text x="122" y="44">5</text><text x="117" y="245">−5</text></g></svg></div></div>

<details markdown="1"><summary>Solution</summary>

<div class="sketch-grid"><div class="sketch-card"><p><strong>(i)</strong> Top right quadrant<br>including its boundary<br>\(x\ge0,\ y\ge0\)</p><svg viewBox="0 0 280 280" role="img" aria-label="Coordinate plane" style="width:100%;max-width:260px"><rect x="140" y="20" width="120" height="120" fill="#1f5fbf" fill-opacity=".15"/><path d="M 20 20 V 260 M 20 20 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 40 20 V 260 M 20 40 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 60 20 V 260 M 20 60 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 80 20 V 260 M 20 80 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 100 20 V 260 M 20 100 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 120 20 V 260 M 20 120 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 140 20 V 260 M 20 140 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 160 20 V 260 M 20 160 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 180 20 V 260 M 20 180 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 200 20 V 260 M 20 200 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 220 20 V 260 M 20 220 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 240 20 V 260 M 20 240 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 260 20 V 260 M 20 260 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 20 140 H 260 M 140 20 V 260" stroke="currentColor" stroke-width="1.2"/><g fill="currentColor" font-size="12" font-family="sans-serif"><text x="264" y="145">x</text><text x="137" y="14">y</text><text x="34" y="156">−5</text><text x="237" y="156">5</text><text x="122" y="44">5</text><text x="117" y="245">−5</text></g></svg></div><div class="sketch-card"><p><strong>(ii)</strong> The line<br>\(y=2x\)</p><svg viewBox="0 0 280 280" role="img" aria-label="Coordinate plane" style="width:100%;max-width:260px"><path d="M 20 20 V 260 M 20 20 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 40 20 V 260 M 20 40 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 60 20 V 260 M 20 60 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 80 20 V 260 M 20 80 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 100 20 V 260 M 20 100 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 120 20 V 260 M 20 120 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 140 20 V 260 M 20 140 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 160 20 V 260 M 20 160 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 180 20 V 260 M 20 180 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 200 20 V 260 M 20 200 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 220 20 V 260 M 20 220 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 240 20 V 260 M 20 240 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 260 20 V 260 M 20 260 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 80 260 L 200 20" stroke="#1f5fbf" stroke-width="2.5"/><path d="M 20 140 H 260 M 140 20 V 260" stroke="currentColor" stroke-width="1.2"/><g fill="currentColor" font-size="12" font-family="sans-serif"><text x="264" y="145">x</text><text x="137" y="14">y</text><text x="34" y="156">−5</text><text x="237" y="156">5</text><text x="122" y="44">5</text><text x="117" y="245">−5</text></g></svg></div><div class="sketch-card"><p><strong>(iii)</strong> The line<br>\(y=3x-4\)</p><svg viewBox="0 0 280 280" role="img" aria-label="Coordinate plane" style="width:100%;max-width:260px"><path d="M 20 20 V 260 M 20 20 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 40 20 V 260 M 20 40 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 60 20 V 260 M 20 60 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 80 20 V 260 M 20 80 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 100 20 V 260 M 20 100 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 120 20 V 260 M 20 120 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 140 20 V 260 M 20 140 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 160 20 V 260 M 20 160 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 180 20 V 260 M 20 180 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 200 20 V 260 M 20 200 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 220 20 V 260 M 20 220 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 240 20 V 260 M 20 240 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 260 20 V 260 M 20 260 H 260" stroke="#e2e5ea" stroke-width="1"/><path d="M 126.6667 260 L 206.6667 20" stroke="#1f5fbf" stroke-width="2.5"/><path d="M 20 140 H 260 M 140 20 V 260" stroke="currentColor" stroke-width="1.2"/><g fill="currentColor" font-size="12" font-family="sans-serif"><text x="264" y="145">x</text><text x="137" y="14">y</text><text x="34" y="156">−5</text><text x="237" y="156">5</text><text x="122" y="44">5</text><text x="117" y="245">−5</text></g></svg></div></div>



-   **(i) Not a subspace.** It is not closed under scalar multiplication. For example,

<div class="math-display">
$$
-1\begin{bmatrix}1\\1\end{bmatrix}=\begin{bmatrix}-1\\-1\end{bmatrix},
$$
</div>

 which is outside the quadrant, even though <span class="math-inline">\\(\begin{bmatrix}1\\\\1\end{bmatrix}\\)</span> is inside it.

-   **(ii) A subspace.** The line contains <span class="math-inline">\\(\vec0\\)</span>. If <span class="math-inline">\\(\vec u=\begin{bmatrix}a\\\\2a\end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec v=\begin{bmatrix}b\\\\2b\end{bmatrix}\\)</span> are on the line, then

<div class="math-display">
$$
\vec u+\vec v=\begin{bmatrix}a+b\\2(a+b)\end{bmatrix},\qquad
    c\vec u=\begin{bmatrix}ca\\2ca\end{bmatrix}
$$
</div>

 are also on the line. It is closed under addition and scalar multiplication, so all three conditions hold.

-   **(iii) Not a subspace.** The line does not contain <span class="math-inline">\\(\vec0\\)</span>, since <span class="math-inline">\\(0\ne3(0)-4\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Now consider the set

<div class="math-display">
$$
W=\left\{\begin{bmatrix}a\\b\\a+b\end{bmatrix}:a,b\in\mathbb{R}\right\}\subseteq\mathbb{R}^3.
$$
</div>

 Find two linearly independent vectors <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> such that <span class="math-inline">\\(\operatorname{span}(\vec u,\vec v)=W\\)</span>.

<details markdown="1"><summary>Solution</summary>

One possible pair is

<div class="math-display">
$$
\boxed{\vec u=\begin{bmatrix}1\\0\\1\end{bmatrix},\qquad
\vec v=\begin{bmatrix}0\\1\\1\end{bmatrix}.}
$$
</div>

 Neither vector is a scalar multiple of the other, so they are linearly independent. Also,

<div class="math-display">
$$
a\vec u+b\vec v=\begin{bmatrix}a\\b\\a+b\end{bmatrix}.
$$
</div>

 Every vector in <span class="math-inline">\\(W\\)</span> can be written this way, and every such linear combination belongs to <span class="math-inline">\\(W\\)</span>. Thus <span class="math-inline">\\(\operatorname{span}(\vec u,\vec v)=W\\)</span>.
</details>
</div>
</div>

</div>

{% endraw %}
