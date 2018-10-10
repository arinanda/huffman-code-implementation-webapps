import sys

from huffman.huffman.compress import compress as huffman_compress
from huffman.huffman.decompress import decompress as huffman_decompress
from huffman.adaptive_huffman.compress import compress as adaptive_huffman_compress
from huffman.adaptive_huffman.decompress import decompress as adaptive_huffman_decompress
from huffman.tunstall.compress import compress as tunstall_compress
from huffman.tunstall.decompress import decompress as tunstall_decompress

if __name__ == '__main__':
    technique, method, filename = sys.argv[1:4]
    globals()['%s_%s' % (technique, method)](filename)
