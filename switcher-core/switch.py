import manager
import sys

def main():
    mngr = manager.Manager("./control.sock")
    mngr.mount(id=0, mountpoint="./mount-dir", mode="proxy", proxy_dir="./proxy-dir")

if __name__ == '__main__':
    main()