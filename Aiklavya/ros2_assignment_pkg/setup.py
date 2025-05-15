from setuptools import setup

package_name = 'ros2_assignment_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='you@example.com',
    description='ROS 2 assignment package',
    license='MIT',
    entry_points={
        'console_scripts': [
            'talker = ros2_assignment_pkg.talker:main',
            'listener = ros2_assignment_pkg.listener:main',
        ],
    },
)
