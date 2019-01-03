import os
import sys

import click
import toml

from src import (__version__, __author__, __email__)

@click.group()
@click.option('-d/-D','--debug/--no-debug')
@click.version_option(version=__version__)
def cli(debug):
  click.echo('This project was started by: %s <%s>' % (__author__, __email__))
  click.echo('Debug mode is %s' % ('on' if debug else 'off'))

@cli.command()
@click.option('--project',
              prompt="What is the project name?",
              default="project_name",
              type=str)
@click.option('--version',
              prompt="What is the version?",
              default="0.0.1",
              type=str)
@click.option('--description',
              prompt="What is the description?",
              default="This is a Description",
              type=str)
@click.option('--license',
              prompt="What is the license?",
              type=click.Choice(['mit','ist','apache','aferro','gpl','lesser','mozilla']),
              default='mit')
@click.option('--fullname',
              prompt="What is your full name?",
              default="John Doe",
              type=str)
@click.option('--email',
              prompt="What is your email?",
              default= "john.doe@example.com",
              type=str)
@click.option('--keywords',
              prompt="What are some keyords that describe your project?",
              default=os.environ.get('PIPSPEC_INIT_KEYWORDS', ''),
              type=str)
@click.option('--pipspec',is_flag=True,default=False)
def init(project,version,description,license,fullname,email,keywords,pipspec):
  """Initializes a Python Project"""

  import textwrap
  def reformat(template):
    return textwrap.dedent(template).lstrip()

  author = "%s <%s>" % (fullname, email)
  maintainer = "%s <%s>" % (fullname, email)

  homepage = "https://%s.github.io/" % project
  repository = "https://www.github.com/USERNAME/%s" % project
  issues = "https://www.github.com/USERNAME/%s/issues" % project
  documentation = "https://%s.github.io/docs" % project

  template = reformat(
    """
    [spec]
    \tname= "%s"
    \tversion= "%s"
    \tdescription= "%s"
    \tlong_description= "README.md"
    \tlicense= "%s"
    \tauthors= [
    \t\t"%s"
    \t]
    \tmaintainers= [
    \t\t"%s"
    \t]

    \thomepage= "%s"
    \trepository= "%s"
    \tissues= "%s"
    \tdocumentation= "%s"

    \tkeywords= [%s]
    \tclassifiers= [
    \t\t"Development Status :: 1 - Planning",
    \t\t"Intended Audience :: Developers",
    \t\t"Operating Systems :: OS Independent",
    \t\t"Programming Languages :: Python",
    \t\t"Programming Languages :: Python :: 3",
    \t\t"Programming Languages :: Python :: 3 :: Only",
    \t\t"Programming Languages :: Python :: 3.7",
    \t\t"Programming Languages :: Python :: 3.8"
    ]
    """ % (
            project,
            version,
            description,
            license,
            author,
            maintainer,
            homepage,
            repository,
            issues,
            documentation,
            keywords,
          )
  )

  if pipspec:
    with open('%s.pipspec' % project, 'w') as f:
      f.write(template)
      f.close
  else:
    with open('Pipfile', 'w') as f:
      f.write(reformat(
        """
        [[soource]]
        \tname= "pypi"
        \turl= "https://pypi.org/simple"
        \tverify_ssl= true

        """
        ))
      f.write(template)
      f.write('\n')
      f.write(reformat(
        """
        [packages]

        [dev-packages]

        [requires]
        \tpython_version= "3.7"
        """
      ))
      f.close

@cli.command()
def login():
  """Login to pypi using OAuth"""
  pass

@cli.command()
def build():
  """Build your package for development"""
  pass

@cli.command()
def upload():
  """Uploads package to pypi"""
  pass

if __name__ == '__main__':
  cli(auto_envvar_prefix='PIPSPEC')
