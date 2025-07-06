file1 = "./data/100STYLE_mixamo/simple/Aeroplane_BR.bvh"
file2 = "./data/100STYLE_mixamo/raw/Aeroplane_BR.bvh"

if __name__=='__main__':
    with open(file1) as f:
        print(len(f.readlines()))
        print(f.readlines())

    with open(file2) as f:
        print(len(f.readlines()))