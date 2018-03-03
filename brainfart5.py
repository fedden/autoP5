# -*- coding: utf-8 -*-
"""
brainfart5 by Leon Fedden

A tiny subset of p5.js, that syntactically is closer to brainfuck, although
not remotely resembling it as a language - it's not stack based or anything
smart at all!

The pro of this language is that it is impossible to be syntactically correct
provided that the chars_to_indices characters are used.

chars_to_indices = string.punctuation + string.ascii_letters + string.digits
"""

import inspect
import math
import wget
import random
import string
import os
from selenium import webdriver


def get_random_program(line_length):
    chars = list(string.punctuation + string.ascii_letters + string.digits)
    function_chars = chars[1:len(functions)]
    tokens = ['!']
    lines = 0
    while lines < line_length:
        function_char = random.choice(function_chars)
        tokens.append(function_char)
        function_index = chars_to_indices[function_char]
        function = functions[function_index]
        lines += 1
        for _ in range(function.arg_size):
            tokens.append(random.choice(chars))
    return tokens


def html_start():
    document =  "<html>\n"
    document += "\n"
    document += "<head>\n"
    document += "<script src='../p5.min.js'></script>\n"
    document += "<script>\n"
    return document


def html_end():
    document =  "</script>\n"
    document += "</head>\n"
    document += "\n"
    document += "<body>\n"
    document += "</body>\n"
    document += "\n"
    document += "</html>\n"
    return document


def code_to_html(code):
    document = html_start()
    document += code
    document += "\n"
    document += html_end()
    return document


def make_dataset(save_path, size, line_length):

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    wget.download('https://github.com/processing/p5.js/releases/download/0.5.16/p5.min.js',
                  out=save_path)

    sketch_save_path = os.path.join(save_path, "sketches")
    if not os.path.exists(sketch_save_path):
        os.makedirs(sketch_save_path)

    tokens_save_path = os.path.join(save_path, "tokens")
    if not os.path.exists(tokens_save_path):
        os.makedirs(tokens_save_path)

    html_save_path = os.path.join(save_path, "html")
    if not os.path.exists(html_save_path):
        os.makedirs(html_save_path)

    images_save_path = os.path.join(save_path, "images")
    if not os.path.exists(images_save_path):
        os.makedirs(images_save_path)

    images_save_path = os.path.abspath(images_save_path)
    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory' : images_save_path}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)

    for i in range(size):
        tokens = get_random_program(line_length)
        code = tokens_to_code(tokens, i)
        document = html_start()
        document += code
        document += "\n"
        document += html_end()

        sketch_path = os.path.join(sketch_save_path, "sketch_{}.js".format(i))
        with open(sketch_path, 'a') as out:
            out.write(code)

        tokens_path = os.path.join(tokens_save_path, "tokens_{}.bf5".format(i))
        with open(tokens_path, 'a') as out:
            out.write(''.join(tokens))

        html_path = os.path.join(html_save_path, "index_{}.html".format(i))
        with open(html_path, 'a') as out:
            out.write(document)

        driver.get('file://' + os.path.abspath(html_path))

        print("{}% finished".format(round((i / size * 100), 1)), "      ", end="\r")
    driver.close()
    print("100% finished      ")


chars_to_tokens = {
    '!': 0,
    '"': 1,
    '#': 2,
    '$': 3,
    '%': 4,
    '&': 5,
    "'": 6,
    '(': 7,
    ')': 8,
    '*': 9,
    '+': 10,
    ',': 11,
    '-': 12,
    '.': 13,
    '/': 14,
    ':': 15,
    ';': 16,
    '<': 17,
    '=': 18,
    '>': 19,
    '?': 20,
    '@': 21,
    '[': 22,
    '\\': 23,
    ']': 24,
    '^': 25,
    '_': 26,
    '`': 27,
    '{': 28,
    '|': 29,
    '}': 30,
    '~': 31,
    'a': 32,
    'b': 33,
    'c': 34,
    'd': 35,
    'e': 36,
    'f': 37,
    'g': 38,
    'h': 39,
    'i': 40,
    'j': 41,
    'k': 42,
    'l': 43,
    'm': 44,
    'n': 45,
    'o': 46,
    'p': 47,
    'q': 48,
    'r': 49,
    's': 50,
    't': 51,
    'u': 52,
    'v': 53,
    'w': 54,
    'x': 55,
    'y': 56,
    'z': 57,
    'A': 58,
    'B': 59,
    'C': 60,
    'D': 61,
    'E': 62,
    'F': 63,
    'G': 64,
    'H': 65,
    'I': 66,
    'J': 67,
    'K': 68,
    'L': 69,
    'M': 70,
    'N': 71,
    'O': 72,
    'P': 73,
    'Q': 74,
    'R': 75,
    'S': 76,
    'T': 77,
    'U': 78,
    'V': 79,
    'W': 80,
    'X': 81,
    'Y': 82,
    'Z': 83,
    '0': 84,
    '1': 85,
    '2': 86,
    '3': 87,
    '4': 88,
    '5': 89,
    '6': 90,
    '7': 91,
    '8': 92,
    '9': 93,
}


