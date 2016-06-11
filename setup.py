from setuptools import setup

setup(name='MapaDaGentileza',
      version='1.0',
      description='OpenShift App',
      author='Mateus',
      author_email='example@example.com',
      url='https://www.python.org/community/sigs/current/distutils-sig',
      install_requires=['Flask>=0.7.2', 'MarkupSafe', 'flask-sqlalchemy','sqlalchemy-migrate','flask-whooshalchemy'],
      )