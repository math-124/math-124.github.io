"""Standalone boxed notices must remain outside assignment parts."""
import unittest

from generate_assignment_markdown import cleanup_markdown


class InterstitialCalloutTests(unittest.TestCase):
    def test_boxed_notice_between_problems_uses_yellow_alert(self):
        rendered = cleanup_markdown("""## Problem 6: Earlier

### Part c)

Find a nonzero input.

::: tcolorbox
**Note: Problems 7--11 require material from Tuesday's lecture.**
:::

## Problem 7: Matrix Products

Compute the products.
""")
        alert = "{: .yellow }\n> **Note: Problems 7--11 require material from Tuesday's lecture.**"
        self.assertIn(alert, rendered)
        self.assertNotIn("::: tcolorbox", rendered)
        before, after = rendered.split(alert)
        self.assertIn('class="assignment-part"', before)
        self.assertEqual(before.count('<div'), before.count('</div>'))
        self.assertTrue(after.lstrip().startswith('## Problem 7:'))


if __name__ == '__main__':
    unittest.main()
