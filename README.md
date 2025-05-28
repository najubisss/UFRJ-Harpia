# UFRJ-Harpia


├── temperature_control/              # pacote com os nós ROS 2 em Python
│   └── temperature_control/
│       ├── temperature_publisher.py
│       ├── temperature_monitor.py
│       ├── average_reset_client.py
│       └── temperature_avg_monitor.py
│
├── temperature_control_bringup/     # pacote com o launch file
│   └── launch/
│       └── start_system.launch.py


# 1. Inicie o container
   
    bash harpia.sh

# 2. Compile o workspace

    cd /harpia_ws
    colcon build
    source install/setup.bash

# 3. Execute o sistema com o launch file

    ros2 launch temperature_control_bringup start_system.launch.py 

# 4. Pacotes e nós

| Pacote                        | Nó                        | Função                                                                                                          |
| ----------------------------- | ------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `temperature_control`         | `temperature_publisher`   | Publica temperatura simulada no tópico `/temperature` (2 Hz)                                                    |
|                               | `temperature_monitor`     | Calcula média das 5 últimas temperaturas e publica em `/average_temperature` + oferece serviço `/reset_average` |
|                               | `average_reset_client`    | Cliente que chama o serviço `/reset_average`                                                                    |
|                               | `temperature_avg_monitor` | Apenas imprime no terminal as médias recebidas                                                                  |
| `temperature_control_bringup` | -                         | Contém o launch file para executar os nós principais                                                            |


Desenvolvido por

Anna Julia 

Para processo seletivo UFRJ Harpia