class token_code(object):

    def __init__(self, functor):
        self.get_code = functor
        self.arg_size = len(inspect.getargspec(functor).args)


def arg_signature(*args):
    code = ""
    for i in range(len(args)):
        code += str(round(args[i], 3))
        if i != (len(args) - 1): code += ", "
    return code


def background(h, s, b):
    return "background(" + arg_signature(h, s, b) + ");\n"


def fill(h, s, b):
    return "fill(" + arg_signature(h, s, b) + ");\n"


def stroke(h, s, b):
    return "stroke(" + arg_signature(h, s, b) + ");\n"


def fill_alpha(h, s, b, a):
    return "fill(" + arg_signature(h, s, b, a) + ");\n"


def stroke_alpha(h, s, b, a):
    return "stroke(" + arg_signature(h, s, b, a) + ");\n"


def no_fill():
    return "noFill();\n"


def stroke_weight(weight):
    weighted_weight = weight * 10.0
    return "strokeWeight(" + str(weighted_weight) + ");\n"


def arc(x, y, w, h, start, end):
    two_pi = math.pi * 2.0
    s = start * two_pi
    e = end * two_pi
    return "arc(" + arg_signature(x, y, w, h, s, e) + ");\n"


def ellipse(x, y, w, h):
    x *= 100
    y *= 100
    w *= 100
    h *= 100
    return "ellipse(" + arg_signature(x, y, w, h) + ");\n"


def circle(x, y, r):
    x *= 100
    y *= 100
    r *= 100
    return "ellipse(" + arg_signature(x, y, r, r) + ");\n"


def line(x1, y1, x2, y2):
    x1 *= 100
    x2 *= 100
    y1 *= 100
    y2 *= 100
    return "line(" + arg_signature(x1, y1, x2, y2) + ");\n"


def point(x, y):
    x *= 100
    y *= 100
    return "point(" + arg_signature(x, y) + ");\n"


def rect(x, y, w, h):
    x *= 100
    y *= 100
    w *= 100
    h *= 100
    return "rect(" + arg_signature(x, y, w, h) + ");\n"


def square(x, y, size):
    x *= 100
    y *= 100
    size *= 100
    return "rect(" + arg_signature(x, y, size, size) + ");\n"


def apply_matrix(a, b, c, d, e, f):
    return "applyMatrix(" + arg_signature(a, b, c, d, e, f) + ");\n"


def reset_matrix():
    return "resetMatrix();\n"


def rotate(angle):
    angle *= (math.pi * 2.0)
    return "rotate(" + str(angle) + ");\n"


functions = [
    token_code(background),
    token_code(fill),
    token_code(stroke),
    token_code(fill_alpha),
    token_code(stroke_alpha),
    token_code(no_fill),
    token_code(stroke_weight),
    token_code(arc),
    token_code(ellipse),
    token_code(circle),
    token_code(line),
    token_code(point),
    token_code(rect),
    token_code(square),
    token_code(apply_matrix),
    token_code(reset_matrix),
    token_code(rotate)
]


def start_code():
    code =  "function setup() {\n"
    code += "    createCanvas(100, 100);\n"
    code += "    colorMode(HSB, 1.0);\n"
    code += "    noLoop();\n"
    code += "}\n\n"
    code += "function draw() {\n"
    return code


def end_code(algorithm_number):
    code =  "    saveCanvas('output_" + str(algorithm_number) + "', 'png');\n"
    code += "}\n"
    return code


def tokens_to_code(tokens, algorithm_number):
    code = start_code()

    i = 0
    while True:
        char = tokens[i]
        function_index = chars_to_indices[char] % len(functions)
        function = functions[function_index]
        arg_start = i + 1
        arg_end = i + 1 + function.arg_size

        if arg_end >= len(tokens):
            break

        arg_chars = tokens[arg_start:arg_end]
        arguments = [(chars_to_indices[char] / len(chars_to_indices))
                     for char in arg_chars]

        code += "    "
        if len(arguments) > 0:
            code += function.get_code(*arguments)
        else:
            code += function.get_code()

        i = arg_end

    code += end_code(algorithm_number)
    return code
