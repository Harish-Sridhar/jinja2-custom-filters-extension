# Jinja2 Custom Filters

Jinja2 offers many [filters](https://jinja.palletsprojects.com/en/2.11.x/templates/#list-of-builtin-filters) to use in your template.
But this is limited.
This repo offers a number of additional filters that can be used in Jinja2 templates.


# How it works


1. The first and foremost is installation.  

        pip install jinja2_custom_filters_extension

2. Add [extension](#Extensions) to your jinja environment.  
        
        from jinja2_custom_filters_extension.string_filters_extension import StringFilterExtension
        environment: Environment = Environment(extensions=[StringFilterExtension])
        
3. Use the filters that are available in the extension as you would use a built in  filter in your jinja templates.  
    for ex:  
    
        {{ "abc DEF" | upper_case_first_letter }}
        
4. Render your template , the filters should be working.

# Extensions

## String Filter Extension

| Filter Name             | Description                                                          | Example Input Value | Generated Output Value |
|-------------------------|----------------------------------------------------------------------|---------------------|------------------------|
| slug                    | Changes the value to lower case and then replaces spaces with dashes | aBc DeF GHi         | abc-def-ghi            |
| upper_case_first_letter | Changes only the first letter of the value to upper case.            | AbC DeF             | abC DeF                |


# Usage with cookiecutter

[cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/index.html) is a famous tool for creating projects from project templates.  
Itis built on top of `jinja2`.  
These extensions can also be used in a cookiecutter project. 

1. Make sure the package `jinja2_custom_filters_extension` is installed.
2. Add extensions in the `cookiecutter.json` file of your project.  
   Refer the [link](https://cookiecutter.readthedocs.io/en/1.7.2/advanced/template_extensions.html) on how to do it.
   Bascially it is adding the below entry to the json.
   
       "_extensions": ["jinja2_custom_filters_extension.string_filters_extension.StringFilterExtension"]
3. Use the filters in your templates. 
4. Thats it. When you run your cookiecutter project, it should work.
   

 

