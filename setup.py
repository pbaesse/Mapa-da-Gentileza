from setuptools import setup

setup(name='MapaDaGentileza',
      version='1.0',
      description='OpenShift App',
      author='Matheus Emanuel, Pedro Baesse',
      author_email='matheusemanuel@gmail.com',
      url='https://www.python.org/community/sigs/current/distutils-sig',
      install_requires=['Flask>=1.0.0', 'MarkupSafe', 'flask-sqlalchemy','sqlalchemy-migrate','flask-whooshalchemy'],
      )