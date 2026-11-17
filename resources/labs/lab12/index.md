---
layout: page
title: "Lab 12: Projecting onto the Column Space"
description: "Lab 12: Projecting onto the Column Space activities."
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

# Lab 12: Projecting onto the Column Space

**due** by the end of class on Wednesday, November 18, 2026

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab12/lab12.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab12/lab12-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
Each lab worksheet will contain several activities, most of which will involve writing math on paper, and some of which will involve running code in a Jupyter Notebook. Lab activities are meant to last an hour, and the second hour of lab is dedicated to starting the homework assignment. To receive credit for a lab, you must show your lab TA your work on both the lab worksheet and homework assignment.

While you must get checked off by your lab TA **individually**, we encourage you to form groups with 1-2 other students to complete the activities together.
</div>

---

## Activities

- [Activity 1: Two approaches](#activity-1-two-approaches)
- [Activity 2: Fitting a line](#activity-2-fitting-a-line)

---

## Activity 1: Two approaches

Consider the matrix <span class="math-inline">\\(A\\)</span> and vector <span class="math-inline">\\(\vec b\\)</span>:

<div class="math-display">
$$
A=\begin{bmatrix}1&2\\1&-2\\1&0\end{bmatrix},\qquad
\vec b=\begin{bmatrix}-7\\13\\0\end{bmatrix}.
$$
</div>

 The columns of <span class="math-inline">\\(A\\)</span> span a plane in <span class="math-inline">\\(\mathbb R^3\\)</span>. Our goal is to find the vector <span class="math-inline">\\(\vec p\\)</span> in this plane that is closest to <span class="math-inline">\\(\vec b\\)</span>. This was the focus of yesterday's lecture, though it turns out that you have already learned how to project onto planes in <span class="math-inline">\\(\mathbb R^3\\)</span>!

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find a nonzero vector <span class="math-inline">\\(\vec n\\)</span> perpendicular to both columns of <span class="math-inline">\\(A\\)</span>. Use it to write an equation for the plane <span class="math-inline">\\(\operatorname{colsp}(A)\\)</span>. Is <span class="math-inline">\\(\vec b\\)</span> in this plane?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Project <span class="math-inline">\\(\vec b\\)</span> onto the line spanned by <span class="math-inline">\\(\vec n\\)</span>. Subtract this projection from <span class="math-inline">\\(\vec b\\)</span> to find <span class="math-inline">\\(\vec p\\)</span>. Explain why subtracting the normal component gives the closest vector in the plane.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Find <span class="math-inline">\\(\vec x^{\ast}\\)</span> that satisfies <span class="math-inline">\\(A^TA\vec x^{\ast}=A^T\vec b\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
Compute <span class="math-inline">\\(A\vec x^{\ast}\\)</span> and verify that it equals the vector <span class="math-inline">\\(\vec p\\)</span> you found geometrically. How many entries does each vector have? Explain how the entries of <span class="math-inline">\\(\vec x^{\ast}\\)</span> combine the columns of <span class="math-inline">\\(A\\)</span> to produce <span class="math-inline">\\(\vec p\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
Keep <span class="math-inline">\\(A\\)</span> fixed. Can <span class="math-inline">\\(\vec p\\)</span> be viewed as a linear transformation of <span class="math-inline">\\(\vec b\\)</span>? Find the corresponding matrix <span class="math-inline">\\(P\\)</span> in terms of <span class="math-inline">\\(A\\)</span>. State its shape. You may leave <span class="math-inline">\\(P\\)</span> as a product of matrices. Explain the difference between <span class="math-inline">\\(\vec x^{\ast}\\)</span>, <span class="math-inline">\\(\vec p\\)</span>, and <span class="math-inline">\\(P\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">f)</div>
<div class="assignment-part-content" markdown="1">
Let <span class="math-inline">\\(\vec a&#95;1\\)</span> and <span class="math-inline">\\(\vec a&#95;2\\)</span> be the columns of <span class="math-inline">\\(A\\)</span>. Suppose we add a third column equal to <span class="math-inline">\\(\vec a&#95;1+\vec a&#95;2\\)</span>, forming

<div class="math-display">
$$
\widetilde A=\begin{bmatrix}1&2&3\\1&-2&-1\\1&0&1\end{bmatrix}.
$$
</div>

 Without doing any new matrix calculations, explain whether this changes the column space, the closest vector to <span class="math-inline">\\(\vec b\\)</span>, or the minimum possible distance to <span class="math-inline">\\(\vec b\\)</span>.

</div>
</div>

</div>

---

## Activity 2: Fitting a line

Consider the dataset below. Find the line <span class="math-inline">\\(y=c+mt\\)</span> that best fits the data, meaning its sum of squared errors is minimized. Draw the line on the plot below.

<em>Hint: You have already done most of the work for this.</em>

<table>
<thead>
<tr>
<th style="text-align: center;"><span class="math-inline">\(t\)</span></th>
<th style="text-align: center;"><span class="math-inline">\(y\)</span></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><span class="math-inline">\(2\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(-7\)</span></td>
</tr>
<tr>
<td style="text-align: center;"><span class="math-inline">\(-2\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(13\)</span></td>
</tr>
<tr>
<td style="text-align: center;"><span class="math-inline">\(0\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(0\)</span></td>
</tr>
</tbody>
</table>

<img src="imgs/lab12-line-data.png" alt="image" style="width: 4in; max-width: 100%;">

{% endraw %}
