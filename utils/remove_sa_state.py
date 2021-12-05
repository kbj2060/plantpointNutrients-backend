from typing import Dict


def remove_sa_state(d: Dict):
  if '_sa_instance_state' in d.keys():
    del d['_sa_instance_state']
  return d
