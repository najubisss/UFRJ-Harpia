entry_points={
    'console_scripts': [
        'temperature_publisher = temperature_control.temperature_publisher:main',
        'temperature_monitor = temperature_control.temperature_monitor:main',
        'temperature_avg_monitor = temperature_control.temperature_avg_monitor:main',
        'average_reset_client = temperature_control.average_reset_client:main',
    ],
},

