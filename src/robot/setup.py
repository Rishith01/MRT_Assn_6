from setuptools import find_packages, setup

package_name = 'robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/models' , ['models/models.sdf']),
        ('share/' + package_name + '/launch', ['launch/gazebo.launch.py']),
        ('share/' + package_name + '/urdf', ['urdf/models.urdf']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rishith',
    maintainer_email='rishithgupta01@gmail.com',
    description='TODO: Package description',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'move_circle = robot.movement.move_circle:main',
        ],
    },
)

