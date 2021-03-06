import sys

# noinspection PyUnresolvedReferences
from huffman.huffman.compress import compress as huffman_compress
# noinspection PyUnresolvedReferences
from huffman.huffman.decompress import decompress as huffman_decompress
# noinspection PyUnresolvedReferences
from huffman.adaptive_huffman.compress import compress as adaptive_huffman_compress
# noinspection PyUnresolvedReferences
from huffman.adaptive_huffman.decompress import decompress as adaptive_huffman_decompress
# noinspection PyUnresolvedReferences
from huffman.tunstall.compress import compress as tunstall_compress
# noinspection PyUnresolvedReferences
from huffman.tunstall.decompress import decompress as tunstall_decompress
# noinspection PyUnresolvedReferences
from arithmetic.compress import compress as arithmetic_compress
# noinspection PyUnresolvedReferences
from arithmetic.decompress import decompress as arithmetic_decompress
# noinspection PyUnresolvedReferences
from dictionary.lzss import compress as lzss_compress
# noinspection PyUnresolvedReferences
from dictionary.lzss import decompress as lzss_decompress
# noinspection PyUnresolvedReferences
from dictionary.lzw import compress as lzw_compress
# noinspection PyUnresolvedReferences
from dictionary.lzw import decompress as lzw_decompress

if __name__ == '__main__':
    technique, method, filename = sys.argv[1:4]
    globals()['%s_%s' % (technique, method)](filename)
