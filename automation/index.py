from .controllers import getLastAutomation

if __name__ == "__main__":
    automation = getLastAutomation('nutrientsupply', {"limit" : 1})
    print(automation)