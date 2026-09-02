---
layout: page
title: "Homework 1: Mathematical Foundations"
description: "Homework 1: Mathematical Foundations problems."
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

# Homework 1: Mathematical Foundations

**due** Tuesday, September 8th at 11:59PM

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw01/hw01.pdf" target="_blank">View as PDF ✏️</a>
</div>

{: .yellow }
<div markdown="1">
Write your solutions to the following problems either by writing them on a piece of paper or on a tablet and scanning your answers as a PDF. Note that you are not allowed to use LaTeX, Google Docs, or any other digital document creation software to type your answers. Homeworks are due to Pensive by 11:59PM on the due date. See the [syllabus](https://math124.org/syllabus/#homework) for details on the slip day policy.

Homework will be evaluated not only on the correctness of your answers, but on your ability to present your ideas clearly and logically. You should always explain and justify your conclusions, using sound reasoning. Your goal should be to convince the reader of your assertions. If a question does not require explanation, it will be explicitly stated.

Before proceeding, make sure you're familiar with the [collaboration policy](https://math124.org/syllabus/#collaboration-and-generative-ai-policy).
</div>

---

## Problems

- [Problem 1: Triangle Time](#problem-1-triangle-time)
- [Problem 2: Paralleling the Lab Activity](#problem-2-paralleling-the-lab-activity)
- [Problem 3: Bob the Builder](#problem-3-bob-the-builder)
- [Problem 4: Mathematical Feng Shui](#problem-4-mathematical-feng-shui)
- [Problem 5: A Systematic Start](#problem-5-a-systematic-start)
- [Problem 6: Programming Activity](#problem-6-programming-activity)

---

## Problem 1: Triangle Time

Solve each part using any method you'd like. But, as with all homework problems, explain your solutions clearly. For expressions involving square roots or inverse trigonometric functions, make sure to provide both the unsimplified expression (e.g. <span class="math-inline">\\(2 \cos^{-1}\left(\frac{1}{3}\right)\\)</span> or <span class="math-inline">\\(\sqrt{15}\\)</span>) **and** a rounded estimate to two decimal places (e.g. <span class="math-inline">\\(141.06^\circ\\)</span> or <span class="math-inline">\\(3.87\\)</span>).

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Let <span class="math-inline">\\(A = (1, 2)\\)</span>, <span class="math-inline">\\(B = (8, 1)\\)</span>, and <span class="math-inline">\\(C = (6, 8)\\)</span>. Compute the area of the triangle ABC.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
A right triangle has side lengths <span class="math-inline">\\(9\\)</span> cm, <span class="math-inline">\\(18\\)</span> cm, and <span class="math-inline">\\(x\\)</span> cm. Compute **all possible** values of <span class="math-inline">\\(x\\)</span>, and find all three angles of the triangle in each case.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
In a triangle <span class="math-inline">\\(ABC\\)</span>, let side <span class="math-inline">\\(a = 9\\)</span> cm, side <span class="math-inline">\\(b = 17\\)</span> cm, and angle <span class="math-inline">\\(C = 13^\circ\\)</span>. Compute the length of side <span class="math-inline">\\(c\\)</span>, and the angles <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span> in degrees. <em>Hint: use the law of cosines and law of sines.</em>

</div>
</div>

</div>

---

## Problem 2: Paralleling the Lab Activity

Consider the line

<div class="math-display">
$$
2x-3y=6.
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Plot the line by hand. Make sure to label your axes and label at least two points on the line.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Find an equation for a line that is parallel to this line and passes through the point <span class="math-inline">\\((5,3)\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Find an equation for a line that is perpendicular to this line and passes through the point <span class="math-inline">\\((1,2)\\)</span>.

</div>
</div>

</div>

---

## Problem 3: Bob the Builder

Write each of the following sets in set-builder notation. Refer to [Chapter 1.2](https://notes.math124.org/ch01/01-02/) of the course notes and Lab 1 for examples.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
All even integers.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
All <span class="math-inline">\\(y\\)</span>-values of points on the parabola <span class="math-inline">\\(y = x^2+3\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
The unit circle in <span class="math-inline">\\(\mathbb{R}^2\\)</span> (two-dimensional space), i.e., the circle with center <span class="math-inline">\\((0,0)\\)</span> and radius <span class="math-inline">\\(1\\)</span>.

</div>
</div>

</div>

---

## Problem 4: Mathematical Feng Shui

In each of the following subparts, you are given a problem along with a potential solution. Identify the mistakes in each solution, and rewrite the solution so that it is mathematically valid. *Note that a solution may yield the right answer, but may make grammatical mistakes along the way.*

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Problem: Solve for <span class="math-inline">\\(x\\)</span> in the equation

<div class="math-display">
$$
3(x-2)+4=2x+7.
$$
</div>

Solution:

<table>
<tbody>
<tr>
<td style="text-align: right;"><span style="color: gray">1</span></td>
<td style="text-align: left;"><span class="math-inline">\(3(x-2)+4=3x-2=2x+7=x=9.\)</span></td>
</tr>
</tbody>
</table>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Problem: Solve the inequality

<div class="math-display">
$$
\frac{1}{x}>2.
$$
</div>

Solution:

<table>
<tbody>
<tr>
<td style="text-align: right;"><span style="color: gray">1</span></td>
<td style="text-align: left;"><span class="math-inline">\(\displaystyle \frac{1}{x}&gt;2\)</span></td>
</tr>
<tr>
<td style="text-align: right;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: right;"><span style="color: gray">2</span></td>
<td style="text-align: left;"><span class="math-inline">\(1&gt;2x\)</span></td>
</tr>
<tr>
<td style="text-align: right;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: right;"><span style="color: gray">3</span></td>
<td style="text-align: left;"><span class="math-inline">\(\displaystyle x&lt;\frac{1}{2}\)</span></td>
</tr>
<tr>
<td style="text-align: right;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: right;"><span style="color: gray">4</span></td>
<td style="text-align: left;">So, the solution set is <span class="math-inline">\(\{x \in \mathbb{R}: x &lt; \frac{1}{2} \}\)</span>.</td>
</tr>
</tbody>
</table>

</div>
</div>

</div>

---

## Problem 5: A Systematic Start

A big focus of this class is learning how to solve systems of equations at scale. For now, let's review your prior knowledge of solving systems. Each part of this problem defines a system of equations --- your job is to state it and solve it without any calculator or software assistance.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
The University of Michigan has been hacked by conniving tricksters, and now their football ticket prices are all wrong! One boothsperson reported that they sold 3 student tickets and 5 adult tickets for <span class="currency tex2jax_ignore">$87.50</span>. Another boothsperson reported that they sold 41 student tickets and 6 adult tickets for <span class="currency tex2jax_ignore">$217.20</span>. What are the current costs of 1 student ticket and 1 adult ticket?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
You, Sarah, and Stephen each have a pet bug. Each bug begins at position <span class="math-inline">\\(0\\)</span> on the number line. A positive position means that the bug moved to the right of its starting point, while a negative position means that it moved to the left.

At the end of the experiment, the following statements are true:

-   The sum of the three bugs' final positions is <span class="math-inline">\\(35\\)</span> centimeters.

-   Five times your bug's position, plus four times Sarah's bug's position, plus Stephen's bug's position is <span class="math-inline">\\(7\\)</span> centimeters.

-   Stephen's bug is <span class="math-inline">\\(7\\)</span> centimeters to the right of Sarah's bug.

Find the final position of each bug. If the winner is the bug whose final position has the greatest absolute value, which bug wins?

</div>
</div>

</div>

---

## Problem 6: Programming Activity

Most homeworks and some labs will have a Jupyter Notebook, containing Python code that supplements our understanding of the relevant mathematical ideas of the week.

To open the notebook for Homework 1, click **this link, coming soon**. Instructions on how to use Google Colab are at [math124.org/running-code](https://math124.org/running-code).

Instructions on what to submit from your notebook are coming soon.

{% endraw %}
