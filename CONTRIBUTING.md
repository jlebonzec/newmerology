# Contributing
Thank you for your interest towards this project. Every contribution, big or small, is welcomed. You can freely create issues and pull requests, but please follow these guidelines:

## Issues
- Test with several browsers first. If your problem only happens on a few of them, give the name and version (go in `about`), together with your OS version.
- Describe explicitly what the problem is
  - Explain how to reproduce. A reproduceable bug if *a lot* more likely to be fixed.
  - Provide examples, screenshots, if applicable
## Pull Requests
- Describe what you are fixing or improving and why
- Follow [PEP8](https://www.python.org/dev/peps/pep-0008/) as much as possible
  - The character limit per line is 100
- If creating any new functions:
  - Add docstrings
  - Unit test it

## Frameworks used
Various frameworks have been used to ease the development:
- [Materializecss](http://materializecss.com/) for the frontend
- [Django-material](https://github.com/viewflow/django-material) to output forms compatible with materialize
- [Django-sass-processor](https://github.com/jrief/django-sass-processor) to compile SASS stylesheets
- [Django_translate](https://github.com/adamziel/django_translate/) for the translations


## Testing
Testing is important and brings confidence regarding improvements or refactor. Please do test.
```bash
python manage.py test calculator.tests calculator.computations.tests
```

## In general
Assume a positive mind-set.

Remember that this project is done on free time. :-)
