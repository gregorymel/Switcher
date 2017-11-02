import manager
import sys
import os

def main():

    if len(sys.argv)==3:
        dir_src = sys.argv[1]
        dir_dst = sys.argv[2]

        if ( not os.path.isdir( dir_src ) or not os.path.isdir( dir_src ) ):
            print( "Wrong parameters! Must be <dir_src> <dir_dst>" )
            sys.exit( 1 )
    
        default_control_sock = "./control.sock" #"/var/run/fuse_control.sock"
        default_mountpoint = "./mount-dir" #"/mnt"
        #os.makedirs(default_mountpoint, mode=0o777)

        mngr = manager.Manager( default_control_sock )
        mngr.mount(id=0, mountpoint=os.path.abspath(default_mountpoint), mode="proxy", proxy_dir=os.path.abspath(dir_src)) 
        mngr.set_mode(id=0, mode="stub")
        mngr.set_mode(id=0, mode="proxy", proxy_dir=os.path.abspath(dir_dst))

if __name__ == '__main__':
    main()
