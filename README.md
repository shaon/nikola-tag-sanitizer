# nikola-tag-sanitizer
To workaround duplicate tag errors while importing wordpress blog.

If you have duplicated tags in wordpress blog, or you have tags and
categories that look similar, you may run into this issue while
importing Wordpress blog into Nikola.

```
ERROR: Nikola: You have tags that are too similar: Monitoring and monitoring
ERROR: Nikola: You have tags that are too similar: appscale and Appscale
ERROR: Nikola: You have tags that are too similar: IaaS and iaas
```

![alt text](https://raw.githubusercontent.com/shaon/nikola-tag-sanitizer/master/error.png "Error")

Nikola comes with this option that convert all tag and category names 
to lower case.
```
nikola import_wordpress --tag-sanitizing-strategy lower <blah.xml>
```

Unfortunately, that didn't solve the tag issue for me.

``nikola_tag_sanitizer.py`` reads all the tags in the ``.meta`` files,
converts all the tags to lower case and removes duplicates.

```
python nikola_tag_sanitizer.py
```

or

```
python nikola_tag_sanitizer.py -p /path/to/new_site/posts/
```

![alt text](https://raw.githubusercontent.com/shaon/nikola-tag-sanitizer/master/convert.png "Convert")