"""Regression checks for homework solution math and currency conversion."""
import tempfile
import unittest
from pathlib import Path

from check_assignment_html import check_source_markdown
from generate_assignment_markdown import (cleanup_markdown, fence_indented_code_blocks,
    replace_itemize_with_html_placeholders, strip_layout_commands, latex_fragment_to_markdown)


class SolutionFormattingTests(unittest.TestCase):
    def test_nested_bullets_preserve_display_math_and_case_continuation(self):
        source = r"""\begin{itemize}
\item First approach: $$0<x<\frac{1}{2}.$$
\item Two cases:
\begin{itemize}
\item $x>0$: positive case.
\item $x<0$: $$1<2x.$$ This is a \textbf{contradiction}.
\end{itemize}
\end{itemize}"""
        marked, blocks = replace_itemize_with_html_placeholders(source)
        self.assertEqual(len(blocks), 1)
        self.assertIn("ITEMIZEHTMLPLACEHOLDER0", cleanup_markdown(marked))
        rendered = blocks[0]
        self.assertEqual(rendered.count("<ul>"), 2)
        self.assertEqual(rendered.count("<li>"), 4)
        self.assertIn('<span class="math display">', rendered)
        self.assertIn("<strong>contradiction</strong>", rendered)
        self.assertLess(rendered.index("contradiction"), rendered.rindex("</li>"))

    def test_indented_cases_remain_math(self):
        source = r"""$$
\begin{cases}
        x+y+z=35,\\
        5x+4y+z=7,\\
        z=y+7.
      \end{cases}
$$"""
        rendered = cleanup_markdown(source)
        self.assertNotIn("```", rendered)
        self.assertIn(r"x+y+z=35,\\", rendered)
        self.assertIn(r"5x+4y+z=7,\\", rendered)
        self.assertIn(r"\end{cases}", rendered)

    def test_currency_does_not_capture_surrounding_prose(self):
        source = r"Hence the student ticket is $\$3.00$ and the adult ticket is $\$15.70$."
        self.assertEqual(
            cleanup_markdown(source),
            'Hence the student ticket is <span class="currency tex2jax_ignore">$3.00</span>'
            ' and the adult ticket is <span class="currency tex2jax_ignore">$15.70</span>.',
        )

    def test_plain_currency_and_regular_math_still_work(self):
        rendered = cleanup_markdown(r"Tickets cost \$87.50, and $x=3$.")
        self.assertIn('<span class="currency tex2jax_ignore">$87.50</span>', rendered)
        self.assertIn('class="math-inline"', rendered)
        self.assertIn("x=3", rendered)

    def test_solution_function_keeps_its_header_and_indentation(self):
        source = r"""\begin{flushleft}
\ttfamily
 def reflection(v, w):\\
 \hspace*{2em}p = np.dot(v, w) / np.dot(w, w) * w\\
 \hspace*{2em}return 2 * p - v
\end{flushleft}"""
        rendered = latex_fragment_to_markdown(strip_layout_commands(source))
        self.assertIn("```python\ndef reflection(v, w):\n    p = np.dot(v, w) / np.dot(w, w) * w\n    return 2 * p - v\n```", rendered)

    def test_samepage_retains_solution_content_without_layout_fences(self):
        rendered = latex_fragment_to_markdown(strip_layout_commands(
            r"\begin{samepage}Substituting gives $x=6t$.\end{samepage}"))
        self.assertIn("Substituting gives", rendered)
        self.assertNotIn(":::", rendered)

    def test_real_python_still_gets_a_code_fence(self):
        rendered = fence_indented_code_blocks("    x = 3\n    print(x)")
        self.assertEqual(rendered, "```python\nx = 3\nprint(x)\n```")

    def test_checker_rejects_code_fences_in_math(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "index.md"
            source.write_text('<div class="math-display">\n$$\n```python\nx=3\n```\n$$\n</div>')
            failures = check_source_markdown(source, allow_solutions=True)
            self.assertTrue(any("code fence leaked inside display math" in failure for failure in failures))


if __name__ == "__main__":
    unittest.main()
