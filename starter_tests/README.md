# Student Self-Checks

From the repository root, run the student-facing checks with:

```bash
python -m unittest discover -s starter_tests
```

These checks are designed to fail until you complete the worksheet TODOs. They
check required function interfaces and representative program behaviors, but do
not replace reading the worksheet instructions or completing its manual
checks.

## AP CSA-Prep OOP Checks

The OOP self-checks cover these nine worksheets:

- `09_basic_oop/01_simple_class.py` through `05_composition_aggregation.py`
- `10_intermediate_oop/01_inheritance.py`, `02_method_overriding.py`,
  `03_super_function.py`, and `05_polymorphism_interfaces.py`

Run just the relevant OOP topic while working:

```bash
python3 -m unittest starter_tests.test_09_basic_oop
python3 -m unittest starter_tests.test_10_intermediate_oop
```

Each worksheet also lists its one-lesson command near the top. As with the
existing checks, failures are expected until you implement the TODOs.

The file and JSON checks load worksheets in a temporary working directory and
use temporary files. They should not alter course files. Likewise, when testing
your own file-handling code, use temporary or practice files rather than
changing the original course materials.
