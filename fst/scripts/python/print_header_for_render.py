import sys

from fst.io import read

common_tile_header_keys = [
    "XResolution", "YResolution", "PixelSize", "EightBit", "ChanNum", "SWdate",
    "StageX", "StageY", "StageZ", "StageR"
]
retained_tile_header_keys = common_tile_header_keys + ["WD"]


def print_header_info(file_name):

    records = read([file_name], lazy=False)
    for record in records:
        header = {}
        for key in retained_tile_header_keys:
            header[key] = record.header.__dict__[key]

        # "Z1217-33m_BR_Sec10, BF 316x100um, 24s @11.5nA /8nm @15nA-1, lens2 14110-40V..., bias 0V, deflector +100V"
        notes = record.header.__dict__["Notes"]
        header["TabID"] = notes[0:notes.find(",")]

        print(f'{file_name}')
        for key in sorted(header.keys()):
            print(f'  {key}: {header[key]}')


if __name__ == "__main__":

    dat_file_name = "/Users/trautmane/Desktop/Merlin-6285_19-06-23_033042_0-0-1.dat" \
        if len(sys.argv) < 2 \
        else sys.argv[1]

    print_header_info(dat_file_name)
