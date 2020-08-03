#!/usr/bin/env python3
import os 
def check_reboot():
    """Devuelve Verdadero si el computador tiene pendiente un reboot."""
    return os.path.exist("run/reboot-required")

def main():
    pass

main()
