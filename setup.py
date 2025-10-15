from setuptools import find_packages,setup
Hypen_e_dot='-e .'

def get_requirements(file_path:str):

    """This function returns the list of requirements.

    It strips newlines and removes the editable install marker ('-e .') if present.
    """
    requirements = []
    with open (file_path) as file_obj:
        requirements = file_obj.readlines()
        # normalize lines and remove empty entries
        requirements = [req.strip() for req in requirements if req.strip()]

        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)
    return requirements


setup(
    name='project',
    version='0.0.1',
    author='chandrakant',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)