---
layout: page
title: "Lab 9: LU Decomposition and Permutation Matrices"
description: "Lab 9: LU Decomposition and Permutation Matrices activities."
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

# Lab 9: LU Decomposition and Permutation Matrices

**due** by the end of class on Wednesday, October 28, 2026

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab09/lab09.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab09/lab09-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
Each lab worksheet will contain several activities, most of which will involve writing math on paper, and some of which will involve running code in a Jupyter Notebook. Lab activities are meant to last an hour, and the second hour of lab is dedicated to starting the homework assignment. To receive credit for a lab, you must show your lab TA your work on both the lab worksheet and homework assignment.

While you must get checked off by your lab TA **individually**, we encourage you to form groups with 1-2 other students to complete the activities together.
</div>

---

## Activities

- [Activity 1: Reordering a three by three matrix](#activity-1-reordering-a-three-by-three-matrix)
- [Activity 2: A general two by two matrix](#activity-2-a-general-two-by-two-matrix)
- [Activity 3: Permutation matrices](#activity-3-permutation-matrices)

---

**How has the course content since fall break felt to you?**

Circle one.

<img src="imgs/mood-1.png" alt="image" style="width: 1.25cm; max-width: 100%;"> <img src="imgs/mood-2.png" alt="image" style="width: 1.25cm; max-width: 100%;"> <img src="imgs/mood-3.png" alt="image" style="width: 1.25cm; max-width: 100%;"> <img src="imgs/mood-4.png" alt="image" style="width: 1.25cm; max-width: 100%;"> <img src="imgs/mood-5.png" alt="image" style="width: 1.25cm; max-width: 100%;">

---

{: .yellow }
> **Do you have any concerns about the class that you would like to share?**

## Activity 1: Reordering a three by three matrix

Consider <span class="math-inline">\\(A=\begin{bmatrix}3&amp;-3&amp;6\\\\6&amp;-6&amp;16\\\\-3&amp;5&amp;-3\end{bmatrix}\\)</span>. Throughout, use ones on the diagonal of <span class="math-inline">\\(L\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Attempt to find an LU factorization without reordering the rows. Find the first row of <span class="math-inline">\\(U\\)</span>, then the first column of <span class="math-inline">\\(L\\)</span>, then the second row of <span class="math-inline">\\(U\\)</span>. At which step do you get stuck? Write the equation that makes it impossible to continue.

<details markdown="1"><summary>Solution</summary>

Write the required shapes:

<div class="math-display">
$$
L=\begin{bmatrix}1&0&0\\\ell_{21}&1&0\\\ell_{31}&\ell_{32}&1\end{bmatrix},\qquad
U=\begin{bmatrix}u_{11}&u_{12}&u_{13}\\0&u_{22}&u_{23}\\0&0&u_{33}\end{bmatrix}.
$$
</div>

 **First, find the first row of <span class="math-inline">\\(U\\)</span>.** It must equal the first row of <span class="math-inline">\\(A\\)</span>, so <span class="math-inline">\\(u&#95;{11}=3\\)</span>, <span class="math-inline">\\(u&#95;{12}=-3\\)</span>, and <span class="math-inline">\\(u&#95;{13}=6\\)</span>.

**Next, find the first column of <span class="math-inline">\\(L\\)</span>.** Matching entries gives

<div class="math-display">
$$
3\ell_{21}=6,\qquad 3\ell_{31}=-3
\quad\Longrightarrow\quad \ell_{21}=2,\quad\ell_{31}=-1.
$$
</div>

 **Then, find the second row of <span class="math-inline">\\(U\\)</span>.** We need

<div class="math-display">
$$
2(-3)+u_{22}=-6,\qquad 2(6)+u_{23}=16,
$$
</div>

 so <span class="math-inline">\\(u&#95;{22}=0\\)</span> and <span class="math-inline">\\(u&#95;{23}=4\\)</span>.

We get stuck when finding <span class="math-inline">\\(\ell&#95;{32}\\)</span>. Entry <span class="math-inline">\\((3,2)\\)</span> would require

<div class="math-display">
$$
(-1)(-3)+\ell_{32}(0)=5,
\quad\text{or}\quad \boxed{3=5.}
$$
</div>

 No choice of <span class="math-inline">\\(\ell&#95;{32}\\)</span> works, so there is no LU factorization in this row order.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Choose two rows to swap so that the reordered matrix has an LU factorization. Write the reordered matrix, then restart the calculation and find its factors <span class="math-inline">\\(L\\)</span> and <span class="math-inline">\\(U\\)</span>.

<details markdown="1"><summary>Solution</summary>

Swap rows 2 and 3. The reordered matrix is

<div class="math-display">
$$
\begin{bmatrix}3&-3&6\\-3&5&-3\\6&-6&16\end{bmatrix}.
$$
</div>

 The first row of <span class="math-inline">\\(U\\)</span> is still <span class="math-inline">\\(\begin{bmatrix}3&amp;-3&amp;6\end{bmatrix}\\)</span>. Matching the first column now gives <span class="math-inline">\\(\ell&#95;{21}=-1\\)</span> and <span class="math-inline">\\(\ell&#95;{31}=2\\)</span>.

Matching the second row gives

<div class="math-display">
$$
(-1)(-3)+u_{22}=5,\qquad (-1)(6)+u_{23}=-3,
$$
</div>

 so <span class="math-inline">\\(u&#95;{22}=2\\)</span> and <span class="math-inline">\\(u&#95;{23}=3\\)</span>. Next, entry <span class="math-inline">\\((3,2)\\)</span> gives

<div class="math-display">
$$
2(-3)+2\ell_{32}=-6\quad\Longrightarrow\quad\ell_{32}=0.
$$
</div>

 Finally, entry <span class="math-inline">\\((3,3)\\)</span> gives <span class="math-inline">\\(2(6)+0(3)+u&#95;{33}=16\\)</span>, so <span class="math-inline">\\(u&#95;{33}=4\\)</span>. Thus

<div class="math-display">
$$
\boxed{L=\begin{bmatrix}1&0&0\\-1&1&0\\2&0&1\end{bmatrix},\qquad
U=\begin{bmatrix}3&-3&6\\0&2&3\\0&0&4\end{bmatrix}.}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Multiply your factors to check your answer. Does their product equal <span class="math-inline">\\(A\\)</span> or the reordered matrix?

<details markdown="1"><summary>Solution</summary>

Multiplying gives

<div class="math-display">
$$
LU=\begin{bmatrix}3&-3&6\\-3&3+2&-6+3\\6&-6&12+4\end{bmatrix}
=\begin{bmatrix}3&-3&6\\-3&5&-3\\6&-6&16\end{bmatrix}.
$$
</div>

 The product equals the **reordered matrix**, not the original matrix <span class="math-inline">\\(A\\)</span>.
</details>

</div>
</div>

</div>

---

## Activity 2: A general two by two matrix

Let <span class="math-inline">\\(B\\)</span> be invertible, and write

<div class="math-display">
$$
B=\begin{bmatrix}a&b\\c&d\end{bmatrix},\qquad
L=\begin{bmatrix}1&0\\\ell&1\end{bmatrix},\qquad
U=\begin{bmatrix}p&q\\0&r\end{bmatrix}.
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Match entries in <span class="math-inline">\\(B=LU\\)</span>: first find the first row of <span class="math-inline">\\(U\\)</span>, then the first column of <span class="math-inline">\\(L\\)</span>, then the second row of <span class="math-inline">\\(U\\)</span>. At which step might you get stuck, and why?

<details markdown="1"><summary>Solution</summary>

Start by multiplying the required shapes:

<div class="math-display">
$$
LU=\begin{bmatrix}p&q\\\ell p&\ell q+r\end{bmatrix}.
$$
</div>

 The first row gives <span class="math-inline">\\(p=a\\)</span> and <span class="math-inline">\\(q=b\\)</span>. Matching the first column then requires <span class="math-inline">\\(\ell a=c\\)</span>. If <span class="math-inline">\\(a\ne0\\)</span>, this gives <span class="math-inline">\\(\ell=c/a\\)</span>. The remaining entry gives

<div class="math-display">
$$
\ell b+r=d\quad\Longrightarrow\quad r=d-\frac{cb}{a}.
$$
</div>

 We might get stuck when finding <span class="math-inline">\\(\ell\\)</span>: if <span class="math-inline">\\(a=0\\)</span>, we cannot divide by <span class="math-inline">\\(a\\)</span>. Since <span class="math-inline">\\(B\\)</span> is invertible, <span class="math-inline">\\(ad-bc\ne0\\)</span>. When <span class="math-inline">\\(a=0\\)</span>, this says <span class="math-inline">\\(-bc\ne0\\)</span>, so <span class="math-inline">\\(c\ne0\\)</span>. The equation <span class="math-inline">\\(\ell\cdot0=c\\)</span> is then impossible.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
For which invertible matrices does this procedure work without reordering the rows? Give formulas for <span class="math-inline">\\(L\\)</span> and <span class="math-inline">\\(U\\)</span>. Explain why both diagonal entries of <span class="math-inline">\\(U\\)</span> are nonzero and why the factors are uniquely determined.

<details markdown="1"><summary>Solution</summary>

The procedure works exactly when <span class="math-inline">\\(\boxed{a\ne0}\\)</span>. In this case,

<div class="math-display">
$$
\boxed{L=\begin{bmatrix}1&0\\c/a&1\end{bmatrix},\qquad
U=\begin{bmatrix}a&b\\0&d-cb/a\end{bmatrix}.}
$$
</div>

 The first diagonal entry of <span class="math-inline">\\(U\\)</span> is <span class="math-inline">\\(a\ne0\\)</span>. The second is

<div class="math-display">
$$
d-\frac{cb}{a}=\frac{ad-bc}{a}\ne0,
$$
</div>

 because <span class="math-inline">\\(B\\)</span> is invertible. Every entry was forced: first <span class="math-inline">\\(p\\)</span> and <span class="math-inline">\\(q\\)</span>, then <span class="math-inline">\\(\ell\\)</span>, then <span class="math-inline">\\(r\\)</span>. Therefore, with ones on the diagonal of <span class="math-inline">\\(L\\)</span>, the factors are uniquely determined.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
If the procedure gets stuck, explain why swapping the rows allows you to continue. Use the invertibility of <span class="math-inline">\\(B\\)</span> to justify your answer, and find the factors for the reordered matrix.

<details markdown="1"><summary>Solution</summary>

The procedure gets stuck when <span class="math-inline">\\(a=0\\)</span>. Invertibility gives <span class="math-inline">\\(-bc\ne0\\)</span>, so both <span class="math-inline">\\(b\\)</span> and <span class="math-inline">\\(c\\)</span> are nonzero. Swapping the rows gives

<div class="math-display">
$$
\begin{bmatrix}c&d\\0&b\end{bmatrix}.
$$
</div>

 This matrix is already upper triangular, so

<div class="math-display">
$$
\boxed{L=\begin{bmatrix}1&0\\0&1\end{bmatrix},\qquad
U=\begin{bmatrix}c&d\\0&b\end{bmatrix}.}
$$
</div>

 Both diagonal entries of <span class="math-inline">\\(U\\)</span> are nonzero. The swap makes the top-left entry nonzero, so we can divide by it when finding the entries of <span class="math-inline">\\(L\\)</span>.
</details>

</div>
</div>

</div>

---

## Activity 3: Permutation matrices

A **permutation matrix** is a square matrix with exactly one <span class="math-inline">\\(1\\)</span> in each row and each column, and zeros everywhere else.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find a <span class="math-inline">\\(3\times3\\)</span> permutation matrix <span class="math-inline">\\(P\\)</span> such that left multiplication by <span class="math-inline">\\(P\\)</span> moves the first row of a matrix to the second row, the second row to the third row, and the third row to the first row.

<details markdown="1"><summary>Solution</summary>

The new row order must be old row 3, old row 1, old row 2. Reorder the rows of the identity matrix in that order:

<div class="math-display">
$$
\boxed{P=\begin{bmatrix}0&0&1\\1&0&0\\0&1&0\end{bmatrix}.}
$$
</div>

 For any matrix <span class="math-inline">\\(M\\)</span> with three rows, the rows of <span class="math-inline">\\(PM\\)</span> are <span class="math-inline">\\(M\\)</span>'s third, first, and second rows. Thus each original row moves to the requested position.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Write down the inverses of the following matrices. Are their inverses also permutation matrices?

<div class="math-display">
$$
Q=\begin{bmatrix}0&1&0\\1&0&0\\0&0&1\end{bmatrix},\qquad
R=\begin{bmatrix}0&0&1\\1&0&0\\0&1&0\end{bmatrix}.
$$
</div>

<details markdown="1"><summary>Solution</summary>

**Undo <span class="math-inline">\\(Q\\)</span>.** The matrix <span class="math-inline">\\(Q\\)</span> swaps rows 1 and 2. Swapping those rows again restores the original order, so

<div class="math-display">
$$
\boxed{Q^{-1}=Q=\begin{bmatrix}0&1&0\\1&0&0\\0&0&1\end{bmatrix}.}
$$
</div>

 **Undo <span class="math-inline">\\(R\\)</span>.** The matrix <span class="math-inline">\\(R\\)</span> changes the row order from <span class="math-inline">\\((1,2,3)\\)</span> to <span class="math-inline">\\((3,1,2)\\)</span>. To undo this, select the current rows in order <span class="math-inline">\\((2,3,1)\\)</span>, giving

<div class="math-display">
$$
\boxed{R^{-1}=\begin{bmatrix}0&1&0\\0&0&1\\1&0&0\end{bmatrix}.}
$$
</div>

 Each inverse has exactly one 1 in each row and each column, with zeros elsewhere. **Both inverses are permutation matrices.** Applying each reordering and its inverse, in either order, restores every row.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Consider the three permutation matrices <span class="math-inline">\\(P&#95;1,P&#95;2,P&#95;3\\)</span> and the matrix <span class="math-inline">\\(B\\)</span>:

<div class="math-display">
$$
P_1=\begin{bmatrix}0&1&0\\1&0&0\\0&0&1\end{bmatrix},\qquad
P_2=\begin{bmatrix}1&0&0\\0&0&1\\0&1&0\end{bmatrix},
$$
</div>



<div class="math-display">
$$
P_3=\begin{bmatrix}0&0&1\\1&0&0\\0&1&0\end{bmatrix},\qquad
B=\begin{bmatrix}2&-1&4\\0&3&5\\-2&6&1\end{bmatrix}.
$$
</div>

 Find each product by observing how the entries are reordered, without explicitly carrying out matrix multiplication. Write each answer as a <span class="math-inline">\\(3\times3\\)</span> matrix.

<div class="math-display">
$$
\text{(i) }P_1P_2\qquad
\text{(ii) }P_2B\qquad
\text{(iii) }P_3B\qquad
\text{(iv) }P_1P_2B\qquad
\text{(v) }BP_1
$$
</div>

<details markdown="1"><summary>Solution</summary>

Left multiplication by a permutation matrix reorders rows; right multiplication reorders columns. For a sequence of row reorderings, the rightmost permutation matrix acts first.

**(i)** <span class="math-inline">\\(P&#95;1\\)</span> swaps the first two rows of <span class="math-inline">\\(P&#95;2\\)</span>, so

<div class="math-display">
$$
\boxed{P_1P_2=\begin{bmatrix}0&0&1\\1&0&0\\0&1&0\end{bmatrix}=P_3.}
$$
</div>

 **(ii)** <span class="math-inline">\\(P&#95;2\\)</span> swaps the last two rows of <span class="math-inline">\\(B\\)</span>:

<div class="math-display">
$$
\boxed{P_2B=\begin{bmatrix}2&-1&4\\-2&6&1\\0&3&5\end{bmatrix}.}
$$
</div>

 **(iii)** <span class="math-inline">\\(P&#95;3\\)</span> puts the rows of <span class="math-inline">\\(B\\)</span> in order <span class="math-inline">\\((3,1,2)\\)</span>:

<div class="math-display">
$$
\boxed{P_3B=\begin{bmatrix}-2&6&1\\2&-1&4\\0&3&5\end{bmatrix}.}
$$
</div>

 **(iv)** First <span class="math-inline">\\(P&#95;2\\)</span> swaps rows 2 and 3, then <span class="math-inline">\\(P&#95;1\\)</span> swaps the current rows 1 and 2. The resulting order is <span class="math-inline">\\((3,1,2)\\)</span>:

<div class="math-display">
$$
\boxed{P_1P_2B=\begin{bmatrix}-2&6&1\\2&-1&4\\0&3&5\end{bmatrix}.}
$$
</div>

 This agrees with part (i), since <span class="math-inline">\\(P&#95;1P&#95;2=P&#95;3\\)</span>.

**(v)** Multiplying <span class="math-inline">\\(B\\)</span> on the right by <span class="math-inline">\\(P&#95;1\\)</span> swaps its first two **columns, not its rows**, so

<div class="math-display">
$$
\boxed{BP_1=\begin{bmatrix}-1&2&4\\3&0&5\\6&-2&1\end{bmatrix}.}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
Return to your factorization in Activity 1, where

<div class="math-display">
$$
A=\begin{bmatrix}3&-3&6\\6&-6&16\\-3&5&-3\end{bmatrix}.
$$
</div>

 Write your answer as <span class="math-inline">\\(PA=LU\\)</span> for a permutation matrix <span class="math-inline">\\(P\\)</span>, and then as <span class="math-inline">\\(A=P'LU\\)</span> for a permutation matrix <span class="math-inline">\\(P'\\)</span>. Write all matrices explicitly in both equations.

<details markdown="1"><summary>Solution</summary>

Our factorization swaps rows 2 and 3, so take

<div class="math-display">
$$
P=\begin{bmatrix}1&0&0\\0&0&1\\0&1&0\end{bmatrix}.
$$
</div>

 With the factors from Activity 1, <span class="math-inline">\\(PA=LU\\)</span> becomes

<div class="math-display">
$$
\boxed{
\begin{bmatrix}1&0&0\\0&0&1\\0&1&0\end{bmatrix}
\begin{bmatrix}3&-3&6\\6&-6&16\\-3&5&-3\end{bmatrix}
=
\begin{bmatrix}1&0&0\\-1&1&0\\2&0&1\end{bmatrix}
\begin{bmatrix}3&-3&6\\0&2&3\\0&0&4\end{bmatrix}.}
$$
</div>

 To recover <span class="math-inline">\\(A\\)</span>, multiply on the left by <span class="math-inline">\\(P^{-1}\\)</span>. A row swap undoes itself, so <span class="math-inline">\\(P'=P^{-1}=P\\)</span>. Thus <span class="math-inline">\\(A=P'LU\\)</span> is

<div class="math-display">
$$
\boxed{
\begin{bmatrix}3&-3&6\\6&-6&16\\-3&5&-3\end{bmatrix}
=
\begin{bmatrix}1&0&0\\0&0&1\\0&1&0\end{bmatrix}
\begin{bmatrix}1&0&0\\-1&1&0\\2&0&1\end{bmatrix}
\begin{bmatrix}3&-3&6\\0&2&3\\0&0&4\end{bmatrix}.}
$$
</div>

</details>
</div>
</div>

</div>

{% endraw %}
