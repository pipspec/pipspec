from invoke import task

@task
def _update_tags(c, version=''):
  msg = "Added tag v{0}".format(version)
  print('')
  print('Adding Files to Stage...')
  print('')
  c.run("git add .")
  print('')
  print('Commiting Staged Files...')
  print('')
  c.run("git commit -m \"Created Tag\"")
  print('')
  print('Creating Tag...')
  print('')
  c.run("git tag -a v{0} -m {0}".format(version,msg))
  print('')
  print('Pushing to Master...')
  print('')
  c.run("git push -u origin master --tags")
