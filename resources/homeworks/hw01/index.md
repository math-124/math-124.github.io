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

# Homework 1: Mathematical Foundations

**due** Tuesday, September 8th at 11:59PM

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw01/hw01.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw01/hw01-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
Write your solutions to the following problems either by writing them on a piece of paper or on a tablet and scanning your answers as a PDF. Note that you are not allowed to use LaTeX, Google Docs, or any other digital document creation software to type your answers. Homeworks are due to Pensive by 11:59PM on the due date. See the [syllabus](https://math124.org/syllabus/#homework) for details on the slip day policy.

Homework will be evaluated not only on the correctness of your answers, but on your ability to present your ideas clearly and logically. You should always explain and justify your conclusions, using sound reasoning. Your goal should be to convince the reader of your assertions. If a question does not require explanation, it will be explicitly stated.

Before proceeding, make sure you're familiar with the [collaboration policy](https://math124.org/syllabus/#collaboration-and-generative-ai-policy).
</div>

---

## Problems

- [Problem 1: Triangle Time](#problem-1-triangle-time-24-pts)
- [Problem 2: Paralleling the Lab Activity](#problem-2-paralleling-the-lab-activity-14-pts)
- [Problem 3: Bob the Builder](#problem-3-bob-the-builder-16-pts)
- [Problem 4: Mathematical Feng Shui](#problem-4-mathematical-feng-shui-16-pts)
- [Problem 5: A Systematic Start](#problem-5-a-systematic-start-16-pts)
- [Problem 6: Programming Activity](#problem-6-programming-activity-14-pts)

---

Total Points: 24 + 14 + 16 + 16 + 16 + 14 = 100

---

## Problem 1: Triangle Time (24 pts)

Solve each part using any method you'd like. But, as with all homework problems, explain your solutions clearly. For expressions involving square roots or inverse trigonometric functions, make sure to provide both the unsimplified expression (e.g. <span class="math-inline">\\(2 \cos^{-1}\left(\frac{1}{3}\right)\\)</span> or <span class="math-inline">\\(\sqrt{15}\\)</span>) **and** a rounded estimate to two decimal places (e.g. <span class="math-inline">\\(141.06^\circ\\)</span> or <span class="math-inline">\\(3.87\\)</span>).

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(8 pts) Let <span class="math-inline">\\(A = (1, 2)\\)</span>, <span class="math-inline">\\(B = (8, 1)\\)</span>, and <span class="math-inline">\\(C = (6, 8)\\)</span>. Compute the area of the triangle ABC. See [**here**](https://edstem.org/us/courses/103314/discussion/8236522) on Ed for a hint.

<details markdown="1"><summary>Solution</summary>

There are two different approaches. One is to inscribe the triangle in a rectangle:

<div style="text-align: center;">
<img src="imgs/hw01-plot-01.png" alt="Coordinate diagram" class="assignment-vector-plot">
</div>

The rectangle has area <span class="math-inline">\\(49\\)</span>, while the three triangles each have areas <span class="math-inline">\\(15,7,\frac{7}{2}\\)</span>. Hence the area is <span class="math-inline">\\(49 - 15-7-\frac{7}{2} = \frac{47}{2}\\)</span>.

The other is to internally subdivide the triangle into three pieces:

<div style="text-align: center;">
<img src="imgs/hw01-plot-02.png" alt="Coordinate diagram" class="assignment-vector-plot">
</div>

The three internal triangles have areas <span class="math-inline">\\(15,6,\frac{5}{2}\\)</span>, hence the area of the triangle is the sum of these areas which is <span class="math-inline">\\(15+6+\frac{5}{2} = \frac{47}{2}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(8 pts) A right triangle has side lengths <span class="math-inline">\\(9\\)</span> cm, <span class="math-inline">\\(18\\)</span> cm, and <span class="math-inline">\\(x\\)</span> cm. Compute **all possible** values of <span class="math-inline">\\(x\\)</span>, and find all three angles of the triangle in each case.

<details markdown="1"><summary>Solution</summary>

Here <span class="math-inline">\\(x\\)</span> can either be the base/height or the hypotenuse. We use Pythagoras' theorem to find the length of <span class="math-inline">\\(x\\)</span> and inverse trigonometric functions to find the angles.

For the first case, <span class="math-inline">\\(x=\sqrt{18^2 - 9^2} = 9\sqrt{3}\approx 15.59\text{ cm}\\)</span> and the angles are 30, 60, and 90 degrees.

For the second case, <span class="math-inline">\\(x = \sqrt{9^2 + 18^2} = 9\sqrt{5}\approx 20.12\text{ cm}\\)</span> and the angles are <span class="math-inline">\\(\sin^{-1}(1/\sqrt{5})\approx 26.57\\)</span>, <span class="math-inline">\\(\sin^{-1}(2/\sqrt{5}) \approx 63.43\\)</span>, and 90 degrees. Other valid answers for the first angle are <span class="math-inline">\\(\cos^{-1}(2/\sqrt{5})\\)</span> or <span class="math-inline">\\(\tan^{-1}(1/2)\\)</span>; for the second angle are <span class="math-inline">\\(\cos^{-1}(1/\sqrt5)\\)</span> or <span class="math-inline">\\(\tan^{-1}(2)\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(8 pts) In a triangle <span class="math-inline">\\(ABC\\)</span>, let side <span class="math-inline">\\(a = 9\\)</span> cm, side <span class="math-inline">\\(b = 17\\)</span> cm, and angle <span class="math-inline">\\(C = 13^\circ\\)</span>. Compute the length of side <span class="math-inline">\\(c\\)</span>, and the angles <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span> in degrees. <em>Hint: use the law of cosines and law of sines.</em>

<details markdown="1"><summary>Solution</summary>

By the law of cosines,

<div class="math-display">
$$
c= \sqrt{9^2 + 17^2 - 2\cdot 9\cdot 17\cos C} = \sqrt{370 - 306\cos(13^\circ)} \approx 8.48\text{ cm}.
$$
</div>

 Sketching the triangle, we see that <span class="math-inline">\\(A\\)</span> must be an acute angle, while <span class="math-inline">\\(B\\)</span> must be obtuse. Finding the angle at <span class="math-inline">\\(A\\)</span> using the law of sines, we obtain

<div class="math-display">
$$
A = \sin^{-1}\left(\frac{9\sin(13^\circ)}{\sqrt{370 - 306\cos(13^\circ)}}\right) \approx 13.82^\circ.
$$
</div>

 The remaining angle at <span class="math-inline">\\(B\\)</span> is found by subtracting the angles at <span class="math-inline">\\(A,C\\)</span> from 180 degrees:

<div class="math-display">
$$
B = 180^\circ - 13^\circ - \sin^{-1}\left(\frac{9\sin(13^\circ)}{\sqrt{370 - 306\cos(13^\circ)}}\right) \approx 153.18^\circ.
$$
</div>

</details>

</div>
</div>

</div>

---

## Problem 2: Paralleling the Lab Activity (14 pts)

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
(4 pts) Plot the line by hand. Make sure to label your axes and label at least two points on the line.

<details markdown="1"><summary>Solution</summary>

The line has slope <span class="math-inline">\\(\frac{2}{3}\\)</span>, <span class="math-inline">\\(x\\)</span>-intercept <span class="math-inline">\\((3,0)\\)</span>, and <span class="math-inline">\\(y\\)</span>-intercept <span class="math-inline">\\((0,-2)\\)</span>.

<div style="text-align: center;">
<img src="imgs/hw01-plot-03.png" alt="Coordinate diagram" class="assignment-vector-plot">
</div>
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Find an equation for a line that is parallel to this line and passes through the point <span class="math-inline">\\((5,3)\\)</span>.

<details markdown="1"><summary>Solution</summary>

The answer is <span class="math-inline">\\(2x-3y=1\\)</span>. An equivalent form is <span class="math-inline">\\(y = \frac{2}{3}x - \frac{1}{3}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Find an equation for a line that is perpendicular to this line and passes through the point <span class="math-inline">\\((1,2)\\)</span>.

<details markdown="1"><summary>Solution</summary>

Tne answer is <span class="math-inline">\\(3x+2y=7\\)</span>. An equivalent form is <span class="math-inline">\\(y = -\frac{3}{2}x + \frac{7}{2}\\)</span>.
</details>

</div>
</div>

</div>

---

## Problem 3: Bob the Builder (16 pts)

Write each of the following sets in set-builder notation. Refer to [Chapter 1.2](https://notes.math124.org/ch01/01-02/) of the course notes and Lab 1 for examples.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) All even integers.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(\lbrace{}2x : x \in \mathbb{Z}\rbrace{}\\)</span>; another valid answer is <span class="math-inline">\\(\lbrace{} x\in \mathbb{Z}: x=2n,\ n\in \mathbb{Z}\rbrace{}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) All <span class="math-inline">\\(y\\)</span>-values of points on the parabola <span class="math-inline">\\(y = x^2+3\\)</span>.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(\lbrace{}y \in \mathbb{R} : y = x^2+3, x \in \mathbb{R}\rbrace{}\\)</span>; other valid answers include <span class="math-inline">\\(\lbrace{} y\in \mathbb{R}: y\geq 3\rbrace{}\\)</span> and <span class="math-inline">\\(\lbrace{} x^2 + 3: x\in \mathbb{R} \rbrace{}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) The unit circle in <span class="math-inline">\\(\mathbb{R}^2\\)</span> (two-dimensional space), i.e., the circle with center <span class="math-inline">\\((0,0)\\)</span> and radius <span class="math-inline">\\(1\\)</span>.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(\lbrace{}\begin{bmatrix} x\\\\y \end{bmatrix} \in \mathbb{R}^2 : x^2 + y^2 = 1\rbrace{}\\)</span> or <span class="math-inline">\\(\lbrace{}(x,y) \in \mathbb{R}^2 : x^2 + y^2 = 1\rbrace{}\\)</span> or other equivalent forms.
</details>

</div>
</div>

</div>

---

## Problem 4: Mathematical Feng Shui (16 pts)

In each of the following subparts, you are given a problem along with a potential solution. Identify the mistakes in each solution, and rewrite the solution so that it is mathematically valid. *Note that a solution may yield the right answer, but may make grammatical mistakes along the way.*

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(7 pts) Problem: Solve for <span class="math-inline">\\(x\\)</span> in the equation

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

<details markdown="1"><summary>Solution</summary>

A correctly written solution is

<div class="math-display">
$$
\begin{aligned}
3(x-2)+4&=2x+7,\\
3x-2&=2x+7,\\
x&=9.
\end{aligned}
$$
</div>

 The original answer incorrectly chains together expressions and equations with equals signs. While it correctly finds that <span class="math-inline">\\(x=9\\)</span>, it is not true that <span class="math-inline">\\(3(x-2) + 4 = 9\\)</span>, which is an implication of the equation written.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(9 pts) Problem: Solve the inequality

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

<details markdown="1"><summary>Solution</summary>

The issue with the provided solution is that we don't know the sign of <span class="math-inline">\\(x\\)</span>. If <span class="math-inline">\\(x\\)</span> were negative, then multiplying both sides of the inequality by <span class="math-inline">\\(x\\)</span> would require changing the direction of the inequality.

Here are two ways to correctly present this solution.

<ul>
<li><p>Notice that <span class="math-inline">\(\frac{1}{x} &gt; 2\)</span> implies that <span class="math-inline">\(x &gt; 0\)</span>, because if <span class="math-inline">\(x\)</span> were negative, then the left-hand side would be negative and could never be greater than positive <span class="math-inline">\(2\)</span>. Then, when <span class="math-inline">\(x &gt; 0\)</span>, we can multiply both sides of <span class="math-inline">\(\frac{1}{x} &gt; 2\)</span> by <span class="math-inline">\(x\)</span> without needing to change the direction of the inequality (as the original solution did), giving <span class="math-inline">\(1 &gt; 2x\)</span> and <span class="math-inline">\(\frac{1}{2} &gt; x\)</span>. This makes the complete solution <span class="math display">\[\{ x \in \mathbb{R} : 0 &lt; x &lt; \frac{1}{2} \}\]</span></p></li>
<li><p>Start from scratch, and break into two cases: <span class="math-inline">\(x &gt; 0\)</span> and <span class="math-inline">\(x &lt; 0\)</span>. (<span class="math-inline">\(x = 0\)</span> is not a valid case; we can’t divide by <span class="math-inline">\(0\)</span>).</p>
<ul>
<li><p><span class="math-inline">\(x &gt; 0\)</span>: Same logic as above.</p></li>
<li><p><span class="math-inline">\(x &lt; 0\)</span>: From <span class="math-inline">\(\frac{1}{x} &gt; 2\)</span>, we multiply both sides by <span class="math-inline">\(x\)</span> to get <span class="math display">\[1 &lt; 2x.\]</span> Notice that the direction of the inequality is flipped here since we are assuming <span class="math-inline">\(x\)</span> to be negative in this case. Then, dividing both sides by <span class="math-inline">\(2\)</span> gives <span class="math-inline">\(\frac{1}{2} &lt; x\)</span>. But, it is impossible for <span class="math-inline">\(x\)</span> to be less than <span class="math-inline">\(0\)</span> and greater than <span class="math-inline">\(\frac{1}{2}\)</span> at the same time – this is a <strong>contradiction</strong>. So, no values of <span class="math-inline">\(x\)</span> can satisfy the inequality and be negative.</p></li>
</ul></li>
</ul>
</details>

</div>
</div>

</div>

---

## Problem 5: A Systematic Start (16 pts)

A big focus of this class is learning how to solve systems of equations at scale. For now, let's review your prior knowledge of solving systems. Each part of this problem defines a system of equations --- your job is to state it and solve it without any calculator or software assistance.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(7 pts) The University of Michigan has been hacked by conniving tricksters, and now their football ticket prices are all wrong! One boothsperson reported that they sold 3 student tickets and 5 adult tickets for <span class="currency tex2jax_ignore">$87.50</span>. Another boothsperson reported that they sold 41 student tickets and 6 adult tickets for <span class="currency tex2jax_ignore">$217.20</span>. What are the current costs of 1 student ticket and 1 adult ticket?

<details markdown="1"><summary>Solution</summary>

Set the student ticket price as <span class="math-inline">\\(x\\)</span> and the adult ticket price as <span class="math-inline">\\(y\\)</span>. The system is

<div class="math-display">
$$
\begin{cases}
        3x+5y=87.50,\\
        41x+6y=217.20.
      \end{cases}
$$
</div>

 We eliminate <span class="math-inline">\\(y\\)</span> by multiplying 6 to the first equation, 5 to the second equation and then subtracting the first from the second. This gives <span class="math-inline">\\(187x=561\\)</span>, so <span class="math-inline">\\(x=3\\)</span>. Substituting this into the first equation gives <span class="math-inline">\\(y=15.70\\)</span>. Hence the student ticket is <span class="currency tex2jax_ignore">$3.00</span> and the adult ticket is <span class="currency tex2jax_ignore">$15.70</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(9 pts) You, Sarah, and Stephen each have a pet bug. Each bug begins at position <span class="math-inline">\\(0\\)</span> on the number line. A positive position means that the bug moved to the right of its starting point, while a negative position means that it moved to the left.

At the end of the experiment, the following statements are true:

-   The sum of the three bugs' final positions is <span class="math-inline">\\(35\\)</span> centimeters.

-   Five times your bug's position, plus four times Sarah's bug's position, plus Stephen's bug's position is <span class="math-inline">\\(7\\)</span> centimeters.

-   Stephen's bug is <span class="math-inline">\\(7\\)</span> centimeters to the right of Sarah's bug.

Find the final position of each bug. If the winner is the bug whose final position has the greatest absolute value, which bug wins?

<details markdown="1"><summary>Solution</summary>

Let <span class="math-inline">\\(x\\)</span>, <span class="math-inline">\\(y\\)</span>, and <span class="math-inline">\\(z\\)</span> be your, Sarah's, and Stephen's bugs' final positions, respectively. Then the system of equations is

<div class="math-display">
$$
\begin{cases}
        x+y+z=35,\\
        5x+4y+z=7,\\
        z=y+7.
      \end{cases}
$$
</div>

 Substituting <span class="math-inline">\\(z=y+7\\)</span> into the first two equations gives <span class="math-inline">\\(x+2y=28\\)</span> and <span class="math-inline">\\(5x+5y=0\\)</span>. The second equation gives <span class="math-inline">\\(x=-y\\)</span>, so substituting this into the first gives <span class="math-inline">\\(y=28\\)</span>. It follows that <span class="math-inline">\\(x=-28\\)</span> and <span class="math-inline">\\(z=35\\)</span>. Therefore your bug finishes at <span class="math-inline">\\(-28\\)</span> cm, Sarah's at <span class="math-inline">\\(28\\)</span> cm, and Stephen's at <span class="math-inline">\\(35\\)</span> cm. Stephen's bug wins.
</details>

</div>
</div>

</div>

---

## Problem 6: Programming Activity (14 pts)

Most homeworks and some labs will have a Jupyter Notebook, containing Python code that supplements our understanding of the relevant mathematical ideas of the week.

To open the notebook for Homework 1, click [**this link**](https://colab.research.google.com/github/math-124/fa26-code/blob/main/homeworks/hw01/hw01.ipynb). Instructions on how to use Google Colab are at [math124.org/running-code](https://math124.org/running-code).

You do not need to submit the notebook anywhere. To get credit for the work you did in this notebook, include screenshots of the following parts of your notebook as part of your PDF submission to Homework 1 on Pensive, specifically under Problem 6:

-   A screenshot of the **code** you wrote in Task 2, to implement the sepia filter.

-   A screenshot of the grayscale and sepia versions of the image you uploaded.

{% endraw %}
