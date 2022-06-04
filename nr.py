
from this import d


def swapFileData():

    source = input("enter the first file:")
    destination = input("enter the second file:")

    with open(source,'r') as s:
        data_s = s.read()
        with open (destination,'r') as b:
            data_d = d.read()


            with open(source, 'w+') as s:
                d.write(data_d)
                with open (destination, 'w+') as d:
                    s.write(data_s)

swapFileData()