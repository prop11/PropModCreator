# Contributing to PropModCreator

Thank you for considering contributing to PropModCreator! This document outlines how to contribute effectively.

# Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/PropModCreator.git`
3. Create a branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Test thoroughly
6. Commit: `git commit -m "Add your feature"`
7. Push: `git push origin feature/your-feature-name`
8. Create a Pull Request

# Development Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/PropModCreator.git
cd PropModCreator

# Install dependencies
pip install -r requirements.txt

# Run the application
python prop_mod_creator.py
```

# Code Style

- Follow PEP 8 style guidelines
- Use meaningful variable names
- Add comments for complex logic
- Keep functions focused and small
- Use docstrings for classes and functions

Example:
```python
def add_profession(self):
    """
    Open dialog to add a new profession.

    Creates and displays a ProfessionDialog instance that allows
    the user to configure a new profession with skills, traits, and items.
    """
    dialog = ProfessionDialog(self.root, self)
```

# Testing

Before submitting a PR:

1. Test all tabs and features
2. Test save/load functionality
3. Test mod generation
4. Test generated mod in Project Zomboid
5. Check for error messages
6. Test on your platform (Windows/Linux/Mac)

# Feature Requests

Have an idea? Great! Please:

1. Check existing issues first
2. Open a new issue with the "enhancement" label
3. Describe the feature clearly
4. Explain the use case
5. Suggest implementation if possible

# Bug Reports

Found a bug? Please:

1. Check if it's already reported
2. Open a new issue with the "bug" label
3. Include:
   - Your OS and Python version
   - Steps to reproduce
   - Expected behavior
   - Actual behavior
   - Screenshots if applicable
   - Error messages

# Pull Request Guidelines

# Before Submitting

- Test your changes thoroughly
- Update documentation if needed
- Follow the code style guidelines
- Make sure your code doesn't break existing features

# PR Description Should Include

- What does this PR do?
- Why is this change needed?
- What issue does it fix? (if applicable)
- Screenshots (for UI changes)
- Testing performed

# Example PR Title

-  `Add recipe creator tab`
-  `Fix profession save bug`
-  `Improve UI responsiveness`
-  `Update file`
-  `Fix bug`

# Areas for Contribution

# High Priority
- [ ] Recipe creator tab functionality
- [ ] Custom items tab functionality
- [ ] Unit tests
- [ ] Error handling improvements

# Medium Priority
- [ ] Icon/image support for professions
- [ ] Mod preview before generation
- [ ] Multiple profession templates
- [ ] Import from existing mods

# Nice to Have
- [ ] Dark theme toggle
- [ ] Localization support
- [ ] Steam Workshop integration
- [ ] Built-in mod testing

# Code Structure

```
PropModCreator/
 prop_mod_creator.py      # Main application
 requirements.txt          # Dependencies
 README.md                 # Documentation
 QUICKSTART.md            # Quick start guide
 examples/                # Example projects
 assets/                  # Images, icons (future)
```

# Key Classes

- PropModCreator: Main application window
- ProfessionDialog: Profession creation dialog
- TraitDialog: Trait creation dialog
- ModGenerator: Generates mod files from data

# Questions?

- Open an issue with the "question" label
- Join the Project Zomboid modding Discord
- Check existing issues and discussions

# License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to PropModCreator!
