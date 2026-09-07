# Teacher Guide

Use this repository as a differentiated programming practice library. The
required AP CSP coding path is programs 01-04 in topics 1-8. Programs 05-06,
advanced OOP, and concurrency are extension material rather than required
daily work.

## Core Pacing

This sequence fits approximately 18-24 class periods when students complete
two to four selected exercises per topic. Adjust the number of exercises to
the class's prior experience and available time.

| Topic | Suggested lessons | Time | Prerequisites | Primary outcome |
|---|---|---:|---|---|
| Variables, expressions, and statements | 01-04 | 2-3 periods | None | Store data, use arithmetic, and format output. |
| Conditionals | 01-04 | 2-3 periods | Variables and comparisons | Write selection logic and validate simple inputs. |
| Loops and iteration | 01-04 | 2-3 periods | Conditionals | Trace and write counted and condition-controlled repetition. |
| Functions | 01-04 | 2-3 periods | Variables, conditionals, loops | Decompose a problem into procedures with parameters and return values. |
| Strings | 01-04 | 2 periods | Loops and functions | Process text with indexing, slicing, methods, and iteration. |
| Lists | 01-04 | 2-3 periods | Loops and functions | Store, traverse, filter, and transform related data. |
| Tuples, sets, and dictionaries | 01-04 | 2-3 periods | Lists | Select an appropriate collection and model key-value data. |
| Exceptions and files | 01-04 | 3-4 periods | Functions and collections | Read, write, validate, and process persistent data safely. |

## AP CSP Alignment

The core coding lessons reinforce the AP CSP programming and data skills below.
Use your district's current College Board framework for official learning
objective language and assessment requirements.

| Course concept | Recommended topics | Teacher emphasis |
|---|---|---|
| Variables, expressions, and output | 01 | Have students trace values and explain each calculation. |
| Selection | 02 | Require test cases for every branch, including invalid input. |
| Iteration | 04 | Contrast counted loops with condition-controlled loops and discuss termination. |
| Procedures and abstraction | 03 | Ask students to write a procedure with a meaningful parameter and use its returned result. |
| Lists and data abstraction | 06-07 | Have students explain why a collection simplifies their program. |
| Algorithms | 03-07 | Practice tracing, debugging, and comparing two valid approaches. |
| Input, output, and data persistence | 08 | Use small local data files and discuss validation and error messages. |

This repository does not by itself cover the AP CSP computer systems, networks,
or computing-impacts content. Pair the programming work with your required
lessons, discussions, and assessments in those areas.

The [AP CSP Companion Activities](ap_csp_companion/README.md) provide four
short, non-programming activities for those topics.

## AP CSA Preparation

After the AP CSP core, use selected OOP exercises to prepare interested
students for Java and AP CSA.

| Focus | Recommended material | Transferable idea |
|---|---|---|
| Classes, constructors, and instance state | `09_basic_oop/01` through `04` | An object combines state and behavior. |
| Composition | `09_basic_oop/05` | Model a "has-a" relationship with collaborating objects. |
| Inheritance and overriding | `10_intermediate_oop/01` through `03` | A subtype can reuse and specialize parent behavior. |
| Polymorphism | `10_intermediate_oop/05` | Code to a shared behavior contract. |

Prioritize object state, constructors, instance methods, method calls, lists of
objects, composition, inheritance, and overriding. Treat Python-specific
features such as descriptors, metaclasses, and dynamic attribute access as
university enrichment, not AP CSA preparation.

### OOP Reference Solutions and Self-Checks

The AP CSA-prep path now has matching reference solutions in `solutions/`,
standard-library checks in `tests/`, and student-facing checks in
`starter_tests/` for exactly these lessons:

- `09_basic_oop/01_simple_class.py`
- `09_basic_oop/02_class_attributes.py`
- `09_basic_oop/03_class_methods.py`
- `09_basic_oop/04_multiple_objects.py`
- `09_basic_oop/05_composition_aggregation.py`
- `10_intermediate_oop/01_inheritance.py`
- `10_intermediate_oop/02_method_overriding.py`
- `10_intermediate_oop/03_super_function.py`
- `10_intermediate_oop/05_polymorphism_interfaces.py`

Use `python3 -m unittest discover -s tests` to verify the teacher references.
Students can run `python3 -m unittest discover -s starter_tests`; the OOP
checks intentionally fail with missing-interface guidance until worksheet TODOs
are complete.

## Extension and Enrichment

Offer extensions as choice-based projects with stated prerequisites and a
timebox. Students should not need them to demonstrate core proficiency.

The student-facing [ENRICHMENT_CATALOG.md](ENRICHMENT_CATALOG.md) provides
prerequisites, timeboxes, and deliverables for every lesson in topics 11-15.

| Material | Suggested audience | Guidance |
|---|---|---|
| Programs 05-06 in topics 03-08 | Students ready for algorithms or multi-part problems | Assign one challenge at a time; provide a planning checkpoint. |
| Advanced OOP (topic 11) | Students comfortable with classes and inheritance | Focus on one feature, such as properties or magic methods. |
| Concurrency, threading, multiprocessing, and asyncio (topics 12-15) | College/university enrichment | Teach one concurrency model at a time and require safe shutdown/error handling. |

## Assessment Rubric

Score each criterion from 0-3. For a short exercise, assess only the first two
or three criteria. For a larger project, use all four.

| Criterion | 3 - Proficient | 2 - Developing | 1 - Beginning | 0 - Missing |
|---|---|---|---|---|
| Correctness | Meets requirements and handles stated edge cases. | Meets the main requirement with a small defect. | Partially works but misses major cases. | Does not run or does not address the task. |
| Abstraction and design | Uses appropriately named procedures, data, or objects to simplify the solution. | Some organization, but repeated or overly coupled logic remains. | Organization is difficult to follow. | No meaningful structure beyond a partial attempt. |
| Readability | Names, formatting, and output make the program easy to trace. | Generally readable with minor naming or formatting issues. | Hard to trace because names or structure are unclear. | Unreadable or undocumented enough to prevent review. |
| Testing and reflection | Demonstrates representative normal, boundary, and invalid cases; explains a revision. | Demonstrates normal and one additional case. | Runs only one example or gives limited evidence. | No evidence of testing. |

## Suggested Classroom Routine

1. Begin with a five-minute trace or prediction task using a small code sample.
2. Model one procedure or algorithm, then assign a focused starter worksheet.
3. Require students to test normal, boundary, and invalid cases before
   submitting.
4. Use the matching file in `solutions/` for feedback after students have had
   time to attempt the task.
5. End with a brief explanation prompt: what data, condition, loop, or
   procedure made the program simpler?
