import sys, random, os, shutil
def splitdirs(files, dir1, dir2, ratio):
    shuffled = files[:]
    random.shuffle(shuffled)
    num = int(round(len(shuffled) * ratio))
    to_dir1, to_dir2 = shuffled[:num], shuffled[num:]
    for d in dir1, dir2:
        if not os.path.exists(d):
            os.mkdir(d)
    for file in to_dir1:
        os.symlink(file, os.path.join(dir1, os.path.basename(file)))
    for file in to_dir2:
        os.symlink(file, os.path.join(dir2, os.path.basename(file)))
    if not os.path.exists('norm_info'):
        os.mkdir('norm_info')
    shutil.copy('/home/jax/latest_features/norm_info/norm_info_mgc_lf0_vuv_bap_63_MVN.dat', '/home/jax/final_data/norm_info/norm.dat')

if __name__ == '__main__':
    if len(sys.argv) != 5:
        sys.exit('Usage: {} files.txt dir1 dir2 ratio'.format(sys.argv[0]))
    else:
        files, dir1, dir2, ratio = sys.argv[1:]
        ratio = float(ratio)
        files = open(files).read().splitlines()
        splitdirs(files, dir1, dir2, ratio)
