# Newmerology

## Purpose
This software is a tool for numerologist. It aims at providing various "numbers" (or computation methods) and an interface to create and modify personal analysis. It is *not* providing any explanation out of the box.

## Features
- Create analysis and automatically save it
- Create generic and personnalised commentaries
- Delete a past analysis
- Add and reorder numbers
- Translatable interface
  - For now the interface is only translated in English and French, and there is now support for database translations.
  - In short, you can set up the application in any language you want (provided you add your translations), but the website will only be trully available in one language.

## Usage
It is a django application, so you should refer to the [official django documentation](https://docs.djangoproject.com) about how to deploy it in production.

During the rest of this section, we will consider the *local testing* case. We assume that you pulled the repository and are now placed in the root directory of the project.

To start the application, you can run the following commands:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
By default you will be able to register a new person but the analysis will be empty: adding the numbers you want to see is required first.

**Uniqueness of a person**

It is important to remember that a person is considered unique given their full given names (first, middle and last names) and their birth date. Spaces matter. If any of those information differ, then the system will, instead of reusing an existing entry, create a new one.

### Adding a number
Given that the computation method already exists, adding a number is a pretty straight-forward operation.
You first need to open the application shell: `python manage.py shell`

Below is a generic example that you will need to personnalise.
```python
from calculator.models import Number
number = Number(code="unique_code",
                name="Name to display in the UI",
                computation_method="my_method",
                description="More info about the number",
                position=4)
number.save()
```

#### Required arguments
`unique_code`  corresponds to the database identifier. It needs to be unique, preferably with no space nor special characters. It needs to be explicit enough so you as a human can remember what it corresponds to.
`name` is what will be displayed in the User Interface. It is often the name of the number computed.
`computation_method` corresponds to the module that should be use to compute the number. All available modules are by default in `calculator.computations`, though it can be overriden by changing the `calculator.config.COMPUTATION_METHODS_PATH`.

#### Optional arguments
`description` is an optional text to give more information about the computation. Often used if the name seem cryptic, it will be displayed below it, as a subtitle.
`position` is really useful to state the order of the number. If you try to add a number at a position already occupied, it will be inserted *before* the occupant - like [list.insert](https://docs.python.org/2/tutorial/datastructures.html#more-on-lists) would. Note that a negative position *disables* the number: it will still be available in the database and the previous data will be kept, but won't be shown to the user anymore.

#### Example
Let's add a life path number to display:
```python
number = Number(code="life_path",
                name="Life Path",
                computation_method="lifepath",
                desc="Main aspirations of the person"
                position=0)
number.save()
```
If you refresh the result page you should now see your new number(s).

### Available routes
- `/`: The root of the application. Proposes a form to perform a new analysis
- `/person`: The list of past analysis. Allows to see and remove past entries. This route is accessible only directly, no link exists in the appication — yet.
- `/person/<id>`: An analysis of the person having the given id.

## Contributing
Thank you for your interest towards this project. Every contribution, big or small, is welcomed. You can freely create issues and pull requests, but please follow these guidelines:

### Issues
- Test with several browsers first. If your problem only happens on a few of them, give the name and version (go in `about`), together with your OS version.
- Describe explicitly what the problem is
  - Explain how to reproduce. A reproduceable bug if *a lot* more likely to be fixed.
  - Provide examples, screenshots, if applicable
### Pull Requests
- Describe what you are fixing or improving and why
- Follow [PEP8](https://www.python.org/dev/peps/pep-0008/) as much as possible
  - The character limit per line is 100
- If creating any new functions:
  - Add docstrings
  - Unit test it

### In general
Assume a positive mind-set.

This project is done on free time, don't expect me to reply in the next hour, but don't hesitate to follow up if a week has passed.

Respecting all those will avoid having comments that could be avoided.

### Frameworks used
Various frameworks have been used to ease the development:
- [Materializecss](http://materializecss.com/) for the frontend
- [Django-material](https://github.com/viewflow/django-material) to output forms compatible with materialize
- [Django-sass-processor](https://github.com/jrief/django-sass-processor) to compile SASS stylesheets
- [Django_translate](https://github.com/adamziel/django_translate/) for the translations


### Testing
Testing is important and brings confidence regarding improvements or refactor. Please do test.
```bash
python manage.py test calculator.tests calculator.computations.tests
```
## License
This work is licensed under [AGPLv3](https://www.gnu.org/licenses/agpl.html)

Please see the file named `COPYING.md` for more information.

## Contact

If you have any question, feel free to reach me using
jonathan.lebonzec+newmerology@gmail.com