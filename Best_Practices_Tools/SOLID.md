# SOLID Principles

## Theory

The SOLID principles are a set of five design principles intended to make software designs more understandable, flexible, and maintainable. They are a subset of many principles promoted by American software engineer Robert C. Martin.

### The SOLID Principles

1. Single Responsibility Principle (SRP):

   - A class should have only one reason to change, meaning it should have only one responsibility.
   - This principle promotes high cohesion and reduces the risk of unintended side effects.

2. Open/Closed Principle (OCP):

   - Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.
   - This means you should be able to add new functionality without changing existing code.

3. Liskov Substitution Principle (LSP):

   - Subtypes must be substitutable for their base types.
   - This principle ensures that derived classes can replace their base classes without altering the correctness of the program.

4. Interface Segregation Principle (ISP):

   - Many client-specific interfaces are better than one general-purpose interface.
   - This principle prevents classes from being forced to implement interfaces they don't use.

5. Dependency Inversion Principle (DIP):

   - High-level modules should not depend on low-level modules. Both should depend on abstractions.
   - Abstractions should not depend on details. Details should depend on abstractions.
   - This principle promotes loose coupling and makes code more flexible and testable.

## Example (Illustrating SRP and OCP):

```python
# SRP Violation (One class doing too much)
class Report:
    def generate(self, data):
        # Generate report
        pass

    def save_to_file(self, filename):
        # Save report to file
        pass

# SRP and OCP Adherence
class ReportGenerator:
    def generate(self, data):
        # Generate report
        pass

class ReportSaver:
    def save(self, report, filename):
        # Save report to file
        pass

# OCP Adherence (Extending without modifying)
class HTMLReportGenerator(ReportGenerator):
    def generate(self, data):
        # Generate HTML report
        pass

class PDFReportSaver(ReportSaver):
    def save(self, report, filename):
        # Save report to PDF
        pass
```
