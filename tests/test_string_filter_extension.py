from jinja2 import Environment
from jinja2 import Template
from jinja2_custom_filters_extension.string_filters_extension import  StringFilterExtension


def test_slug():
    template :Template = environment.from_string("""{{ "abc DEF" | slug }}""")
    assert template.render()=="abc-def"
    template: Template = environment.from_string("""{{ "999" | slug }}""")
    assert template.render() == "999"
    template: Template = environment.from_string("""{{ "" | slug }}""")
    assert template.render() == ""

def test_upper_case_first_letter():
    template :Template = environment.from_string("""{{ "abc DEF" | upper_case_first_letter }}""")
    assert template.render()=="Abc DEF"
    template: Template = environment.from_string("""{{ "999" | upper_case_first_letter }}""")
    assert template.render() == "999"
    template: Template = environment.from_string("""{{ "" | upper_case_first_letter }}""")
    assert template.render() == ""




environment: Environment = Environment(extensions=[StringFilterExtension])