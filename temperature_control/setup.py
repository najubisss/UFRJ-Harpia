from setuptools import find_packages, setup

package_name = 'temperature_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='najubiss',
    maintainer_email='annajulialira.25@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
    'console_scripts': [
        'temperature_publisher = temperature_control.temperature_publisher:main',
        'temperature_monitor = temperature_control.temperature_monitor:main',
        'temperature_avg_monitor = temperature_control.temperature_avg_monitor:main',
        'average_reset_client = temperature_control.average_reset_client:main',
    ],
},

)
