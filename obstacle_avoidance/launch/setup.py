from setuptools import setup

package_name = 'turtlebot3_obstacle_avoidance'

setup(
    name=package_name,
    version='1.0.0',
    packages=['obstacle_avoidance'],
    install_requires=['setuptools'],
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'avoider = obstacle_avoidance.avoider:main'
        ],
    },
)
