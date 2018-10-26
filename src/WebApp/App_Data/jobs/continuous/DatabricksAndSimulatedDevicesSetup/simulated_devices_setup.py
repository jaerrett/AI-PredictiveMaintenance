import os
import json
import random
from iot_hub_helpers import IoTHub

def create_device(iot_hub, device_id, simulation_parameters):
    iot_hub.create_device(device_id)

    tags = {
        'simulated': True
    }
    
    tags.update(simulation_parameters)

    twin_properties = {
        'tags': tags
    }
    
    iot_hub.update_twin(device_id, json.dumps(twin_properties))

if __name__ == "__main__":
    IOT_HUB_NAME = os.environ['IOT_HUB_NAME']
    IOT_HUB_OWNER_KEY = os.environ['IOT_HUB_OWNER_KEY']
    
    iot_hub = IoTHub(IOT_HUB_NAME, IOT_HUB_OWNER_KEY)
    
    count = 2
    for i in range(count):
        device_id = 'Abrams-{0:03d}'.format(i)
        h1 = random.uniform(0.8, 0.95)
        h2 = random.uniform(0.8, 0.95)

        simulation_parameters = {
            'simulator': 'devices.engines.Engine',
            'h1': h1,
            'h2': h2
        }

        create_device(iot_hub, device_id, simulation_parameters)

    count = 4
    for i in range(count):
        device_id = 'C-130-A-{0:03d}'.format(i)
        h1 = random.uniform(0.8, 0.95)
        h2 = random.uniform(0.8, 0.95)

        simulation_parameters = {
            'simulator': 'devices.engines.Engine',
            'h1': h1,
            'h2': h2
        }

        create_device(iot_hub, device_id, simulation_parameters)

    count = 4
    for i in range(count):
        device_id = 'C-130-B-{0:03d}'.format(i)
        h1 = random.uniform(0.8, 0.95)
        h2 = random.uniform(0.8, 0.95)

        simulation_parameters = {
            'simulator': 'devices.engines.Engine',
            'h1': h1,
            'h2': h2
        }

        create_device(iot_hub, device_id, simulation_parameters)

    count = 4
    for i in range(count):
        device_id = 'C-130-C-{0:03d}'.format(i)
        h1 = random.uniform(0.8, 0.95)
        h2 = random.uniform(0.8, 0.95)

        simulation_parameters = {
            'simulator': 'devices.engines.Engine',
            'h1': h1,
            'h2': h2
        }

        create_device(iot_hub, device_id, simulation_parameters)

    count = 2
    for i in range(count):
        device_id = 'AmphibiousTransport-{0:03d}'.format(i)
        h1 = random.uniform(0.8, 0.95)
        h2 = random.uniform(0.8, 0.95)

        simulation_parameters = {
            'simulator': 'devices.engines.Engine',
            'h1': h1,
            'h2': h2
        }

        create_device(iot_hub, device_id, simulation_parameters)

    count = 3
    for i in range(count):
        device_id = 'M-ATV-{0:03d}'.format(i)
        h1 = random.uniform(0.8, 0.95)
        h2 = random.uniform(0.8, 0.95)

        simulation_parameters = {
            'simulator': 'devices.engines.Engine',
            'h1': h1,
            'h2': h2
        }

        create_device(iot_hub, device_id, simulation_parameters)

    count = 5
    for i in range(count):
        device_id = 'Chinook-{0:03d}'.format(i)
        h1 = random.uniform(0.8, 0.95)
        h2 = random.uniform(0.8, 0.95)

        simulation_parameters = {
            'simulator': 'devices.engines.Engine',
            'h1': h1,
            'h2': h2
        }

        create_device(iot_hub, device_id, simulation_parameters)
