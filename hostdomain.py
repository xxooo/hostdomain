# coding=utf-8
from dns import resolver
import re
from optparse import OptionParser


def hostdomain(domain, outputfile):
    try:
        domain = domain.strip()
        ans = resolver.query(domain, "A")
        iplist = []
        for i in ans.response.answer:
            for ip in i.items:
                if ip.rdtype == 1:
                    iplist.append(ip.address)
        with open(outputfile, "a") as file:
            for ip in iplist:
                file.write(domain+"----->"+ip + '\n')
    except Exception as e:
        with open(outputfile, "a") as file:
            file.write("resolver error: "+str(e) + '\n')


def main():
    print '''
$$\                             $$\           $$\                                   $$\           
$$ |                            $$ |          $$ |                                  \__|          
$$$$$$$\   $$$$$$\   $$$$$$$\ $$$$$$\    $$$$$$$ | $$$$$$\  $$$$$$\$$$$\   $$$$$$\  $$\ $$$$$$$\  
$$  __$$\ $$  __$$\ $$  _____|\_$$  _|  $$  __$$ |$$  __$$\ $$  _$$  _$$\  \____$$\ $$ |$$  __$$\ 
$$ |  $$ |$$ /  $$ |\$$$$$$\    $$ |    $$ /  $$ |$$ /  $$ |$$ / $$ / $$ | $$$$$$$ |$$ |$$ |  $$ |
$$ |  $$ |$$ |  $$ | \____$$\   $$ |$$\ $$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$  __$$ |$$ |$$ |  $$ |
$$ |  $$ |\$$$$$$  |$$$$$$$  |  \$$$$  |\$$$$$$$ |\$$$$$$  |$$ | $$ | $$ |\$$$$$$$ |$$ |$$ |  $$ |
\__|  \__| \______/ \_______/    \____/  \_______| \______/ \__| \__| \__| \_______|\__|\__|  \__|
	'''
    usage = "usage: python %prog -i targetfile -o outputfile"
    parser = OptionParser(usage=usage)
    parser.add_option('-i', dest='targetfile', type='string',
                      help='Enter the path to the file you want to batch resolve the domain name')
    parser.add_option('-o', dest='outputfile', type='string',
                      help='Enter the resulting path you want to output')
    (options, args) = parser.parse_args()
    targetfile = options.targetfile
    outputfile = options.outputfile
    if targetfile and outputfile:
        with open(targetfile, "r")as f:
            line = f.readlines()
            for line_list in line:
                print "resolve " + line_list
                hostdomain(line_list, outputfile)
    else:
        print "Please enter -h to view usage"


if __name__ == "__main__":
    main()
