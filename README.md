# Newmerology

## Purpose
This software is a tool for numerologist. It aims at providing various "numbers" (or computation methods) and an interface to create and modify personal analysis. It is *not* providing any explanation out of the box.

## Features
- Create analysis and automatically save it
- Create generic and personalised commentaries
- Delete a past analysis
- Add and reorder numbers
- Translatable interface
  - For now the interface is only translated in English and French, and there is no support for database translations.
  - In short, you can set up the application in any language you want (provided you add your translations), but the website will only be truly available in one language.
  
## Screenshots

Custom text (Markdown editable)
![image](https://user-images.githubusercontent.com/10447820/197407199-c2cbebac-21a9-4917-a923-d66400daa796.png)

Some numbers are date-related, it then shows as a time arrow (circled is the number being commented on, the yellow dot indicate the current age)

![image](https://user-images.githubusercontent.com/10447820/197407062-bcb63f80-98c3-447d-bc3c-a85d0f90092c.png)

Some numbers are referred into a grid (the number being commented on in circled)

![image](https://user-images.githubusercontent.com/10447820/197407106-68952947-6879-48de-8605-2baed8498567.png)

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

Below is a generic example that you will need to personalise.
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
                desc="Main aspirations of the person",
                position=0)
number.save()
```
If you refresh the result page you should now see your new number(s).

### Available routes
- `/`: The root of the application. Proposes a form to perform a new analysis
- `/person`: The list of past analysis. Allows to see and remove past entries. This route is accessible only directly, no link exists in the appication — yet.
- `/person/<id>`: An analysis of the person having the given id.

## License
This work is licensed under [AGPLv3](https://www.gnu.org/licenses/agpl.html)

Please see the file named `COPYING.md` for more information.

## Contact

If you have any question, feel free to reach me using
jonathan.lebonzec+newmerology@gmail.com
