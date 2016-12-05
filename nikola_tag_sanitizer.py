import os
import re
import argparse


class NikolaTagSanitizer(object):
    def __init__(self, post_dir):
        CBOLD = '\33[1m'
        COLD = '\33[91m'
        CNEW = '\33[32m'
        CEND = '\33[0m'

        for dirname, dirnames, filenames in os.walk(post_dir):
            for filename in filenames:
                if filename.endswith('.meta'):
                    meta_file = os.path.join(dirname, filename)
                    meta_contents = ""
                    with open(meta_file, 'rw') as fp:
                        for line in fp:
                            orig_line = line
                            if re.search("tags", line):
                                tag_contents = line.split(':')
                                tags = tag_contents[1].strip()
                                tags_lower = self.sanitize(tags)
                                tag_contents[1] = " " + tags_lower + "\n"
                                new_tag_contents = ":".join(tag_contents)
                                line = line.replace(line, new_tag_contents)
                            if orig_line != line:
                                print CBOLD + meta_file + CEND
                                print COLD + "-" + orig_line[:-1] + CEND
                                print CNEW + "+" + line + CEND

                            meta_contents = meta_contents + line
                    with open(meta_file, "w") as f:
                        f.write(meta_contents)

    def sanitize(self, tags):
        tag_list = tags.split(',')
        tags_lower = list(set([t.lower() for t in tag_list]))
        tags_lower.sort(key=str.lower)
        return ",".join(tags_lower)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--post-directory", help="Location of the posts "
                                                       "directory")
    args = parser.parse_args()
    post_dir = args.post_directory

    if not post_dir:
        # print "Location of the post directory: "
        post_dir = raw_input("Location of the post directory: ")

    NikolaTagSanitizer(post_dir)
