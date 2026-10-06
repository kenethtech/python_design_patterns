from abc import ABCMeta, abstractmethod

class Director(object, metaclass=ABCMeta):
    def __init__(self):
        self._buider = None
    def set_builder(self, builder):
        self._buider = builder

    @abstractmethod
    def construct(self, field_list):
        pass

    def get_constructed_object(self):
        return self._buider.constructed_object

class AbstractFormBuilder(object, metaclass=ABCMeta):
    def __init__(self):
        self.constructed_object = None

    @abstractmethod
    def add_text_field(self, text_dict):
        pass

    @abstractmethod
    def add_checkbox(self, check_dict):
        pass

    @abstractmethod
    def add_button(self, button_dict):
        pass

class HtmlForm(object):
    def __init__(self):
        self.field_list = []

    def __repr__(self):
        return "\n<form>{}\n</form>\n".format("".join(self.field_list))

class HtmlFormBuilder(AbstractFormBuilder):
    def __init__(self):
        self.constructed_object = HtmlForm()

    def add_text_field(self, text_dict):
        self.constructed_object.field_list.append(
            '\n<label>{0}<br><input type="text" name="{1}"><br>'.format(
                text_dict["label"], text_dict["name"])
        )

    def add_checkbox(self, check_dict):
        self.constructed_object.field_list.append(
            '\n<label><input type="checkbox" id="{0}" name="{1}" value="{2}">{3}<br>'.format(
                check_dict["id"],
                check_dict["name"],
                check_dict["value"],
                check_dict["label"]
            )
        )

    def add_button(self, button_dict):
        self.constructed_object.field_list.append(
            '\n<button type="button">{}</button>'.format(
                button_dict["name"]
            )
        )

class FormDirector(Director):
    def __init__(self):
        super().__init__()

    def construct(self, field_list):
        for field in field_list:
            if field["type"] == "text":
                self._buider.add_text_field(field)

            elif field["type"] == "checkbox":
                self._buider.add_checkbox(field)

            elif field["type"] == "button":
                self._buider.add_button(field)

if __name__ == "__main__":
    director = FormDirector()
    html_form_builder = HtmlFormBuilder()
    director.set_builder(html_form_builder)

    fields = [
        {
            "type": "text",
            "name": "1st_text_field",
            "label": "Text Field 1"
        },
        {
            "type": "checkbox",
            "id": "check_me",
            "name": "check_me",
            "value": "checked",
            "label": "check_me"
        },
        {
            "type": "button",
            "name": "Click Me"
        }
    ]

    director.construct(fields)

    with open("form_file3.html", "w") as file:
        file.write(
            '<html><body>{0!r}</body></html>'.format(
                director.get_constructed_object()
            )
        )        
       


