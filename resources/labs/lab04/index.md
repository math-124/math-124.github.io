---
layout: page
title: "Lab 4: Lines and Planes in $\\mathbb{R}^3$"
description: "Lab 4: Lines and Planes in $\\mathbb{R}^3$ activities."
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

# Lab 4: Lines and Planes in $\mathbb{R}^3$

**due** by the end of class on Wednesday, September 23, 2026

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab04/lab04.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab04/lab04-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
Each lab worksheet will contain several activities, most of which will involve writing math on paper, and some of which will involve running code in a Jupyter Notebook. To receive credit for today's lab, you must show your lab TA your work on this worksheet.

While you must get checked off by your lab TA **individually**, we encourage you to form groups with 1-2 other students to complete the activities together.
</div>

---

## Activities

- [Activity 1: The Span of One Vector](#activity-1-the-span-of-one-vector)
- [Activity 2: The Same Plane, Different Directions](#activity-2-the-same-plane-different-directions)
- [Activity 3: A Plane in Two Forms](#activity-3-a-plane-in-two-forms)
- [Activity 4: A Line in Equation Form](#activity-4-a-line-in-equation-form)
- [Activity 5: An Affine Line in Parametric Form](#activity-5-an-affine-line-in-parametric-form)
- [Activity 6: An Affine Plane in Parametric Form](#activity-6-an-affine-plane-in-parametric-form)
- [Activity 7: An Equation for an Affine Plane](#activity-7-an-equation-for-an-affine-plane)
- [Activity 8: An Affine Line as the Solution of a Linear System](#activity-8-an-affine-line-as-the-solution-of-a-linear-system)

---

Today's lab is split into two parts, all of which are covered in Chapter 2.4 of the course notes:

-   Activities 1-4 involve content from the previous two lectures.

-   Activities 5-8 involve affine lines and planes in <span class="math-inline">\\(\mathbb{R}^3\\)</span> -- that is, objects that don't necessarily pass through the origin, <span class="math-inline">\\((0,0,0)\\)</span>. We will give a brief overview of these in lab and revisit them in tomorrow's lecture. (Activities 5-8 are the same as Questions 5-8 from yesterday's lecture worksheet, which we didn't get to.)

---

## Activity 1: The Span of One Vector

The line <span class="math-inline">\\(\ell\\)</span> is given in scalar-parametric form by

<div class="math-display">
$$
x=5t,\qquad y=-9t,\qquad z=2t,\qquad t\in\mathbb{R}.
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find a vector <span class="math-inline">\\(\vec{u}\\)</span> such that <span class="math-inline">\\(\ell=\operatorname{span}(\vec{u})\\)</span>.

<details markdown="1"><summary>Solution</summary>

The line <span class="math-inline">\\(\ell\\)</span> consists of all scalar multiples of a single direction vector. Any nonzero point on <span class="math-inline">\\(\ell\\)</span> gives such a direction vector; setting <span class="math-inline">\\(t=1\\)</span> is convenient because we can read the coefficients directly:

<div class="math-display">
$$
\vec{u}=\begin{bmatrix}5\\-9\\2\end{bmatrix}.
$$
</div>

 Then every point on <span class="math-inline">\\(\ell\\)</span> has the form <span class="math-inline">\\(t\vec{u}\\)</span>, so

<div class="math-display">
$$
\ell=\{t\vec{u}:t\in\mathbb{R}\}=\operatorname{span}(\vec{u}).
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Find a different vector with the same span. Explain why your vector describes the same line.

<details markdown="1"><summary>Solution</summary>

Scaling a direction vector does not change the line it determines. Any nonzero scalar multiple of <span class="math-inline">\\(\vec{u}\\)</span> has the same span. For example,

<div class="math-display">
$$
\vec{w}=\begin{bmatrix}10\\-18\\4\end{bmatrix}=2\vec{u}.
$$
</div>

 To see that <span class="math-inline">\\(\operatorname{span}(\vec{w})=\operatorname{span}(\vec{u})\\)</span>, we check both containments. If <span class="math-inline">\\(\vec{x}\in\operatorname{span}(\vec{w})\\)</span>, then <span class="math-inline">\\(\vec{x}=c\vec{w}=c(2\vec{u})=(2c)\vec{u}\in\operatorname{span}(\vec{u})\\)</span>. Conversely, if <span class="math-inline">\\(\vec{x}=t\vec{u}\\)</span>, then <span class="math-inline">\\(\vec{x}=\frac{t}{2}\vec{w}\in\operatorname{span}(\vec{w})\\)</span>. So the two spans are equal and describe the same line through the origin.
</details>

</div>
</div>

</div>

---

## Activity 2: The Same Plane, Different Directions

The plane <span class="math-inline">\\(P\\)</span> is given in scalar-parametric form by

<div class="math-display">
$$
x=s+t,\qquad y=s-t,\qquad z=2t,\qquad s,t\in\mathbb{R}.
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find vectors <span class="math-inline">\\(\vec{u}\\)</span> and <span class="math-inline">\\(\vec{v}\\)</span> such that <span class="math-inline">\\(P=\operatorname{span}(\vec{u},\vec{v})\\)</span>.

<details markdown="1"><summary>Solution</summary>

Rewrite the parametric equations as a linear combination of two vectors, one for each parameter:

<div class="math-display">
$$
\begin{bmatrix}x\\y\\z\end{bmatrix}
=
s\begin{bmatrix}1\\1\\0\end{bmatrix}
+
t\begin{bmatrix}1\\-1\\2\end{bmatrix},
\qquad s,t\in\mathbb{R}.
$$
</div>

 The coefficients of <span class="math-inline">\\(s\\)</span> and <span class="math-inline">\\(t\\)</span> are the spanning vectors, so one choice is

<div class="math-display">
$$
\vec{u}=\begin{bmatrix}1\\1\\0\end{bmatrix},
\qquad
\vec{v}=\begin{bmatrix}1\\-1\\2\end{bmatrix}.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Are <span class="math-inline">\\(\vec{u}\\)</span> and <span class="math-inline">\\(\vec{v}\\)</span> the only pair of vectors that span <span class="math-inline">\\(P\\)</span>? Compute <span class="math-inline">\\(\vec{u}+\vec{v}\\)</span> and <span class="math-inline">\\(\vec{u}-\vec{v}\\)</span>, and explain why this pair also spans <span class="math-inline">\\(P\\)</span>. <em>Hint: Can you write each of <span class="math-inline">\\(\vec{u}\\)</span> and <span class="math-inline">\\(\vec{v}\\)</span> as a linear combination of <span class="math-inline">\\(\vec{u}+\vec{v}\\)</span> and <span class="math-inline">\\(\vec{u}-\vec{v}\\)</span>?</em>

<details markdown="1"><summary>Solution</summary>

No. A plane has many (in fact, infinitely!) pairs of spanning vectors. Any two vectors that live on the plane that are not scalar multiples of each other span the plane. Using the vectors from part (a),

<div class="math-display">
$$
\vec{u}+\vec{v}=\begin{bmatrix}2\\0\\2\end{bmatrix},
\qquad
\vec{u}-\vec{v}=\begin{bmatrix}0\\2\\-2\end{bmatrix}.
$$
</div>

 The key observation is that each original spanning vector is a linear combination of this new pair:

<div class="math-display">
$$
\vec{u}=\tfrac12(\vec{u}+\vec{v})+\tfrac12(\vec{u}-\vec{v}),
\qquad
\vec{v}=\tfrac12(\vec{u}+\vec{v})-\tfrac12(\vec{u}-\vec{v}).
$$
</div>

 So every vector in <span class="math-inline">\\(\operatorname{span}(\vec{u},\vec{v})\\)</span> can be built from <span class="math-inline">\\(\vec{u}+\vec{v}\\)</span> and <span class="math-inline">\\(\vec{u}-\vec{v}\\)</span>, and vice versa. Therefore

<div class="math-display">
$$
\operatorname{span}(\vec{u},\vec{v})
=
\operatorname{span}(\vec{u}+\vec{v},\vec{u}-\vec{v}).
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Use <span class="math-inline">\\(\vec{u}+\vec{v}\\)</span> and <span class="math-inline">\\(\vec{u}-\vec{v}\\)</span> to write a different scalar-parametric form for <span class="math-inline">\\(P\\)</span>. Write your answer as equations for <span class="math-inline">\\(x\\)</span>, <span class="math-inline">\\(y\\)</span>, and <span class="math-inline">\\(z\\)</span>, and state the possible values of your parameters.

<details markdown="1"><summary>Solution</summary>

Replace <span class="math-inline">\\(\vec{u}\\)</span> and <span class="math-inline">\\(\vec{v}\\)</span> with <span class="math-inline">\\(\vec{u}+\vec{v}\\)</span> and <span class="math-inline">\\(\vec{u}-\vec{v}\\)</span> in the vector form from part (a). Using parameters <span class="math-inline">\\(s,t\in\mathbb{R}\\)</span>,

<div class="math-display">
$$
\begin{bmatrix}x\\y\\z\end{bmatrix}
=
s\begin{bmatrix}2\\0\\2\end{bmatrix}
+
t\begin{bmatrix}0\\2\\-2\end{bmatrix}.
$$
</div>

 Reading off components gives

<div class="math-display">
$$
x=2s,\qquad y=2t,\qquad z=2s-2t,\qquad s,t\in\mathbb{R}.
$$
</div>

 This is a different parametrization of the same plane. For example, the original form with <span class="math-inline">\\(s=1,t=0\\)</span> gives <span class="math-inline">\\((1,1,0)\\)</span>, and here that point occurs when <span class="math-inline">\\(s=\tfrac12,t=\tfrac12\\)</span>.
</details>

</div>
</div>

</div>

---

## Activity 3: A Plane in Two Forms

Let

<div class="math-display">
$$
\vec{u}=\begin{bmatrix}5\\-7\\3\end{bmatrix},\qquad
\vec{v}=\begin{bmatrix}4\\1\\-2\end{bmatrix},\qquad
P=\operatorname{span}(\vec{u},\vec{v}).
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Write <span class="math-inline">\\(P\\)</span> in scalar-parametric form by writing three separate equations: one for <span class="math-inline">\\(x\\)</span>, one for <span class="math-inline">\\(y\\)</span>, and one for <span class="math-inline">\\(z\\)</span>. All three should use the same two parameters, <span class="math-inline">\\(s,t\in\mathbb{R}\\)</span>.

<details markdown="1"><summary>Solution</summary>

Since <span class="math-inline">\\(P=\operatorname{span}(\vec{u},\vec{v})\\)</span>, every point in <span class="math-inline">\\(P\\)</span> has the form <span class="math-inline">\\(s\vec{u}+t\vec{v}\\)</span>:

<div class="math-display">
$$
\begin{bmatrix}x\\y\\z\end{bmatrix}
=
s\begin{bmatrix}5\\-7\\3\end{bmatrix}
+
t\begin{bmatrix}4\\1\\-2\end{bmatrix},
\qquad s,t\in\mathbb{R}.
$$
</div>

 Reading off components gives

<div class="math-display">
$$
x=5s+4t,\qquad y=-7s+t,\qquad z=3s-2t,\qquad s,t\in\mathbb{R}.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Find a nonzero vector <span class="math-inline">\\(\vec{n}\\)</span> that is perpendicular to both <span class="math-inline">\\(\vec{u}\\)</span> and <span class="math-inline">\\(\vec{v}\\)</span>. Verify your answer using dot products.

<details markdown="1"><summary>Solution</summary>

A vector normal to the plane must be orthogonal to both spanning vectors. If <span class="math-inline">\\(\vec{n}=\begin{bmatrix}a\\\\b\\\\c\end{bmatrix}\\)</span>, then

<div class="math-display">
$$
\vec{n}\cdot\vec{u}=5a-7b+3c=0,
\qquad
\vec{n}\cdot\vec{v}=4a+b-2c=0.
$$
</div>

 From the second equation, <span class="math-inline">\\(b=-4a+2c\\)</span>. Substituting into the first gives <span class="math-inline">\\(33a-11c=0\\)</span>, so <span class="math-inline">\\(c=3a\\)</span> and <span class="math-inline">\\(b=2a\\)</span>. Taking <span class="math-inline">\\(a=1\\)</span> gives

<div class="math-display">
$$
\vec{n}=\begin{bmatrix}1\\2\\3\end{bmatrix}.
$$
</div>

 Verification:

<div class="math-display">
$$
\vec{n}\cdot\vec{u}=5-14+9=0,
\qquad
\vec{n}\cdot\vec{v}=4+2-6=0.
$$
</div>

 Any nonzero scalar multiple of <span class="math-inline">\\(\vec{n}\\)</span> is also correct.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Use <span class="math-inline">\\(\vec{n}\\)</span> to write a linear equation of the form <span class="math-inline">\\(ax+by+cz=0\\)</span> for <span class="math-inline">\\(P\\)</span>. Graph your equation on Desmos, [desmos.com/3d](https://www.desmos.com/3d).

<details markdown="1"><summary>Solution</summary>

Because <span class="math-inline">\\(P\\)</span> passes through the origin, every point <span class="math-inline">\\(\begin{bmatrix}x\\\\y\\\\z\end{bmatrix}\\)</span> in <span class="math-inline">\\(P\\)</span> satisfies <span class="math-inline">\\(\vec{n}\cdot\begin{bmatrix}x\\\\y\\\\z\end{bmatrix}=0\\)</span>. With <span class="math-inline">\\(\vec{n}=\begin{bmatrix}1\\\\2\\\\3\end{bmatrix}\\)</span>, this becomes

<div class="math-display">
$$
x+2y+3z=0.
$$
</div>

 On Desmos 3D, graph this equation. It should match the parametric plane from part (a): same plane, just written in a different form.
</details>

</div>
</div>

</div>

---

## Activity 4: A Line in Equation Form

Consider the line from Activity 1:

<div class="math-display">
$$
\ell=\operatorname{span}\left(\begin{bmatrix}5\\-9\\2\end{bmatrix}\right).
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find two vectors that are both orthogonal to <span class="math-inline">\\(\begin{bmatrix}5\\\\-9\\\\2\end{bmatrix}\\)</span> and are not scalar multiples of each other, i.e. two linearly independent vectors on <span class="math-inline">\\(\ell^\perp\\)</span>.

<details markdown="1"><summary>Solution</summary>

We need two linearly independent vectors in <span class="math-inline">\\(\ell^\perp\\)</span>, the plane of vectors orthogonal to <span class="math-inline">\\(\ell\\)</span>. If <span class="math-inline">\\(\vec{n}=\begin{bmatrix}a\\\\b\\\\c\end{bmatrix}\\)</span> is orthogonal to <span class="math-inline">\\(\vec{d}=\begin{bmatrix}5\\\\-9\\\\2\end{bmatrix}\\)</span>, then

<div class="math-display">
$$
5a-9b+2c=0.
$$
</div>

 We can find two different solutions by setting convenient variables to zero. Setting <span class="math-inline">\\(a=0\\)</span> and <span class="math-inline">\\(b=2\\)</span> gives <span class="math-inline">\\(c=9\\)</span>, so

<div class="math-display">
$$
\vec{n}_1=\begin{bmatrix}0\\2\\9\end{bmatrix}.
$$
</div>

 Setting <span class="math-inline">\\(b=0\\)</span> and <span class="math-inline">\\(a=-2\\)</span> gives <span class="math-inline">\\(c=5\\)</span>, so

<div class="math-display">
$$
\vec{n}_2=\begin{bmatrix}-2\\0\\5\end{bmatrix}.
$$
</div>

 Check orthogonality:

<div class="math-display">
$$
\vec{n}_1\cdot\vec{d}=0-18+18=0,
\qquad
\vec{n}_2\cdot\vec{d}=-10+0+10=0.
$$
</div>

 These two vectors are not scalar multiples of each other, so they form a basis for <span class="math-inline">\\(\ell^\perp\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Use those vectors to write a system of two linear equations and three unknowns (<span class="math-inline">\\(x\\)</span>, <span class="math-inline">\\(y\\)</span>, and <span class="math-inline">\\(z\\)</span>) whose solution set is the line <span class="math-inline">\\(\ell\\)</span>.

<details markdown="1"><summary>Solution</summary>

Each vector <span class="math-inline">\\(\vec{n}&#95;i\\)</span> is normal to a plane through the origin. A point <span class="math-inline">\\(\begin{bmatrix}x\\\\y\\\\z\end{bmatrix}\\)</span> lies on that plane exactly when <span class="math-inline">\\(\vec{n}&#95;i\cdot\begin{bmatrix}x\\\\y\\\\z\end{bmatrix}=0\\)</span>. Since <span class="math-inline">\\(\ell\\)</span> passes through the origin, it is the intersection of the two planes orthogonal to <span class="math-inline">\\(\vec{n}&#95;1\\)</span> and <span class="math-inline">\\(\vec{n}&#95;2\\)</span>:

<div class="math-display">
$$
\begin{cases}
\vec{n}_1\cdot\begin{bmatrix}x\\y\\z\end{bmatrix}=0
\;\;\Longleftrightarrow\;\;
2y+9z=0,\\[4pt]
\vec{n}_2\cdot\begin{bmatrix}x\\y\\z\end{bmatrix}=0
\;\;\Longleftrightarrow\;\;
-2x+5z=0.
\end{cases}
$$
</div>

 A point lies on <span class="math-inline">\\(\ell\\)</span> exactly when it satisfies both equations.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Graph both equations on Desmos, [desmos.com/3d](https://www.desmos.com/3d). What do they look like?

<details markdown="1"><summary>Solution</summary>

Each equation describes a plane through the origin in <span class="math-inline">\\(\mathbb{R}^3\\)</span>. On Desmos, you should see two flat sheets that cross along a single line. That intersection line is exactly

<div class="math-display">
$$
\ell=\operatorname{span}\!\left(\begin{bmatrix}5\\-9\\2\end{bmatrix}\right).
$$
</div>

 This illustrates the general idea: a line through the origin can be described as the intersection of two planes through the origin.
</details>

The remaining activities are about affine lines and planes -- that is, objects that don't necessarily pass through the origin, <span class="math-inline">\\((0,0,0)\\)</span>. These are discussed at the bottom of Chapter 2.4. We will give a brief overview \~an hour into lab to help you get started.

<span class="answer-blank"></span>

</div>
</div>

</div>

---

## Activity 5: An Affine Line in Parametric Form

Let <span class="math-inline">\\(\displaystyle \ell' = \begin{bmatrix} 1\\\\ 2\\\\ -1 \end{bmatrix} + \operatorname{span} \left( \begin{bmatrix} 2\\\\ -1\\\\ 3 \end{bmatrix} \right).\\)</span>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Write <span class="math-inline">\\(\ell'\\)</span> explicitly in vector-parametric form.

<div class="math-display">
$$
\ell'
=
\left\{
\hspace{11cm}
\right\}.
$$
</div>

<details markdown="1"><summary>Solution</summary>

The notation <span class="math-inline">\\(\vec{p}+\operatorname{span}(\vec{d})\\)</span> means: start at the point <span class="math-inline">\\(\vec{p}\\)</span>, then add every scalar multiple of <span class="math-inline">\\(\vec{d}\\)</span>. Here <span class="math-inline">\\(\vec{p}=\begin{bmatrix}1\\\\2\\\\-1\end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec{d}=\begin{bmatrix}2\\\\-1\\\\3\end{bmatrix}\\)</span>, so

<div class="math-display">
$$
\ell'
=
\left\{
\begin{bmatrix}1\\2\\-1\end{bmatrix}
+
t\begin{bmatrix}2\\-1\\3\end{bmatrix}
:
t\in\mathbb{R}
\right\}.
$$
</div>

 When <span class="math-inline">\\(t=0\\)</span>, we get the point <span class="math-inline">\\((1,2,-1)\\)</span>; changing <span class="math-inline">\\(t\\)</span> moves along the line in the direction of <span class="math-inline">\\(\vec{d}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Write the corresponding scalar-parametric equations for <span class="math-inline">\\(x\\)</span>, <span class="math-inline">\\(y\\)</span>, and <span class="math-inline">\\(z\\)</span>.

<div class="math-display">
$$
\begin{aligned}
x&=\underline{\hspace{4cm}},\\[5pt]
y&=\underline{\hspace{4cm}},\\[5pt]
z&=\underline{\hspace{4cm}}.
\end{aligned}
$$
</div>

<details markdown="1"><summary>Solution</summary>

Expand the vector sum component-wise:

<div class="math-display">
$$
\begin{bmatrix}x\\y\\z\end{bmatrix}
=
\begin{bmatrix}1\\2\\-1\end{bmatrix}
+
t\begin{bmatrix}2\\-1\\3\end{bmatrix}
=
\begin{bmatrix}1+2t\\2-t\\-1+3t\end{bmatrix}.
$$
</div>

 So

<div class="math-display">
$$
\begin{aligned}
x&=1+2t,\\[5pt]
y&=2-t,\\[5pt]
z&=-1+3t.
\end{aligned}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Graph <span class="math-inline">\\(\ell'\\)</span> on Desmos, [desmos.com/3d](https://www.desmos.com/3d). To get the entire line to appear, you may have to change the upper and lower bounds for <span class="math-inline">\\(t\\)</span>.

<details markdown="1"><summary>Solution</summary>

In Desmos 3D, enter the parametric curve <span class="math-inline">\\((1+2t,2-t,-1+3t)\\)</span>. Unlike a line through the origin, this affine line passes through <span class="math-inline">\\((1,2,-1)\\)</span> but not through <span class="math-inline">\\((0,0,0)\\)</span>. You may need to widen the bounds for <span class="math-inline">\\(t\\)</span> so the entire line appears on screen.
</details>

</div>
</div>

</div>

---

## Activity 6: An Affine Plane in Parametric Form

Now let's switch to discussing affine planes. Let <span class="math-inline">\\(\displaystyle P' = \begin{bmatrix} 2\\\\ -1\\\\ 4 \end{bmatrix} + \operatorname{span} \left( \begin{bmatrix} 1\\\\ 2\\\\ -1 \end{bmatrix}, \begin{bmatrix} 2\\\\ -1\\\\ 3 \end{bmatrix} \right).\\)</span>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Write <span class="math-inline">\\(P'\\)</span> explicitly in vector-parametric form using two parameters <span class="math-inline">\\(s\\)</span> and <span class="math-inline">\\(t\\)</span>.

<div class="math-display">
$$
P'
=
\left\{
\hspace{11cm}
\right\}.
$$
</div>

<details markdown="1"><summary>Solution</summary>

An affine plane is a base point plus all linear combinations of two direction vectors. Here the base point is <span class="math-inline">\\(\begin{bmatrix}2\\\\-1\\\\4\end{bmatrix}\\)</span>, and the plane is spanned by <span class="math-inline">\\(\begin{bmatrix}1\\\\2\\\\-1\end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix}2\\\\-1\\\\3\end{bmatrix}\\)</span>:

<div class="math-display">
$$
P'
=
\left\{
\begin{bmatrix}2\\-1\\4\end{bmatrix}
+
s\begin{bmatrix}1\\2\\-1\end{bmatrix}
+
t\begin{bmatrix}2\\-1\\3\end{bmatrix}
:
s,t\in\mathbb{R}
\right\}.
$$
</div>

 When <span class="math-inline">\\(s=t=0\\)</span>, we get the point <span class="math-inline">\\((2,-1,4)\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Write the corresponding scalar-parametric equations for <span class="math-inline">\\(x\\)</span>, <span class="math-inline">\\(y\\)</span>, and <span class="math-inline">\\(z\\)</span>.

<div class="math-display">
$$
\begin{aligned}
x&=\underline{\hspace{4cm}},\\[5pt]
y&=\underline{\hspace{4cm}},\\[5pt]
z&=\underline{\hspace{4cm}}.
\end{aligned}
$$
</div>

<details markdown="1"><summary>Solution</summary>

Add the base point to the linear combination from part (a):

<div class="math-display">
$$
\begin{bmatrix}x\\y\\z\end{bmatrix}
=
\begin{bmatrix}2\\-1\\4\end{bmatrix}
+
s\begin{bmatrix}1\\2\\-1\end{bmatrix}
+
t\begin{bmatrix}2\\-1\\3\end{bmatrix}.
$$
</div>

 Reading off components gives

<div class="math-display">
$$
\begin{aligned}
x&=2+s+2t,\\[5pt]
y&=-1+2s-t,\\[5pt]
z&=4-s+3t.
\end{aligned}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Graph <span class="math-inline">\\(P'\\)</span> on Desmos. Start with <https://www.desmos.com/3d/llepnyv69l> (found by Googling "plane in parametric form on Desmos") and make modifications as necessary.

<details markdown="1"><summary>Solution</summary>

Use the scalar-parametric equations from part (b) in Desmos 3D. The graph should be a flat sheet through <span class="math-inline">\\((2,-1,4)\\)</span>. It is an *affine* plane because it does not necessarily pass through the origin: setting <span class="math-inline">\\(s=t=0\\)</span> gives <span class="math-inline">\\((2,-1,4)\\)</span>, but there is no choice of <span class="math-inline">\\(s,t\\)</span> that produces <span class="math-inline">\\((0,0,0)\\)</span>.
</details>

</div>
</div>

</div>

---

## Activity 7: An Equation for an Affine Plane

Consider the affine plane from Activity 6: <span class="math-inline">\\(\displaystyle P' = \begin{bmatrix} 2\\\\ -1\\\\ 4 \end{bmatrix} + \operatorname{span} \left( \begin{bmatrix} 1\\\\ 2\\\\ -1 \end{bmatrix}, \begin{bmatrix} 2\\\\ -1\\\\ 3 \end{bmatrix} \right).\\)</span>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find a nonzero normal vector <span class="math-inline">\\(\vec n\\)</span> perpendicular to both spanning vectors above.

<details markdown="1"><summary>Solution</summary>

The normal vector must be orthogonal to both spanning vectors. If <span class="math-inline">\\(\vec{n}=\begin{bmatrix}a\\\\b\\\\c\end{bmatrix}\\)</span>, then

<div class="math-display">
$$
a+2b-c=0,
\qquad
2a-b+3c=0.
$$
</div>

 From the first equation, <span class="math-inline">\\(c=a+2b\\)</span>. Substituting into the second gives <span class="math-inline">\\(5a+5b=0\\)</span>, so <span class="math-inline">\\(b=-a\\)</span> and <span class="math-inline">\\(c=-a\\)</span>. One choice is

<div class="math-display">
$$
\vec{n}=\begin{bmatrix}1\\-1\\-1\end{bmatrix}.
$$
</div>

 Verification:

<div class="math-display">
$$
\vec{n}\cdot\begin{bmatrix}1\\2\\-1\end{bmatrix}=1-2+1=0,
\qquad
\vec{n}\cdot\begin{bmatrix}2\\-1\\3\end{bmatrix}=2+1-3=0.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
A point <span class="math-inline">\\(\displaystyle \begin{bmatrix} x\\\\ y\\\\ z \end{bmatrix}\\)</span> lies in <span class="math-inline">\\(P'\\)</span> when <span class="math-inline">\\(\displaystyle \vec n\cdot \begin{bmatrix} x\\\\ y\\\\ z \end{bmatrix} = \vec n\cdot \begin{bmatrix} 2\\\\ -1\\\\ 4 \end{bmatrix}.\\)</span>

Compute the constant on the right-hand side.

<div class="math-display">
$$
\vec n\cdot
\begin{bmatrix}
2\\
-1\\
4
\end{bmatrix}
=
\underline{\hspace{4cm}}.
$$
</div>

<details markdown="1"><summary>Solution</summary>

Using <span class="math-inline">\\(\vec n=\begin{bmatrix}1\\\\-1\\\\-1\end{bmatrix}\\)</span> from the previous part, we get

<div class="math-display">
$$
\vec{n}\cdot\begin{bmatrix}2\\-1\\4\end{bmatrix}
=(1)(2)+(-1)(-1)+(-1)(4)
=2+1-4=-1.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Write an equation for <span class="math-inline">\\(P'\\)</span> in dot-product form.

<div class="math-display">
$$
\vec n\cdot
\begin{bmatrix}
x\\
y\\
z
\end{bmatrix}
=
\underline{\hspace{2cm}}.
$$
</div>

<details markdown="1"><summary>Solution</summary>

Substitute the constant from part (b):

<div class="math-display">
$$
\vec{n}\cdot\begin{bmatrix}x\\y\\z\end{bmatrix}=-1.
$$
</div>

 This is the dot-product form of the affine plane equation.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
Write a linear equation of the form <span class="math-inline">\\(ax+by+cz=d\\)</span> for <span class="math-inline">\\(P'\\)</span>.

<details markdown="1"><summary>Solution</summary>

Expanding the dot product gives

<div class="math-display">
$$
x-y-z=-1.
$$
</div>

 Notice that the right-hand side is <span class="math-inline">\\(-1\\)</span>, not <span class="math-inline">\\(0\\)</span>, because <span class="math-inline">\\(P'\\)</span> does not pass through the origin.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
Graph your equation for <span class="math-inline">\\(P'\\)</span> on Desmos, [desmos.com/3d](https://www.desmos.com/3d). Compare the graph with the one you made in Activity 6(c).

<details markdown="1"><summary>Solution</summary>

The graph of <span class="math-inline">\\(x-y-z=-1\\)</span> should match the parametric plane from Activity 6. Both describe the same affine plane <span class="math-inline">\\(P'\\)</span>; one uses parameters <span class="math-inline">\\(s,t\\)</span>, the other uses a single linear equation. You can check that <span class="math-inline">\\((2,-1,4)\\)</span> satisfies <span class="math-inline">\\(2-(-1)-4=-1\\)</span>.
</details>

</div>
</div>

</div>

---

## Activity 8: An Affine Line as the Solution of a Linear System

Finally, let's return to the affine line from Activity 5: <span class="math-inline">\\(\displaystyle \ell' = \begin{bmatrix} 1\\\\ 2\\\\ -1 \end{bmatrix} + \operatorname{span} \left( \begin{bmatrix} 2\\\\ -1\\\\ 3 \end{bmatrix} \right).\\)</span>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find two normal vectors <span class="math-inline">\\(\vec n&#95;1\\)</span> and <span class="math-inline">\\(\vec n&#95;2\\)</span> perpendicular to the direction vector above that are not scalar multiples of each other.

<details markdown="1"><summary>Solution</summary>

Use the same method as Activity 4, but with the correct direction vector for this line. If <span class="math-inline">\\(\vec{n}=\begin{bmatrix}a\\\\b\\\\c\end{bmatrix}\\)</span> is orthogonal to <span class="math-inline">\\(\vec{d}=\begin{bmatrix}2\\\\-1\\\\3\end{bmatrix}\\)</span>, then

<div class="math-display">
$$
2a-b+3c=0.
$$
</div>

 Setting <span class="math-inline">\\(a=0\\)</span> and <span class="math-inline">\\(b=3\\)</span> gives <span class="math-inline">\\(c=1\\)</span>, so

<div class="math-display">
$$
\vec{n}_1=\begin{bmatrix}0\\3\\1\end{bmatrix}.
$$
</div>

 Setting <span class="math-inline">\\(b=0\\)</span> and <span class="math-inline">\\(a=-3\\)</span> gives <span class="math-inline">\\(c=2\\)</span>, so

<div class="math-display">
$$
\vec{n}_2=\begin{bmatrix}-3\\0\\2\end{bmatrix}.
$$
</div>

 Check:

<div class="math-display">
$$
\vec{n}_1\cdot\vec{d}=0-3+3=0,
\qquad
\vec{n}_2\cdot\vec{d}=-6+0+6=0.
$$
</div>

 These are not scalar multiples of each other.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
A point <span class="math-inline">\\(\displaystyle \begin{bmatrix} x\\\\ y\\\\ z \end{bmatrix}\\)</span> lies on <span class="math-inline">\\(\ell'\\)</span> when <span class="math-inline">\\(\displaystyle \vec n&#95;1\cdot \begin{bmatrix} x\\\\ y\\\\ z \end{bmatrix} = \vec n&#95;1\cdot \begin{bmatrix} 1\\\\ 2\\\\ -1 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\displaystyle \vec n&#95;2\cdot \begin{bmatrix} x\\\\ y\\\\ z \end{bmatrix} = \vec n&#95;2\cdot \begin{bmatrix} 1\\\\ 2\\\\ -1 \end{bmatrix}.\\)</span>

Compute the two constants on the right-hand sides.

<div class="math-display">
$$
\vec n_1\cdot
\begin{bmatrix}
1\\
2\\
-1
\end{bmatrix}
=
\underline{\hspace{3cm}},
\qquad
\vec n_2\cdot
\begin{bmatrix}
1\\
2\\
-1
\end{bmatrix}
=
\underline{\hspace{3cm}}.
$$
</div>

<details markdown="1"><summary>Solution</summary>

Use the base point <span class="math-inline">\\(\begin{bmatrix}1\\\\2\\\\-1\end{bmatrix}\\)</span> on <span class="math-inline">\\(\ell'\\)</span>:

<div class="math-display">
$$
\vec{n}_1\cdot\begin{bmatrix}1\\2\\-1\end{bmatrix}
=0+6-1=5,
$$
</div>



<div class="math-display">
$$
\vec{n}_2\cdot\begin{bmatrix}1\\2\\-1\end{bmatrix}
=-3+0-2=-5.
$$
</div>

 Because <span class="math-inline">\\(\ell'\\)</span> is affine, these constants are generally nonzero.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Write a system of two linear equations and three unknowns (<span class="math-inline">\\(x\\)</span>, <span class="math-inline">\\(y\\)</span>, and <span class="math-inline">\\(z\\)</span>) whose solution set is <span class="math-inline">\\(\ell'\\)</span>.

<details markdown="1"><summary>Solution</summary>

Each normal vector determines a plane. A point lies on <span class="math-inline">\\(\ell'\\)</span> when it lies on both planes, so

<div class="math-display">
$$
\begin{cases}
\vec{n}_1\cdot\begin{bmatrix}x\\y\\z\end{bmatrix}=5
\;\;\Longleftrightarrow\;\;
3y+z=5,\\[4pt]
\vec{n}_2\cdot\begin{bmatrix}x\\y\\z\end{bmatrix}=-5
\;\;\Longleftrightarrow\;\;
-3x+2z=-5.
\end{cases}
$$
</div>

 Each equation describes a plane, and their intersection is the affine line <span class="math-inline">\\(\ell'\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
Graph both equations in your system on Desmos, [desmos.com/3d](https://www.desmos.com/3d). The two planes should intersect in the affine line <span class="math-inline">\\(\ell'\\)</span>. Compare the intersection with the graph from Activity 5(c).

<details markdown="1"><summary>Solution</summary>

On Desmos, graph the two planes <span class="math-inline">\\(3y+z=5\\)</span> and <span class="math-inline">\\(-3x+2z=-5\\)</span>. They should intersect in the same affine line as the parametric graph from Activity 5(c). Unlike Activity 4, the planes here do not pass through the origin, which is why the right-hand sides are nonzero.
</details>
</div>
</div>

</div>

{% endraw %}
