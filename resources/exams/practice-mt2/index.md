---
layout: page
title: "Practice Midterm 2"
description: "Practice Midterm 2 problems."
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
.word-choice { margin: 0.85rem 0; }
.word-choice .mc-square { margin-right: 0.35rem; }
</style>

# Practice Midterm 2

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/exams/practice-mt2/practice-mt2.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/exams/practice-mt2/practice-mt2-solutions.pdf" target="_blank">Solutions PDF ✅</a>
<a class="btn btn-info assignment-pdf-button" href="https://www.youtube.com/playlist?list=PLWQsSvehReUk" target="_blank" rel="noopener">Video Walkthroughs 🎥</a>
</div>

*This page is meant to give you quick access to problems and their solutions. Refer to the original exam PDF, linked above, for test-taking instructions and formatting. Note that we’ve kept the problem text identical, which is why you may see things like “write your answer in the box below” despite there not being a box on this page.*


---

## Problems

- [Problem 1](#problem-1-8-pts)
- [Problem 2](#problem-2-10-pts)
- [Problem 3](#problem-3-10-pts)
- [Problem 4](#problem-4-13-pts)
- [Problem 5](#problem-5-16-pts)
- [Problem 6](#problem-6-16-pts)
- [Problem 7](#problem-7-11-pts)
- [Problem 8](#problem-8-16-pts)

---

<h2 id="problem-1-8-pts" markdown="span">Problem 1 (8 pts) <a class="btn btn-info assignment-pdf-button problem-video-button" href="https://youtu.be/QUz1Sc0KBvY" target="_blank" rel="noopener" aria-label="Walkthrough video for Problem 1">🎥 Walkthrough</a></h2>

Let <span class="math-inline">\\(c\\)</span> be a real constant, and let 

<div class="math-display">
$$
A=\begin{bmatrix}4&-2\\-3&5\\6&1\end{bmatrix},\qquad
B=\begin{bmatrix}7&3&-4\\2&c&5\end{bmatrix}.
$$
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">

(4 pts) Give the shape of each expression (e.g. <span class="math-inline">\\(5\times3\\)</span>), or write "undefined."

<div class="math-display">
$$
AB\qquad BA\qquad A+B\qquad A(BA)
$$
</div>

<details markdown="1"><summary>Solution</summary>

The shape of <span class="math-inline">\\(A\\)</span> is <span class="math-inline">\\(3\times2\\)</span>, and the shape of <span class="math-inline">\\(B\\)</span> is <span class="math-inline">\\(2\times3\\)</span>. Therefore, 

<div class="math-display">
$$
\boxed{AB:\ 3\times3,\qquad BA:\ 2\times2,\qquad A+B:\ \text{undefined},\qquad A(BA):\ 3\times2.}
$$
</div>

 For a product, the inner dimensions must agree, and the outer dimensions give its shape. Addition requires identical shapes.

</details>

</div>
</div>


<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">

(4 pts) Suppose the second column of <span class="math-inline">\\(AB\\)</span> is 

<div class="math-display">
$$
\begin{bmatrix}20\\-29\\14\end{bmatrix}.
$$
</div>

 Find the value of <span class="math-inline">\\(c\\)</span>.

<details markdown="1"><summary>Solution</summary>

The second column of <span class="math-inline">\\(AB\\)</span> is <span class="math-inline">\\(A\\)</span> times the second column of <span class="math-inline">\\(B\\)</span>: 

<div class="math-display">
$$
A\begin{bmatrix}3\\c\end{bmatrix}
=3\begin{bmatrix}4\\-3\\6\end{bmatrix}+c\begin{bmatrix}-2\\5\\1\end{bmatrix}
=\begin{bmatrix}12-2c\\-9+5c\\18+c\end{bmatrix}.
$$
</div>

 The first entry gives <span class="math-inline">\\(12-2c=20\\)</span>, so <span class="math-inline">\\(\boxed{c=-4}\\)</span>. This also gives <span class="math-inline">\\(-9+5(-4)=-29\\)</span> and <span class="math-inline">\\(18+(-4)=14\\)</span>, as required.

</details>

</div>
</div>


---

<h2 id="problem-2-10-pts" markdown="span">Problem 2 (10 pts) <a class="btn btn-info assignment-pdf-button problem-video-button" href="https://youtu.be/IjBUKvubtS8" target="_blank" rel="noopener" aria-label="Walkthrough video for Problem 2">🎥 Walkthrough</a></h2>



<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">

(6 pts) Let <span class="math-inline">\\(T:\mathbb R^3\to\mathbb R^2\\)</span> be a linear transformation, and suppose 

<div class="math-display">
$$
T\!\left(\begin{bmatrix}2\\-1\\4\end{bmatrix}\right)=\begin{bmatrix}6\\-4\end{bmatrix},\qquad
T\!\left(\begin{bmatrix}-3\\5\\2\end{bmatrix}\right)=\begin{bmatrix}-5\\7\end{bmatrix}.
$$
</div>

 **i)** (1 pt) What is the shape of the matrix corresponding to <span class="math-inline">\\(T\\)</span>, i.e., of the matrix <span class="math-inline">\\(A\\)</span> where <span class="math-inline">\\(T(\vec x)=A\vec x\\)</span>?

Shape:

**ii)** (5 pts) Find <span class="math-inline">\\(T\left(\begin{bmatrix}-4\\\\9\\\\8\end{bmatrix}\right)\\)</span> without finding the matrix of <span class="math-inline">\\(T\\)</span>.

<details markdown="1"><summary>Solution</summary>

**i)** The domain is <span class="math-inline">\\(\mathbb R^3\\)</span> and the codomain is <span class="math-inline">\\(\mathbb R^2\\)</span>, so the matrix has shape <span class="math-inline">\\(\boxed{2\times3}\\)</span>.

**ii)** Recall that a linear transformation preserves addition and scalar multiplication: for all vectors <span class="math-inline">\\(\vec u,\vec v\\)</span> in its domain and all scalars <span class="math-inline">\\(c\\)</span>,

<div class="math-display">
$$
T(\vec u+\vec v)=T(\vec u)+T(\vec v),\qquad T(c\vec u)=cT(\vec u).
$$
</div>

 Because we know <span class="math-inline">\\(T\\)</span> at two inputs, we look for a linear combination of those inputs that equals the requested input. The same coefficients will then combine their outputs. Observe that

<div class="math-display">
$$
\begin{bmatrix}-4\\9\\8\end{bmatrix}
=\begin{bmatrix}2\\-1\\4\end{bmatrix}+2\begin{bmatrix}-3\\5\\2\end{bmatrix}.
$$
</div>

 Using the fact that <span class="math-inline">\\(T\\)</span> is a linear transformation, 

<div class="math-display">
$$
T\!\left(\begin{bmatrix}-4\\9\\8\end{bmatrix}\right)
=\begin{bmatrix}6\\-4\end{bmatrix}+2\begin{bmatrix}-5\\7\end{bmatrix}
=\boxed{\begin{bmatrix}-4\\10\end{bmatrix}}.
$$
</div>

</details>

</div>
</div>


<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">

(4 pts) Which of the following transformations from <span class="math-inline">\\(\mathbb R^2\\)</span> to <span class="math-inline">\\(\mathbb R^2\\)</span> are linear? **Select all that apply.**

<div class="word-choice" markdown="1">

<span class="mc-square" aria-hidden="true"></span> Rotate <span class="math-inline">\\(30^\circ\\)</span> clockwise about the origin, then add <span class="math-inline">\\(1\\)</span> to the horizontal component.

</div>

<div class="word-choice" markdown="1">

<span class="mc-square" aria-hidden="true"></span> Reflect across the line <span class="math-inline">\\(y=-2x\\)</span>, then multiply the vertical component by <span class="math-inline">\\(4\\)</span>.

</div>

<div class="word-choice" markdown="1">

<span class="mc-square" aria-hidden="true"></span> Project orthogonally onto the line <span class="math-inline">\\(y=3x\\)</span>.

</div>

<div class="word-choice" markdown="1">

<span class="mc-square" aria-hidden="true"></span> Replace the vertical component by its square, leaving the horizontal component unchanged.

</div>

<details markdown="1"><summary>Solution</summary>

**Select the second and third transformations.**

-   The first is not linear: it sends <span class="math-inline">\\(\vec0\\)</span> to <span class="math-inline">\\(\begin{bmatrix}1\\\\0\end{bmatrix}\\)</span>.

-   The second is linear: reflection across a line through the origin is linear, and multiplying the vertical component by <span class="math-inline">\\(4\\)</span> is multiplication by <span class="math-inline">\\(\begin{bmatrix}1&amp;0\\\\0&amp;4\end{bmatrix}\\)</span>. A composition of linear transformations is linear.

-   The third is linear: projection onto a line through the origin is a linear transformation.

-   The fourth is not linear. If <span class="math-inline">\\(R\left(\begin{bmatrix}x\\\\y\end{bmatrix}\right)=\begin{bmatrix}x\\\\y^2\end{bmatrix}\\)</span>, then <span class="math-inline">\\(R\left(2\begin{bmatrix}0\\\\1\end{bmatrix}\right)=\begin{bmatrix}0\\\\4\end{bmatrix}\\)</span>, whereas <span class="math-inline">\\(2R\left(\begin{bmatrix}0\\\\1\end{bmatrix}\right)=\begin{bmatrix}0\\\\2\end{bmatrix}\\)</span>.

</details>

</div>
</div>


---

<h2 id="problem-3-10-pts" markdown="span">Problem 3 (10 pts) <a class="btn btn-info assignment-pdf-button problem-video-button" href="https://youtu.be/t41Q_LIlh5Q" target="_blank" rel="noopener" aria-label="Walkthrough video for Problem 3">🎥 Walkthrough</a></h2>



<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">

(6 pts) Find the <span class="math-inline">\\(2\times2\\)</span> matrix <span class="math-inline">\\(P\\)</span> that projects each vector in <span class="math-inline">\\(\mathbb R^2\\)</span> onto the line spanned by <span class="math-inline">\\(\begin{bmatrix}2\\\\5\end{bmatrix}\\)</span>.

<details markdown="1"><summary>Solution</summary>

Let <span class="math-inline">\\(\vec v=\begin{bmatrix}2\\\\5\end{bmatrix}\\)</span>. The projection of <span class="math-inline">\\(\vec x\\)</span> onto its span is 

<div class="math-display">
$$
\frac{\vec v\cdot\vec x}{\vec v\cdot\vec v}\vec v
=\frac{2x_1+5x_2}{29}\begin{bmatrix}2\\5\end{bmatrix}
=\frac1{29}\begin{bmatrix}4x_1+10x_2\\10x_1+25x_2\end{bmatrix}.
$$
</div>

 Thus 

<div class="math-display">
$$
\boxed{P=\frac1{29}\begin{bmatrix}4&10\\10&25\end{bmatrix}.}
$$
</div>

</details>

</div>
</div>


<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">

(4 pts) The diagram shows <span class="math-inline">\\(T(\vec e&#95;1)\\)</span> and <span class="math-inline">\\(T(\vec e&#95;2)\\)</span> for a linear transformation <span class="math-inline">\\(T:\mathbb R^2\to\mathbb R^2\\)</span>, where <span class="math-inline">\\(\vec e&#95;1=\begin{bmatrix}1\\\\0\end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec e&#95;2=\begin{bmatrix}0\\\\1\end{bmatrix}\\)</span>. Find the matrix <span class="math-inline">\\(B\\)</span> corresponding to <span class="math-inline">\\(T\\)</span>.

<img class="assignment-vector-plot" src="transformation.png" width="560" alt="Coordinate diagram: T(e1) points from the origin to (4, 1), and T(e2) points from the origin to (-2, 3).">

<details markdown="1"><summary>Solution</summary>

In general, if <span class="math-inline">\\(T(\vec x)=A\vec x\\)</span>, then

<div class="math-display">
$$
T(\vec e_1)=A\vec e_1=A\begin{bmatrix}1\\0\end{bmatrix}
=\text{first column of }A.
$$
</div>

 Multiplication by <span class="math-inline">\\(\begin{bmatrix}1\\\\0\end{bmatrix}\\)</span> takes one copy of the first column and zero copies of the second. Similarly,

<div class="math-display">
$$
T(\vec e_2)=A\vec e_2=A\begin{bmatrix}0\\1\end{bmatrix}
=\text{second column of }A.
$$
</div>

 Here the matrix is called <span class="math-inline">\\(B\\)</span>. The diagram gives <span class="math-inline">\\(T(\vec e&#95;1)=\begin{bmatrix}4\\\\1\end{bmatrix}\\)</span> and <span class="math-inline">\\(T(\vec e&#95;2)=\begin{bmatrix}-2\\\\3\end{bmatrix}\\)</span>, so placing these outputs in the first and second columns gives

<div class="math-display">
$$
\boxed{B=\begin{bmatrix}4&-2\\1&3\end{bmatrix}.}
$$
</div>

</details>

</div>
</div>


---

<h2 id="problem-4-13-pts" markdown="span">Problem 4 (13 pts) <a class="btn btn-info assignment-pdf-button problem-video-button" href="https://youtu.be/WYO4hZ_p3AU" target="_blank" rel="noopener" aria-label="Walkthrough video for Problem 4">🎥 Walkthrough</a></h2>



<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">

(4 pts) An invertible <span class="math-inline">\\(3\times3\\)</span> matrix <span class="math-inline">\\(A\\)</span> satisfies 

<div class="math-display">
$$
A\begin{bmatrix}4\\-3\\2\end{bmatrix}=\begin{bmatrix}1\\0\\0\end{bmatrix},\qquad
A\begin{bmatrix}-2\\5\\1\end{bmatrix}=\begin{bmatrix}0\\1\\0\end{bmatrix},\qquad
A\begin{bmatrix}3\\1\\4\end{bmatrix}=\begin{bmatrix}0\\0\\1\end{bmatrix}.
$$
</div>

 Find <span class="math-inline">\\(A^{-1}\\)</span> without first finding <span class="math-inline">\\(A\\)</span>. Explain how you found your answer.

<details markdown="1"><summary>Solution</summary>

Multiplying each given equation by <span class="math-inline">\\(A^{-1}\\)</span> tells us where the matrix <span class="math-inline">\\(A^{-1}\\)</span> sends the standard basis vectors <span class="math-inline">\\(\vec e&#95;1\\)</span>, <span class="math-inline">\\(\vec e&#95;2\\)</span>, and <span class="math-inline">\\(\vec e&#95;3\\)</span>. For example, <span class="math-inline">\\(A^{-1}\vec e&#95;1=\begin{bmatrix}4\\\\-3\\\\2\end{bmatrix}\\)</span>.

These three outputs are the columns of <span class="math-inline">\\(A^{-1}\\)</span>! 

<div class="math-display">
$$
\boxed{A^{-1}=\begin{bmatrix}4&-2&3\\-3&5&1\\2&1&4\end{bmatrix}.}
$$
</div>

 Equivalently, multiplying <span class="math-inline">\\(A\\)</span> by this matrix produces <span class="math-inline">\\(I&#95;3\\)</span>, since the three resulting columns are <span class="math-inline">\\(\vec e&#95;1,\vec e&#95;2,\vec e&#95;3\\)</span>.

</details>

</div>
</div>


<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">

(4 pts) Find <span class="math-inline">\\(B^{-1}\\)</span>, where 

<div class="math-display">
$$
B=\begin{bmatrix}5&4\\6&8\end{bmatrix}.
$$
</div>

<details markdown="1"><summary>Solution</summary>

Using the two-by-two inverse formula, 

<div class="math-display">
$$
B^{-1}=\frac1{5(8)-4(6)}\begin{bmatrix}8&-4\\-6&5\end{bmatrix}
=\boxed{\frac1{16}\begin{bmatrix}8&-4\\-6&5\end{bmatrix}.}
$$
</div>

 The denominator is nonzero, so the inverse exists.

</details>

</div>
</div>


<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">

(5 pts) An invertible matrix <span class="math-inline">\\(C\\)</span> has inverse 

<div class="math-display">
$$
C^{-1}=\begin{bmatrix}3&-2\\4&-1\end{bmatrix}.
$$
</div>

 Solve for <span class="math-inline">\\(\vec x\\)</span>: 

<div class="math-display">
$$
C\left(4\vec x+\begin{bmatrix}5\\-4\end{bmatrix}\right)=\begin{bmatrix}7\\4\end{bmatrix}.
$$
</div>

<details markdown="1"><summary>Solution</summary>

Multiply both sides by <span class="math-inline">\\(C^{-1}\\)</span>: 

<div class="math-display">
$$
4\vec x+\begin{bmatrix}5\\-4\end{bmatrix}
=\begin{bmatrix}3&-2\\4&-1\end{bmatrix}\begin{bmatrix}7\\4\end{bmatrix}
=\begin{bmatrix}13\\24\end{bmatrix}.
$$
</div>

 Consequently, 

<div class="math-display">
$$
4\vec x=\begin{bmatrix}8\\28\end{bmatrix},\qquad
\boxed{\vec x=\begin{bmatrix}2\\7\end{bmatrix}.}
$$
</div>

</details>

</div>
</div>


---

<h2 id="problem-5-16-pts" markdown="span">Problem 5 (16 pts) <a class="btn btn-info assignment-pdf-button problem-video-button" href="https://youtu.be/mzH1JRxcl-s" target="_blank" rel="noopener" aria-label="Walkthrough video for Problem 5">🎥 Walkthrough</a></h2>



<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">

(8 pts) Find a scalar <span class="math-inline">\\(k\\)</span> and matrices <span class="math-inline">\\(P\\)</span>, <span class="math-inline">\\(L\\)</span>, and <span class="math-inline">\\(U\\)</span> such that <span class="math-inline">\\(PA=LU\\)</span>, where 

<div class="math-display">
$$
A=\begin{bmatrix}0&3&-4\\4&-2&6\\-4&8&k\end{bmatrix},\qquad U=\begin{bmatrix}4&a&b\\0&3&c\\0&0&5\end{bmatrix}.
$$
</div>

 Here, <span class="math-inline">\\(P\\)</span> is a permutation matrix, and <span class="math-inline">\\(L\\)</span> is lower triangular with ones on its diagonal. Write all entries of <span class="math-inline">\\(P\\)</span>, <span class="math-inline">\\(L\\)</span>, and <span class="math-inline">\\(U\\)</span> in the labeled boxes.

<details markdown="1"><summary>Solution</summary>

The first row of <span class="math-inline">\\(LU\\)</span> equals the first row of <span class="math-inline">\\(U\\)</span>. Its first entry is <span class="math-inline">\\(4\\)</span>, so put the second row of <span class="math-inline">\\(A\\)</span> first. Choose 

<div class="math-display">
$$
P=\begin{bmatrix}0&1&0\\1&0&0\\0&0&1\end{bmatrix},\qquad
PA=\begin{bmatrix}4&-2&6\\0&3&-4\\-4&8&k\end{bmatrix}.
$$
</div>

 Write 

<div class="math-display">
$$
L=\begin{bmatrix}1&0&0\\\ell_{21}&1&0\\\ell_{31}&\ell_{32}&1\end{bmatrix}.
$$
</div>

 Matching the first row of <span class="math-inline">\\(LU\\)</span> with <span class="math-inline">\\(PA\\)</span> gives <span class="math-inline">\\(a=-2\\)</span> and <span class="math-inline">\\(b=6\\)</span>. Matching the first column gives 

<div class="math-display">
$$
4\ell_{21}=0,\qquad4\ell_{31}=-4,
\qquad\text{so}\qquad\ell_{21}=0,\quad\ell_{31}=-1.
$$
</div>

 Entry <span class="math-inline">\\((2,3)\\)</span> gives <span class="math-inline">\\(0(6)+c=-4\\)</span>, so <span class="math-inline">\\(c=-4\\)</span>. Entry <span class="math-inline">\\((3,2)\\)</span> gives 

<div class="math-display">
$$
(-1)(-2)+3\ell_{32}=8,\qquad\text{so}\qquad\ell_{32}=2.
$$
</div>

 Finally, entry <span class="math-inline">\\((3,3)\\)</span> gives <span class="math-inline">\\(k=(-1)(6)+2(-4)+5=-9\\)</span>. Therefore, 

<div class="math-display">
$$
\boxed{k=-9,\qquad P=\begin{bmatrix}0&1&0\\1&0&0\\0&0&1\end{bmatrix},}
$$
</div>

 

<div class="math-display">
$$
\boxed{L=\begin{bmatrix}1&0&0\\0&1&0\\-1&2&1\end{bmatrix},\qquad
U=\begin{bmatrix}4&-2&6\\0&3&-4\\0&0&5\end{bmatrix}.}
$$
</div>

 As a check, <span class="math-inline">\\(LU=\begin{bmatrix}4&amp;-2&amp;6\\\\0&amp;3&amp;-4\\\\-4&amp;8&amp;-9\end{bmatrix}=PA\\)</span>.

</details>

</div>
</div>


<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">

(8 pts) A different <span class="math-inline">\\(3\times3\\)</span> matrix <span class="math-inline">\\(B\\)</span> has the factorization <span class="math-inline">\\(PB=LU\\)</span>, where 

<div class="math-display">
$$
P=\begin{bmatrix}0&1&0\\0&0&1\\1&0&0\end{bmatrix},\qquad L=\begin{bmatrix}1&0&0\\2&1&0\\-1&-2&1\end{bmatrix},\qquad U=\begin{bmatrix}3&4&-2\\0&-5&5\\0&0&4\end{bmatrix}.
$$
</div>

 Use these factors to solve 

<div class="math-display">
$$
B\vec x=\begin{bmatrix}26\\8\\1\end{bmatrix}.
$$
</div>

 For full credit, solve using two triangular systems; don't find the entries of <span class="math-inline">\\(B\\)</span> directly.

<details markdown="1"><summary>Solution</summary>

First reorder the right-hand side: 

<div class="math-display">
$$
P\begin{bmatrix}26\\8\\1\end{bmatrix}=\begin{bmatrix}8\\1\\26\end{bmatrix}.
$$
</div>

 Solve <span class="math-inline">\\(L\vec y=P\vec b\\)</span> by forward substitution: 

<div class="math-display">
$$
y_1=8,\qquad2y_1+y_2=1,\qquad-y_1-2y_2+y_3=26.
$$
</div>

 Thus <span class="math-inline">\\(y&#95;1=8\\)</span>, <span class="math-inline">\\(y&#95;2=-15\\)</span>, and <span class="math-inline">\\(y&#95;3=4\\)</span>. Next, solve <span class="math-inline">\\(U\vec x=\vec y\\)</span> by back substitution: 

<div class="math-display">
$$
\begin{aligned}
4x_3&=4 &&\Longrightarrow\quad x_3=1,\\
-5x_2+5x_3&=-15 &&\Longrightarrow\quad x_2=4,\\
3x_1+4x_2-2x_3&=8 &&\Longrightarrow\quad x_1=-2.
\end{aligned}
$$
</div>

 Therefore <span class="math-inline">\\(\boxed{\vec x=\begin{bmatrix}-2\\\\4\\\\1\end{bmatrix}}\\)</span>. The entries are already in the original variable order.

</details>

</div>
</div>


---

<h2 id="problem-6-16-pts" markdown="span">Problem 6 (16 pts) <a class="btn btn-info assignment-pdf-button problem-video-button" href="https://youtu.be/oSgA3kJHb4M" target="_blank" rel="noopener" aria-label="Walkthrough video for Problem 6">🎥 Walkthrough</a></h2>



<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">

(8 pts) Let 

<div class="math-display">
$$
A=\begin{bmatrix}2&-4&6&0\\-4&8&-9&6\\6&-12&15&-6\end{bmatrix}.
$$
</div>

 Find all real numbers <span class="math-inline">\\(s\\)</span> for which the following system has infinitely many solutions: 

<div class="math-display">
$$
A\vec x=\begin{bmatrix}s\\1\\4\end{bmatrix}.
$$
</div>

 If there are multiple such values of <span class="math-inline">\\(s\\)</span>, separate them with commas. You do not need to write the solution set.

<details markdown="1"><summary>Solution</summary>

Find an LU factorization by matching entries in the product. The first row of <span class="math-inline">\\(U\\)</span> is the first row of <span class="math-inline">\\(A\\)</span>. Matching the first column gives <span class="math-inline">\\(\ell&#95;{21}=-2\\)</span> and <span class="math-inline">\\(\ell&#95;{31}=3\\)</span>. The second row must then satisfy 

<div class="math-display">
$$
(-2)(-4)+u_{22}=8,\qquad(-2)(6)+u_{23}=-9,\qquad u_{24}=6,
$$
</div>

 so its entries are <span class="math-inline">\\(0,0,3,6\\)</span>. Matching entry <span class="math-inline">\\((3,3)\\)</span> gives <span class="math-inline">\\(3(6)+3\ell&#95;{32}=15\\)</span>, so <span class="math-inline">\\(\ell&#95;{32}=-1\\)</span>. The remaining entries of the last row of <span class="math-inline">\\(U\\)</span> are zero. Hence 

<div class="math-display">
$$
A=\underbrace{\begin{bmatrix}1&0&0\\-2&1&0\\3&-1&1\end{bmatrix}}_L
\underbrace{\begin{bmatrix}2&-4&6&0\\0&0&3&6\\0&0&0&0\end{bmatrix}}_U.
$$
</div>

 Solve <span class="math-inline">\\(L\vec y=\begin{bmatrix}s\\\\1\\\\4\end{bmatrix}\\)</span>: 

<div class="math-display">
$$
y_1=s,\qquad-2y_1+y_2=1,\qquad3y_1-y_2+y_3=4.
$$
</div>

 This gives <span class="math-inline">\\(\vec y=\begin{bmatrix}s\\\\1+2s\\\\5-s\end{bmatrix}\\)</span>. The last equation of <span class="math-inline">\\(U\vec x=\vec y\\)</span> is <span class="math-inline">\\(0=5-s\\)</span>, so consistency requires <span class="math-inline">\\(s=5\\)</span>.

When <span class="math-inline">\\(s=5\\)</span>, the zero row gives <span class="math-inline">\\(0=0\\)</span>. Columns 1 and 3 contain pivots, and <span class="math-inline">\\(x&#95;2,x&#95;4\\)</span> are free: the second equation determines <span class="math-inline">\\(x&#95;3\\)</span> and the first determines <span class="math-inline">\\(x&#95;1\\)</span> for every choice of <span class="math-inline">\\(x&#95;2,x&#95;4\\)</span>. Thus there are infinitely many solutions exactly when <span class="math-inline">\\(\boxed{s=5}\\)</span>.

**Another approach** is to try to solve directly. The three equations are 

<div class="math-display">
$$
\begin{aligned}
2x_1-4x_2+6x_3&=s,\\
-4x_1+8x_2-9x_3+6x_4&=1,\\
6x_1-12x_2+15x_3-6x_4&=4.
\end{aligned}
$$
</div>

 Observe what happens when we add the last two equations:

<div class="math-display">
$$
2x_1-4x_2+6x_3=5.
$$
</div>

 For this to be consistent with the first equation, we need <span class="math-inline">\\(\boxed{s=5}\\)</span>. Otherwise, there is no solution.

</details>

</div>
</div>


<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">

(8 pts) Find all solutions of the following system. Give your answer in vector-parametric form. <span class="math-inline">\\(\boxed{\text{Circle}}\\)</span> your final answer. 

<div class="math-display">
$$
\begin{bmatrix}
2&0&-4&6&0\\
0&3&6&-3&0\\
0&0&0&0&5\\
0&0&0&0&0
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\\x_4\\x_5\end{bmatrix}
=\begin{bmatrix}8\\-9\\20\\0\end{bmatrix}.
$$
</div>

<details markdown="1"><summary>Solution</summary>

The equations are 

<div class="math-display">
$$
2x_1-4x_3+6x_4=8,\qquad3x_2+6x_3-3x_4=-9,\qquad5x_5=20,\qquad0=0.
$$
</div>

 The pivot variables are <span class="math-inline">\\(x&#95;1,x&#95;2,x&#95;5\\)</span>, and the free variables are <span class="math-inline">\\(x&#95;3,x&#95;4\\)</span>. Let <span class="math-inline">\\(x&#95;3=s\\)</span> and <span class="math-inline">\\(x&#95;4=t\\)</span>. Then 

<div class="math-display">
$$
x_1=4+2s-3t,\qquad x_2=-3-2s+t,\qquad x_5=4.
$$
</div>

 The complete solution set is 

<div class="math-display">
$$
\boxed{\vec x=\begin{bmatrix}4\\-3\\0\\0\\4\end{bmatrix}
+s\begin{bmatrix}2\\-2\\1\\0\\0\end{bmatrix}
+t\begin{bmatrix}-3\\1\\0\\1\\0\end{bmatrix},\qquad s,t\in\mathbb R.}
$$
</div>

</details>

</div>
</div>


---

<h2 id="problem-7-11-pts" markdown="span">Problem 7 (11 pts) <a class="btn btn-info assignment-pdf-button problem-video-button" href="https://youtu.be/n46UCNag9_c" target="_blank" rel="noopener" aria-label="Walkthrough video for Problem 7">🎥 Walkthrough</a></h2>



<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">

(5 pts) Let 

<div class="math-display">
$$
S=\left\{\begin{bmatrix}3a-2b\\6a-4b\\5a+b\end{bmatrix}:a,b\in\mathbb R\right\}.
$$
</div>

 Find a <span class="math-inline">\\(3\times3\\)</span> matrix <span class="math-inline">\\(A\\)</span> such that <span class="math-inline">\\(\operatorname{colsp}(A)=S\\)</span>.

<details markdown="1"><summary>Solution</summary>

Write each vector in <span class="math-inline">\\(S\\)</span> as 

<div class="math-display">
$$
\begin{bmatrix}3a-2b\\6a-4b\\5a+b\end{bmatrix}
=a\begin{bmatrix}3\\6\\5\end{bmatrix}+b\begin{bmatrix}-2\\-4\\1\end{bmatrix}.
$$
</div>

 Use these two vectors as the first two columns of <span class="math-inline">\\(A\\)</span>. To get the required <span class="math-inline">\\(3\times3\\)</span> shape, the third column should be any other vector in <span class="math-inline">\\(S\\)</span>: any linear combination of these first two columns. An easy choice is <span class="math-inline">\\(\begin{bmatrix}0\\\\0\\\\0\end{bmatrix}\\)</span>, obtained by taking both coefficients to be zero. Thus one answer is 

<div class="math-display">
$$
\boxed{A=\begin{bmatrix}3&-2&0\\6&-4&0\\5&1&0\end{bmatrix}.}
$$
</div>

 Every linear combination of its columns belongs to <span class="math-inline">\\(S\\)</span>, and every vector of <span class="math-inline">\\(S\\)</span> is obtained using coefficients <span class="math-inline">\\(a,b,0\\)</span>. The zero column does not change the column space.

</details>

</div>
</div>


<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">

(6 pts) For each set below, explain why it is **not** a subspace of <span class="math-inline">\\(\mathbb R^3\\)</span>.

**i)** (2 pts) 

<div class="math-display">
$$
W=\left\{\begin{bmatrix}x\\y\\z\end{bmatrix}\in\mathbb R^3:z=1\right\}.
$$
</div>

**ii)** (4 pts) 

<div class="math-display">
$$
V=\left\{\begin{bmatrix}x\\y\\z\end{bmatrix}\in\mathbb R^3:y=0,\ z=x^2\right\}.
$$
</div>

<details markdown="1"><summary>Solution</summary>

**i)** The zero vector does not belong to <span class="math-inline">\\(W\\)</span>, because its third entry is <span class="math-inline">\\(0\\)</span>, not <span class="math-inline">\\(1\\)</span>. Every subspace contains the zero vector, so <span class="math-inline">\\(W\\)</span> is not a subspace.

**ii)** The vector <span class="math-inline">\\(\vec v=\begin{bmatrix}1\\\\0\\\\1\end{bmatrix}\\)</span> belongs to <span class="math-inline">\\(V\\)</span>, since <span class="math-inline">\\(1=1^2\\)</span>. However, <span class="math-inline">\\(2\vec v=\begin{bmatrix}2\\\\0\\\\2\end{bmatrix}\\)</span> does not belong to <span class="math-inline">\\(V\\)</span>, since <span class="math-inline">\\(2\ne2^2\\)</span>. Thus <span class="math-inline">\\(V\\)</span> is not closed under scalar multiplication and is not a subspace.

</details>

</div>
</div>


---

<h2 id="problem-8-16-pts" markdown="span">Problem 8 (16 pts) <a class="btn btn-info assignment-pdf-button problem-video-button" href="https://youtu.be/ST9k_UpGHI4" target="_blank" rel="noopener" aria-label="Walkthrough video for Problem 8">🎥 Walkthrough</a></h2>



<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">

(8 pts) Let <span class="math-inline">\\(\vec p,\vec q,\vec r\in\mathbb R^7\\)</span> be linearly independent. Find the rank of each matrix.

<div class="math-display">
$$
A=\begin{bmatrix}|&|&|&|\\\vec p+\vec q&\vec q+\vec r&\vec p+\vec r&4\vec r\\|&|&|&|\end{bmatrix}
$$
</div>

<div class="math-display">
$$
B=\begin{bmatrix}|&|\\2\vec p-\vec q&8\vec p-4\vec q\\|&|\end{bmatrix}
$$
</div>

<div class="math-display">
$$
C=\begin{bmatrix}|&|&|\\\vec p+2\vec q&3\vec q-\vec r&2\vec p+7\vec q-\vec r\\|&|&|\end{bmatrix}
$$
</div>

<div class="math-display">
$$
D=\begin{bmatrix}|&|&|&|\\\vec p+\vec q&\vec q+\vec r&\vec p-\vec r&2\vec p+\vec q-\vec r\\|&|&|&|\end{bmatrix}.
$$
</div>

<details markdown="1"><summary>Solution</summary>

The rank is the number of vectors in a basis for the column space. We will keep linearly independent columns and express the remaining columns as linear combinations of them. Recall that vectors are linearly independent if none can be written as a linear combination of the others.

**<span class="math-inline">\\(A\\)</span>: rank 3.** The first column, <span class="math-inline">\\(\vec p+\vec q\\)</span>, is nonzero: otherwise <span class="math-inline">\\(\vec p=-\vec q\\)</span>, contradicting the independence of <span class="math-inline">\\(\vec p,\vec q,\vec r\\)</span>.

The second column cannot be a multiple of the first. If <span class="math-inline">\\(\vec q+\vec r=c(\vec p+\vec q)\\)</span>, then

<div class="math-display">
$$
\vec r=c\vec p+(c-1)\vec q,
$$
</div>

 which would write <span class="math-inline">\\(\vec r\\)</span> as a linear combination of <span class="math-inline">\\(\vec p\\)</span> and <span class="math-inline">\\(\vec q\\)</span>.

The third column cannot be a linear combination of the first two either. Suppose

<div class="math-display">
$$
\vec p+\vec r=a(\vec p+\vec q)+b(\vec q+\vec r)
=a\vec p+(a+b)\vec q+b\vec r.
$$
</div>

 The coefficients of <span class="math-inline">\\(\vec p,\vec q,\vec r\\)</span> on the two sides must match: if any coefficient differed, rearranging would express that vector as a linear combination of the other two. The <span class="math-inline">\\(\vec p\\)</span> and <span class="math-inline">\\(\vec r\\)</span> coefficients require <span class="math-inline">\\(a=b=1\\)</span>, but then the <span class="math-inline">\\(\vec q\\)</span> coefficient is <span class="math-inline">\\(a+b=2\\)</span>, whereas it is <span class="math-inline">\\(0\\)</span> on the left. This is impossible.

Thus the first three columns are linearly independent. The fourth is a linear combination of them:

<div class="math-display">
$$
4\vec r=-2(\vec p+\vec q)+2(\vec q+\vec r)+2(\vec p+\vec r).
$$
</div>

 The first three columns therefore form a basis for the column space, so <span class="math-inline">\\(\boxed{\operatorname{rank}(A)=3}\\)</span>.

**<span class="math-inline">\\(B\\)</span>: rank 1.** The second column is four times the first. The first column, <span class="math-inline">\\(2\vec p-\vec q\\)</span>, is nonzero, since otherwise <span class="math-inline">\\(\vec q=2\vec p\\)</span>. Thus the first column alone is a basis for the column space, and <span class="math-inline">\\(\boxed{\operatorname{rank}(B)=1}\\)</span>.

**<span class="math-inline">\\(C\\)</span>: rank 2.** The first column, <span class="math-inline">\\(\vec p+2\vec q\\)</span>, is nonzero, since otherwise <span class="math-inline">\\(\vec p=-2\vec q\\)</span>. The second column cannot be a multiple of it: if <span class="math-inline">\\(3\vec q-\vec r=c(\vec p+2\vec q)\\)</span>, then

<div class="math-display">
$$
\vec r=-c\vec p+(3-2c)\vec q,
$$
</div>

 contradicting the independence of <span class="math-inline">\\(\vec p,\vec q,\vec r\\)</span>. The first two columns are therefore linearly independent. The third is twice the first plus the second:

<div class="math-display">
$$
2\vec p+7\vec q-\vec r=2(\vec p+2\vec q)+(3\vec q-\vec r).
$$
</div>

 Thus the first two columns form a basis for the column space, and <span class="math-inline">\\(\boxed{\operatorname{rank}(C)=2}\\)</span>.

**<span class="math-inline">\\(D\\)</span>: rank 2.** The first two columns are <span class="math-inline">\\(\vec p+\vec q\\)</span> and <span class="math-inline">\\(\vec q+\vec r\\)</span>, which we showed are linearly independent when analyzing <span class="math-inline">\\(A\\)</span>. The third and fourth columns are linear combinations of these two:

<div class="math-display">
$$
\vec p-\vec r=(\vec p+\vec q)-(\vec q+\vec r),
$$
</div>



<div class="math-display">
$$
2\vec p+\vec q-\vec r=2(\vec p+\vec q)-(\vec q+\vec r).
$$
</div>

 Thus the first two columns form a basis for the column space, and <span class="math-inline">\\(\boxed{\operatorname{rank}(D)=2}\\)</span>.

</details>

</div>
</div>


<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">

(2 pts) A <span class="math-inline">\\(6\times8\\)</span> matrix <span class="math-inline">\\(E\\)</span> has rank <span class="math-inline">\\(3\\)</span>. How many free variables does <span class="math-inline">\\(E\vec x=\vec0\\)</span> have?

Number of free variables:

<details markdown="1"><summary>Solution</summary>

Rank 3 means that an echelon factor <span class="math-inline">\\(U\\)</span> of <span class="math-inline">\\(E\\)</span> has 3 pivots. For example, one possible arrangement is 

<div class="math-display">
$$
U=\begin{bmatrix}
\boxed{p_1}&*&*&*&*&*&*&*\\
0&0&\boxed{p_2}&*&*&*&*&*\\
0&0&0&0&0&\boxed{p_3}&*&*\\
0&0&0&0&0&0&0&0\\
0&0&0&0&0&0&0&0\\
0&0&0&0&0&0&0&0
\end{bmatrix},\qquad p_1,p_2,p_3\ne0.
$$
</div>

 The boxed entries are the pivots; each <span class="math-inline">\\(\ast\\)</span> can be any number. In this example, the variables are grouped as 

<div class="math-display">
$$
\begin{array}{c|cccccccc}
\text{Variable}&x_1&x_2&x_3&x_4&x_5&x_6&x_7&x_8\\ \hline
\text{Type}&\text{pivot}&\text{free}&\text{pivot}&\text{free}&\text{free}&\text{pivot}&\text{free}&\text{free}
\end{array}
$$
</div>

 The actual pivot columns may differ, but there must be 3 pivot columns among the 8 columns. The other <span class="math-inline">\\(\boxed{8-3=5}\\)</span> columns give free variables. The homogeneous system is always consistent, so all five free variables can be chosen freely.

</details>

</div>
</div>


<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">

(3 pts) A <span class="math-inline">\\(4\times7\\)</span> matrix <span class="math-inline">\\(F\\)</span> has rank <span class="math-inline">\\(4\\)</span>. Is every vector in <span class="math-inline">\\(\mathbb R^4\\)</span> a possible output of <span class="math-inline">\\(F\\)</span>? Briefly explain.

<details markdown="1"><summary>Solution</summary>

**Yes.** The column space of <span class="math-inline">\\(F\\)</span> is a subspace of <span class="math-inline">\\(\mathbb R^4\\)</span> with dimension 4, so it equals <span class="math-inline">\\(\mathbb R^4\\)</span>. Thus every vector in <span class="math-inline">\\(\mathbb R^4\\)</span> is a possible output of <span class="math-inline">\\(F\\)</span>.

</details>

</div>
</div>


<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">

(3 pts) A <span class="math-inline">\\(6\times4\\)</span> matrix <span class="math-inline">\\(G\\)</span> has rank <span class="math-inline">\\(4\\)</span>. Could <span class="math-inline">\\(G\vec x=\vec b\\)</span> have exactly one solution for some <span class="math-inline">\\(\vec b\in\mathbb R^6\\)</span>? Briefly explain.

<details markdown="1"><summary>Solution</summary>

**Yes.** Since <span class="math-inline">\\(G\\)</span> has rank 4 and 4 columns, its echelon factor <span class="math-inline">\\(U\\)</span> has a pivot in every column. There are no free variables, so any consistent system has exactly one solution, determined by back substitution.

</details>

</div>
</div>


{% endraw %}
