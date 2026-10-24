---
layout: page
title: "Homework 6: Inverses and LU Factorization"
description: "Homework 6: Inverses and LU Factorization problems."
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

# Homework 6: Inverses and LU Factorization

**due** Friday, October 30th at 11:59PM

{: .yellow }
<div markdown="1">
Write your solutions to the following problems either by writing them on a piece of paper or on a tablet and scanning your answers as a PDF. Note that you are not allowed to use LaTeX, Google Docs, or any other digital document creation software to type your answers. Homeworks are due to Pensive by 11:59PM on the due date. See the [syllabus](https://math124.org/syllabus/#homework) for details on the slip day policy.

Homework will be evaluated not only on the correctness of your answers, but on your ability to present your ideas clearly and logically. You should always explain and justify your conclusions, using sound reasoning. Your goal should be to convince the reader of your assertions. If a question does not require explanation, it will be explicitly stated.

Before proceeding, make sure you're familiar with the [collaboration policy](https://math124.org/syllabus/#collaboration-and-generative-ai-policy).
</div>

---

## Problems

- [Problem 1: Homework 5 solutions review](#problem-1-homework-5-solutions-review-6-pts)
- [Problem 2: Finding Inverses](#problem-2-finding-inverses-8-pts)
- [Problem 3: Inverse of a Rotation](#problem-3-inverse-of-a-rotation-8-pts)
- [Problem 4: Inverse of a $3\times3$ Matrix](#problem-4-inverse-of-a-3times3-matrix-12-pts)
- [Problem 5: Inverses in NumPy](#problem-5-inverses-in-numpy-12-pts)
- [Problem 6: LU Factorization of $2\times2$ Matrices](#problem-6-lu-factorization-of-2times2-matrices-16-pts)
- [Problem 7: LU Factorization of a $3\times3$ Matrix](#problem-7-lu-factorization-of-a-3times3-matrix-20-pts)
- [Problem 8: Separating Songs](#problem-8-separating-songs-18-pts)

---

Total Points: <span class="math-inline">\\(6+8+8+12+12+16+20+18=100\\)</span>

---

Remember to look at [Chapter 3.6](https://notes.math124.org/ch03/03-06) and [Chapter 4](https://notes.math124.org/ch04/04-01) of the course notes while working on the homework!

---

## Problem 1: Homework 5 solutions review (6 pts)

Review [the solutions to Homework 5](https://math124.org/resources/homeworks/hw05/). Pick **two problem parts** (for example, Problem 3a) and Problem 5b)) from Homework 5 in which your solutions have the most room for improvement, i.e., where they have unsound reasoning, could be significantly more efficient or clearer, etc. **Include a screenshot of your solution to each problem part**, and in a few sentences, explain what was deficient and how it could be fixed.

Alternatively, if you think one of your solutions is significantly better than the posted one, copy it here and explain why you think it is better. If you didn't do Homework 5, choose two problem parts from it that look challenging to you, and in a few sentences, explain the key ideas behind their solutions in your own words.

---

## Problem 2: Finding Inverses (8 pts)

Suppose <span class="math-inline">\\(A=BC\\)</span>, where <span class="math-inline">\\(B\\)</span> is an unknown invertible <span class="math-inline">\\(2\times2\\)</span> matrix and

<div class="math-display">
$$
A=\begin{bmatrix}1&5\\0&3\end{bmatrix},\qquad
C=\begin{bmatrix}1&2\\-1&1\end{bmatrix}
$$
</div>

 Find <span class="math-inline">\\(B^{-1}\\)</span>. For full credit, you may only use the formula for the inverse of a <span class="math-inline">\\(2\times2\\)</span> matrix **once**; you do not need to find <span class="math-inline">\\(B\\)</span> first.

---

## Problem 3: Inverse of a Rotation (8 pts)

As we've seen, the matrix

<div class="math-display">
$$
R_\theta=\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}
$$
</div>

 rotates vectors in <span class="math-inline">\\(\mathbb R^2\\)</span> counterclockwise by <span class="math-inline">\\(\theta\\)</span> radians.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Find <span class="math-inline">\\(R&#95;\theta^{-1}\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Now, find <span class="math-inline">\\(R&#95;{-\theta}\\)</span> for a rotation of <span class="math-inline">\\(\theta\\)</span> radians clockwise, i.e. for <span class="math-inline">\\(-\theta\\)</span>. What do you notice, and why?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) A linear transformation <span class="math-inline">\\(T:\mathbb R^2\to\mathbb R^2\\)</span> first rotates vectors counterclockwise by <span class="math-inline">\\(30^\circ\\)</span>, then multiplies their horizontal coordinates by <span class="math-inline">\\(5\\)</span> and their vertical coordinates by <span class="math-inline">\\(\frac12\\)</span>. Find the matrix of <span class="math-inline">\\(T^{-1}\\)</span>. <em>Hint: While it's possible to do this by first finding the matrix for <span class="math-inline">\\(T\\)</span>, that is not necessary!</em>

</div>
</div>

</div>

---

## Problem 4: Inverse of a <span class="math-inline">\\(3\times3\\)</span> Matrix (12 pts)

Let

<div class="math-display">
$$
A=\begin{bmatrix}2&-3&4\\1&-2&3\\3&-5&8\end{bmatrix}
=\begin{bmatrix}|&|&|\\\vec a_1&\vec a_2&\vec a_3\\|&|&|\end{bmatrix}.
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) For each vector below, find coefficients <span class="math-inline">\\(c&#95;1,c&#95;2,c&#95;3\\)</span> such that <span class="math-inline">\\(c&#95;1\vec a&#95;1+c&#95;2\vec a&#95;2+c&#95;3\vec a&#95;3\\)</span> equals that vector. Show how you find the coefficients, and write each coefficient vector vertically.

<div class="math-display">
$$
\text{(i) }\begin{bmatrix}1\\0\\0\end{bmatrix},\qquad
\text{(ii) }\begin{bmatrix}0\\1\\0\end{bmatrix},\qquad
\text{(iii) }\begin{bmatrix}0\\0\\1\end{bmatrix}.
$$
</div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Place your three coefficient vectors in the columns of a matrix <span class="math-inline">\\(X\\)</span>, in the order above. Explain why <span class="math-inline">\\(AX=I&#95;3\\)</span> and why this means <span class="math-inline">\\(X=A^{-1}\\)</span>. You may use the fact that for square matrices, <span class="math-inline">\\(AX=I&#95;3\\)</span> also implies <span class="math-inline">\\(XA=I&#95;3\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Use your inverse to solve <span class="math-inline">\\(A\vec x=\begin{bmatrix}11\\\\7\\\\19\end{bmatrix}\\)</span>. Verify your work by multiplying <span class="math-inline">\\(A\vec x\\)</span> and checking it is equal to <span class="math-inline">\\(\begin{bmatrix}11\\\\7\\\\19\end{bmatrix}\\)</span>.

</div>
</div>

</div>

---

## Problem 5: Inverses in NumPy (12 pts)

In this problem, we will investigate several <span class="math-inline">\\(3\times3\\)</span> matrices and see whether they are invertible. Consider the following six matrices:

<div class="math-display">
$$
M_1=\begin{bmatrix}1&2&0\\0&1&1\\1&0&1\end{bmatrix},\qquad
M_2=\begin{bmatrix}1&2&0\\2&4&1\\4&8&-1\end{bmatrix},\qquad
M_3=\begin{bmatrix}2&0&1\\1&1&0\\0&2&1\end{bmatrix},
$$
</div>



<div class="math-display">
$$
M_4=\begin{bmatrix}1&0&1\\2&2&4\\-1&1&0\end{bmatrix},\qquad
M_5=\begin{bmatrix}1&0&2\\0&0&1\\2&0&-1\end{bmatrix},\qquad
M_6=\begin{bmatrix}0&1&2\\1&0&1\\2&1&0\end{bmatrix}.
$$
</div>

 Before proceeding, open the supplemental Jupyter Notebook. To open the notebook for Homework 6, click [**this link**](https://colab.research.google.com/github/math-124/fa26-code/blob/main/homeworks/hw06/hw06.ipynb). Instructions on how to use Google Colab are at [math124.org/running-code](https://math124.org/running-code).

There, we provide instructions on how to compute a matrix's inverse using `np.linalg.inv`. For the matrices in this problem, if that function call raises the error `LinAlgError: Singular matrix`, then the matrix is not invertible!

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) For all six matrices, try to compute their inverse. Report which ones are invertible and which are not.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) For the matrices that are invertible, multiply their inverse by the original matrix and show that the result is the identity matrix. <span style="color: #E67E22">**In Your PDF:** Include a screenshot that contains this check for all invertible matrices.</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) For each non-invertible matrix, suppose the columns are named <span class="math-inline">\\(\vec x\\)</span>, <span class="math-inline">\\(\vec y\\)</span>, and <span class="math-inline">\\(\vec z\\)</span>, from left to right. Write one column as a linear combination of the other two. For example, you could write <span class="math-inline">\\(\vec z=a\vec x+b\vec y\\)</span> for specific numbers <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span>, or express <span class="math-inline">\\(\vec x\\)</span> or <span class="math-inline">\\(\vec y\\)</span> in terms of the other two columns. The coefficients may be zero. What do all the non-invertible matrices have in common?

</div>
</div>

</div>

---

## Problem 6: LU Factorization of <span class="math-inline">\\(2\times2\\)</span> Matrices (16 pts)

For each <span class="math-inline">\\(2\times2\\)</span> matrix <span class="math-inline">\\(A\\)</span> below:

<ol class="assignment-enumeration" markdown="1">
<li markdown="1">
<div class="assignment-enumeration-label">1.</div>
<div class="assignment-enumeration-content" markdown="1">

Find an LU factorization with **ones on the diagonal of <span class="math-inline">\\(L\\)</span>**. If necessary, multiply <span class="math-inline">\\(A\\)</span> by a permutation matrix <span class="math-inline">\\(P\\)</span>, i.e., find <span class="math-inline">\\(PA=LU\\)</span>. If no row swap is needed, use <span class="math-inline">\\(P=I\\)</span>.

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">2.</div>
<div class="assignment-enumeration-content" markdown="1">

Use the same <span class="math-inline">\\(L\\)</span> and <span class="math-inline">\\(U\\)</span> to solve <span class="math-inline">\\(A\vec x=\vec b&#95;1\\)</span> and <span class="math-inline">\\(A\vec x=\vec b&#95;2\\)</span>.

</div></li>
</ol>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(8 pts)
<div class="math-display">
$$
A=\begin{bmatrix}4&3\\8&9\end{bmatrix},\qquad
\vec b_1=\begin{bmatrix}11\\25\end{bmatrix},\qquad
\vec b_2=\begin{bmatrix}5\\19\end{bmatrix}.
$$
</div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(8 pts)
<div class="math-display">
$$
A=\begin{bmatrix}0&5\\6&4\end{bmatrix},\qquad
\vec b_1=\begin{bmatrix}15\\24\end{bmatrix},\qquad
\vec b_2=\begin{bmatrix}-10\\10\end{bmatrix}.
$$
</div>

</div>
</div>

</div>

---

## Problem 7: LU Factorization of a <span class="math-inline">\\(3\times3\\)</span> Matrix (20 pts)

For each <span class="math-inline">\\(3\times3\\)</span> matrix below, find an LU factorization as in Problem 6, then use <span class="math-inline">\\(L\\)</span> and <span class="math-inline">\\(U\\)</span> to solve <span class="math-inline">\\(A\vec x=\vec b\\)</span> for the given vector <span class="math-inline">\\(\vec b\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(10 pts)
<div class="math-display">
$$
A=\begin{bmatrix}3&4&-2\\6&13&-1\\-3&6&12\end{bmatrix},\qquad
\vec b=\begin{bmatrix}-4\\-4\\24\end{bmatrix}.
$$
</div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(10 pts)
<div class="math-display">
$$
A=\begin{bmatrix}3&3&0\\6&6&5\\3&7&2\end{bmatrix},\qquad
\vec b=\begin{bmatrix}3\\21\\5\end{bmatrix}.
$$
</div>

</div>
</div>

</div>

---

## Problem 8: Separating Songs (18 pts)

Five speakers are playing five different songs at the same time, **one song per speaker**. Five microphones record them, but each microphone picks up a different mixture of all five speakers. The speakers stand in a line, with microphones arranged around them in a circle. The diagram shows which song each speaker plays.

<img src="imgs/hw06-plot-01.png" alt="Coordinate diagram" class="assignment-vector-plot">

Every microphone picks up all five speakers, but not evenly.

We know the song titles, but **do not** have access to the original song files -- all we have are what our microphones recorded. Our goal is to recover the audio originally depicted by each speaker -- i.e., the original songs -- from these mixtures.

A digital audio recording stores a sound's amplitude at regularly spaced instants. Each amplitude is a number that can be positive, negative, or zero. At a sample rate of <span class="math-inline">\\(8{,}000\\)</span> Hz, there are <span class="math-inline">\\(8{,}000\\)</span> amplitude measurements per second. Thus, a four-second clip is a vector of <span class="math-inline">\\(32{,}000\\)</span> numbers.

At a particular instant, let <span class="math-inline">\\(x&#95;1,x&#95;2,x&#95;3,x&#95;4,x&#95;5\\)</span> be the sound amplitudes coming from the five speakers and <span class="math-inline">\\(b&#95;1,b&#95;2,b&#95;3,b&#95;4,b&#95;5\\)</span> be the amplitudes recorded by the five microphones. Each microphone records a weighted sum of the speaker amplitudes, using the known weights below. **Assume these weights stay fixed throughout the problem.**

<table>
<thead>
<tr>
<th style="text-align: center;"></th>
<th style="text-align: center;">Speaker 1<br><small><span>(Song 1)</span></small></th>
<th style="text-align: center;">Speaker 2<br><small><span>(Song 2)</span></small></th>
<th style="text-align: center;">Speaker 3<br><small><span>(Song 3)</span></small></th>
<th style="text-align: center;">Speaker 4<br><small><span>(Song 4)</span></small></th>
<th style="text-align: center;">Speaker 5<br><small><span>(Song 5)</span></small></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Microphone 1</td>
<td style="text-align: center;"><span class="math-inline">\(0.9\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(0.8\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(0.6\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(0.5\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(0.7\)</span></td>
</tr>
<tr>
<td style="text-align: center;">Microphone 2</td>
<td style="text-align: center;"><span class="math-inline">\(0.7\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(0.9\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(0.8\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(0.7\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(0.6\)</span></td>
</tr>
<tr>
<td style="text-align: center;">Microphone 3</td>
<td style="text-align: center;"><span class="math-inline">\(0.5\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(0.6\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(0.8\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(0.9\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(0.8\)</span></td>
</tr>
<tr>
<td style="text-align: center;">Microphone 4</td>
<td style="text-align: center;"><span class="math-inline">\(0.8\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(0.7\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(0.9\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(0.8\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(0.6\)</span></td>
</tr>
<tr>
<td style="text-align: center;">Microphone 5</td>
<td style="text-align: center;"><span class="math-inline">\(0.6\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(0.8\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(0.7\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(0.6\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(0.9\)</span></td>
</tr>
</tbody>
</table>

For example, Microphone 1 records

<div class="math-display">
$$
b_1=0.9x_1+0.8x_2+0.6x_3+0.5x_4+0.7x_5.
$$
</div>

Before proceeding, open the supplemental Jupyter Notebook. To open the notebook for Homework 6, click [**this link**](https://colab.research.google.com/github/math-124/fa26-code/blob/main/homeworks/hw06/hw06.ipynb). Instructions on how to use Google Colab are at [math124.org/running-code](https://math124.org/running-code).

The notebook provides two four-second recording sessions, using different excerpts of the same five songs. We know the microphone recordings and the weights, but must solve for what each speaker was playing.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Write the five equations relating the speaker amplitudes to the microphone amplitudes at one instant. Then write your system as <span class="math-inline">\\(A\vec x=\vec b\\)</span>, where

<div class="math-display">
$$
\vec x=\begin{bmatrix}x_1\\x_2\\x_3\\x_4\\x_5\end{bmatrix},\qquad
\vec b=\begin{bmatrix}b_1\\b_2\\b_3\\b_4\\b_5\end{bmatrix}.
$$
</div>

 State <span class="math-inline">\\(A\\)</span> and its shape.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) In the notebook, enter your matrix <span class="math-inline">\\(A\\)</span> and use `scipy.linalg.lu` to find <span class="math-inline">\\(P,L,U\\)</span> satisfying <span class="math-inline">\\(PA=LU\\)</span>. The notebook explains how to use SciPy to do this. Verify that <span class="math-inline">\\(PA=LU\\)</span>, and then use <span class="math-inline">\\(L\\)</span> and <span class="math-inline">\\(U\\)</span> to solve for the five speaker amplitudes, i.e., <span class="math-inline">\\(\vec x\\)</span>, for the one instant <span class="math-inline">\\(\vec b\\)</span> selected in the notebook.

<span style="color: #E67E22">**In Your PDF:** Include a screenshot of the microphone amplitudes and the recovered speaker amplitudes for the one instant provided.</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Recall, in the first four-second clip, there are a total of <span class="math-inline">\\(32{,}000\\)</span> "instants," i.e., <span class="math-inline">\\(32{,}000\\)</span> vectors <span class="math-inline">\\(\vec b\\)</span>, each of which describes the amplitude recorded by each of the five microphones.

Using the LU decomposition from part b), follow the notebook's instructions to solve all these systems together and recover the five song clips. Listen to the mixtures and the recovered clips.

<span style="color: #E67E22">**In Your PDF:** Include a screenshot of the code that starts with `X1 =` and of the five audio players that appear afterwards.</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) In the second session, each speaker plays a different excerpt of its song. Recover these five clips **without computing another LU factorization**. Check your answer and listen to the recovered clips.

<span style="color: #E67E22">**In Your PDF:** Include a screenshot of your code and check for the second recording session.</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(6 pts)

<ol class="assignment-enumeration" markdown="1">
<li markdown="1">
<div class="assignment-enumeration-label">i)</div>
<div class="assignment-enumeration-content" markdown="1">

(3 pts) Why were we able to use our original <span class="math-inline">\\(P\\)</span>, <span class="math-inline">\\(L\\)</span>, and <span class="math-inline">\\(U\\)</span> for the second set of recordings without recomputing them?

</div></li>
<li markdown="1">
<div class="assignment-enumeration-label">ii)</div>
<div class="assignment-enumeration-content" markdown="1">

(3 pts) Suppose only Microphone 1 was working. Could you uniquely recover all five speaker amplitudes at a given instant from its recording alone? Why or why not?

</div></li>
</ol>
</div>
</div>

</div>

{% endraw %}
