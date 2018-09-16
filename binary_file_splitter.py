
import click
import sys

class BasedIntParamType(click.ParamType):
    name = 'integer'

    def convert(self, value, param, ctx):
        try:
            if value[:2].lower() == '0x':
                return int(value[2:], 16)
            elif value[:1] == '0':
                return int(value, 8)
            return int(value, 10)
        except ValueError:
            self.fail('%s is not a valid integer' % value, param, ctx)

BASED_INT = BasedIntParamType()


@click.command()
@click.option('--src', help='binary file to be split.')
@click.option('--dst', help='binary file to after split.')
@click.option('--start', default=0x0, type=BASED_INT, help='Start address to split.')
@click.option('--size', default=0x100, type=BASED_INT, help='Size')
def binary_split(src, dst, start, size):
    try:
        with open(src, 'rb') as src_fh:
            src_fh.seek(start)
            data = src_fh.read(size)
    except:
        print("FAILED: Can not open file %s."%(src))
        sys.exit()

    try:
        with open(dst, 'wb') as dst_fh:
            dst_fh.write(data)
    except:
        print("FAILED:Can not create file %s" %(dst))
        sys.exit()
    print("Successful...")
    print("file %s length is 0x%x" %(dst,len(data)))


if __name__ == '__main__':
    binary_split()

