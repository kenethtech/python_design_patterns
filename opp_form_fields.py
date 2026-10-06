

class Htmlfields(object):
    def __init__(self, **kwargs):
        self.html = ""
        if kwargs["type"] == "text":
            self.html = self.construct_text_field(kwargs["label"], kwargs["name"])

        elif kwargs["type"] == "checkbox":
            self.html = self.construct_checkbox(kwargs["id"], kwargs["value"], kwargs["name"], kwargs["label"])

    def construct_text_field(self, label, name):
        return '<label>{0}:<br><input type="text" name="{1}"><br>'.format(label, name)

    def construct_checkbox(self, id, value, name, label):
        return '<label><input type="checkbox" id="{0}" value="{1}" name="{2}">{3}: <br>'.format(id, value, name, label)

    def __str__(self):
        return self.html

def generate_webform(all_fields):
    generated_webfields = []
    
    for field in all_fields:
        try:
            object_field = Htmlfields(**field)
            generated_webfields.append(str(object_field))
        except Exception as e:
            print("Error: {}".format(e))

    generated_fields = "\n".join(generated_webfields)

    return '<form>{fields}</form>'.format(fields=generated_fields)

def build_forms(fields):
    with open("form_file2.html", "w") as file:
        file.write(
            '<html><body>{}</body></html>'.format(generate_webform(fields))
        )


if __name__ == "__main__":
    fieds = [
        {
            "type": "text",
            "name": "first_textfield",
            "label": "1st_textfield"
        },
        {
            "type": "checkbox",
            "id": "1st_checkbox",
            "value": "first",
            "name": "checkbox1",
            "label": "Checkbox1"
        },
        {
            "type": "text",
            "name": "second_textfield",
            "label": "2nd_textfield"
        }
    ]

    try:
        build_forms(fieds)
        print("form built successful")
    except Exception as e:
        print(str(e))