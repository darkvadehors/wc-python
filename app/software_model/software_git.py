#  https://code.visualstudio.com/sha/download?build=stable&os=darwin-universal
#  https://az764295.vo.msecnd.net/stable/3a6960b964327f0e3882ce18fcebd07ed191b316/VSCode-darwin-universal.zip
import os

def make_url():
    """ Class model for nmake download url """


# https://sourceforge.net/projects/git-osx-installer/
# https://sourceforge.net/projects/git-osx-installer/files/latest/download

    os_type:str = None
    if os.uname()[0] == "Darwin":
        os_type = "git-osx-installer"
    elif os.uname()[0] == "Linux":
        if os.uname()[1] == "debian":
            os_type = "linux-deb-x64"
        elif os.uname()[1] == "Centos" or os.uname()[1] == "RHEL":
            os_type = "linux-rpm-x64"
    else:
        print("Change d'ordinateur")

    return "https://sourceforge.net/projects/\
{}/files/latest/download".format(
        os_type
        )

    #print("test",[x for x in a for a in lst])
    # try:
    #     float(lst[0])
    #     print("1",lst[0])
    # except:
    #     pass

if __name__ == "__main__":
    print(make_url())