import os
import preprocessing

def main():
    """> Run in superdir, fix imports"""
    PATH = 'data/pdfs'
    textdir = os.listdir('data/texts')
    for filename in os.listdir(PATH):
        if '.pdf' not in filename:
            continue

        ifile = '%s/%s' % (PATH, filename)
        ofile = '%s/%s' % ('data/texts', filename.replace('.pdf', '.txt'))

        if filename.replace('.pdf', '.txt') not in textdir:
            try:
                preprocessing.extract_text(files=[ifile], outfile=ofile)
                print('{} > {}'.format(ifile, ofile))
            except Exception as e:
                print(e, ofile)
        else:
            print('File %s already exists. Skipping' % ofile)


if __name__ == '__main__':
    main()