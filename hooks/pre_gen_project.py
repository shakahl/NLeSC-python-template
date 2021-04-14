{{ cookiecutter.update({
    "derived": {
        "project_name": cookiecutter.project_name.lower().replace("-", "_"),
        "package_name": cookiecutter.package_name.lower().replace(" ", "_").replace("-", "_"),
        "module_name": cookiecutter.package_name.lower().replace(" ", "_").replace("-", "_"),
        "full_name": cookiecutter.full_name.replace('\"', '\\\"'),
        "repository": "https://github.com/" + cookiecutter.github_organization + "/" + cookiecutter.project_name.lower().replace("-", "_"),
        "project_short_description": cookiecutter.project_short_description.replace('\"', '\\\"')
    }
}) }}
