from invoke import task

@task
def _update_tags(c, version=''):
  msg = "Added tag v%(version)s"
  print('')
  print('Adding Files to Stage...')
  print('')
  c.run("git add .")
  print('')
  print('Commiting Staged Files...')
  print('')
  c.run("git commit -am %(msg)s ")
  print('')
  print('Creating Tag...')
  print('')
  c.run("git tag -a v%(version)s -m %(msg)s")
  print('')
  print('Pushing to Master...')
  print('')
  c.run("git push -u origin master --tags")
